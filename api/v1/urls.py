from django.urls import path
from api.v1.views import OrderViewSet, api_root


order_post = OrderViewSet.as_view({
    'post': 'create',
})

urlpatterns = [
    path('', api_root),
    path('orders/', order_post, name='order_create'),
]
