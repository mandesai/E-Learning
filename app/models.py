from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Course(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=(
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('business', 'Business'),
        # Add more categories as needed
    ))
    duration = models.IntegerField()  # Duration in hours
    level = models.CharField(max_length=100, choices=(
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ))
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='course_images/')
    video = models.FileField(upload_to='course_videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})

class Material(models.Model):
    course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Quiz(models.Model):
    title = models.CharField(max_length=100, default="Title")
    total_score = models.IntegerField(default=10)
    course = models.ForeignKey(Course, related_name='quizzes', on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_quizzes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    title = models.CharField(max_length=100, default="Title")
    total_score = models.IntegerField(default=100)
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_assignments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100, default="abc")

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.quiz.title} - {self.score}'

class AssignmentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.student.name} - {self.assignment.title} - {self.score}'

class PayoutStatement(models.Model):
    payment_details = models.CharField(max_length=200)
    image = models.ImageField(upload_to='payout_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_details