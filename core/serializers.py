from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import Note, User


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
