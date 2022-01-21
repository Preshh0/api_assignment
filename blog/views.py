from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializers

# Create your views here.
class Blog(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers