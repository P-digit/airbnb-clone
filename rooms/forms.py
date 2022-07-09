from django import forms
from . import models


class SearchForm(forms.Form):

    city = forms.CharField()
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(models.RoomType.objects.all())
