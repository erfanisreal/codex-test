# لیست کارها با جنگو

پروژه آموزشی ساده با رابط فارسی: افزودن، تغییر وضعیت و حذف کارها. داده‌ها در SQLite ذخیره می‌شوند.

## اجرا

Python 3.10 یا جدیدتر لازم است. در پوشه پروژه:

```bash
python -m venv .venv
```

ویندوز (Command Prompt):

```bat
.venv\Scripts\activate
```

لینوکس و مک:

```bash
source .venv/bin/activate
```

سپس:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

صفحه برنامه: http://127.0.0.1:8000/

ساخت مدیر اختیاری: `python manage.py createsuperuser`؛ سپس `/admin/`.

## بررسی

```bash
python manage.py check
python manage.py test
```

## تنظیمات

این پروژه برای اجرای محلی و یادگیری است. کارها بین تمام بازدیدکنندگان مشترک‌اند و ورود کاربری ندارند.
برای استقرار واقعی، `DJANGO_SECRET_KEY` را تنظیم کنید، `DJANGO_DEBUG=0` بگذارید و دامنه‌ها را در `DJANGO_ALLOWED_HOSTS` با کاما جدا کنید. از وب‌سرور مناسب استقرار و HTTPS استفاده کنید.
