from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField


class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish

    class Meta:
        ordering = ('position',)


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')

    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('category', 'position',)
        constraints = [
            models.UniqueConstraint(
                fields=['position', 'category'],
                name='unique_position_per_category'
            )
        ]
        unique_together = ['id', 'slug']


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/')
    is_visible = models.BooleanField(default=True)


class Reservation(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^0[0-9]{9}$',
        message='Phone number must be entered in the format: 0xxxxxxxxx',
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=200, blank=True)

    is_processed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone}: {self.date} {self.time}'

    class Meta:
        ordering = ('-date',)


class ContactInfoItem(models.Model):
    item = RichTextField()
    position = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ('position', )


class Chef(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.CharField(max_length=100)

    bio = models.TextField()
    image = models.ImageField(upload_to='chefs/')
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_social_links(self):
        social_links = {
            'twitter': self.twitter,
            'facebook': self.facebook,
            'instagram': self.instagram,
            'linkedin': self.linkedin,
        }
        return {platform: link for platform, link in social_links.items() if link}

    def get_short_bio(self, max_length=100):
        if len(self.bio) <= max_length:
            return self.bio
        return self.bio[:max_length] + '...'

    class Meta:
        ordering = ('order', )



class Event(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField()
    short_desc = models.TextField(max_length=500, blank=True)
    desc = models.TextField(max_length=2000, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='events/', blank=True)
    date_time = models.DateTimeField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Events'
        ordering = ('position', )
        unique_together = ['id', 'slug']


class IconBox(models.Model):
    icon_class = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title