from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


# models here:

class Question (models.Model):
    question_text = models.TextField()
    question_date = models.DateTimeField('date submitted')

    # the definition of types of the question
    multi_choice_question = "MC"
    descriptive_question = "DES"
    blank_question = "BLK"
    true_false_question = "TF"
    question_types = (
        (multi_choice_question, "چند گزینه ای"),
        (descriptive_question, "تشریحی"),
        (blank_question, "جای خالی"),
        (true_false_question, "صحیح غلط")
    )
    # end of definition

    question_type = models.CharField(max_length=20, choices=question_types, default=descriptive_question)

    # rate validation function
    def valid_rate(number):
        if (number < 0) or (number > 5):
            raise ValidationError(('%(number) is not in range 0 to 5'),
            params={'number': number},
        )
    # end of function
    question_rate = models.IntegerField(validators=[valid_rate], default=0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Answer(models.Model):
    answer_text = models.TextField()
    answer_ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_date = models.DateTimeField('last edit')
    answer_uploader = None
    answer_rate = models.IntegerField(validators=[Question.valid_rate], default=0)
