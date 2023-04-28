from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.captcha import captcha_urlpatterns
from core.schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/user/', include('apps.users.urls'), name='users'),
    # path('canban/', include('apps.canban.urls'), name='canban')
]
urlpatterns += swagger_urlpatterns
urlpatterns += captcha_urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
