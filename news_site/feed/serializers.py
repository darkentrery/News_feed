from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    date = serializers.DateTimeField(input_formats=['%m/%d/%Y',])
    photo = serializers.ImageField()



    class Meta:
        model = Article
        # fields = ('pk', 'title', 'anons', 'full_text', 'date_public', 'photo', 'date',)
        fields = ('pk', 'title', 'anons', 'full_text', 'photo', 'date',)
        read_only_fields = ('pk',)


