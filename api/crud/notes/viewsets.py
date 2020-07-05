from rest_framework import viewsets
from .models import Note, User
from .serializers import *
from rest_framework.generics import *

class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteCreateUpdateSerializer

class NoteView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteCreateUpdateSerializer



class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
