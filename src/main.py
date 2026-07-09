import sys
import os

# Ensure the project root is in sys.path for module discovery
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import asyncio
import logging
import time

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties

# Direct imports from the top-level packages
from config import config
from src import keyboards
from src import logger as logger_module
from src import hwid_manager
from src import proxy_manager
from src import data_hunter

# Access attributes directly from the imported modules
BOT_TOKEN = config.BOT_TOKEN
ALLOWED_HWID = config.ALLOWED_HWID
ADMIN_ID = config.ADMIN_ID
PROXIES = config.PROXIES
APIS = config.APIS

main_menu_keyboard = keyboards.main_menu_keyboard
settings_menu_keyboard = keyboards.settings_menu_keyboard
back_to_main_menu_keyboard = keyboards.back_to_main_menu_keyboard

logger = logger_module.logger
check_hwid = hwid_manager.check_hwid
generate_hwid = hwid_manager.generate_hwid
ProxyManager = proxy_manager.ProxyManager
DataHunter = data_hunter.DataHunter

# Configure logging (already done in logger.py, just use the logger instance)

async def simulate_hunt_progress(message: types.Message, total_steps: int):
    # This function remains the same as it's part of the UI
    for i in range(total_steps + 1):
        progress = int((i / total_steps) * 100)
        progress_bar = "█" * (progress // 5) + "░" * (20 - (progress // 5))
        status_message = f"<b>جاري البحث...</b>\n<code>[{progress_bar}] {progress}%</code>"
        if i == 0:
            sent_message = await message.answer(status_message)
        else:
            await message.edit_text(status_message)
        await asyncio.sleep(0.5) # Simulate work
    return sent_message

def generate_hunt_result_message(data: dict) -> str:
    # This function remains the same as it's part of the UI
    message_text = "<b>✅ تم العثور على بيانات!</b>\n\n"
    message_text += "<pre>" # Using <pre> for fixed-width font for table alignment
    message_text += "| المفتاح       | القيمة        |\n"
    message_text += "|:--------------|:-------------|\n"
    for key, value in data.items():
        message_text += f"| {key:<12} | {str(value):<12} |\n"
    message_text += "</pre>"
    message_text += "\n<i>تم العثور على هذه البيانات بنجاح.</i>"
    return message_text

async def main():
    logger.info("Starting bot initialization...")

    # HWID Check
    if not check_hwid(ALLOWED_HWID):
        current_hwid = generate_hwid()
        logger.critical(f"HWID Mismatch! Bot cannot start. Your HWID: {current_hwid}")
        print(f"[CRITICAL] HWID Mismatch! Bot cannot start. Your HWID: {current_hwid}")
        print("Please update ALLOWED_HWID in config/config.py with your HWID.")
        sys.exit(1)
    logger.info("HWID check passed.")

    # Initialize ProxyManager and DataHunter
    proxy_manager = ProxyManager(PROXIES)
    data_hunter = DataHunter(APIS, proxy_manager)

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def command_start_handler(message: types.Message) -> None:
        if message.from_user.id != ADMIN_ID:
            await message.answer("عذراً، أنت غير مصرح لك باستخدام هذا البوت.")
            logger.warning(f"Unauthorized access attempt by user {message.from_user.id}")
            return
        logger.info(f"Received /start command from user {message.from_user.id}")
        await message.answer(
            f"مرحباً بك يا {message.from_user.full_name}! أنا بوت Data Hunter الخاص بك. كيف يمكنني مساعدتك اليوم؟",
            reply_markup=main_menu_keyboard()
        )

    @dp.callback_query(F.data == "main_menu")
    async def main_menu_handler(callback: types.CallbackQuery) -> None:
        if callback.from_user.id != ADMIN_ID:
            await callback.answer("عذراً، أنت غير مصرح لك باستخدام هذا البوت.", show_alert=True)
            logger.warning(f"Unauthorized callback attempt by user {callback.from_user.id}")
            return
        logger.info(f"User {callback.from_user.id} navigated to main menu.")
        await callback.message.edit_text(
            "القائمة الرئيسية:",
            reply_markup=main_menu_keyboard()
        )
        await callback.answer()

    @dp.callback_query(F.data == "settings")
    async def settings_handler(callback: types.CallbackQuery) -> None:
        if callback.from_user.id != ADMIN_ID:
            await callback.answer("عذراً، أنت غير مصرح لك باستخدام هذا البوت.", show_alert=True)
            logger.warning(f"Unauthorized callback attempt by user {callback.from_user.id}")
            return
        logger.info(f"User {callback.from_user.id} navigated to settings.")
        await callback.message.edit_text(
            "الإعدادات:",
            reply_markup=settings_menu_keyboard()
        )
        await callback.answer()

    @dp.callback_query(F.data == "start_hunt")
    async def start_hunt_handler(callback: types.CallbackQuery) -> None:
        if callback.from_user.id != ADMIN_ID:
            await callback.answer("عذراً، أنت غير مصرح لك باستخدام هذا البوت.", show_alert=True)
            logger.warning(f"Unauthorized callback attempt by user {callback.from_user.id}")
            return
        logger.info(f"User {callback.from_user.id} initiated data hunt.")
        await callback.message.edit_text(
            "الرجاء إدخال استعلام البحث:",
            reply_markup=back_to_main_menu_keyboard()
        )
        # Here, you would typically wait for the user's input for the query
        # For demonstration, let's use a dummy query and simulate the hunt
        query = "dummy_query"

        # Simulate progress bar
        progress_message = await callback.message.edit_text(
            "<b>جاري بدء البحث...</b>\n<code>[░░░░░░░░░░░░░░░░░░░░] 0%</code>",
            reply_markup=back_to_main_menu_keyboard()
        )
        await simulate_hunt_progress(progress_message, 20)

        # Perform actual data hunt
        hunt_results = await data_hunter.hunt_data(query)

        if hunt_results:
            # For simplicity, just display the first result
            result_message_text = generate_hunt_result_message(hunt_results[0])
            await progress_message.edit_text(result_message_text, reply_markup=back_to_main_menu_keyboard())
            await callback.answer("تم الانتهاء من البحث بنجاح!")
        else:
            await progress_message.edit_text("<b>❌ لم يتم العثور على بيانات.</b>", reply_markup=back_to_main_menu_keyboard())
            await callback.answer("لم يتم العثور على بيانات.")

    # Start the bot
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
