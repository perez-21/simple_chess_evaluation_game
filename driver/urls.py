from django.urls import path
from .views import index, PositionDetailView

urlpatterns = [
  path("", index, name='home',),
  path("<int:pk>", PositionDetailView.as_view(), name='test'),
]