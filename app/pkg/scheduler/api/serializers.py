from rest_framework import serializers
from app.pkg.scheduler import Group, User, Lesson

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url','pk','name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')

    class Meta:
        model = User
        fields = ('url','pk','group')

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')

    class Meta:
        model = Lesson
        fields = ('url','day','number','teacher','subject','classroom','week','group')