from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from .models import File, Word
from .serializers import FileSerializer, WordSerializer

class FilesViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
        

class WordsViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer