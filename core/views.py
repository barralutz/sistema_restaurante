# core/views.py
from rest_framework import viewsets
from .models import Area, Platillo, Pedido, Parte
from .serializers import AreaSerializer, PlatilloSerializer, PedidoSerializer, ParteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]

class PlatilloViewSet(viewsets.ModelViewSet):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer
    permission_classes = [IsAuthenticated]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        pedido = Pedido.objects.create(
            mesa=data['mesa'],
            mesero=request.user,
            estado='Pendiente'
        )
        for platillo_id in data['platillos']:
            platillo = Platillo.objects.get(id=platillo_id)
            for area in platillo.areas.all():
                Parte.objects.create(
                    pedido=pedido,
                    platillo=platillo,
                    area=area,
                    estado='Pendiente'
                )
        serializer = self.get_serializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def cerrar(self, request, pk=None):
        pedido = self.get_object()
        pedido.estado = 'Cerrado'
        pedido.save()
        return Response({'status': 'Pedido cerrado'})

class ParteViewSet(viewsets.ModelViewSet):
    queryset = Parte.objects.all()
    serializer_class = ParteSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def actualizar_estado(self, request, pk=None):
        parte = self.get_object()
        estado = request.data.get('estado')
        if estado in dict(Parte.ESTADOS_PARTE).keys():
            parte.estado = estado
            parte.save()
            return Response({'status': f'Parte actualizada a {estado}'})
        else:
            return Response({'error': 'Estado inválido'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def completar(self, request, pk=None):
        parte = self.get_object()
        parte.estado = 'Completado'
        parte.save()
        return Response({'status': 'Parte completada'})
