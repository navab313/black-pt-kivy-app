# -*- coding: utf-8 -*-
# ----------------------------------------------------
# 🌟 سیستم پیش‌بینی نمره دانشجو با Kivy 🌟
# مبتنی بر الگوهای ریاضیاتی پیچیده و طبیعی
# ----------------------------------------------------

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.core.window import Window
import math
import os

# تنظیم سایز پنجره
Window.size = (1200, 800)

# ثبت فونت فارسی
FONT_PATH = os.path.join(os.path.dirname(__file__), 'fonts', 'farsi.ttf')
if os.path.exists(FONT_PATH):
    LabelBase.register(name='Persian', fn_regular=FONT_PATH)
    print(f"✅ فونت بارگذاری شد: {FONT_PATH}")
else:
    print(f"⚠️ فونت یافت نشد، از پیش‌فرض استفاده می‌شود")


# تابع تبدیل متن فارسی برای نمایش صحیح
def reshape_text(text):
    """تبدیل متن فارسی برای نمایش RTL"""
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    except ImportError:
        # اگر کتابخانه نصب نباشد، متن را برعکس می‌کنیم
        return text[::-1]


# ----------------------------------------------------
# 1. دیکشنری کامل پایگاه‌های بسیج (22 منطقه)
# ----------------------------------------------------
TEHRAN_BASES = {
    1: ["جنداله", "شهید چمران", "شهدای ولنجک", "صاحب الزمان", "مدافعان ولایت", "ثاراله"],
    2: ["شکاری", "کانون توحید", "شهدای بقیع", "سیادت", "بهشتی", "المهدی", "الزهرا", "شهداء"],
    3: ["شهید بهشتی", "امام خمینی", "حضرت ابوالفضل", "شهید رجایی", "پاسداران", "قائم", "فاطمیه"],
    4: ["امام حسین", "شهید مطهری", "حضرت علی اکبر", "شهدای کهریزک", "پردیسان", "مقاومت"],
    5: ["شهید مدنی", "امام رضا", "شهید صدوقی", "حضرت رقیه", "شهدای عاشورا", "تقوی"],
    6: ["شهید باقری", "امام علی", "انقلاب", "شهدای مصلی", "آزادی", "امین"],
    7: ["شهید کاظمی", "حضرت معصومه", "امام صادق", "شهدای سعدی", "مصباح", "رسالت"],
    8: ["شهید محلاتی", "امام جواد", "شهدای شوش", "حضرت ابوطالب", "مقداد", "نور"],
    9: ["شهید عباسپور", "امام سجاد", "شهدای فردوسی", "حضرت زینب", "راه آسمان", "ولایت"],
    10: ["صاحب الزمان", "شهید همت", "شهید باکری", "شهدای خلیج فارس", "امام زمان", "فتح"],
    11: ["شهید بروجردی", "امام باقر", "شهدای اندیشه", "حضرت فاطمه", "استقلال", "توحید"],
    12: ["شهید فهمیده", "امام کاظم", "شهدای جوانمردان", "حضرت خدیجه", "سرافراز", "شهادت"],
    13: ["شهید شهریاری", "امام موسی", "شهدای صالحین", "حضرت مریم", "پیروزی", "اخلاص"],
    14: ["شهید زین الدین", "امام حسن عسکری", "شهدای قیام", "حضرت معصومه", "عدالت", "وحدت"],
    15: ["مالک اشتر", "حوزه 317", "امام رضا", "شهدای دانشگاه", "شاهد", "علم و دانش"],
    16: ["شهید لشکری", "امام هادی", "شهدای مهر", "حضرت سکینه", "عشاق", "ایثار"],
    17: ["ابوذر", "حوزه 249", "المهدی", "شهدای کن", "صالحین", "استقامت"],
    18: ["شهید تهرانی مقدم", "امام حسن", "شهدای ری", "حضرت زهرا", "شهامت", "بصیرت"],
    19: ["شهید منتظری", "امام محمد باقر", "شهدای عبدل‌آباد", "حضرت عباس", "صبر", "جهاد"],
    20: ["شهید کشوری", "امام موسی صدر", "شهدای فرهنگی", "حضرت ام البنین", "نصرت", "کوثر"],
    21: ["شهید ستاری", "امام جعفر صادق", "شهدای ورامین", "حضرت حکیمه", "عفاف", "حماسه"],
    22: ["دهکده المپیک", "شهرک دانشگاه شریف", "آزاد شهر", "شهید سیروس", "علمدار", "کوثر", "منتظران"]
}


# ----------------------------------------------------
# 2. الگوریتم پیچیده محاسبه نمره (مبتنی بر روابط غیرخطی)
# ----------------------------------------------------
def calculate_grade_advanced(inputs):
    """
    محاسبه نمره با الگوریتم پیچیده ریاضیاتی
    - روابط غیرخطی و تعاملی بین متغیرها
    - منطق طبیعی واقع‌گرایانه
    """

    # استخراج مقادیر با مدیریت خطا
    def safe_float(key, default):
        try:
            return float(inputs.get(key, default))
        except:
            return float(default)

    def safe_int(key, default):
        try:
            return int(inputs.get(key, default))
        except:
            return int(default)

    study_hours = safe_float('study_hours_per_week', 10)
    sleep_hours = safe_float('sleep_hours_per_day', 7)
    attendance = safe_float('attendance_percentage', 90)
    assignments = safe_float('assignments_completed', 0.8)
    past_failures = safe_int('past_failures', 0)
    family_rel = safe_int('famrel', 4)
    substance = safe_int('Substance_Use', 1)

    participation = inputs.get('participation_level', 'Medium')
    internet = inputs.get('internet_access', 'Yes')
    parental_edu = inputs.get('parental_education', 'Bachelor')
    school_support = inputs.get('schoolsup', 'no')

    # --- 1. تابع سیگموئیدی برای ساعات مطالعه (تأثیر غیرخطی) ---
    # کمتر از 5 ساعت: تأثیر منفی قوی
    # 15-25 ساعت: نقطه بهینه
    # بیش از 40 ساعت: بازده کاهشی (burnout)

    optimal_study = 20.0
    study_deviation = abs(study_hours - optimal_study)

    if study_hours < 5:
        study_score = 20 + (study_hours / 5.0) * 15  # 20-35
    elif study_hours < 15:
        study_score = 35 + ((study_hours - 5) / 10.0) * 25  # 35-60
    elif study_hours <= 30:
        study_score = 60 + ((study_hours - 15) / 15.0) * 30  # 60-90
    else:
        # بازده کاهشی برای مطالعه بیش از حد
        excess = study_hours - 30
        study_score = 90 - (excess / 10.0) * 5  # کاهش تدریجی

    study_score = max(20, min(95, study_score))

    # --- 2. تأثیر تعاملی تکالیف × ساعات مطالعه ---
    # اگر ساعت مطالعه کم است، تکالیف بالا کمک نمی‌کند (تقلب محتمل)
    # اگر ساعت مطالعه زیاد است، تکالیف بالا تقویت می‌کند

    assignment_score = assignments * 100  # 0-100

    if study_hours < 5:
        # با مطالعه کم، تکالیف بالا مشکوک است
        assignment_weight = 0.3
    elif study_hours < 10:
        assignment_weight = 0.5
    elif study_hours < 20:
        assignment_weight = 0.8
    else:
        assignment_weight = 1.0

    weighted_assignment = assignment_score * assignment_weight

    # --- 3. تابع لگاریتمی برای حضور ---
    # حضور کمتر از 60% تأثیر منفی شدید
    # حضور بالای 90% تأثیر مثبت قوی

    if attendance < 60:
        attendance_score = 25 + (attendance / 60.0) * 20  # 25-45
    elif attendance < 80:
        attendance_score = 45 + ((attendance - 60) / 20.0) * 25  # 45-70
    else:
        attendance_score = 70 + ((attendance - 80) / 20.0) * 25  # 70-95

    attendance_score = max(25, min(95, attendance_score))

    # --- 4. تأثیر نمایی خواب بر عملکرد شناختی ---
    # خواب بهینه: 7-8 ساعت
    # کم‌خوابی یا پرخوابی: کاهش عملکرد

    optimal_sleep = 7.5
    sleep_diff = abs(sleep_hours - optimal_sleep)

    if sleep_diff < 0.5:
        sleep_multiplier = 1.0
    elif sleep_diff < 1.5:
        sleep_multiplier = 0.95
    elif sleep_diff < 3:
        sleep_multiplier = 0.85
    else:
        sleep_multiplier = 0.70

    # --- 5. تأثیر مرکب سابقه مردودی (تأثیر نمایی) ---
    # هر مردودی تأثیر بیشتری از قبلی دارد
    failure_penalty = 0
    if past_failures > 0:
        failure_penalty = 8 * math.pow(1.5, past_failures - 1)

    failure_penalty = min(failure_penalty, 35)  # حداکثر 35 نمره کسر

    # --- 6. تأثیر مشارکت با ضریب تعاملی ---
    participation_map = {
        'High': 1.15,
        'Medium': 1.0,
        'Low': 0.85
    }
    participation_multiplier = participation_map.get(participation, 1.0)

    # --- 7. تأثیر تحصیلات والدین (غیرخطی) ---
    parental_map = {
        'Master/PhD': 8,
        'Bachelor': 5,
        'High School': 2,
        'Primary': 0,
        'None': -3
    }
    parental_bonus = parental_map.get(parental_edu, 0)

    # --- 8. تأثیر روابط خانوادگی بر تمرکز ---
    family_factor = (family_rel - 1) / 4.0  # 0 تا 1
    family_multiplier = 0.90 + (family_factor * 0.15)  # 0.90 تا 1.05

    # --- 9. تأثیر مواد مخدر (تأثیر شدید و غیرخطی) ---
    substance_penalty = 0
    if substance > 1:
        substance_penalty = 5 * math.pow(1.8, substance - 1)

    substance_penalty = min(substance_penalty, 30)

    # --- 10. بونوس‌های جانبی ---
    internet_bonus = 3 if internet == 'Yes' else -2
    support_bonus = 4 if school_support == 'yes' else 0

    # --- محاسبه نمره نهایی با روابط پیچیده ---

    # میانگین وزنی اصلی (40% study, 25% attendance, 20% assignments)
    base_score = (
            study_score * 0.40 +
            attendance_score * 0.25 +
            weighted_assignment * 0.20 +
            50 * 0.15  # پایه ثابت
    )

    # اعمال ضرایب تعاملی
    adjusted_score = base_score * sleep_multiplier * participation_multiplier * family_multiplier

    # اعمال جریمه‌ها و بونوس‌ها
    final_score = adjusted_score + parental_bonus + internet_bonus + support_bonus
    final_score = final_score - failure_penalty - substance_penalty

    # محدودسازی به بازه 0-100
    final_score = max(0, min(100, final_score))

    return round(final_score, 1)


