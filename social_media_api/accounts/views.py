from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

CustomUser = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username")


class FollowUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(self.get_queryset(), pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=400)

        following = getattr(request.user, "following", None)
        if following is None:
            return Response({"detail": "Follow relationship not configured on user model."}, status=500)

        if following.filter(pk=target.pk).exists():
            return Response({"detail": "Already following."})
        following.add(target)
        return Response({"detail": "Followed successfully."})


