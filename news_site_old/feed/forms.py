from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of article'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
            }),
            "full_text": DateTimeInput(attrs={
                'class': 'form-control',
            })
        }