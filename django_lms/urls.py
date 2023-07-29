from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include
from django.urls import re_path
from assignments import views
from django_lms import views as project_views
from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    re_path(r'^$', project_views.index, name="home"),
    path('admin/', admin.site.urls),
    re_path(r'^users/', include('users.urls', namespace='users')),
    re_path(r'^courses/', include('courses.urls', namespace="courses")),
    re_path(r'^assignments/', include('assignments.urls', namespace='assignments')),
    re_path(r'^resources/', include('resources.urls', namespace="resources")),
    re_path(r'^editor/', include('editor.urls', namespace="editor")),
    re_path(r'^user_profile/(?P<pk>[-\w]+)/$',
        project_views.UserProfile.as_view(), name="profile"),
    re_path('graphql/', FileUploadGraphQLView.as_view(graphiql=True)),
    path("__reload__/", include("django_browser_reload.urls"))
]
