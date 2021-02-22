from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class LikeCommentLogSerializer(serializers.Serializer):
    class Meta:
        model = LikeCommentLog
        fields = ['id', 'comment', 'user', 'like_or_dislike']
