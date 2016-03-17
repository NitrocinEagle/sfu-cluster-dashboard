from django import forms

class SimpleForm(forms.Form):
    plugin_name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)