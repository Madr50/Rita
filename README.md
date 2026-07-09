# Data Hunter Telegram Bot

## نظرة عامة

هذا المشروع عبارة عن بوت Telegram متقدم مصمم لـ "صيد البيانات" وأتمتة الأمن السيبراني، مبني باستخدام Python 3.12+ و Aiogram 3.x. يهدف البوت إلى توفير واجهة مستخدم Cyber-Themed تفاعلية مع قدرات معالجة بيانات عالية الأداء تعتمد على البرمجة غير المتزامنة (Asyncio) ودعم البروكسيات ونظام حماية HWID Lock.

## الميزات الرئيسية

*   **واجهة مستخدم Cyber-Themed:** تعتمد على Aiogram 3.x مع أزرار Inline Keyboards ديناميكية وقوائم متداخلة.
*   **أشرطة تقدم في الوقت الفعلي:** عرض حالة العمليات الجارية باستخدام أشرطة تقدم داخل الرسائل.
*   **تنسيق احترافي للنتائج:** استخدام HTML/MarkdownV2 لعرض البيانات في جداول (Pipe Tables) بأسلوب تقني.
*   **محرك برمجي غير متزامن بالكامل (Asyncio):** لضمان سرعة وكفاءة عالية في معالجة الطلبات.
*   **دعم Multi-threading/Multi-processing:** للتعامل مع البيانات الضخمة وتحقيق التوازي في العمليات (مخطط للتنفيذ ضمن محرك Data Hunter).
*   **دعم Proxies (SOCKS5/HTTP):** مع نظام Auto-rotation لضمان إخفاء الهوية وتجاوز القيود الجغرافية.
*   **نظام Account Checker/Data Scraper:** يعتمد على طلبات الـ API المباشرة لجمع البيانات.
*   **حماية HWID Lock:** لربط البوت بجهاز المستخدم ومنع التوزيع غير المصرح به.
*   **تعمية الكود المصدري (Obfuscation):** لزيادة صعوبة الهندسة العكسية.

## هيكل المشروع

```
Rita/
├── config/
│   └── config.py
├── data/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── keyboards.py
│   ├── logger.py
│   ├── hwid_manager.py
│   ├── proxy_manager.py
│   ├── data_hunter.py
│   └── obfuscator.py
└── requirements.txt
```

## الإعداد والتشغيل

### المتطلبات

*   Python 3.12+
*   pip (مدير الحزم لـ Python)

### خطوات الإعداد

1.  **استنساخ المستودع (Clone the repository):**
    ```bash
    git clone https://github.com/Madr50/Rita.git
    cd Rita
    ```

