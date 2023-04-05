from django.db import models


# Create your models here.
class College(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100)
    c_loc=models.CharField(max_length=100)
    def __str__(self):
        return self.c_name

class Subjects(models.Model):
    stid=models.CharField(max_length=100,primary_key=True)
    c_id=models.ForeignKey(College,on_delete=models.CASCADE)
    
    s1_t=models.CharField(max_length=100)
    s1_e=models.CharField(max_length=100)
    s1_h=models.CharField(max_length=100)
    def __str__(self):
        return self.stid

class Student(models.Model):
    stid=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    s1_tmarks=models.IntegerField()
    s1_emarks=models.IntegerField()
    s1_hmarks=models.IntegerField()
    

