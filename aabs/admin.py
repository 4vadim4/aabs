from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CASBook, LoadFileForm, UserProfile
from django.utils.translation import ugettext_lazy as _


admin.site.register(CASBook)
admin.site.register(LoadFileForm)


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = _('Additionally info')

# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline, )

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)