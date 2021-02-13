"""User model"""
from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(models.Manager):
    """user model manager"""

    def create_user(self, data):
        """Create user"""
        return self.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            password=make_password(data.get("password"))
        )

    def get_user_details(self, pk):
        """
        :param pk:
        :return:
        """
        user = self.filter(id=pk)
        if user.exists():
            return {
                "id": user[0].id,
                "name": f"{user[0].first_name} {user[0].last_name}"
            }


class TagManager(models.Manager):
    """Tag manager"""

    def create_tag(self, data):
        """
        :param data:
        :return:
        """
        user = User.objects.filter(pk=data.get("id"))
        if user.exists():
            for tag in data.get("tags"):
                new_tag = self.create(
                    name=tag,
                    expiry=data.get("expiry")
                )
                user[0].tags.add(new_tag)


class Tags(models.Model):
    """User tag atrribute"""
    name = models.TextField(max_length=300)
    expiry = models.PositiveIntegerField()

    objects = TagManager()

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class User(models.Model):
    """User model atrribute"""
    first_name = models.TextField()
    last_name = models.TextField()
    password = models.TextField()
    tags = models.ManyToManyField(Tags)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name}"
