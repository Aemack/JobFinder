from django import forms

class SearchForm(forms.Form):
    job_title = forms.CharField(label='Job Title ', max_length=250, widget=forms.TextInput(attrs={'class':"form-control"}))
    location = forms.CharField(label='Location ', max_length=250, widget=forms.TextInput(attrs={'class':"form-control"}))
