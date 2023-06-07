from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from PathBase.models import User, Session, Character


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('SessionId', 'NameSession')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('UserID',)


class SessionFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('SessionId', 'NameSession', 'User_id', 'UserStatus', 'CharacterID')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
