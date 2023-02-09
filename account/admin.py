from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()  #получение актульного юзера в данном проекте
# admin.site.register(User)

admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('email' 'name', 'is_staff')
    list_filter = (('is_staff', admin.BooleanFieldListFilter),)