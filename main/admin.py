from django.contrib import admin
from .models import Course, Module, Lesson, Slide


# --- Слайды внутри урока ---
class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1
    fields = ('order', 'content')
    ordering = ('order',)
    verbose_name = "Слайд"
    verbose_name_plural = "Слайды"


# --- Уроки внутри модуля ---
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ('order', 'title', 'description')
    ordering = ('order',)
    show_change_link = True
    verbose_name = "Урок"
    verbose_name_plural = "Уроки"


# --- Модули внутри курса ---
class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    fields = ('order', 'title', 'description')
    ordering = ('order',)
    show_change_link = True
    verbose_name = "Раздел"
    verbose_name_plural = "Разделы"


# --- Админка курса ---
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    inlines = [ModuleInline]


# --- Админка модуля ---
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'description')
    inlines = [LessonInline]


# --- Админка урока ---
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order')
    list_filter = ('module',)
    search_fields = ('title', 'description')
    inlines = [SlideInline]


# --- Админка слайда ---
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'order', 'short_content')

    def short_content(self, obj):
        return (obj.content[:70] + '...') if len(obj.content) > 70 else obj.content

    short_content.short_description = "Контент (обрезано)"