# ----------------------------------------------------
# 3. ویجت نمودار دایره‌ای پیشرفته
# ----------------------------------------------------
class GaugeWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grade = 0
        self.color = [0, 0.68, 0.94, 1]

    def update_gauge(self, grade, color):
        self.grade = int(grade)
        self.color = color
        self.canvas.clear()

        with self.canvas:
            # پس‌زمینه
            Color(0.15, 0.15, 0.15, 1)
            Rectangle(pos=self.pos, size=self.size)

            # دایره خاکستری پس‌زمینه
            Color(0.25, 0.25, 0.25, 1)
            Line(circle=(self.center_x, self.center_y, dp(80)), width=dp(20))

            # دایره نمره با انیمیشن
            Color(*color)
            angle = (grade / 100.0) * 360
            Line(circle=(self.center_x, self.center_y, dp(80), 90, 90 - angle), width=dp(20))

            # دایره داخلی
            Color(0.2, 0.2, 0.2, 1)
            Ellipse(pos=(self.center_x - dp(60), self.center_y - dp(60)), size=(dp(120), dp(120)))


# ----------------------------------------------------
# 4. لیبل فارسی سفارشی
# ----------------------------------------------------
class PersianLabel(Label):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.text = reshape_text(text)
        self.font_name = 'Persian' if os.path.exists(FONT_PATH) else 'Roboto'
        self.halign = 'right'
        self.valign = 'middle'
        self.bind(size=self._update_text_size)

    def _update_text_size(self, *args):
        self.text_size = (self.width, None)


