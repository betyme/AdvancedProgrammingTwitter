from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Tweet

# unregister groups
admin.site.unregister(Group)

# add profile info into User
class ProfileInline(admin.StackedInline):
    model = Profile

# extend user model 
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
# register initial user
admin.site.unregister(User)
# register user and profile user
admin.site.register(User, UserAdmin)
# register tweets
admin.site.register(Tweet)





    