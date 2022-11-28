from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Catagories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=350)
    about_title = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=350, null=True, blank=True)
    about_author = models.TextField(null=True, blank=True)
    illustrator = models.CharField(max_length=350, null=True, blank=True)
    asin = models.CharField(max_length=254, null=True, blank=True)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    print_length = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=254, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    release_date = models.DateField(auto_now=False, auto_now_add=False,
                                    blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hero = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
