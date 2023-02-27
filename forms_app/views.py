from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import PromptForm
import openai

api_secret = "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"
openai.api_key = api_secret

def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message = completions.choices[0].text
    return message


def get_prompt(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PromptForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            prompt= form.cleaned_data.get("prompt")
            openai_response = generate_response(prompt)

            # redirect to a new URL:
            return render(request, 'forms_app/openai.html', {'form': form, 'openai_response': openai_response})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PromptForm()

    return render(request, 'forms_app/openai.html', {'form': form})


