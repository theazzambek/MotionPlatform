from django.contrib import admin

from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'created_date')
    search_fields = ('firstname', 'lastname', 'email')


admin.site.register(MyUser, MyUserAdmin)


# from django import forms
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.core.exceptions import ValidationError
#
# from .models import MyUser
#
#
# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = MyUser
#         fields = ('email', 'firstname', 'lastname', 'speciality', 'experience')
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])  # Используем set_password для установки хешированного пароля
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = MyUser
#         fields = ('email', 'password', 'firstname', 'lastname', 'is_admin')
#
#
# class UserAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     list_display = ('firstname', 'lastname', 'email', 'created_date', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('firstname', 'lastname', 'speciality', 'experience')}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('firstname', 'lastname', 'email', 'password1', 'password2', 'is_admin', 'speciality', 'experience'),
#         }),
#     )
#     search_fields = ('firstname', 'lastname', 'email')
#     ordering = ('email',)
#     filter_horizontal = ()
#
#
# admin.site.register(MyUser, UserAdmin)
