# from django.contrib.auth.models import User
# from django.db import models
#
#
# def user_directory_path(instance, filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)
#
#
# class ExtendedUser(models.Model):
#     user = models.ForeignKey(
#         User, null=True,
#         on_delete=models.CASCADE,
#     )
#     profile_image = models.ImageField(null=True, blank=True, upload_to='user_directory_path')
#
#     class Meta:
#         db_table = "Extended Details"
#
#     def __str__(self):
#         return str(self.user)
