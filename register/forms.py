from django import forms
from .models import Participants, Vehicle
from django.forms import formset_factory


class ParticipantsForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = '__all__'  # You can specify the fields you want to include if not all
ParticipantsFormSet = formset_factory(ParticipantsForm)
    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if not Participants.is_valid_phone(phone):
    #         raise forms.ValidationError("Invalid phone number format. It must start with '+' and be followed by postal codes, then phone digits.")
    #     return phone
class VehiclesForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'  # You can specify the fields you want to include if not all

VehiclesFormSet = formset_factory(VehiclesForm)