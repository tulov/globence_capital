from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from api.v1.models import Order
from api.v1.serializers import OrderPostSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'orders': reverse('order_create', request=request, format=format),
    })


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderPostSerializer
