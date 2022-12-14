from django.contrib import admin
from crm.models import Customer ,Project,Profile,Task

# Register your models here.

admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Task)

class UserAdmin(admin.ModelAdmin):
    list_display = ('email','mobile','password')