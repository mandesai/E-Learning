"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views, user_login
from django.conf import settings  # Import settings module
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', user_login.REGISTER, name = 'register'),
    path('doLogin', user_login.DO_LOGIN, name="doLogin"),
    path('upload_course/', views.upload_course, name='upload_course'), 
    path('course/<int:pk>/detail/', views.course_detail, name='course_detail'),
    path('course/<int:pk>/overview/', views.course_overview, name='course_overview'),
    path('course/<int:course_id>/', views.quiz_detail, name='quiz_detail'),
    path('assign-quiz/', views.assign_quiz, name='assign_quiz'),
    path('upload/', views.upload_result, name='upload_result'),
    path('upload_assignment/', views.upload_assignment_result, name='upload_assignment_result'),
    path('result/<int:student_id>/', views.view_result, name='view_result'),
    path('result/&lt;int:student_id&gt;/', views.view_result, name='view_result'),
    path('student_results/', views.student_results, name='student_results'),
    path('create/', views.create_payout_statement, name='create_payout_statement'),
    path('list/', views.payout_statement_list, name='payout_statement_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)