from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('stk_push_callback/', views.stk_push_callback, name='stk_push_callback'),
]
