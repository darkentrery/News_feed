from django.db import models


def my_path(obj, name):
    return str(obj.article_id) + '/' + (name)


class Articles(models.Model):
    title = models.CharField('Title', max_length=100)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text of article')
    date = models.DateTimeField('Date of public')
    photo = models.ImageField(upload_to="photos", verbose_name="Photo")



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
