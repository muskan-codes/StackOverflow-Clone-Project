from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #OneToOneField ensures that one user have only one profile
    bio = models.CharField(max_length=1000)
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(default = 'default.jpg', upload_to = "profile_pic")

    def __str__(self): #__str__ dender str
        return f'{self.user.username} - Profile' # It gonna show as Muskan - Profile

#Limiting the image    
    def save(self, *args, **kwargs): #Define a save function
        super().save(*args, **kwargs)
        img = Image.open(self.image.path) # define variable img after importing Image from pillow and after opening the image from path
        if img.height > 300 or img.width > 300:  #checking if the conditions met
            output_size = (300, 300)   #redefine the size we want
            img.thumbnail(output_size)  #pass the redefined image size
            img.save(self.image.path)   #and save it 
    


