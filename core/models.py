from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField("core.Order", related_name="user")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

class Category(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})
        


class Item(models.Model):

    plate_size_options = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('full', 'Full'),
    )

    name = models.CharField(max_length=100);
    image = models.ImageField(upload_to="items/")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField()
    discounts = models.IntegerField(default=0)
    size = models.CharField(choices=plate_size_options, max_length=50, blank=True, null=True)
    veg = models.BooleanField()

    class Meta:
        verbose_name = ("item")
        verbose_name_plural = ("items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})

class Order(models.Model):

    order_status_options = (
        ('received', 'Received'),
        ('cooking', 'Cooking'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )

    items = models.ManyToManyField(Item, related_name="order")
    ordered_at = models.DateTimeField(default=timezone.now)
    total_price = models.IntegerField()
    status = models.CharField(choices=order_status_options, max_length=50)
    discounts = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})

