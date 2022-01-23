from django import forms
from .models import AdharCardDetail
from django.forms.fields import DateField
from django.forms import widgets



class AdharDetailFirstForm(forms.ModelForm):
    
    date_of_birth = DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = AdharCardDetail
        exclude = ('full_name_hi', 'relation_hi', 'gender_hi', 'relation_name_hi', 'address_hi', 'city_hi', 'state_hi',)



class AdharDetailForm(forms.ModelForm):
    
    class Meta:
        model = AdharCardDetail
        fields = '__all__'

