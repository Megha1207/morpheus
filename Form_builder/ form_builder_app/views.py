# form_builder_app/views.py
from django.shortcuts import render, redirect
from .models import Form, Question, Response
from .forms import FormCreationForm, ResponseForm
from django.db.models import Count
import json
from collections import Counter


def admin_dashboard(request):
    if request.method == 'POST':
        form = FormCreationForm(request.POST)
        if form.is_valid():
            new_form = Form.objects.create(title=form.cleaned_data['title'])
            questions_data = form.cleaned_data['questions']
            for q_data in questions_data:
                question = Question.objects.create(
                    text=q_data['text'],
                    question_type=q_data['question_type'],
                    options=q_data.get('options', ''),
                    form=new_form
                )
            return redirect('admin_dashboard')
    else:
        form = FormCreationForm()
    return render(request, 'form_builder/admin_dashboard.html', {'form': form})


from django.shortcuts import render
from .models import Form


def fill_form(request, form_id):
    # Retrieve the form by ID
    form = Form.objects.get(id=form_id)

    # Split options for each question into a list if options exist
    for question in form.questions.all():
        if question.options:
            # Split the options by comma and strip any extra spaces
            question.options = [option.strip() for option in question.options.split(',')]

    # Render the form template with the form object
    return render(request, 'form_builder/fill_form.html', {'form': form})

def thank_you(request):
    return render(request, 'form_builder/thank_you.html')


def view_analytics(request, form_id):
    form = Form.objects.get(id=form_id)
    responses = Response.objects.filter(form=form)

    text_data = []
    checkbox_data = []
    dropdown_data = []

    for response in responses:
        response_json = json.loads(response.response_data)
        for question in form.questions.all():
            answer = response_json.get(str(question.id))
            if question.question_type == 'text':
                text_data.extend(answer.split())
            elif question.question_type == 'checkbox':
                checkbox_data.extend(answer.split(','))
            elif question.question_type == 'dropdown':
                dropdown_data.append(answer)

    text_counter = Counter([word for word in text_data if len(word) >= 5])
    checkbox_counter = Counter(checkbox_data)
    dropdown_counter = Counter(dropdown_data)

    return render(request, 'form_builder/analytics.html', {
        'form': form,
        'text_data': text_counter.most_common(5),
        'checkbox_data': checkbox_counter.most_common(5),
        'dropdown_data': dropdown_counter.most_common(5),
    })

def form_list(request):
    forms = Form.objects.all()  # Retrieve all forms
    return render(request, 'form_builder/form_list.html', {'forms': forms})