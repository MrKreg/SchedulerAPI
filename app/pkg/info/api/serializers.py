from rest_framework import serializers

from app.pkg.info.models import Classroom, Lesson, Subject, Teacher


# ****************************************************************************
# TEACHER SERIALIZERS
# ****************************************************************************

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


class ShortTeacherSerializer(serializers.ModelSerializer):
    initials = serializers.ReadOnlyField()

    class Meta:
        model = Teacher
        fields = ('initials',)


# ****************************************************************************
# SUBJECT SERIALIZERS
# ****************************************************************************

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


# ****************************************************************************
# LESSON SERIALIZERS
# ****************************************************************************

class LessonSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    second_teacher = TeacherSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'


# ****************************************************************************
# CLASSROOM SERIALIZERS
# ****************************************************************************

class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = '__all__'


class ShortClassRoomSerializer(serializers.ModelSerializer):
    info = serializers.ReadOnlyField()

    class Meta:
        model = Classroom
        fields = ('info',)
