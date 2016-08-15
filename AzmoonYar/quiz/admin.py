from django.contrib import admin
from .models import Question, Answer


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['question_date', 'question_text', 'question_type', 'user']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'answer_ques', 'answer_date']


admin.site.register(Question)
admin.site.register(Answer)