2.  **إنشاء بيئة افتراضية (Virtual Environment):** (موصى به)
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # لنظامي Linux/macOS
    # venv\Scripts\activate  # لنظام Windows
    ```

3.  **تثبيت الاعتمادات (Install dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **تكوين البوت (Configure the bot):**
    *   افتح الملف `config/config.py`.
    *   `BOT_TOKEN`: تم تحديثه بالفعل بالتوكن الخاص بك.
    *   `ADMIN_ID`: تم تحديثه بالفعل بمعرف المستخدم الخاص بك.
    *   **HWID Lock:** عند تشغيل البوت لأول مرة، سيقوم بإنشاء `hwid.key` في مجلد `config/` وسيطبع الـ HWID الخاص بجهازك في الـ console. انسخ هذا الـ HWID والصقه في متغير `ALLOWED_HWID` في `config/config.py`.
    *   **Proxies:** أضف قائمة البروكسيات الخاصة بك (SOCKS5/HTTP) إلى قائمة `PROXIES` في `config/config.py`.
    *   **APIs:** قم بتكوين واجهات الـ API التي ترغب في استخدامها لـ "صيد البيانات" في قائمة `APIS` في `config/config.py`.

5.  **تشغيل البوت (Run the bot):**
    ```bash
    python3 src/main.py
    ```

## تفاصيل المكونات

### `config/config.py`

يحتوي على المتغيرات البيئية والإعدادات الأساسية للبوت:

*   `BOT_TOKEN`: رمز البوت الخاص بـ Telegram.
*   `ADMIN_ID`: معرف المستخدم الخاص بك (للحماية).
*   `ALLOWED_HWID`: الـ HWID المسموح به لتشغيل البوت. يتم إنشاؤه تلقائيًا عند التشغيل الأول.
*   `PROXIES`: قائمة بالبروكسيات (SOCKS5/HTTP) التي سيستخدمها البوت.
*   `APIS`: قائمة بتكوينات واجهات الـ API التي سيتم استخدامها لجمع البيانات.

### `src/main.py`

النقطة الرئيسية لتشغيل البوت. يتعامل مع:

*   تهيئة Bot و Dispatcher من Aiogram.
*   معالجة الأوامر مثل `/start`.
*   معالجة الـ Callback Queries من الأزرار الديناميكية.
*   دمج نظام التسجيل (Logger) ونظام HWID Lock.
*   عرض أشرطة التقدم ونتائج البحث.
*   **حماية User ID:** يتحقق من `ADMIN_ID` قبل معالجة الأوامر والـ callbacks.

### `src/keyboards.py`

يحتوي على دوال لإنشاء Inline Keyboards ديناميكية:

*   `main_menu_keyboard()`: القائمة الرئيسية للبوت.
*   `settings_menu_keyboard()`: قائمة الإعدادات الفرعية.
*   `back_to_main_menu_keyboard()`: زر للعودة إلى القائمة الرئيسية.

### `src/logger.py`

يقوم بإعداد نظام التسجيل (logging) لتسجيل الأحداث والأخطاء في ملف `bot.log` وفي الـ console.

### `src/hwid_manager.py`

يدير نظام HWID Lock:

*   `generate_hwid()`: ينشئ HWID فريدًا بناءً على معلومات الجهاز.
*   `check_hwid()`: يتحقق مما إذا كان الـ HWID الحالي يطابق الـ HWID المحفوظ أو المسموح به.

### `src/proxy_manager.py`

يدير قائمة البروكسيات ويوفر وظائف لاختيار واختبار البروكسيات:

*   `ProxyManager`: فئة لإدارة البروكسيات مع دعم Auto-rotation.
*   `get_next_proxy()`: يعيد البروكسي التالي في القائمة.
*   `test_proxy()`: يختبر صلاحية البروكسي.
*   `get_working_proxy()`: يبحث عن بروكسي عامل من القائمة.

### `src/data_hunter.py`

محرك "صيد البيانات" غير المتزامن:

*   `DataHunter`: فئة تقوم بإجراء طلبات API متزامنة (concurrent) باستخدام `httpx`.
*   `_make_request()`: يقوم بطلب API واحد باستخدام بروكسي.
*   `hunt_data()`: ينفذ عمليات البحث عبر واجهات API متعددة بشكل متوازٍ.

### `src/obfuscator.py`

سكربت لتعمية الكود المصدري:

*   `obfuscate_file()`: يقوم بإزالة التعليقات وإعادة تسمية المتغيرات في ملف Python واحد.
*   `obfuscate_project()`: يطبق التعمية على جميع ملفات Python في مجلد معين.

## كيفية استخدام نظام التعمية

لتعمية الكود المصدري الخاص بك، يمكنك تشغيل دالة `obfuscate_project` من سكربت `obfuscator.py`. على سبيل المثال، لتعمية مجلد `src` إلى مجلد جديد `obfuscated_src`:

```python
from src.obfuscator import obfuscate_project

obfuscate_project("src", "obfuscated_src")
```

**ملاحظة هامة:** التعمية المقدمة هنا هي تعمية أساسية. للحصول على حماية أقوى ضد الهندسة العكسية، قد تحتاج إلى استخدام أدوات تعمية متخصصة أو تقنيات تشفير أكثر تعقيدًا.

## المساهمة

نرحب بالمساهمات لتحسين هذا المشروع. يرجى فتح "مشكلة" (issue) أو إرسال "طلب سحب" (pull request).

## الترخيص

هذا المشروع مرخص بموجب ترخيص MIT. انظر ملف `LICENSE` لمزيد من التفاصيل.

---

**تم بناء هذا البوت بواسطة Manus AI**
