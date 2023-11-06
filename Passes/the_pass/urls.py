from django.urls import path
from .views import Pereval_addedAPICreate, PerevalOne, PerevalByUserEmailList


urlpatterns = [
    path('submitData', Pereval_addedAPICreate.as_view()),
    path('submitData/', Pereval_addedAPICreate.as_view()),
    path('submitData/<int:pk>/', PerevalOne.as_view()),
    path('submitData/', PerevalByUserEmailList.as_view({'get': 'list'})),
]
