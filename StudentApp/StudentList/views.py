from django.shortcuts import render
from .models import StudentInfo

def student_list(request):
    students = StudentInfo.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student/student_list.html', context)

def student_detail_info(request, std_id):
    student_info = StudentInfo.objects.get(pk=std_id)

    context = {
        'student_info': student_info
    }
    return render(request, 'student/student_detail.html', context)