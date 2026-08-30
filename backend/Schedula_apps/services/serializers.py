from rest_framework import serializers

from .models import Service, ServiceImage


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['id', 'file']


class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['provider', 'category', 'title', 'description', 'price', 'duration', 'images']

    def create(self, validated_data):
        obj = Service.objects.create(**validated_data)
        return obj

    def update(self, instance, validated_data):
        for name, value in validated_data.items():
            setattr(instance, name, value)
        instance.save()
        return instance

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError({
                "price": ["price must be grater than zero"]
            })
        return value

    def validate_title(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError({
                "title": ["title is not correct"]
            })
        return value

    def validate_description(self, value):
        if len(value) < 50:
            raise serializers.ValidationError({
                "description": ["inter at least 50 character"]
            })

