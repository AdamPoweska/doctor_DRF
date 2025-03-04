from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateDoctor(forms.ModelForm):
    class Meta:
        model = DoctorName
        fields = '__all__'
  

class CreateDoctorType(forms.ModelForm):
    class Meta:
        model = DoctorType
        fields = '__all__'


class AppointmentDatesForm(forms.ModelForm):
    class Meta:
        model = AppointmentDates
        fields = '__all__'


class DoctorTypeSelect(forms.Form):
    doctor_type_select = forms.ModelChoiceField(
        queryset=DoctorType.objects.all(),
        required=True
    )


class DoctorNameSelect(forms.Form):
    doctor_name_select = forms.ModelChoiceField(
        queryset=DoctorName.objects.all(), 
        label="Choose doctor"
    )

    def __init__(self, *args, **kwargs):
        # przekazanie tylko odpwoednich lekarzy przez widok
        specialization_pk = kwargs.pop('specialization_pk', None)
        super().__init__(*args, **kwargs)
        
        if specialization_pk:
            # filtracja lekarzy po typie
            self.fields['doctor_name_select'].queryset = DoctorName.objects.filter(main_specialization__pk=specialization_pk)


class VisitDateSelect(forms.Form):
    doctor_date_select = forms.ModelChoiceField(
        queryset=AppointmentDates.objects.all(),
        label="Choose date"
        # required=True
    )

    def __init__(self, *args, **kwargs):
        # przekazanie doctor-PK zeby zobaczyc przypisane im daty
        doctor_pk = kwargs.pop('doctor_pk', None)
        super().__init__(*args, **kwargs)
        
        if doctor_pk:
            self.fields['doctor_date_select'].queryset = AppointmentDates.objects.filter(doctor__pk=doctor_pk)
