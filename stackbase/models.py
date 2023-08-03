from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Question(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=10000) 
    #content = models.TextField(null=True, blank=True) #Content of the Q
    content = RichTextField()
    likes = models.ManyToManyField(User, related_name='question_post') 
    date_created = models.DateTimeField(default= timezone.now) 


    def __str__(self):
         return f'{self.user.username} - Question' 
    
    def get_absolute_url(self):  #when Q is posted from frontend after it is posted reerse page to its details.
        return reverse('stackbase:question_detail', kwargs={'pk': self.pk})
    
    def total_likes(self): # total upvotes 
        return self.likes.count()
    
class Comment(models.Model): #create a model Comment
    question = models.ForeignKey(Question, related_name="comment", on_delete= models.CASCADE) #(Question)so that it can acess all the fields in Question class above ,(related_name) to access this model from any part of our website, (on_delete)used so that when user got delete its Q. also get deleted
    name = models.CharField(max_length=1000)
    #content = models.TextField(null=True, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self): #return Q title and user who posted the comment
        return '%s -%s' %(self.question.title, self.question.user)
    
    def get_absolute_url(self): #redirect page to the question_detail after comment is posted
        return reverse('stackbase:question_detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs): #save the comment
        super().save(*args, **kwargs)
    