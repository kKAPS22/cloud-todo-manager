from django.db import models
from django.contrib.auth.models import User

'''A Foreign Key is a field in one table that refers to the Primary Key of
another table to create a relationship between them.'''
class Todo(models.Model):
    srno=models.AutoField(primary_key=True,auto_created=True)#Primary_Key->Unique Key hai ,Auto_Created=>Django Khud Generate Karega
    title=models.CharField(max_length=25)
    description=models.TextField()
    due_at=models.DateTimeField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)#agar User Delete Toh Kal Ko uske Saare Todo Bhi dlete 
    is_completed=models.BooleanField(default=False)
    
