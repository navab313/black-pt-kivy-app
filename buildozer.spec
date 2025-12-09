[app]

# مشخصات برنامه
title = Grade Predictor
package.name = gradepredictor
package.domain = ir.mycompany
version = 1.0.0

# مسیر کد
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,ttc,otf
source.include_dirs = fonts,data

# آیکون و اسپلش
icon.filename = data/icon.png
presplash.filename = data/splash.png

# --- نیازمندی‌های ضروری ---
# کتابخانه‌های اصلی مورد نیاز
requirements = 
    python3==3.10.9,
    kivy==2.3.0,
    arabic-reshaper==3.0.0,
    python-bidi==0.4.2,
    pillow==10.1.0,
    pyjnius==1.5.0

# --- تنظیمات اندروید ---
# مجوزها
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# نسخه API
android.api = 33
android.minapi = 21
android.maxapi = 33

# معماری
android.archs = arm64-v8a  # فقط یک معماری برای کاهش خطا

# NDK و SDK
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 

# Build tools (نسخه پایدار)
android.build_tools = 34.0.0

# Bootstrap
p4a.bootstrap = sdl2
android.accept_sdk_license = True

# جهت‌گیری
orientation = portrait
fullscreen = 0

# تنظیمات اضافی
android.enable_androidx = True
android.meta_data = 
android.add_activity = 

# --- تنظیمات Buildozer ---
log_level = 2
warn_on_root = 1

# پوشه خروجی
bin_dir = ./bin

[buildozer]
log_level = 2

