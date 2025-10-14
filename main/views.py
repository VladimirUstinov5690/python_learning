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


def lesson_view(request, lesson_id, slide_order=1):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    slides = lesson.slides.all()
    current_slide = slides.filter(order=slide_order).first()
    
    context = {
        'lesson': lesson,
        'module': lesson.module,
        'course': lesson.module.course,
        'modules': lesson.module.course.modules.all(),
        'slides': slides,
        'current_slide': current_slide,
    }
    return render(request, 'main/lesson.html', context)
