from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Todo(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    tag = models.ManyToManyField(Tag, related_name='tasks', blank=True)

    def __str__(self):
        return self.title