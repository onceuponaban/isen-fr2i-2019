from django import forms


class QuizForm(forms.Form):
   
    choice_field = forms.ChoiceField(label='', widget=forms.RadioSelect)
    answerID = ''
