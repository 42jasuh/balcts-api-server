# views.py
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def health_check(request):
    if request.method == 'GET':
        data = {'msg': 'healthy'}
        return Response(data, status=status.HTTP_200_OK)