from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Patient

from django.http import HttpResponse

"""
MAIN PAGES

    frontend mag set sa final correct template
    pwede pud mag butang ug dummy context for testing

    backend mag populate sa final context
"""

def home(request):
    context = {'url_name': 'HOME'}
    return render(request, 'main/link_correct_template_here.html', context)

def room(request):
    context = {'url_name': 'ROOM'}
    return render(request, 'main/link_correct_template_here.html', context)

def patients(request):
    context = {'url_name': 'PATIENTS'}
    return render(request, 'main/link_correct_template_here.html', context)

def summary(request):
    context = {'url_name': 'SUMMARY'}
    return render(request, 'main/link_correct_template_here.html', context)

def inquiry(request):
    context = {'url_name': 'INQUIRY'}
    return render(request, 'main/link_correct_template_here.html', context)


##----------------------

def login(request):
    context = {
        "cities": [
            { 'pk': 1, 'name':'faw'},
            { 'pk': 2, 'name':'second'}
        ]
    }
    return render(request, 'main/patient_form.html', context)
    
def test(request):
    context = {'post': request.POST}
    
    sexz = request.POST.get('gender')
    if not sexz:
        sexz = 'x'
    
    patient = Patient(
        first_name = request.POST.get('firstname'),
        last_name = request.POST.get('lastname'),
        middle_name = request.POST.get('middleinitial'),
        age = request.POST.get('age'),
        sex = sexz
    )
    patient.save()
    return redirect('patient_list')

class PatientCreate(CreateView):
    model = Patient
    fields = [
		'first_name',
		'last_name',
		'middle_name',
		'age',
		'sex',
	]
	
	# first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # middle_name = models.CharField(max_length=255)
    # age = models.SmallIntegerField()
    # sex = models.CharField(max_length=1)
# Create your views here.

class PatientList(ListView):

    model = Patient
    # paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        # return context