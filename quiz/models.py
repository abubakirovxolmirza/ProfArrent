from django.db import models
# Create your models here.


class Careers(models.Model):
    name = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name
    

class RoadMaps(models.Model):
    careers_id = models.ForeignKey(Careers, on_delete=models.CASCADE, related_name='roadmaps_set')
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Body(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    roadmaps_id = models.ForeignKey(RoadMaps, on_delete=models.CASCADE, related_name='body_set')

    def __str__(self):  
        return self.name
    

class Question(models.Model):
    question = models.CharField(max_length=200)
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Options(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    A_B_option = models.CharField(max_length=100)
    
    def __str__(self):
        return self.A_B_option


class Type(models.Model):   
    
    name = models.CharField(max_length=200)
    number_of_tests = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.name


class Test(models.Model):
    careers_id = models.ForeignKey(Careers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

