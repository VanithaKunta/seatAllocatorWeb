from django import forms
from django.forms import ModelForm
from .models import deptAndSec,addAndDel,classRooms
from django.forms import formset_factory
class NameForm(ModelForm):
    class Meta:
        model=classRooms
        exclude=()



