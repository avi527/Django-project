from django.db import models

# Create your models here.
#start one to one relation
class Customer(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='vehicle'
        )
    def __str__(self):
        return self.name
class Teacher(models.Model):
	name=models.CharField(max_length=50)
	mobilenumber=models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Student(models.Model):
	studentname=models.CharField(max_length=30)
	clastime=models.TimeField() 
	subject=models.CharField(max_length=20)
	Teacher=models.OneToOneField(Teacher,on_delete=models.CASCADE,related_name='Student')
	def __str__(self):
		return self.studentname
#end one to one relation

#start one to many relation
class Laptop(models.Model):
	brand=models.CharField(max_length=20)
	generation=models.CharField(max_length=10)
	def __str__(self):
		return self.brand
class Language(models.Model):
	name=models.CharField(max_length=10)
	uses=models.CharField(max_length=20)
	Laptop=models.ForeignKey(Laptop,on_delete=models.CASCADE,related_name='Language')
	def __str__(self):
		return self.name
#end one to many relation

#start many to many relation
class Worker(models.Model):
	name=models.CharField(max_length=20)
	working_area=models.CharField(max_length=15)
	def __str__(self):
		return self.name
class Machine(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField(
        Worker,
        related_name='Machine'
    )
    def __str__(self):
    	return self.name

#end many to many relation

