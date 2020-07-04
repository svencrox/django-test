from django.contrib import admin
from .models import uploaded_file

class uploadFileAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title',]
  
admin.site.register(uploaded_file, uploadFileAdmin)