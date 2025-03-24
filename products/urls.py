from  django.urls import path
from products import views
from utils.constants import LIST_CREATE,RETRIEVE_UPDATE_DESTROY

urlpatterns = [
    path('',views.product_list_create_api_view),
    path('<int:id>/', views.procduct_datail_api_view),
    path('categories/',views.CategoryListApiView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailApiView.as_view()),
    path('tags/', views.TagModelViewSet.as_view(LIST_CREATE)),
    path('tags/<int:id>/', views.TagModelViewSet.as_view(RETRIEVE_UPDATE_DESTROY))
]