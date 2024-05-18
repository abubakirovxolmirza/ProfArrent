from django.shortcuts import render
from .models import Options, Question, Type, Test, Careers, RoadMaps, Body
from .serializers import OptionsSerializer, QuestionSerializer, TypeSerializer, TestSerializer, CareersSerializer, RoadMapsSerializer, BodySerializer
from rest_framework import generics
from rest_framework import permissions
# Create your views here.


class OptionsListView(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
    permission_classes = [permissions.IsAuthenticated]

class OptionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer   
    permission_classes = [permissions.IsAuthenticated]

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeListView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestListView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class CareersListView(generics.ListCreateAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    permission_classes = [permissions.IsAuthenticated]


class CareersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoadMapsListView(generics.ListCreateAPIView):
    queryset = RoadMaps.objects.all()
    serializer_class = RoadMapsSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoadMapsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoadMaps.objects.all()
    serializer_class = RoadMapsSerializer
    permission_classes = [permissions.IsAuthenticated]


class BodyListView(generics.ListCreateAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]


class BodyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]

