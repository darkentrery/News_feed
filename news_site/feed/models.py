from django.db import models


class Article(models.Model):
    title = models.CharField('Title', max_length=100)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text of article')
    date = models.DateTimeField('Date of public', auto_now=True)
    photo = models.ImageField(upload_to="photos", verbose_name="Photo")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
