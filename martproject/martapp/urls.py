from django.urls import path
from .views import martbilling,billing_id

urlpatterns = [
    path('postdata/',martbilling),
    path('getdata/<int:id>/',billing_id),
]