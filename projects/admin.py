from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Skill, Contact, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'project_count']
    search_fields = ['name']

    def project_count(self, obj):
        count = obj.projects.count()
        return format_html('<span style="color:#6366f1;font-weight:bold">{}</span>', count)
    project_count.short_description = "Loyihalar soni"


class TagInline(admin.TabularInline):
    model = Project.technologies.through
    extra = 1
    verbose_name = "Texnologiya"
    verbose_name_plural = "Texnologiyalar"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'is_featured', 'order', 'preview_image', 'created_at']
    list_filter = ['status', 'is_featured', 'technologies']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured', 'order', 'status']
    filter_horizontal = ['technologies']
    readonly_fields = ['created_at', 'updated_at', 'preview_image']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'slug', 'description', 'detailed_description', 'status', 'is_featured', 'order')
        }),
        ('Media va Linklar', {
            'fields': ('image', 'preview_image', 'github_link', 'demo_link')
        }),
        ('Texnologiyalar', {
            'fields': ('technologies',)
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:80px;height:50px;object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return format_html('<span style="color:#6b7280;font-style:italic">Rasm yo\'q</span>')
    preview_image.short_description = "Ko'rinish"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level_bar', 'order']
    list_filter = ['category']
    list_editable = ['order']
    search_fields = ['name']
    ordering = ['category', 'order']

    def level_bar(self, obj):
        color = '#6366f1' if obj.level >= 80 else '#10b981' if obj.level >= 60 else '#f59e0b'
        return format_html(
            '<div style="display:flex;align-items:center;gap:8px;">'
            '<div style="width:120px;background:#374151;border-radius:4px;height:8px;">'
            '<div style="width:{}%;background:{};border-radius:4px;height:8px;"></div>'
            '</div>'
            '<span style="color:{};font-weight:bold;">{}%</span>'
            '</div>',
            obj.level, color, color, obj.level
        )
    level_bar.short_description = "Daraja"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'ip_address', 'created_at']
    list_editable = ['status']

    def has_add_permission(self, request):
        return False

    fieldsets = (
        ('Jo\'natuvchi', {
            'fields': ('name', 'email', 'ip_address', 'created_at')
        }),
        ('Xabar', {
            'fields': ('subject', 'message')
        }),
        ('Holati', {
            'fields': ('status',)
        }),
    )


# Admin saytini sozlash
admin.site.site_header = "Portfolio Admin Paneli"
admin.site.site_title = "Portfolio"
admin.site.index_title = "Boshqaruv Paneli"
