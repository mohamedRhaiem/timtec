__author__ = 'dali'
from .models import PortfolioQuestion, PortfolioAnswer, Comment
from rest_framework import serializers


class JSONSerializerField(serializers.WritableField):
    pass


class PortfolioQuestionSerializer(serializers.ModelSerializer):

    thumbnail = serializers.Field(source='thumbnail')

    class Meta:
        model = PortfolioQuestion
        fields = ('id', 'course', 'title', 'video', 'thumbnail', 'document', 'description', 'timestamp')


class PortfolioAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioAnswer



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
