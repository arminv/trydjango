from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # Note, we do NOT have to specify all the available fields (i.e. only the ones we want):
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
