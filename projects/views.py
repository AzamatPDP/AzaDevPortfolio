from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Skill, Contact
from .forms import ContactForm


def home(request):
    """Asosiy sahifa — barcha loyihalar va mahoratlar"""
    projects = Project.objects.prefetch_related('technologies').all()
    featured_projects = projects.filter(is_featured=True)
    all_projects = projects

    # Mahoratlarni kategoriya bo'yicha guruhlash
    skills = Skill.objects.all()
    skill_categories = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skill_categories:
            skill_categories[cat] = []
        skill_categories[cat].append(skill)

    # Contact formasi
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            # IP manzilini saqlash
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                contact.ip_address = x_forwarded_for.split(',')[0]
            else:
                contact.ip_address = request.META.get('REMOTE_ADDR')
            contact.save()
            messages.success(request, "✅ Xabaringiz muvaffaqiyatli yuborildi! Tez orada javob beraman.")
            return redirect('home')
        else:
            messages.error(request, "❌ Xatolik yuz berdi. Iltimos, maydonlarni to'g'ri to'ldiring.")
    else:
        form = ContactForm()

    context = {
        'featured_projects': featured_projects,
        'all_projects': all_projects,
        'skill_categories': skill_categories,
        'form': form,
        'total_projects': all_projects.count(),
        'total_skills': skills.count(),
    }
    return render(request, 'projects/home.html', context)


def project_detail(request, slug):
    """Loyiha detail sahifasi"""
    project = get_object_or_404(
        Project.objects.prefetch_related('technologies'),
        slug=slug
    )

    # O'xshash loyihalar (bir xil texnologiyalar)
    project_tags = project.technologies.all()
    related_projects = Project.objects.filter(
        technologies__in=project_tags
    ).exclude(pk=project.pk).distinct()[:3]

    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)
