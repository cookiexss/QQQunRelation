from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('findQQ.urls'))
    path('', views.home, name="home"),
    path('find/', views.optionselect, name='find'),
]
