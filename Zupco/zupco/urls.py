
from django.urls import include, path
from django.contrib import admin
from tabs.views import home_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("users.urls")),
    path("", include("maps.urls" , namespace="maps")),
    path("admin/", admin.site.urls),
    path('home/',home_page,name="home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)