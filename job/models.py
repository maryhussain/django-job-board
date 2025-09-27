from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

JOB_TYPE=[
    ('full time','full time'),
    ('part time','part time')
]
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default= 0)
    experience = models.IntegerField(default= 1)
    category = models.ForeignKey(Category,max_length = 25,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    




