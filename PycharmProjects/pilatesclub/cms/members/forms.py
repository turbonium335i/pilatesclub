from django.forms import ModelForm, Textarea
from .models import *

class addClient(ModelForm):
    class Meta:
        model = client
        fields = '__all__'

class addVocab(ModelForm):
    class Meta:
        model = word
        fields = '__all__'