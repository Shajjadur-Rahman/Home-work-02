from django.urls import path
from . import views

app_name = 'Students'

urlpatterns = [
    path('student-list/', views.student_list, name='student-list'),
    path('student-detail/<int:std_id>', views.student_detail_info, name='student-detail'),
]