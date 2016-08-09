from django.db import models
from django.core.exceptions import ValidationError
# from django.conf import settings
# from random import randint


# models here:

class Question (models.Model):
    text = models.TextField()
    url_slug = models.SlugField(allow_unicode=True, null=True)

    def save(self, *args, **kwargs):
        self.url_slug = self.lesson + "-" + self.question_types[type] + str(hash(self.question_text))  # TODO: incorrect
        super(Question, self).save(*args, **kwargs)




    # slug creator helper!!
    #def slug_helper(string):
     #   list = []
      #  counter = 0
       # for i in len(string):
        #    if string[i] == " ":
         #       list.append(string[counter:i])
          #      counter = i + 1

    # slug creator function
    # def slug_creator(strings):
    #    nemidonam = None

    publish_date = models.DateTimeField('date submitted', null=True)
    draft_date = models.DateTimeField('date drafted', null=True)
    # publish or draft choice list
    publish = "Publish"
    draft = "Draft"
    pubdr_choices = (
        (publish, "انتشار"),
        (draft, "چرک نویس"),
    )

    pubdr = models.CharField(choices=pubdr_choices, default=publish)
    # end of publish or draft

    # the definition of types of the question
    multi_choice_question = "Multi"
    descriptive_question = "Descriptive"
    blank_question = "Blank"
    true_false_question = "TrueFlase"
    question_types = (
        (multi_choice_question, "چند گزینه ای"),
        (descriptive_question, "تشریحی"),
        (blank_question, "جای خالی"),
        (true_false_question, "صحیح غلط")
    )
    # end of definition

    type = models.CharField(max_length=20, choices=question_types, default=descriptive_question)

    # rate validation function
    def valid_rate(number):
        if (number < 0) or (number >= 5):
            raise ValidationError('%(number) is not in range 0 to 5',
                                  params={'number': number},
                                  )
    # end of function
    rate = models.IntegerField(validators=[valid_rate], default=0)
    difficulty = models.IntegerField(validators=[valid_rate], default=0)

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

    user = models.CharField(max_length=50)  # TODO: should get from request.uer

    def __str__(self):
        return self.lesson + ":" + self.question_text[:10]

    class Meta:
        ordering = ("-question_date",)


class Answer(models.Model):
    text = models.TextField()
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateTimeField('last edit', auto_now=True)
    uploader = models.CharField(max_length=50)
    rate = models.IntegerField(validators=[Question.valid_rate], default=0)

    def __str__(self):
        return self.answer_ques.question_text[:10] + self.answer_text[:10]
