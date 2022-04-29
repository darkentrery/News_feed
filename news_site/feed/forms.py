from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of article'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of public'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of article'
            }),
        }
