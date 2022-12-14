from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField('제목', max_length=126, null=False)
    content = models.TextField('내용', null=False)
    author = models.CharField('작성자', max_length=16, null=False)
    created = models.DateTimeField('작성시간', auto_now_add=True)

class PyBlog(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    update_dt = models.DateTimeField(auto_now=True)
    regist_dt = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     db_table = 'py_blog'

class Reply(models.Model):
    boardNum = models.IntegerField(null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
