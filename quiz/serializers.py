from rest_framework import serializers
from .models import Options, Question, Type, Test, Careers, RoadMaps, Body

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'


class RoadMapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMaps
        fields = '__all__'


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'




