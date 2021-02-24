from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .serializers import *
from .models import *


class LikeCommentLogList(APIView):
    """
    Retrieve, update and delete a LikeCommentLog object and
    update Comment(like & dislike) object.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request):
        actions = LikeCommentLog.objects.filter(user=request.user)
        serializer = LikeCommentLogSerializer(actions, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        comment = self.get_object(pk)
        like_dislike = True if request.data['like_dislike'] == 'true' else False
        if like_dislike:
            LikeCommentLog.objects.create(comment=comment, user=request.user, like_or_dislike=True)
            comment.like += 1
            comment.save()
            return Response(status=status.HTTP_200_OK)
        else:
            LikeCommentLog.objects.create(comment=comment, user=request.user, like_or_dislike=False)
            comment.dislike += 1
            comment.save()
            return Response(status=status.HTTP_200_OK)

    def put(self, request, pk):
        comment = self.get_object(pk)
        like_dislike = True if request.data['like_dislike'] == 'true' else False
        try:
            action = LikeCommentLog.objects.get(comment=comment, user=request.user)
            action.like_or_dislike = like_dislike
            action.save()
        except LikeCommentLog.DoesNotExist:
            return Http404

        if like_dislike:
            comment.dislike -= 1
            comment.like += 1
            comment.save()
            return Response(status=status.HTTP_200_OK)
        else:
            comment.like -= 1
            comment.dislike += 1
            comment.save()
            return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        try:
            action = LikeCommentLog.objects.get(comment=comment, user=request.user)
            like_dislike = action.like_or_dislike
            action.delete()
        except LikeCommentLog.DoesNotExist:
            return Http404

        if like_dislike:
            comment.like -= 1
            comment.save()
            return Response(status=status.HTTP_200_OK)
        else:
            comment.dislike -= 1
            comment.save()
            return Response(status=status.HTTP_200_OK)


class LikePostLogList(APIView):
    """
    Retrieve, update and delete a LikePostLog object and
    update Post(like & dislike) object.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request):
        actions = LikePostLog.objects.filter(user=request.user)
        serializer = LikePostLogSerializer(actions, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        post = self.get_object(pk)
        like_dislike = True if request.data['like_dislike'] == 'true' else False
        if like_dislike:
            LikePostLog.objects.create(post=post, user=request.user, like_or_dislike=True)
            post.like += 1
            post.save()
            return Response(status=status.HTTP_200_OK)
        else:
            LikePostLog.objects.create(post=post, user=request.user, like_or_dislike=False)
            post.dislike += 1
            post.save()
            return Response(status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = self.get_object(pk)
        like_dislike = True if request.data['like_dislike'] == 'true' else False
        try:
            action = LikePostLog.objects.get(post=post, user=request.user)
            action.like_or_dislike = like_dislike
            action.save()
        except LikeCommentLog.DoesNotExist:
            return Http404

        if like_dislike:
            post.dislike -= 1
            post.like += 1
            post.save()
            return Response(status=status.HTTP_200_OK)
        else:
            post.like -= 1
            post.dislike += 1
            post.save()
            return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        post = self.get_object(pk)
        try:
            action = LikePostLog.objects.get(post=post, user=request.user)
            like_dislike = action.like_or_dislike
            action.delete()
        except LikeCommentLog.DoesNotExist:
            return Http404

        if like_dislike:
            post.like -= 1
            post.save()
            return Response(status=status.HTTP_200_OK)
        else:
            post.dislike -= 1
            post.save()
            return Response(status=status.HTTP_200_OK)
