from django import forms

class InputForm(forms.Form):
	url = forms.URLField()
	number = forms.IntegerField(min_value=1)