from django.db import models

# Create your models here.
class QuestionDb(models.Model):
    Question=models.CharField(max_length=200)
    option_a=models.CharField(max_length=200)
    option_b=models.CharField(max_length=200)
    option_c=models.CharField(max_length=200)
    option_d=models.CharField(max_length=200)
    correct_answer=models.CharField(max_length=200)
class SubmissionDb(models.Model):
    student_name=models.CharField(max_length=100)
    Question_id=models.ForeignKey(QuestionDb,on_delete=models.CASCADE,related_name='submission')
    Selected_answer=models.CharField(max_length=500)
    submitted_at=models.DateTimeField(auto_now_add=True)