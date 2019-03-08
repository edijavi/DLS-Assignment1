from .models import Word, File
from rest_framework import serializers

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('path', 'name', 'nchars', 'nlines')

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('value', 'file', 'line')