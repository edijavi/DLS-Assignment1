from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# from rest_framework import authentication, permissions
from .models import File, Word
from .serializers import FileSerializer, WordSerializer

class FilesViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
        

class WordsViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    @action(detail=False, methods=['post'])
    def get_words(self, request):
        data = Word.objects.filter(value=request.data['query']).values()
        return Response(data, status=status.HTTP_200_OK)