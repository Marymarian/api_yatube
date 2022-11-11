from rest_framework import serializers
from posts.models import Comment, Post, Group


class PostSerializer(serializers.ModelSerializer):
    """Сериализация объектов типа Post."""
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализация объектов типа Group."""

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализация объектов типа Comment."""
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
