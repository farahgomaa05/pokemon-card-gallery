from django.contrib import admin
from django.urls import path, include
from api.views import index_view  # or replace 'api' with the correct app name
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # this gives you /api/cards/

]

urlpatterns += [
    re_path(r'^.*$', index_view),  # fallback to React
]