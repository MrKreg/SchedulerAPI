from django.conf.urls import url
from app.pkg.scheduler.api import views

urlpatterns = [
    url(r'^users/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
    url(r'^groups/$',
        views.GroupList.as_view(),
        name=views.GroupList.name),
    url(r'^groups/(?P<pk>[0-9]+)$',
        views.GroupDetail.as_view(),
        name=views.GroupDetail.name),
    url(r'^lessons/$',
        views.LessonList.as_view(),
        name=views.LessonList.name),
    url(r'^lessons/(?P<pk>[0-9]+)$',
        views.LessonDetail.as_view(),
        name=views.LessonDetail.name),
]