[app]

# تنظیمات اصلی برنامه
title = Grade Predictor
package.name = gradepredictor
package.domain = com.mycompany
version = 1.0.0
main.py = main.py

# مسیرهای سورس
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,ttc,otf
source.include_dirs = fonts,data

# آیکون و صفحه بارگذاری
icon.filename = data/icon.png
presplash.filename = data/splash.png
presplash.duration = 3000
orientation = portrait
fullscreen = 0

# نیازمندی‌های پایتون (بسیار مهم!)
requirements = 
    python3==3.10.9,
    kivy==2.3.0,
    arabic-reshaper==3.0.0,
    python-bidi==0.4.2,
    pillow==10.1.0,
    pyjnius==1.5.0

# تنظیمات اندروید
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.maxapi = 33

# معماری - فقط یک معماری برای کاهش خطا
android.archs = arm64-v8a

# NDK و Build Tools
android.ndk = 25b
android.build_tools = 34.0.0

# Bootstrap و تنظیمات
p4a.bootstrap = sdl2
android.accept_sdk_license = True
android.enable_androidx = True

# تنظیمات Buildozer
log_level = 2
warn_on_root = 1
bin_dir = ./bin

[buildozer]
log_level = 2
