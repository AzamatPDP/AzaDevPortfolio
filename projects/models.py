from django.db import models


class Tag(models.Model):
    """Texnologiya teglari (Python, Django, React, etc.)"""
    name = models.CharField(max_length=50, unique=True, verbose_name="Texnologiya nomi")
    color = models.CharField(
        max_length=20,
        default='indigo',
        verbose_name="Rang",
        help_text="Tailwind rang nomi: indigo, emerald, rose, amber, sky, etc."
    )

    class Meta:
        verbose_name = "Texnologiya"
        verbose_name_plural = "Texnologiyalar"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio loyihasi"""
    STATUS_CHOICES = [
        ('completed', 'Tugallangan'),
        ('in_progress', 'Jarayonda'),
        ('archived', 'Arxivlangan'),
    ]

    name = models.CharField(max_length=200, verbose_name="Loyiha nomi")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL slug")
    description = models.TextField(verbose_name="Qisqa tavsif")
    detailed_description = models.TextField(
        blank=True,
        verbose_name="Batafsil tavsif",
        help_text="Loyiha haqida to'liq ma'lumot"
    )
    technologies = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="Texnologiyalar",
        related_name='projects'
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        verbose_name="Loyiha rasmi"
    )
    github_link = models.URLField(blank=True, verbose_name="GitHub linki")
    demo_link = models.URLField(blank=True, verbose_name="Demo linki")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='completed',
        verbose_name="Holati"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Featured (Asosiy)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('project_detail', kwargs={'slug': self.slug})


class Skill(models.Model):
    """Dasturchi mahoratlari"""
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Ma\'lumotlar bazasi'),
        ('devops', 'DevOps'),
        ('tools', 'Vositalar'),
        ('other', 'Boshqa'),
    ]

    name = models.CharField(max_length=100, verbose_name="Mahorat nomi")
    level = models.PositiveIntegerField(
        verbose_name="Daraja (%)",
        help_text="0 dan 100 gacha qiymat kiriting"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='backend',
        verbose_name="Kategoriya"
    )
    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Icon nomi",
        help_text="devicon yoki fa class nomi"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Mahorat"
        verbose_name_plural = "Mahoratlar"
        ordering = ['category', 'order', '-level']

    def __str__(self):
        return f"{self.name} — {self.level}%"


class Contact(models.Model):
    """Sayt orqali kelgan xabarlar"""
    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('read', 'O\'qilgan'),
        ('replied', 'Javob berilgan'),
        ('archived', 'Arxivlangan'),
    ]

    name = models.CharField(max_length=100, verbose_name="Ismi")
    email = models.EmailField(verbose_name="Email manzili")
    subject = models.CharField(max_length=200, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar matni")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Holati"
    )
    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True,
        verbose_name="IP manzil"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject} ({self.created_at.strftime('%d.%m.%Y')})"
