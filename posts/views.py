from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET', 'POST'])
def get_time_gap(request, pk1, pk2):
    try:
        pk1 = Post.objects.get(pk=pk1)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        pk2 = Post.objects.get(pk=pk2)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(pk1.created_at - pk2.created_at)


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

