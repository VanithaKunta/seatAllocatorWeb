from django import forms
from .models import deptAndSec,addAndDel,classRooms
from django.forms import ModelForm
class NameForm2(ModelForm):
    class Meta:
        model=deptAndSec
        exclude=()
        widgets={''}


