
from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include


urlpatterns = [
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^admin/', admin.site.urls),
]
