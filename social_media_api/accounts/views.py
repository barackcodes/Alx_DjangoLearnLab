from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

CustomUser = get_user_model()
class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username")


class FollowUserAPIView(generics.GenericAPIView):
    
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return CustomUser.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(self.get_queryset(), pk=user_id)


        following_field = getattr(request.user, "following", None)
        if following_field is not None:
            
            if target == request.user:
                return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            if following_field.filter(pk=target.pk).exists():
                return Response({"detail": "Already following."}, status=status.HTTP_200_OK)
            following_field.add(target)
            return Response({"detail": "Followed successfully."}, status=status.HTTP_200_OK)

    
        target_followers = getattr(target, "followers", None)
        if target_followers is not None:
            if target == request.user:
                return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            if target_followers.filter(pk=request.user.pk).exists():
                return Response({"detail": "Already following."}, status=status.HTTP_200_OK)
            target_followers.add(request.user)
            return Response({"detail": "Followed successfully (via target.followers)."}, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Follow relationship not configured on user model. Update follow view to match your fields."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class UnfollowUserAPIView(generics.GenericAPIView):
    """
    POST /unfollow/<int:user_id>/
    Removes the target user from the authenticated user's 'following' relationship.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(self.get_queryset(), pk=user_id)

        following_field = getattr(request.user, "following", None)
        if following_field is not None:
            if not following_field.filter(pk=target.pk).exists():
                return Response({"detail": "Not following this user."}, status=status.HTTP_200_OK)
            following_field.remove(target)
            return Response({"detail": "Unfollowed successfully."}, status=status.HTTP_200_OK)

        target_followers = getattr(target, "followers", None)
        if target_followers is not None:
            if not target_followers.filter(pk=request.user.pk).exists():
                return Response({"detail": "Not following this user."}, status=status.HTTP_200_OK)
            target_followers.remove(request.user)
            return Response({"detail": "Unfollowed successfully (via target.followers)."}, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Follow relationship not configured on user model. Update unfollow view to match your fields."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
