from django.contrib import admin
from  .models import Text

# Register your models here.
 
class pesonalize(admin.ModelAdmin):
    list_display=('plaintext','finaltext')
admin.site.register(Text,pesonalize)