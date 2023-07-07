#from django.conf.urls import url
from django.urls import path, include

from .views import (
    AccountView,
    AccountsDetailedView
)


urlpatterns = [

    path('v1',AccountView.as_view()),
    path('v1/<int:account_ID>/',AccountsDetailedView.as_view())


]
