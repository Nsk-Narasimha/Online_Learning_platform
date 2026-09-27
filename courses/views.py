
from django.shortcuts import render, get_object_or_404
from .models import Course,Lesson,Quiz
from django.conf import settings
from django.http import FileResponse, Http404
from pathlib import Path

def serve_media(request, path):
    media_root = Path(settings.MEDIA_ROOT).resolve()
    file_path = (media_root / path).resolve()

    if not file_path.is_relative_to(media_root):
        raise Http404("Invalid media path")

    if not file_path.is_file():
        raise Http404("Media file not found")

    return FileResponse(open(file_path, "rb"))

def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all() 
    return render(request, 'courses/coursedetail.html', {'course': course, 'lessons': lessons,
})

def about(request):
    return render(request, 'courses/about.html')

def contact(request):
    return render(request, 'courses/contact.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def quiz_view(request, lesson_id):
    quiz = get_object_or_404(Lesson, id=lesson_id)
    
    quiz = get_object_or_404(Quiz, lesson_id=lesson_id)
    
    return render(request, 'courses/quiz.html', {'quiz': quiz})
