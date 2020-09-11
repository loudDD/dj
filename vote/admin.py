from django.contrib import admin

# Register your models here.
import vote

admin.site.register(vote.models.Question)
admin.site.register(vote.models.Choice)