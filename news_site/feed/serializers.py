from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    # print(f"{photo=}")

    class Meta:
        model = Article
        fields = ('pk', 'title', 'anons', 'full_text', 'date_public', 'photo', 'date',)

