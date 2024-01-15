from django.urls import path
from . import views

urlpatterns=[
    path('',views.listadoProvincias),
    path('guardarProvincia/',views.guardarProvincia),
    path('eliminarProvincia/<id_bg>' ,views.eliminarProvincia),
    path('editarProvincia/<id_bg>' ,views.editarProvincia),
    path('procesarActualizacionProvincia/', views.procesarActualizacionProvincia),
    path('listadoClientes/',views.listadoClientes),
    path('eliminarCliente/<id_bg>' ,views.eliminarCliente),
    path('guardarCliente/',views.guardarCliente),
    path('editarCliente/<id_bg>' ,views.editarCliente),
    path('procesarActualizacionCliente/', views.procesarActualizacionCliente),
    path('listadoTipos/',views.listadoTipos),
    path('eliminarTipo/<id_bg>' ,views.eliminarTipo),
    path('guardarTipo/',views.guardarTipo),
    path('editarTipo/<id_bg>' ,views.editarTipo),
    path('procesarActualizacionTipo/', views.procesarActualizacionTipo),
    path('listadoPedidos/',views.listadoPedidos),
    path('eliminarPedido/<id_bg>' ,views.eliminarPedido),
    path('guardarPedido/',views.guardarPedido),
    path('editarPedido/<id_bg>' ,views.editarPedido),
    path('procesarActualizacionPedido/', views.procesarActualizacionPedido),
    path('listadoPlatillos/',views.listadoPlatillos),
    path('eliminarPlatillo/<id_bg>' ,views.eliminarPlatillo),
    path('guardarPlatillo/',views.guardarPlatillo),
    path('editarPlatillo/<id_bg>' ,views.editarPlatillo),
    path('procesarActualizacionPlatillo/', views.procesarActualizacionPlatillo),
    path('listadoDetalles/',views.listadoDetalles),
    path('eliminarDetalle/<id_bg>' ,views.eliminarDetalle),
    path('guardarDetalle/',views.guardarDetalle),
    path('editarDetalle/<id_bg>' ,views.editarDetalle),
    path('procesarActualizacionDetalle/', views.procesarActualizacionDetalle),
    path('listadoIngredientes/',views.listadoIngredientes),
    path('eliminarIngrediente/<id_bg>' ,views.eliminarIngrediente),
    path('guardarIngrediente/',views.guardarIngrediente),
    path('editarIngrediente/<id_bg>' ,views.editarIngrediente),
    path('procesarActualizacionIngrediente/', views.procesarActualizacionIngrediente),
    path('listadoRecetas/',views.listadoRecetas),
    path('eliminarReceta/<id_bg>' ,views.eliminarReceta),
    path('guardarReceta/',views.guardarReceta),
    path('editarReceta/<id_bg>' ,views.editarReceta),
    path('procesarActualizacionReceta/', views.procesarActualizacionReceta),
























]
