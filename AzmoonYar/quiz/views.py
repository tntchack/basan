from django.shortcuts import render
# from django.http import HttpRequest
from .forms import UploadForm, ExamCreator
from .models import Question, Answer
from django.utils import timezone, text

# Create your views here.


def uploader(request):
    # string fo list function
    def str_to_list(string):
        str_list = []
        counter = 0
        for i in range(len(string)):
            if string[i] == " ":
                str_list.append(string[counter:i])
                counter = i + 1
        return str_list
    # end of function

    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form_clean = form.cleaned_data
            form_text = str_to_list(form_clean['text'])
            questions = Question.objects.all()
            same_counter = 0
            for question in questions:
                for item in form_text:
                    if item in str_to_list(question.text):  # TODO: should use str_to_list??
                        same_counter += 1
                if same_counter:
                    if float(len(str_to_list(question.text))) / same_counter >= 0.9:
                        error_same = 'این سوال قبلا ذخیره شده است'
                        same_counter = 0
                        return render(request, 'upload/upload.html', {'form': form, 'error': error_same})
            query_q = Question(
                text = form_clean['text'],
                pubdr = form_clean['situation'],
                type = form_clean['type'],
                difficulty = 5,  # TODO: probably should change model structure
                lesson = form_clean['lesson'],
                user = request.user,
                url_slug = text.slugify(form_text, allow_unicode=True),
                publish_date = timezone.now() if form_clean['situation'] == UploadForm.publish else None,
                draft_date = timezone.now() if form_clean['situation'] == UploadForm.draft else None,
            )
            query_q.save()
            query_a = Answer(
                text = form_clean['answer'],
                uploader = request.user,
                related_question = Question.objects.get(pk=query_q.id)
            )
            query_a.save()
            form = UploadForm()
            return render(request, 'upload/upload.html', {'form': form, 'message': 'سوال با موفقیت اضافه شد'})
        else:
            form = UploadForm()
            return render(request, 'upload/upload.html', {'form': form})
    else:
        form = UploadForm(request.GET)
        return render(request, 'upload/upload.html', {'form': form})\



def exam_creator(request):
    form = ExamCreator(request.GET)
    return render(request, 'exam/exam_creator.html', {'form': form})


def exam(request):
    return None

