__author__ = 'dali'
from .models import PortfolioQuestion, PortfolioAnswer
from rest_framework import serializers


class JSONSerializerField(serializers.WritableField):
    pass


class PortfolioQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioQuestion
        fields = ('id', 'course', 'description', 'timestamp', 'type')


class PortfolioAnswerSerializer(serializers.ModelSerializer):
    given = JSONSerializerField('given')

    class Meta:
        model = PortfolioAnswer
        fields = ('id', 'portfolio_question', 'user', 'timestamp', 'given', 'title', 'description')