# ----------------------------------------------------
# 5. رابط کاربری اصلی
# ----------------------------------------------------
class GradePredictorApp(App):
    def build(self):
        self.title = 'Grade Predictor'

        # لی‌اوت اصلی افقی
        main_layout = BoxLayout(orientation='horizontal', padding=dp(15), spacing=dp(15))

        # تنظیم پس‌زمینه
        with main_layout.canvas.before:
            Color(0.12, 0.12, 0.12, 1)
            self.rect = Rectangle(size=Window.size, pos=(0, 0))

        # --- بخش راست: فرم ورودی ---
        right_box = BoxLayout(orientation='vertical', size_hint=(0.45, 1), spacing=dp(10))

        # عنوان فرم
        title = PersianLabel(
            text='اطلاعات دانشجو',
            size_hint=(1, 0.08),
            font_size=dp(22),
            color=[0.2, 0.8, 1, 1],
            bold=True
        )
        right_box.add_widget(title)

        # اسکرول فرم
        scroll = ScrollView(size_hint=(1, 0.92))
        form_layout = GridLayout(cols=1, spacing=dp(8), size_hint_y=None, padding=dp(5))
        form_layout.bind(minimum_height=form_layout.setter('height'))

        # ذخیره ویجت‌ها
        self.inputs = {}

        # تعریف فیلدها
        fields = [
            ('منطقه تهران', 'tehran_region', 'spinner', [str(i) for i in range(1, 23)], '10'),
            ('نام دانشجو', 'student_name', 'text', None, 'دانشجو'),
            ('ساعت مطالعه هفتگی', 'study_hours_per_week', 'text', None, '10'),
            ('تکالیف (0-1)', 'assignments_completed', 'text', None, '0.8'),
            ('ساعت خواب روزانه', 'sleep_hours_per_day', 'text', None, '7'),
            ('درصد حضور', 'attendance_percentage', 'text', None, '90'),
            ('تعداد مردودی', 'past_failures', 'text', None, '0'),
            ('روابط خانواده (1-5)', 'famrel', 'text', None, '4'),
            ('مصرف مواد (1-5)', 'Substance_Use', 'text', None, '1'),
            ('تحصیلات والدین', 'parental_education', 'spinner',
             ['Master/PhD', 'Bachelor', 'High School', 'Primary', 'None'], 'Bachelor'),
            ('مشارکت', 'participation_level', 'spinner',
             ['High', 'Medium', 'Low'], 'Medium'),
            ('اینترنت', 'internet_access', 'spinner',
             ['Yes', 'No'], 'Yes'),
            ('حمایت مدرسه', 'schoolsup', 'spinner',
             ['yes', 'no'], 'no'),
        ]

        for label_text, key, widget_type, options, default in fields:
            # باکس هر فیلد
            field_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(45), spacing=dp(10))

            # برچسب
            lbl = PersianLabel(
                text=label_text,
                size_hint=(0.5, 1),
                font_size=dp(13),
                color=[0.9, 0.9, 0.9, 1]
            )
            field_box.add_widget(lbl)

            # ویجت ورودی
            if widget_type == 'text':
                widget = TextInput(
                    text=default,
                    multiline=False,
                    size_hint=(0.5, 1),
                    font_size=dp(14),
                    background_color=[0.2, 0.2, 0.2, 1],
                    foreground_color=[1, 1, 1, 1],
                    cursor_color=[0.2, 0.8, 1, 1],
                    padding=[dp(10), dp(10)]
                )
                widget.bind(text=self.on_input_change)
            else:
                widget = Spinner(
                    text=default,
                    values=options,
                    size_hint=(0.5, 1),
                    font_size=dp(13),
                    background_color=[0.2, 0.2, 0.2, 1],
                    color=[1, 1, 1, 1]
                )
                widget.bind(text=self.on_input_change)

            self.inputs[key] = widget
            field_box.add_widget(widget)
            form_layout.add_widget(field_box)

        scroll.add_widget(form_layout)
        right_box.add_widget(scroll)

        # --- بخش چپ: نتایج ---
        left_box = BoxLayout(orientation='vertical', size_hint=(0.55, 1), spacing=dp(10))

        # نمودار
        gauge_container = BoxLayout(size_hint=(1, 0.35))
        self.gauge = GaugeWidget(size_hint=(1, 1))
        gauge_container.add_widget(self.gauge)
        left_box.add_widget(gauge_container)

        # نمایش نمره
        self.grade_label = Label(
            text='0',
            font_size=dp(70),
            size_hint=(1, 0.12),
            color=[0.2, 0.8, 1, 1],
            bold=True
        )
        left_box.add_widget(self.grade_label)

        # جدول پایگاه‌ها
        bases_title = PersianLabel(
            text='پایگاه‌های بسیج',
            size_hint=(1, 0.05),
            font_size=dp(16),
            color=[1, 0.8, 0.2, 1],
            bold=True
        )
        left_box.add_widget(bases_title)

        bases_scroll = ScrollView(size_hint=(1, 0.25))
        self.bases_label = PersianLabel(
            text='',
            size_hint_y=None,
            font_size=dp(12),
            color=[0.8, 0.8, 0.8, 1]
        )
        self.bases_label.bind(texture_size=self.bases_label.setter('size'))
        bases_scroll.add_widget(self.bases_label)
        left_box.add_widget(bases_scroll)

        # دکمه محاسبه
        calc_btn = Button(
            text=reshape_text('محاسبه نمره'),
            size_hint=(1, 0.08),
            font_size=dp(18),
            background_color=[0.2, 0.7, 0.3, 1],
            bold=True
        )
        calc_btn.bind(on_press=self.calculate_grade)
        left_box.add_widget(calc_btn)

        # نمایش وضعیت
        self.status_label = PersianLabel(
            text='',
            size_hint=(1, 0.15),
            font_size=dp(13),
            color=[1, 1, 1, 1]
        )
        left_box.add_widget(self.status_label)

        # اضافه به لی‌اوت اصلی
        main_layout.add_widget(right_box)
        main_layout.add_widget(left_box)

        # محاسبه اولیه
        self.calculate_grade(None)
        self.update_bases()

        return main_layout

    def on_input_change(self, instance, value):
        """به‌روزرسانی خودکار"""
        self.calculate_grade(None)
        if instance == self.inputs.get('tehran_region'):
            self.update_bases()

    def update_bases(self):
        """به‌روزرسانی لیست پایگاه‌ها"""
        try:
            region = int(self.inputs['tehran_region'].text)
            bases = TEHRAN_BASES.get(region, [])

            if bases:
                text = '\n'.join([f'• {base}' for base in bases])
            else:
                text = 'اطلاعات پایگاه موجود نیست'

            self.bases_label.text = reshape_text(text)
        except:
            self.bases_label.text = reshape_text('منطقه نامعتبر')

    def calculate_grade(self, instance):
        """محاسبه و نمایش نمره"""
        try:
            inputs = {key: widget.text for key, widget in self.inputs.items()}
            grade = calculate_grade_advanced(inputs)

            # تعیین رنگ
            if grade >= 85:
                color = [0.2, 0.8, 0.3, 1]
                msg = 'عالی! 🏆'
            elif grade >= 70:
                color = [0.2, 0.7, 1, 1]
                msg = 'خوب ⭐'
            elif grade >= 50:
                color = [1, 0.8, 0.2, 1]
                msg = 'متوسط 💡'
            else:
                color = [1, 0.3, 0.2, 1]
                msg = 'ضعیف ⚠️'

            # به‌روزرسانی نمایش
            self.grade_label.text = str(int(grade))
            self.grade_label.color = color
            self.gauge.update_gauge(grade, color)

            name = inputs.get('student_name', 'دانشجو')
            status_text = f'نمره {name}: {int(grade)}/100\n{msg}'
            self.status_label.text = reshape_text(status_text)
            self.status_label.color = color

        except Exception as e:
            self.status_label.text = reshape_text(f'خطا: {str(e)}')
            self.status_label.color = [1, 0.3, 0.2, 1]


# ----------------------------------------------------
# اجرا
# ----------------------------------------------------
if __name__ == '__main__':
    GradePredictorApp().run()