from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class Question (models.Model):
    question_text = models.TextField()
    url_slug = models.SlugField(null=True)
    # slug creator function

    def slug_creator(strings):
        None

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
    question_difficulty = models.IntegerField(validators=[valid_rate], default=0)

    # lesson validator function
    def valid_lessons(name):
        lesson_names = ("دین و زندگی", "انگلیسی", "فیزیک", "شیمی", "ریاضی",
                        "هندسه", "حساب دیفرانسیل و انتگرال", "ادبیات فارسی",
                        "زبان فارسی")
        if not name in lesson_names:
            raise ValidationError('%(name) is not a valid lesson name', params={'name': name})
        # TODO: completing the function
    # end of function

    lesson = models.CharField(max_length=50, validators=[valid_lessons], default="ریاضی")

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.lesson + ":" + self.question_text[:10]


class Answer(models.Model):
    answer_text = models.TextField()
    answer_ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_date = models.DateTimeField('last edit')
    answer_uploader = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer_rate = models.IntegerField(validators=[Question.valid_rate], default=0)

    def __str__(self):
        return self.answer_ques.question_text[:10] + self.answer_text[:10]
