from django.urls import path, include
from .views import StatusAPIView, StateAPIView, LogAPIView


urlpatterns = [
    path('status/', StatusAPIView.as_view(), name='status'),
    path('log/', LogAPIView.as_view(), name='log'),
    path('state/', StateAPIView.as_view(), name='state'),
]
