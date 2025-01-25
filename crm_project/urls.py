from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # صفحه ادمین
    path('', include('crm.urls')),  # صفحه اصلی و سایر URL‌های اپلیکیشن crm
]