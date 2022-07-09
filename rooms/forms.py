from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    country = CountryField(default="KR").formfield()
    city = forms.CharField()
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(
        queryset=models.RoomType.objects.all(), required=False, empty_label="Any kind"
    )
    guests = forms.IntegerField(required=False)
    besrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple
    )
