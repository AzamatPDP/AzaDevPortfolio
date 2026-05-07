"""
Demo ma'lumotlarini bazaga yuklash uchun management command.
Ishlatish: python manage.py populate_demo
"""
from django.core.management.base import BaseCommand
from projects.models import Project, Skill, Tag


class Command(BaseCommand):
    help = 'Demo ma\'lumotlarini bazaga yuklaydi'

    def handle(self, *args, **kwargs):
        self.stdout.write('Demo ma\'lumotlar yuklanmoqda...')

        # Texnologiya teglari
        tags_data = [
            ('Python', 'indigo'), ('Django', 'emerald'), ('React', 'sky'),
            ('PostgreSQL', 'blue'), ('Docker', 'sky'), ('REST API', 'violet'),
            ('JavaScript', 'amber'), ('Tailwind CSS', 'teal'), ('Redis', 'rose'),
            ('Celery', 'orange'), ('AWS', 'amber'), ('Git', 'orange'),
        ]
        tags = {}
        for name, color in tags_data:
            tag, _ = Tag.objects.get_or_create(name=name, defaults={'color': color})
            tags[name] = tag

        # Loyihalar
        projects = [
            {
                'name': 'E-Commerce Platform',
                'slug': 'e-commerce-platform',
                'description': 'Django REST Framework va React asosidagi to\'liq funksional elektron tijorat platformasi.',
                'detailed_description': 'Bu loyiha Django REST Framework backend va React frontend yordamida yaratilgan. Foydalanuvchi autentifikatsiyasi, mahsulot katalogi, savat va to\'lov tizimi mavjud. Redis kesh va Celery orqali asinxron vazifalar bajariladi.',
                'github_link': 'https://github.com',
                'demo_link': 'https://example.com',
                'status': 'completed',
                'is_featured': True,
                'order': 1,
                'techs': ['Python', 'Django', 'React', 'PostgreSQL', 'Redis'],
            },
            {
                'name': 'Task Management API',
                'slug': 'task-management-api',
                'description': 'JWT autentifikatsiya va real-time bildirishnomalar bilan to\'liq RESTful API.',
                'detailed_description': 'Django REST Framework yordamida yaratilgan task management API. JWT autentifikatsiya, permission system, filter va search imkoniyatlari mavjud. Swagger orqali dokumentatsiyalangan.',
                'github_link': 'https://github.com',
                'demo_link': '',
                'status': 'completed',
                'is_featured': True,
                'order': 2,
                'techs': ['Python', 'Django', 'PostgreSQL', 'REST API', 'Docker'],
            },
            {
                'name': 'Portfolio CMS',
                'slug': 'portfolio-cms',
                'description': 'Dasturchilar uchun Django asosidagi maxsus content management tizimi.',
                'detailed_description': 'Bu aynan ushbu portfolio saytining o\'zi! Django, Tailwind CSS va PostgreSQL asosida qurilgan. Admin panel orqali to\'liq boshqarish imkoniyati mavjud.',
                'github_link': 'https://github.com',
                'demo_link': 'https://example.com',
                'status': 'completed',
                'is_featured': False,
                'order': 3,
                'techs': ['Python', 'Django', 'Tailwind CSS'],
            },
            {
                'name': 'Real-time Chat App',
                'slug': 'realtime-chat-app',
                'description': 'Django Channels va WebSocket texnologiyasi yordamida qurilgan real-time chat ilovasi.',
                'detailed_description': 'Django Channels orqali WebSocket ulanish, xona tizimi, foydalanuvchi holati ko\'rsatgichi mavjud. Redis orqali channel layer sozlangan.',
                'github_link': 'https://github.com',
                'demo_link': '',
                'status': 'in_progress',
                'is_featured': False,
                'order': 4,
                'techs': ['Python', 'Django', 'Redis', 'JavaScript'],
            },
        ]

        for p_data in projects:
            techs = p_data.pop('techs')
            project, created = Project.objects.get_or_create(
                slug=p_data['slug'],
                defaults=p_data
            )
            for tech_name in techs:
                if tech_name in tags:
                    project.technologies.add(tags[tech_name])
            status = "yaratildi" if created else "allaqachon mavjud"
            self.stdout.write(f"  ✓ {project.name} — {status}")

        # Mahoratlar
        skills_data = [
            ('Python', 95, 'backend'), ('Django', 90, 'backend'),
            ('Django REST Framework', 88, 'backend'), ('PostgreSQL', 82, 'database'),
            ('Redis', 75, 'database'), ('Docker', 78, 'devops'),
            ('Git', 90, 'tools'), ('Linux', 80, 'devops'),
            ('JavaScript', 75, 'frontend'), ('React', 70, 'frontend'),
            ('Tailwind CSS', 85, 'frontend'), ('HTML/CSS', 90, 'frontend'),
            ('Celery', 72, 'backend'), ('AWS', 65, 'devops'),
        ]

        for name, level, category in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=name,
                defaults={'level': level, 'category': category}
            )
            if created:
                self.stdout.write(f"  ✓ Skill: {name} ({level}%)")

        self.stdout.write(self.style.SUCCESS('\n✅ Demo ma\'lumotlar muvaffaqiyatli yuklandi!'))
        self.stdout.write(self.style.WARNING('Admin: python manage.py createsuperuser'))
