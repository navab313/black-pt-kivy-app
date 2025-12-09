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

# --- نیازمندی‌ها (مثال؛ بر اساس بسته‌های پروژه خودت تغییر بده) ---
requirements = python3,kivy,pyjnius,cryptography,requests,flask,socketIO,selenium,ttkbootstrap

# کتابخانه‌های p4a محلی (اگر recipes محلی داری، در پوشه patches قرار بگیرند)
# دقت: اگر پوشه patches فقط یک فایل patch است (نه recipe)، توضیح بعدی را ببین.
p4a.local_recipes = patches

# مجوزها و تنظیمات اندروید
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,ACCESS_FINE_LOCATION
android.api = 33
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a
android.ndk = 25b

# ساخت و خروجی
fullscreen = 0
orientation = portrait

# پوشه خروجی APK
bin_dir = ./bin

# --- Buildozer / p4a settings ---
log_level = 2
warn_on_root = 1

# اگر نیاز داری گزینه‌های اضافی p4a:
# p4a.branch = stable
# p4a.bootstrap = sdl2

[buildozer]
log_level = 2

