
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers
from.models import Annotation, CharacterSet


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('id', 'user', 'integer', 'annotation')


class CharacterSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSet
        fields = ('regex')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        print(user)
        Token.objects.create(user=user)
        return user
