from  django.urls import path
from products import views


urlpatterns = [
    path('',views.product_list_create_api_view),
    path('<int:id>/', views.procduct_datail_api_view),
]