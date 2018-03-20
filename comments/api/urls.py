from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import CommentListAPIView, CommentCreateAPIView, CommentUpdateAPIView

app_name="srvup-comments"

urlpatterns = [
    re_path(r'^$', CommentListAPIView.as_view(), name='list'),
    re_path(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', CommentUpdateAPIView.as_view(), name='update'),
]
