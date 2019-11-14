from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
