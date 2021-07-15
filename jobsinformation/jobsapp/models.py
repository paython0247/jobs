from django.db import models
# Create your models here.
class Hydjobs(models.Model):
	date=models.DateField();
	company=models.CharField(max_length=(100));
	title=models.CharField(max_length=(100));
	address=models.CharField(max_length=(100));
	email=models.EmailField();
	phonenumber=models.IntegerField();
class Punejobs(models.Model):
	date=models.DateField();
	company=models.CharField(max_length=(100));
	title=models.CharField(max_length=(100));
	address=models.CharField(max_length=(100));
	email=models.EmailField();
	phonenumber=models.IntegerField();

class Chennaijobs(models.Model):
	date=models.DateField();
	company=models.CharField(max_length=(100));
	title=models.CharField(max_length=(100));
	address=models.CharField(max_length=(100));
	email=models.EmailField();
	phonenumber=models.IntegerField();


class Banglorejobs(models.Model):
	date=models.DateField();
	company=models.CharField(max_length=(100));
	title=models.CharField(max_length=(100));
	address=models.CharField(max_length=(100));
	email=models.EmailField();
	phonenumber=models.IntegerField();
# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30)
	marks=models.IntegerField()
	add=models.CharField(max_length=50)
	mobile=models.IntegerField()
	email=models.EmailField()