from re import T
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
STATUS_CHOICES =(
    ('new','New'),
    ('todo','ToDo'),
    ('completed','Completed'),
    ('archived','Archived')
)

User = get_user_model()

class Project(models.Model):
    title = models.CharField(max_length=64,verbose_name=_('title'))
    status = models.CharField(max_length=64,choices=STATUS_CHOICES,default='new',verbose_name=_('status'))
    admin_todo = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project_admin')
    team_member = models.ManyToManyField(User,related_name='project_member')
    
    class Meta:
        ordering=('title',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todoapp:project_detail',args=[self.title,self.id])


class Task(models.Model):
    title = models.CharField(max_length=64 ,verbose_name=_('title'))
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='task' , null=True )
    team_member = models.ManyToManyField(User,related_name='task_member',blank=True)
    text_todo = models.TextField(verbose_name=_('text'))
    status = models.CharField(max_length=64,choices=STATUS_CHOICES,default='new',verbose_name=_('status'))
    start_date = models.DateTimeField(auto_now_add=True,verbose_name=_('start'))
    end_date = models.DateTimeField(verbose_name=_('end'))


    class Meta:
        ordering=('title',)
    
    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse('todoapp:task_detail',args=[self.title,self.id])
    


    










