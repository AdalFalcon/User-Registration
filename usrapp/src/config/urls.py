from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path("up/", include("up.urls")),
    path("", include("pages.urls")),
    path("account/", include("account.urls")), # <---- Users App / Aplicion Usuarios.
    path("admin/", admin.site.urls),
]
if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
        path("__debug__/", include("debug_toolbar.urls")),
    ]
