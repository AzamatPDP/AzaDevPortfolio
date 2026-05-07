# 🚀 Django Portfolio — O'rnatish va Ishga Tushirish

## Loyiha Arxitekturasi

```
portfolio/
├── manage.py
├── requirements.txt
├── portfolio/                 # Asosiy Django konfig
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── projects/                  # Asosiy app
│   ├── models.py             # Project, Skill, Contact, Tag
│   ├── views.py              # home(), project_detail()
│   ├── urls.py               # URL marshrutlar
│   ├── admin.py              # Maxsus admin panel
│   ├── forms.py              # ContactForm
│   └── management/
│       └── commands/
│           └── populate_demo.py
├── templates/
│   ├── base.html             # Asosiy layout (nav + footer)
│   └── projects/
│       ├── home.html         # Asosiy sahifa
│       └── project_detail.html
├── static/
│   ├── css/
│   └── js/
└── media/                    # Yuklangan rasmlar
```

---

## 🛠️ O'rnatish

### 1. Virtual muhit yarating
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 2. Kutubxonalarni o'rnating
```bash
pip install -r requirements.txt
```

### 3. Ma'lumotlar bazasini sozlang
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Superuser yarating (Admin uchun)
```bash
python manage.py createsuperuser
```

### 5. Demo ma'lumotlar yuklang (ixtiyoriy)
```bash
python manage.py populate_demo
```

### 6. Serverni ishga tushiring
```bash
python manage.py runserver
```

---

## 🌐 URL Manzillar

| URL | Tavsif |
|-----|--------|
| `http://127.0.0.1:8000/` | Asosiy sahifa |
| `http://127.0.0.1:8000/projects/<slug>/` | Loyiha detail |
| `http://127.0.0.1:8000/admin/` | Admin panel |

---

## ⚙️ Admin Paneli

Admin panelidan quyidagilarni boshqarish mumkin:

- **Loyihalar** — qo'shish, tahrirlash, rasm yuklash, featured belgilash
- **Texnologiyalar** — teg rangi va nomi
- **Mahoratlar** — kategoriya va foiz darajasi
- **Xabarlar** — contact formadan kelgan xabarlar

---

## 🎨 Dizayn Xususiyatlari

- **Dark Theme** — #030712 asosiy fon
- **Tailwind CSS CDN** — CDN orqali ulangan
- **Space Grotesk** font — sarlavhalar uchun
- **JetBrains Mono** — kod qismlari uchun
- **Scroll animatsiyalar** — Intersection Observer API
- **Skill bar animatsiya** — CSS transition
- **Responsive** — Mobile-first dizayn

---

## 📦 Ishlatilgan Texnologiyalar

- **Backend:** Django 4.2, Python 3.x
- **Frontend:** Tailwind CSS (CDN), Vanilla JS
- **Database:** SQLite (development), PostgreSQL (production)
- **Media:** Django Pillow (rasm yuklash)
- **Fonts:** Google Fonts (Space Grotesk, DM Sans, JetBrains Mono)

---

## 🚀 Production uchun

Production muhitida quyidagilarni o'zgartiring:

```python
# settings.py
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['yourdomain.com']

# PostgreSQL database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
