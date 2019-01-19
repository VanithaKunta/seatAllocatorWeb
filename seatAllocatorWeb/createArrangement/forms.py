from django import forms
from django.forms import ModelForm
from .models import deptAndSec,addAndDel,classRooms
from django.forms import formset_factory
class NameForm(ModelForm):
    class Meta:
        model = classRooms
        exclude=()
        """widgets = {'addNum': forms.Textarea(attrs={'cols': 20, 'rows': 5})}
        widgets2 = {'addNumRoll': forms.Textarea(attrs={'cols': 20, 'rows': 5})}
        widgets3 = {'delNum': forms.Textarea(attrs={'cols': 20, 'rows': 5})}
        widget4 = {'delNumRoll': forms.Textarea(attrs={'cols': 20, 'rows': 5})}"""
        #widgets={'noOfRooms': forms.Textarea(attrs={'cols':20,'rows':3})}
NameFormSet = formset_factory(NameForm,extra=3,)


