[app]
# --- مشخصات برنامه ---
title = Grade Predictor
package.name = gradepredictor
package.domain = ir.mycompany
version = 1.0.0

# --- مسیر کد ---
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,ttc,otf,txt,json
source.include_dirs = fonts,data,patches

# آیکون و presplash (مسیر نسبت به ریشه پروژه)
icon.filename = data/icon.png
presplash.filename = data/splash.png

# --- نیازمندی‌ها (فقط پکیج‌های سازگار و ضروری) ---
# flask, selenium, socketIO و ttkbootstrap حذف شدند.
requirements = python3,kivy,pyjnius,cryptography,requests

# کتابخانه‌های p4a محلی
# اگر در پوشه patches فقط پچ برای pyjnius (مثلاً رفع مشکل long) دارید، این خط درست است.
p4a.local_recipes = patches

# مجوزها و تنظیمات اندروید
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE
# مجوز ACCESS_FINE_LOCATION نیاز به توضیح دلیل در پلی‌استور دارد.
android.api = 33
android.minapi = 21
# رفع اخطار قدیمی Buildozer:
android.archs = armeabi-v7a, arm64-v8a
android.ndk = 25b
# اجبار Build-Tools برای حل مشکل مجوز 36.1:
android.build_tools = 33.0.2 

# ساخت و خروجی
fullscreen = 0
orientation = portrait

# پوشه خروجی APK
bin_dir = ./bin

# --- Buildozer / p4a settings ---
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2

