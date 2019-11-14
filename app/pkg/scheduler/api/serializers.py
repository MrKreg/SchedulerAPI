from rest_framework import serializers

from app.pkg.info.api.serializers import LessonInfoSerializer, ClassroomSerializer


class LessonSerializer(serializers.ModelSerializer):
    info = LessonInfoSerializer()
    classroom = ClassroomSerializer()

    class Meta:
        exclude = ('weeks',)
