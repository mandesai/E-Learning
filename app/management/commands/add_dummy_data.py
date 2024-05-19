from django.core.management.base import BaseCommand
from app.models import Student, Quiz, Result, Assignment, AssignmentResult

class Command(BaseCommand):
    help = 'Add dummy data to the database'

    def handle(self, *args, **kwargs):
        # Create some students
        student1 = Student.objects.create(name='Alice')
        student2 = Student.objects.create(name='Bob')
        student3 = Student.objects.create(name='Charlie')

        # Create a quiz
        quiz = Quiz.objects.create(title='Sample Quiz', total_score=10)

        # Create results for the students
        Result.objects.create(student=student1, quiz=quiz, score=8)
        Result.objects.create(student=student2, quiz=quiz, score=6)
        Result.objects.create(student=student3, quiz=quiz, score=9)

        # Create assignments
        assignment1 = Assignment.objects.create(title='Assignment 1', total_score=100)
        assignment2 = Assignment.objects.create(title='Assignment 2', total_score=100)

        # Create assignment results for the students
        AssignmentResult.objects.create(student=student1, assignment=assignment1, score=85)
        AssignmentResult.objects.create(student=student2, assignment=assignment1, score=75)
        AssignmentResult.objects.create(student=student3, assignment=assignment1, score=95)
        
        AssignmentResult.objects.create(student=student1, assignment=assignment2, score=88)
        AssignmentResult.objects.create(student=student2, assignment=assignment2, score=78)
        AssignmentResult.objects.create(student=student3, assignment=assignment2, score=98)

        self.stdout.write(self.style.SUCCESS('Dummy data added successfully'))
