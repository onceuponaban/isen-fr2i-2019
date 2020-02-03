from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Question, Answer

admin.site.register(User, UserAdmin)

class AnswersInline(admin.StackedInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswersInline,
    ]


#admin.site.register(Question)
#admin.site.register(Answer)