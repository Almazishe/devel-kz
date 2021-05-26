from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        # Version 1 of API
        path('v1/', include([
            # Authorization, User related apis
            path('auth/', include('src.accounts.urls')),
            
            # Another apis
            # ...
            path('finance/', include('src.operations.urls')),
        ]))
    ])),
]
