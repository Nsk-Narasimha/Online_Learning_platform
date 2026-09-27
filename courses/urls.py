from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/quiz/', views.quiz_view, name='quiz_view'),
    path('about/', views.about, name='about'),
    path('courses/', views.course_list, name='courses'),
    path('contact/', views.contact, name='contact'), 
    path('courses/', views.course_list, name='course_list'), 

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)