from django.db import models
# from django.utils.text import slugify

    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='team/')
    behance = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class PortfolioPage(models.Model):
    data_time = models.CharField(max_length=100,  )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.name

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(PortfolioPage, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return f"Image for {self.portfolio.name}"


    
    
class die_shop(models.Model):
    name = models.CharField(max_length=100)    
    description = models.TextField()
    image = models.ImageField(upload_to='works/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    

class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='works/')  # asosiy rasm

    def __str__(self):
        return self.name


class OfferImage(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='works/gallery/')

    def __str__(self):
        return f"Image for {self.offer.name}"


class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    blocked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

class Certificate(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name or "No name"
    
class ServicePage(models.Model):
    title = models.CharField(max_length=200)  
    subtitle = models.CharField(max_length=200, blank=True, null=True)  
    description = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title


class ServiceAccordion(models.Model):
    service = models.ForeignKey(ServicePage, on_delete=models.CASCADE, related_name="accordions")
    accordion_title = models.CharField(max_length=200)
    accordion_desc = models.TextField()

    def __str__(self):
        return f"{self.service.title} - {self.accordion_title}"
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)      
    description = models.TextField()             
    date = models.DateField()                   

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="blog_images/")

    def __str__(self):
        return f"Image for {self.post.title}"