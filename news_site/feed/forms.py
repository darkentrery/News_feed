from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'photo']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of article'
            }),
            #"date": DateTimeInput(attrs={
            #    'class': 'form-control',
            #    'placeholder': 'Date of public'
            #}),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of article'
            }),

        }
