from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User
from .models import Question, Answer

class AnswersInline(admin.StackedInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswersInline,
    ]


#admin.site.register(Question)
#admin.site.register(Answer)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_student', 'is_teacher', 'is_staff')
    list_filter = ('is_student','is_teacher', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('is_student','is_teacher',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)