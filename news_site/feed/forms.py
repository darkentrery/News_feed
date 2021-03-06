from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput, SplitDateTimeWidget, TimeInput, DateInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
import datetime


class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/xdsoft_datetimepicker.html'


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'date', 'full_text', 'photo']


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
                'placeholder': 'Date of public',

                'type': 'date',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of article'
            }),
            "photo": FileInput(attrs={
                'class': 'form-add-image',
                'placeholder': 'Add image',
            }),

        }
