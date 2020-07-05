from django.conf.urls import url
from .viewsets import *
from rest_framework import routers

app_name = "notes"

router = routers.SimpleRouter()
router.register('users', UserListView)

urlpatterns = [
    url(r'^notes/$', NoteListView.as_view(), name='list-notes'),
    url(r'^notes/create$', NoteCreateView.as_view(), name='create-notes'),
    url(r'^notes/(?P<pk>\d+)$', NoteView.as_view(), name='details-note'),
]

urlpatterns += router.urls