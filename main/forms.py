from django import forms
from django.forms import ModelForm
from .models import Patient
from .enums import Enums

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['last_name', 'first_name', 'middle_initial']
        
    last_name = forms.CharField (
        label = 'Last Name',
        widget = forms.TextInput ( attrs = {
            'class' : 'input',
            'placeholder' : 'Last Name'
        })
    )
    
    first_name = forms.CharField (
        label = 'First Name',
        widget = forms.TextInput ( attrs = {
            'class' : 'input',
            'placeholder' : 'First Name'
        })
    )
    
    middle_initial = forms.CharField (
        label = 'Middle Initial',
        widget = forms.TextInput ( attrs = {
            'class' : 'input',
            'placeholder' : 'Middle Initial'
        })
    )
	
    age = forms.IntegerField (
        label = 'Age',
		widget = forms.NumberInput ( attrs = {
            'class' : 'form-control, input',
			'placeholder' : 'Age'
        })
    )
    
    sex = forms.CharField (
        label = 'Sex',
        widget = forms.Select (
			attrs = {
				'class' : 'form-control, input'
			},
            choices = Enums.SEX
        )
    )
    
    diagnosis = forms.CharField (
        label = 'Diagnosis',
        widget = forms.Select (
			attrs = {
				'class' : 'form-control, input'
			},
		    choices = [
				['default', 'Diagnosis'],
			    ['all', 'Acute Lymphoblastic Leukemia'],
		        ['bg', 'Brainstem Glioma'],
	        ]
            # choices = DIAGNOSIS
        )
    )
    
    region = forms.CharField (
        label = 'Region',
        widget = forms.Select (
			attrs = {
				'class' : 'form-control, input'
			},
            
			choices = Enums.REGIONS
        )
    )
    
    province = forms.CharField (
        label = 'Province',
        widget = forms.Select (
			attrs = {
				'class' : 'form-control, input'
			},
		    
            choices = Enums.PROVINCES
        )
    )
    
    city = forms.CharField (
        label = 'City',
        widget = forms.Select (
			attrs = {
				'class' : 'form-control, input'
			},
            choices = Enums.CITIES
        )
    )
	
class RoomForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['last_name', 'first_name', 'middle_initial']
        
    last_name = forms.CharField (
        label = 'Last Name',
        widget = forms.TextInput ( attrs = {
            'class' : 'input',
            'placeholder' : 'Last Name'
        })
    )
    
    first_name = forms.CharField (
        label = 'First Name',
        widget = forms.TextInput ( attrs = {
            'class' : 'input',
            'placeholder' : 'First Name'
        })
    )
    
    middle_initial = forms.CharField (
        label = 'Middle Initial',
        widget = forms.TextInput ( attrs = {
            'class' : 'input',
            'placeholder' : 'Middle Initial'
        })
    )
	
    relationship = forms.MultipleChoiceField (
        label = 'Relationship',
		widget = forms.CheckboxSelectMultiple,
		choices = [
			['rel-1', 'Mother'],
			['rel-2', 'Father'],
		]
    )
	
    date_from = forms.DateField(
        widget=forms.DateInput( format = '%m/%d/%Y' ),
        input_formats = ( '%m/%d/%Y' )
    )
    
    date_to = forms.DateField(
        widget=forms.DateInput(
            format = '%m/%d/%Y',
            attrs = { 'class': 'datepicker' }
        ),
        input_formats = ( '%m/%d/%Y' )
    )