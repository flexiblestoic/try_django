from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(label='Your prompt', max_length=1000)

    forms.TextInput()