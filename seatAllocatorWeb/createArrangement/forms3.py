from django import forms
from django.forms import ModelForm
from .models import deptAndSec,addAndDel,classRooms
from django.forms import formset_factory
class NameForm3(ModelForm):
    class Meta:
        model=addAndDel
        exclude=()
NameFormSet = formset_factory(NameForm3,extra=3,)


