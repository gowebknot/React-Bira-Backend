from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Issue(BaseModel):
    PRIORITY_SHOWSTOPPER = "SHOWSTOPPER"
    PRIORITY_HIGH = "HIGH"
    PRIORITY_MEDIUM = "MEDIUM"
    PRIORITY_LOW = "LOW"
    PRIORITY_VERY_LOW = "VERY LOW"

    PRIORITY_CHOICES = [PRIORITY_SHOWSTOPPER, PRIORITY_HIGH, PRIORITY_MEDIUM, PRIORITY_LOW, PRIORITY_VERY_LOW]

    STATUS_TODO = "TODO"
    STATUS_DOING = "DOING"
    STATUS_DONE = "DONE"

    STATUS_CHOICES = [STATUS_TODO, STATUS_DOING, STATUS_DONE]

    short_id = models.CharField(max_length=31)
    title = models.CharField(max_length=127, null=True, blank=True)
    description = models.TextField()
    priority = models.CharField(max_length=63, choices=zip(PRIORITY_CHOICES, PRIORITY_CHOICES))
    status = models.CharField(max_length=31, choices=zip(STATUS_CHOICES, STATUS_CHOICES))
    assignee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="assigned_issues")


class UserProfile(BaseModel):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, related_name="user_profile")
    title = models.CharField(max_length=63, null=True, blank=True)
    profile_pic = models.URLField()

    def __str__(self):
        return "{} - {}".format(self.user.email, self.title)
