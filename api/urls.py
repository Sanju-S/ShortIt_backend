from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllLinkView.as_view(), name="all_links"),
    path('create/', views.GetShortLinkView.as_view(), name="get_short_link"),
    path('get/', views.GetFullLinkView.as_view(), name="get_full_link"),
    path('test/', views.GetShortLink.as_view(), name="test"),
]
