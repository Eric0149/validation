from django.contrib import admin
from .models import Participants, Vehicle
# Register your models here.

admin.site.register(Participants)
admin.site.register(Vehicle)
# class ParticipantsAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'date_of_birth', 'phone', 'gender', 'email')
#     search_fields = ('first_name', 'last_name', 'email')
#     list_filter = ('gender', 'date_of_birth')
