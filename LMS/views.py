from django.shortcuts import redirect, render, get_object_or_404
from app.forms import ResultForm, AssignmentResultForm, PayoutStatementForm
from app.models import Course, Student, Result, AssignmentResult, PayoutStatement

def BASE(request):
    uploaded_courses = Course.objects.all()
    return render(request, 'base.html', {'uploaded_courses': uploaded_courses})

def upload_course(request):
    if request.method == 'POST':
        # Get form data
        course_code = request.POST['course_code']
        course_title = request.POST['course_title']
        course_description = request.POST['course_description']
        course_category = request.POST['course_category']
        course_duration = request.POST['course_duration']
        course_level = request.POST['course_level']
        course_price = request.POST['course_price']
        course_image = request.FILES['course_image']
        course_video = request.FILES['course_video']
        course_quizzes = request.FILES.getlist('course_quizzes')
        course_assignments = request.FILES.getlist('course_assignments')
        course_materials = request.FILES.getlist('course_materials')

        # Save course to database
        course = Course.objects.create(
            code=course_code,
            title=course_title,
            description=course_description,
            category=course_category,
            duration=course_duration,
            level=course_level,
            price=course_price,
            image=course_image,
            video=course_video
        )
        for material in course_materials:
            course.materials.create(file=material)
        for quiz in course_quizzes:
            course.quizzes.create(file=quiz)
        for assignment in course_assignments:
            course.assignments.create(file=assignment)

        # Redirect to My Courses page
        return redirect('base')
    else:
        uploaded_courses = Course.objects.all()
        return render(request, 'upload_course.html', {'uploaded_courses': uploaded_courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

def course_overview(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_overview.html', {'course': course})

def delete_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')  # Assuming you pass the course ID via POST request
        course = get_object_or_404(Course, pk=course_id)
        course.delete()
        return redirect('base')  # Redirect to base or any other page
    return redirect('base')  # Redirect to base if request method is not POST


def quiz_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    student_count = course.students.count()
    quiz_results = QuizResult.objects.filter(quiz__course=course)
    # You can manipulate quiz_results as needed to display
    # the quiz results for each student
    return render(request, 'quiz_detail.html', {'course': course, 'student_count': student_count, 'quiz_results': quiz_results})

def assign_quiz(request):
    if request.method == 'POST':
        form = AssignQuizForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            quiz = form.cleaned_data['quiz']
            students = course.students.all()  # Get all students in the selected course
            
            # Assign the quiz to each student
            for student in students:
                QuizResult.objects.create(student=student, quiz=quiz, score=0.0)  # Default score is 0.0

            return redirect('quiz_detail', course_id=course.id)
    else:
        form = AssignQuizForm()
    
    return render(request, 'assign_quiz.html', {'form': form})

def upload_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html')
    else:
        form = ResultForm()
    return render(request, 'upload_result.html', {'form': form})

def upload_assignment_result(request):
    if request.method == 'POST':
        form = AssignmentResultForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html')
    else:
        form = AssignmentResultForm()
    return render(request, 'upload_assignment_result.html', {'form': form})

def view_result(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    results = Result.objects.filter(student=student)
    assignment_results = AssignmentResult.objects.filter(student=student)
    return render(request, 'view_result.html', {'student': student, 'results': results})

def student_results(request):
    results = Result.objects.all().select_related('student', 'quiz')
    assignment_results = AssignmentResult.objects.all().select_related('student', 'assignment')
    return render(request, 'student_results.html', {'results': results, 'assignment_results': assignment_results})

def create_payout_statement(request):
    if request.method == 'POST':
        form = PayoutStatementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payout_statement_list')
        else:
            print(form.errors) 
    else:
        form = PayoutStatementForm()
    return render(request, 'create_payout_statement.html', {'form': form})

def payout_statement_list(request):
    payouts = PayoutStatement.objects.all()
    return render(request, 'payout_statement_list.html', {'payouts': payouts})
