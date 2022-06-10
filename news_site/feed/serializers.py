from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'anons', 'full_text', 'date_public', 'photo', 'date',)

