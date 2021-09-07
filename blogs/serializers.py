from .models import Blog
from rest_framework import serializers

## Create a Serializer for Our Model
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    # nest a Meta class to configure the serializer
    class Meta:
        # which model does it serialize
        model = Blog
        # which fields should be serialized
        fields = ["id", "title", "body"]