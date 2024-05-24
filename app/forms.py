# forms.py
from django import forms
from .models import Result, AssignmentResult, PayoutStatement

# class AssignQuizForm(forms.Form):
#     course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Select Course")
#     quiz = forms.ModelChoiceField(queryset=Quiz.objects.all(), label="Select Quiz")
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'quiz', 'score']

class AssignmentResultForm(forms.ModelForm):
    class Meta:
        model = AssignmentResult
        fields = ['student', 'assignment', 'score']

class PayoutStatementForm(forms.ModelForm):
    class Meta:
        model = PayoutStatement
        fields = ['payment_details', 'image']