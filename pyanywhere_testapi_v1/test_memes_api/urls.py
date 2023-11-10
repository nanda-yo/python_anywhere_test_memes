#from django.conf.urls import url
from django.urls import path, include

from .views import (
    AccountView,
    AccountsDetailedView
)

app_name = 'test_memes_api'
urlpatterns = [

    path('v1',AccountView.as_view(),name = 'api'),
    path('v1/<int:account_ID>/',AccountsDetailedView.as_view())


]
