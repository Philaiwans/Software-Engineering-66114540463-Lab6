from django.contrib import admin
from django.urls import path, include  # ✅ เพิ่ม include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # ✅ เรียก urls ของแอป core
]
