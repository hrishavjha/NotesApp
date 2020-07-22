from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
	user = models.ForeignKey(
		User, null=True,
		on_delete=models.CASCADE,
	)
	doc = models.DateTimeField(auto_now=True)
	content = models.TextField(max_length=None, blank=False, null=False)
	title = models.CharField(max_length=400, blank=False, null=False)

	class Meta:
		db_table = "Notes"

	def __str__(self):
		return str(self.user)