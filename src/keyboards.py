from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔍 بدء البحث", callback_data="start_hunt"),
        InlineKeyboardButton(text="⚙️ الإعدادات", callback_data="settings"),
    )
    builder.row(
        InlineKeyboardButton(text="📊 الإحصائيات", callback_data="stats"),
        InlineKeyboardButton(text="ℹ️ حول البوت", callback_data="about"),
    )
    return builder.as_markup()

def settings_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🌐 إعدادات البروكسي", callback_data="proxy_settings"),
        InlineKeyboardButton(text="🔒 إعدادات الحماية", callback_data="security_settings"),
    )
    builder.row(
        InlineKeyboardButton(text="🔙 رجوع", callback_data="main_menu"),
    )
    return builder.as_markup()

def back_to_main_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔙 رجوع للقائمة الرئيسية", callback_data="main_menu"),
    )
    return builder.as_markup()
