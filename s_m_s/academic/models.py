from django.db import models

# Create your models here.

class Department(models.Model):
	name=models.CharField(max_length=25, unique=True)
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name

class ClassInfo(models.Model):
	name=models.CharField(max_length=40, unique=True)
	dispaly_name=models.CharField(max_length=45, unique=True)
	date= models.DateField(auto_now_add=True)
	def __str__(self):
		return self.dispaly_name

class Section(models.Model):
	name=models.CharField(max_length=25, unique=True)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return self.name
class Session(models.Model):
	name= models.IntegerField(unique=True)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return self.name
class Shift(models.Model):
	name=models.CharField(max_length=25, unique=True)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return self.name
class GuideTeacher(models.Model):
	name=models.OneToOneField('teacher.PersonalInfo',on_delete=models.CASCADE , null=True)
	date=models.DateField(auto_now_add=True)
	def __str__(self):
		return self.name
class ClassRegistration(models.Model):
	name=models.CharField(max_length=10,unique=True)
	department_select=(
		('general', 'General'),
		('science', 'Science'),
		('business','Business'),
		('humanities','Humanities')
		)
	department=models.CharField(choices=department_select, max_length=15)
	class_name=models.ForeignKey(ClassInfo,on_delete=models.CASCADE, null=True)
	section=models.ForeignKey(Section,on_delete=models.CASCADE, null=True)
	session=models.ForeignKey(Session,on_delete=models.CASCADE, null=True)
	shift=models.ForeignKey(Shift, on_delete=models.CASCADE, null=True)
	guide_teacher=models.OneToOneField(GuideTeacher, on_delete=models.CASCADE, null=True)
	date=models.DateField(auto_now_add=True)

	class meta:
		unique_together=[ 'class_name', 'section', 'guide_teacher','shift']
	def __str__(self):
		return self.name