from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    #if image is not uploaded
    image=models.ImageField(default='./../media/profile_pics/default.jpg',upload_to='profile_pics')

    #lets be more restricted and use dunders
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        
        from PIL import Image
        img=Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)