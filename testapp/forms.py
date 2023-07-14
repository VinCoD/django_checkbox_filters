from django import forms

class RestaurantFilterForm(forms.Form):
    price_choices = (
        ('cheap', 'Cheap'),
        ('moderate', 'Moderate'),
        ('expensive', 'Expensive'),
    )
    price_range = forms.MultipleChoiceField(choices=price_choices, widget=forms.CheckboxSelectMultiple)
