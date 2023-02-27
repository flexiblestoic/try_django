from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'{title} is taken')
        if title.lower().strip() == "the office":
            self.add_error('title', 'this title is taken')
            # raise forms.ValidationError('this title is taken')
        return cleaned_data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('this title is taken')
    #     print(title)
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if title.lower().strip() == "the office":
            self.add_error('title', 'this title is taken')
            # raise forms.ValidationError('this title is taken')
        return cleaned_data