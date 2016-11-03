from django.db import models

class Article(models.Model):
    STATUS_CHOICE = (
        ('d','draft'),
        ('P','published')
    )
    title = models.CharField('标题',max_length=70)
    text = models.TextField('正文')
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间',auto_now=True)
    status = models.CharField('文章状态',max_length=1,choices=STATUS_CHOICE)
    abstract = models.CharField('摘要',max_length=50,blank=True,null=True,help_text='可选，如无则摘取正文前50字符')
    #### blank=True;null=True,表示该字段可为空，可不填
    views = models.PositiveIntegerField('浏览量',default=0)
    likes = models.PositiveIntegerField('点赞数',default=0)
    topped = models.BooleanField('置顶',default=False)
    category = models.ForeignKey('Category',verbose_name='分类',null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    class meta:
        ordering = ['-last_modified_time']

class Category(models.Model):
    name =models.CharField('类名',max_length=20)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间',auto_now=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    comments = models.TextField('评论')
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    article = models.ForeignKey('Article',verbose_name='所属文章')
    articleid = models.IntegerField('文章ID',default=0)
    def __str__(self):
        return self.comments


