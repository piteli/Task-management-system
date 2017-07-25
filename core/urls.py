from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/', include('tasks.urls', namespace='tasker')),
    url(r'^auth/', include('authentication.urls', namespace='auth')),
    url(r'^', include('home.urls', namespace='home')),
]
