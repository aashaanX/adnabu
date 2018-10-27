from rest_framework import serializers


class URequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    urls = serializers.ListField()



