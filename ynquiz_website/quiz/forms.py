from django import forms
from .models import User

class QuizForm(forms.Form):
   
    choice_field = forms.ChoiceField(label='', widget=forms.RadioSelect)
    answerID = ''


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('is_student','is_teacher')


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('is_student','is_teacher','score')