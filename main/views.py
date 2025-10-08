from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def courses(request):
    return render(request, 'main/courses.html')


def course_detail(request):
    return render(request, 'main/course_detail.html')
