from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class ToDoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text

class Folder(MPTTModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folder", null=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	name = models.CharField(max_length=255)
	file = models.FileField(upload_to='media',blank=True)
	publish = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class MPTTMeta:
		order_insertion_by = ['publish']

	def __str__(self):
		return self.name