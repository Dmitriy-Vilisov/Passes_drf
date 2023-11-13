from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        # fields = ['data', 'title', 'the_pass']
        fields = ['data', 'title']
        # fields = '__all__'


class Pereval_addedSerializer(WritableNestedModelSerializer):
    photos = PhotoSerializer(many=True)
    user = UserSerializer()
    coords = CoordsSerializer()

    class Meta:
        model = Pereval_added
        # exclude = ['add_time', 'status']  # статус должен выставляется на new
        fields = '__all__'

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')

        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        coords_serializer = CoordsSerializer(data=coords_data)
        coords_serializer.is_valid(raise_exception=True)
        coords = coords_serializer.save()

        pereval = Pereval_added.objects.create(user=user, coords=coords, **validated_data)

        for photo_data in photos_data:
            data = photo_data.pop('data')
            title = photo_data.pop('title')
            Photo.objects.create(data=data, title=title, pereval=pereval)

        return pereval


class PerevalSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    coords = CoordsSerializer()
    photos = PhotoSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Pereval_added
        exclude = ['add_time']
