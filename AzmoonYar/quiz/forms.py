from django import forms


class UploadForm (forms.ModelForm):
    text = forms.CharField(label="متن سوال", widget=forms.Textarea)
    answer = forms.CharField(label="متن پاسخ", widget=forms.Textarea)

    # define choices for question type
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

    type = forms.CharField(max_length=20, choices=question_types, default=descriptive_question)

    # define question difficulty
    very_hard = 5
    hard = 4
    normal = 3
    easy = 2
    very_easy = 1
    difficulty_types = (
        (very_hard, "خیلی سخت"),
        (hard, "سخت"),
        (normal, "متوسط"),
        (easy, "آسان"),
        (very_easy, "خیلی آسان"),
    )
    # end of definition

    difficulty = forms.ChoiceField(choices=difficulty_types)

    # define situation of whole article
    publish = "Publish"
    draft = "Draft"
    situation_choices = (
        (publish, "انتشار"),
        (draft, "چرک نویس"),
    )
    # end of definition

    situation = forms.CharField(choices=situation_choices)
    lesson = forms.CharField(label="نام درس", max_length=30)