from rest_framework import serializers


# ****************************************************************************
# TEACHER SERIALIZERS
# ****************************************************************************

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'


class ShortTeacherSerializer(serializers.ModelSerializer):
    initials = serializers.ReadOnlyField()

    class Meta:
        fields = ('initials',)


# ****************************************************************************
# SUBJECT SERIALIZERS
# ****************************************************************************

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'


# ****************************************************************************
# LESSON INFO SERIALIZERS
# ****************************************************************************

class LessonInfoSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    second_teacher = TeacherSerializer()

    class Meta:
        fields = '__all__'


# ****************************************************************************
# CLASSROOM SERIALIZERS
# ****************************************************************************

class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'


class ShortClassRoomSerializer(serializers.ModelSerializer):
    info = serializers.ReadOnlyField()

    class Meta:
        fields = ('info',)
