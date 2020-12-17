from django.urls import path
from . import views

urlpatterns = [
    path('', views.recom_home, name='recom_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.RecommendationDetail.as_view(), name='recommendation-details'),
    path('<int:pk>/update', views.RecommendationUpdate.as_view(), name='recommendation-update'),
    path('<int:pk>/delete', views.RecommendationDelete.as_view(), name='recommendation-delete'),

]
