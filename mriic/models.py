from django.db import models

# Create your models here.
class Blog(models.Model):
    CATEGORY_CHOICES = [('Tech', 'Science & Technology'),
                 ('Food', 'Food'),
                 ('Lifestyle', 'Lifestyle'),]
    Blog_id = models.CharField(max_length=30, unique = True)
    Blog_title = models.CharField(max_length=300)
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Tech')
    Content = models.TextField()
    Blog_image = models.ImageField(upload_to='images/')
    Created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Blog_id
    
class Contact_Us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=400)  
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email