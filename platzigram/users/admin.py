#Django
from django.contrib import admin

#Models
from users.models import Profile

# Register your models here.
# admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	# pass
	list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
	list_display_links = ('pk', 'user')
	list_editable = ('phone_number', 'website', 'picture')
	search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number', 'user__username')

	list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')