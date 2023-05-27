from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('register/', views.reg, name="register"),
    path('logout/',views.log_out, name="logout"),
    path('predict/', views.predictor, name='predict'),
    path('records/', views.db_record, name='records'),
    path('delete/<int:pk>', views.delete, name='delete')
]
