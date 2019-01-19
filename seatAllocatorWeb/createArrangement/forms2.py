from django import forms
from .models import deptAndSec,addAndDel,classRooms
from django.forms import ModelForm
class NameForm2(ModelForm):
    class Meta:
        model=deptAndSec
        exclude=()
        """fields=('addNum','addNumRoll','delNum','delNumRoll')
        widgets = {'addNum': forms.Textarea(attrs={'cols':20,'rows':5})}
        widgets2 = {'addNumRoll': forms.Textarea(attrs={'cols':20,'rows':5})}
        widgets3={'delNum': forms.Textarea(attrs={'cols':20,'rows':5})}
        widget4={'delNumRoll': forms.Textarea(attrs={'cols':20,'rows':5})}"""
        widgets={''}


