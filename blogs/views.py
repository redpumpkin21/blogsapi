from .models import Blog
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    ## Give it the main query for the index route
    queryset = Blog.objects.all()
    # THe serializer for serializing
    serializer_class = BlogSerializer
    ## Optional Permissions
    permission_classes = [permissions.AllowAny]