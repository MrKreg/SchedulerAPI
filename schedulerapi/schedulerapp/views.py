from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from django_filters import AllValuesFilter, AllValuesMultipleFilter
from django_filters import Filter
from django_filters import FilterSet
from django_filters.fields import Lookup
from schedulerapp.models import *
from schedulerapp.serializers import *

class LessonFilter(FilterSet):
    day = AllValuesFilter(field_name='day')
    group = AllValuesFilter(field_name='group')
    week = AllValuesMultipleFilter(field_name='week')

    class Meta:
        model = Lesson
        fields = (
            'day',
            'group',
            'week',
        )

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    name = 'group-list'
    filter_fields = (
        'name',
    )

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    name = 'group-detail'

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    filter_fields = (
        'id',
    )

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    name = 'lesson-list'
    filter_class = LessonFilter
    filter_fields = (
        'day',
        'group',
        'week',
    )

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    name = 'lesson-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'groups': reverse(GroupList.name, request=request),
            'users': reverse(UserList.name, request=request),
            'lessons': reverse(LessonList.name, request=request),
        })

blabla