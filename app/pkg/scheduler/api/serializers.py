from rest_framework import serializers

from app.pkg.info.api.serializers import LessonInfoSerializer, ClassroomSerializer


class LessonSerializer(serializers.ModelSerializer):
    info = LessonInfoSerializer()
    classroom = ClassroomSerializer()

    class Meta:
        fields = '__all__'


class SimpleLessonSerializer(serializers.ModelSerializer):
    classroom = serializers.CharField(read_only=True, source='classroom.info')
    teacher = serializers.CharField(read_only=True, source='info.teacher.initials')
    second_teacher = serializers.CharField(read_only=True, source='info.second_teacher.initials')
    subject = serializers.CharField(read_only=True, source='info.subject.name')

