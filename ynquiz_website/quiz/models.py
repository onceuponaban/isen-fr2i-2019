from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    school_field = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    
class Question (models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    question_content = models.CharField(max_length=500)

    class Meta:
        verbose_name = "question"

    def __str__(self):
        return self.question_content

class Answer (models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField('correct answer', default=False)

    class Meta:
        verbose_name = "réponse"

    def __str__(self):
        return self.answer_text
    