from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'name', 'last_name', 'patronimic', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        # fields = ['data', 'title', 'the_pass']
        fields = '__all__'


class Pereval_addedSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    coords = CoordsSerializer()
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = UsersSerializer()
    # photos = PhotoSerializer(required=False)
    photos = PhotoSerializer()

    class Meta:
        model = Pereval_added
        exclude = ['add_time', 'status']  # статус выставляется на new


class PerevalSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    coords = CoordsSerializer()
    # photo = PhotoSerializer()
    user = UsersSerializer()

    class Meta:
        model = Pereval_added
        exclude = ['add_time']