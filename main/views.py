from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Slide


def home(request):
    return render(request, 'main/home.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'main/courses.html', {'all_courses': all_courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = course.modules.prefetch_related('lessons')
    
    context = {
        'course': course,
        'modules': modules,
    }
    return render(request, 'main/course_detail.html', context)


def lesson_view(request, lesson_id, slide_order):
    lesson = Lesson.objects.get(pk=lesson_id)
    module = lesson.module
    course = module.course
    slides = list(lesson.slides.all())
    current_slide = next((s for s in slides if s.order == slide_order), None)
    
    modules = list(course.modules.all())
    
    # ищем следующий урок в текущем разделе
    lessons_in_module = list(module.lessons.all())
    next_lesson = None
    for l in lessons_in_module:
        if l.order > lesson.order:
            next_lesson = l
            break
    
    # если уроков больше нет — ищем следующий модуль
    next_module = None
    next_module_first_lesson = None
    if not next_lesson:
        for m in modules:
            if m.order > module.order:
                next_module = m
                next_module_first_lesson = m.lessons.first()
                break
    
    context = {
        'lesson': lesson,
        'course': course,
        'modules': modules,
        'slides': slides,
        'current_slide': current_slide,
        'next_lesson': next_lesson,
        'next_module': next_module,
        'next_module_first_lesson': next_module_first_lesson,
    }
    
    return render(request, 'main/lesson.html', context)


def console(request):
    return render(request, 'main/console.html')
