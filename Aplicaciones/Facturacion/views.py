from django.shortcuts import render, redirect
from .models import Provincia
from .models import Cliente
from .models import Tipo
from .models import Pedido
from .models import Platillo
from .models import DetallePlatillo
from .models import Ingrediente
from .models import Receta
from django.contrib import messages

# Create your views here.
def listadoProvincias(request):
    provinciaBdd = Provincia.objects.all()
    return render(request, 'listadoProvincias.html', {'provincias': provinciaBdd})


def guardarProvincia(request):
    nombre_bg=request.POST["nombre_bg"]
    poblacion_bg=request.POST["poblacion_bg"]
    capital_bg=request.POST["capital_bg"]
    fotografia=request.FILES.get("fotografia")
    #Insertando datos mediante el ORM de django
    provincia =Provincia.objects.create(nombre_bg=nombre_bg,poblacion_bg=poblacion_bg,capital_bg=capital_bg,fotografia=fotografia)
    messages.success(request, 'PROVINCIA GUARDADO EXITOSAMENTE')
    return redirect('/')


def eliminarProvincia(request,id_bg):
    provinciaEliminar=Provincia.objects.get(id_bg=id_bg)
    provinciaEliminar.delete()
    messages.success(request, 'PROVINCIA ELIMINADA EXITOSAMENTE')
    return redirect('/')

def editarProvincia(request, id_bg):
    provinciaEditar=Provincia.objects.get(id_bg=id_bg)
    provinciasBdd=Provincia.objects.all()
    return  render(request, 'editarProvincia.html',{'provincia':provinciaEditar,'provincias':provinciasBdd})


def procesarActualizacionProvincia(request):
    id_bg=request.POST["id_bg"]
    nombre_bg=request.POST["nombre_bg"]
    poblacion_bg=request.POST["poblacion_bg"]
    capital_bg=request.POST["capital_bg"]
    fotografia=request.POST["fotografia"]

    #Insertando datos mediante el ORM de DJANGO
    provinciaEditar=Provincia.objects.get(id_bg=id_bg)
    provinciaEditar.nombre_bg=nombre_bg
    provinciaEditar.poblacion_bg=poblacion_bg
    provinciaEditar.capital_bg=capital_bg
    provinciaEditar.fotografia=fotografia
    provinciaEditar.save()
    messages.success(request,
      'PROVINCIA ACTUALIZADA EXITOSAMENTE')
    return redirect('/')


def listadoClientes(request):
    clientesBdd = Cliente.objects.all()
    provinciaBdd = Provincia.objects.all()

    return render(request, 'listadoClientes.html', {'clientes': clientesBdd, 'provincias': provinciaBdd})

def eliminarCliente(request,id_bg):
    clienteEliminar=Cliente.objects.get(id_bg=id_bg)
    clienteEliminar.delete()
    messages.success(request, 'CLIENTE ELIMINADO EXITOSAMENTE')
    return redirect('/listadoClientes/')

def guardarCliente(request):
    id_provincia=request.POST["id_provincia"]
    #capturando el tipo seleccionado por el usuario
    provinciaSeleccionado=Provincia.objects.get(id_bg=id_provincia)

    cedula_bg=request.POST["cedula_bg"]
    apellido_bg=request.POST["apellido_bg"]
    nombre_bg=request.POST["nombre_bg"]
    direccion_bg=request.POST["direccion_bg"]
    fecha_nacimiento_bg=request.POST["fecha_nacimiento_bg"]
    correo_bg=request.POST["correo_bg"]
    #Insertando datos mediante el ORM de django

    cliente =Cliente.objects.create(cedula_bg=cedula_bg,apellido_bg=apellido_bg,nombre_bg=nombre_bg,direccion_bg=direccion_bg,fecha_nacimiento_bg=fecha_nacimiento_bg,correo_bg=correo_bg, provincia_bg=provinciaSeleccionado)
    messages.success(request, 'CLIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoClientes/')

def editarCliente(request, id_bg):
    clienteEditar=Cliente.objects.get(id_bg=id_bg)
    clientesBdd=Cliente.objects.all()
    provinciaBdd = Provincia.objects.all()
    return  render(request, 'editarCliente.html',{'cliente':clienteEditar,'clientes':clientesBdd,'provincias': provinciaBdd})


def procesarActualizacionCliente(request):
    id_bg = request.POST["id_bg"]
    id_provincia = request.POST["id_provincia"]
    provinciaSeleccionado = Provincia.objects.get(id_bg=id_provincia)
    cedula_bg = request.POST["cedula_bg"]
    apellido_bg = request.POST["apellido_bg"]
    nombre_bg = request.POST["nombre_bg"]
    direccion_bg = request.POST["direccion_bg"]
    fecha_nacimiento_bg = request.POST["fecha_nacimiento_bg"]
    correo_bg = request.POST["correo_bg"]

    # Insertando datos mediante el ORM de DJANGO
    clienteEditar = Cliente.objects.get(id_bg=id_bg)
    clienteEditar.provincia_bg = provinciaSeleccionado  # Corregido el nombre del campo
    clienteEditar.cedula_bg = cedula_bg
    clienteEditar.apellido_bg = apellido_bg  # Corregido el nombre del campo
    clienteEditar.nombre_bg = nombre_bg
    clienteEditar.direccion_bg = direccion_bg  # Corregido el nombre del campo
    clienteEditar.fecha_nacimiento_bg = fecha_nacimiento_bg
    clienteEditar.correo_bg = correo_bg  # Corregido el nombre del campo
    clienteEditar.save()

    messages.success(request, 'Cliente ACTUALIZADO Exitosamente')
    return redirect('/listadoClientes/')


def listadoTipos(request):
    tipoBdd = Tipo.objects.all()
    return render(request, 'listadoTipos.html', {'tipos': tipoBdd})

def eliminarTipo(request,id_bg):
    tipoEliminar=Tipo.objects.get(id_bg=id_bg)
    tipoEliminar.delete()
    messages.success(request, 'TIPO ELIMINADO EXITOSAMENTE')
    return redirect('/listadoTipos/')

def guardarTipo(request):
    nombre_bg=request.POST["nombre_bg"]
    descripcion_bg=request.POST["descripcion_bg"]
    fotografia=request.FILES.get("fotografia")
    #Insertando datos mediante el ORM de django
    tipo =Tipo.objects.create(nombre_bg=nombre_bg,descripcion_bg=descripcion_bg,fotografia=fotografia)
    messages.success(request, 'TIPO GUARDADO EXITOSAMENTE')
    return redirect('/listadoTipos/')


def editarTipo(request, id_bg):
    tipoEditar=Tipo.objects.get(id_bg=id_bg)
    tiposBdd=Tipo.objects.all()
    return  render(request, 'editarTipo.html',{'tipo':tipoEditar,'tipos':tiposBdd})

def procesarActualizacionTipo(request):
    id_bg=request.POST["id_bg"]
    nombre_bg=request.POST["nombre_bg"]
    descripcion_bg=request.POST["descripcion_bg"]
    fotografia=request.POST["fotografia"]

    #Insertando datos mediante el ORM de DJANGO
    tipoEditar=Tipo.objects.get(id_bg=id_bg)
    tipoEditar.nombre_bg=nombre_bg
    tipoEditar.descripcion_bg=descripcion_bg
    tipoEditar.fotografia=fotografia
    tipoEditar.save()
    messages.success(request,
      'TIPO ACTUALIZADO EXITOSAMENTE')
    return redirect('/listadoTipos/')


def listadoPedidos(request):
    pedidosBdd = Pedido.objects.all()
    clienteBdd = Cliente.objects.all()

    return render(request, 'listadoPedidos.html', {'pedidos': pedidosBdd, 'clientes': clienteBdd})

def eliminarPedido(request,id_bg):
    pedidoEliminar=Pedido.objects.get(id_bg=id_bg)
    pedidoEliminar.delete()
    messages.success(request, 'PEDIDO ELIMINADO EXITOSAMENTE')
    return redirect('/listadoPedidos/')

def guardarPedido(request):
    id_cliente=request.POST["id_cliente"]
    #capturando el tipo seleccionado por el usuario
    clienteSeleccionado=Cliente.objects.get(id_bg=id_cliente)

    fecha_bg=request.POST["fecha_bg"]
    estado_bg=request.POST["estado_bg"]
    observaciones_bg=request.POST["observaciones_bg"]
    #Insertando datos mediante el ORM de django

    pedido =Pedido.objects.create(fecha_bg=fecha_bg,estado_bg=estado_bg,observaciones_bg=observaciones_bg,cliente_bg=clienteSeleccionado)
    messages.success(request, 'CLIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoPedidos/')

def editarPedido(request, id_bg):
    pedidoEditar=Pedido.objects.get(id_bg=id_bg)
    pedidosBdd=Pedido.objects.all()
    clienteBdd = Cliente.objects.all()
    return  render(request, 'editarPedido.html',{'pedido':pedidoEditar,'pedidos':pedidosBdd,'clientes': clienteBdd})

def procesarActualizacionPedido(request):
    id_bg = request.POST["id_bg"]
    id_cliente = request.POST["id_cliente"]
    clienteSeleccionado = Cliente.objects.get(id_bg=id_cliente)
    fecha_bg = request.POST["fecha_bg"]
    estado_bg = request.POST["estado_bg"]
    observaciones_bg = request.POST["observaciones_bg"]

    # Insertando datos mediante el ORM de DJANGO
    pedidoEditar = Pedido.objects.get(id_bg=id_bg)
    pedidoEditar.cliente_bg = clienteSeleccionado  # Corregido el nombre del campo
    pedidoEditar.fecha_bg = fecha_bg
    pedidoEditar.estado_bg = estado_bg  # Corregido el nombre del campo
    pedidoEditar.observaciones_bg = observaciones_bg
    pedidoEditar.save()

    messages.success(request, 'PEDIDO ACTUALIZADO CORRECTAMENTE')
    return redirect('/listadoPedidos/')

def listadoPlatillos(request):
    platillosBdd = Platillo.objects.all()
    tipoBdd = Tipo.objects.all()

    return render(request, 'listadoPlatillos.html', {'platillos': platillosBdd, 'tipos': tipoBdd})

def eliminarPlatillo(request,id_bg):
    platilloEliminar=Platillo.objects.get(id_bg=id_bg)
    platilloEliminar.delete()
    messages.success(request, 'PLATILLO ELIMINADO EXITOSAMENTE')
    return redirect('/listadoPlatillos/')

def guardarPlatillo(request):
    id_tipo=request.POST["id_tipo"]
    #capturando el tipo seleccionado por el usuario
    tipoSeleccionado=Tipo.objects.get(id_bg=id_tipo)

    nombre_bg=request.POST["nombre_bg"]
    precio_bg=request.POST["precio_bg"]
    disponibilidad_bg=request.POST["disponibilidad_bg"]
    fotografia=request.FILES.get("fotografia")
    #Insertando datos mediante el ORM de django

    platillo =Platillo.objects.create(nombre_bg=nombre_bg,precio_bg=precio_bg,disponibilidad_bg=disponibilidad_bg,fotografia=fotografia,tipo_bg=tipoSeleccionado)
    messages.success(request, 'CLIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoPlatillos/')

def editarPlatillo(request, id_bg):
    platilloEditar=Platillo.objects.get(id_bg=id_bg)
    platillosBdd=Tipo.objects.all()
    tipoBdd=Tipo.objects.all()
    return  render(request, 'editarPlatillo.html',{'platillo':platilloEditar,'platillos':platillosBdd, 'tipos':tipoBdd})

def procesarActualizacionPlatillo(request):
    id_bg = request.POST["id_bg"]
    id_tipo = request.POST["id_tipo"]
    tipoSeleccionado = Tipo.objects.get(id_bg=id_tipo)
    nombre_bg = request.POST["nombre_bg"]
    precio_bg = request.POST["precio_bg"]
    disponibilidad_bg = request.POST["disponibilidad_bg"]
    fotografia=request.POST["fotografia"]


    # Insertando datos mediante el ORM de DJANGO
    platilloEditar = Platillo.objects.get(id_bg=id_bg)
    platilloEditar.tipo_bg = tipoSeleccionado  # Corregido el nombre del campo
    platilloEditar.nombre_bg = nombre_bg
    platilloEditar.precio_bg = precio_bg  # Corregido el nombre del campo
    platilloEditar.disponibilidad_bg = disponibilidad_bg
    platilloEditar.fotografia=fotografia

    platilloEditar.save()

    messages.success(request, 'PLATILLO ACTUALIZADO CORRECTAMENTE')
    return redirect('/listadoPlatillos/')

def listadoDetalles(request):
    detalleplatillosBdd = DetallePlatillo.objects.all()

    pedidoBdd = Pedido.objects.all()
    platilloBdd = Platillo.objects.all()

    return render(request, 'listadoDetalles.html', {'detalles': detalleplatillosBdd, 'platillos': platilloBdd,'pedidos': pedidoBdd})

def eliminarDetalle(request,id_bg):
    detalleEliminar=DetallePlatillo.objects.get(id_bg=id_bg)
    detalleEliminar.delete()
    messages.success(request, 'DETALLE ELIMINADO EXITOSAMENTE')
    return redirect('/listadoDetalles/')

def guardarDetalle(request):
    id_platillo=request.POST["id_platillo"]
    id_pedido=request.POST["id_pedido"]
    #capturando el tipo seleccionado por el usuario
    platilloSeleccionado=Platillo.objects.get(id_bg=id_platillo)
    pedidoSeleccionado=Pedido.objects.get(id_bg=id_pedido)

    descripcion_bg=request.POST["descripcion_bg"]
    calorias_bg=request.POST["calorias_bg"]
    fecha_bg=request.POST["fecha_bg"]
    #Insertando datos mediante el ORM de django

    detalle =DetallePlatillo.objects.create(descripcion_bg=descripcion_bg,calorias_bg=calorias_bg,fecha_bg=fecha_bg,platillo_bg=platilloSeleccionado,pedido_bg=pedidoSeleccionado)
    messages.success(request, 'DETALLE DEL PLATILLO GUARDADO EXITOSAMENTE')
    return redirect('/listadoDetalles/')


def editarDetalle(request, id_bg):
    detalleEditar=DetallePlatillo.objects.get(id_bg=id_bg)
    detallesBdd=DetallePlatillo.objects.all()
    platilloBdd=Platillo.objects.all()
    pedidoBdd=Pedido.objects.all()
    return  render(request, 'editarDetalle.html',{'detalle':detalleEditar,'detalles':detallesBdd, 'platillos':platilloBdd, 'pedidos':pedidoBdd})


def procesarActualizacionDetalle(request):
    id_bg = request.POST["id_bg"]
    id_platillo = request.POST["id_platillo"]
    platilloSeleccionado = Platillo.objects.get(id_bg=id_platillo)
    id_pedido = request.POST["id_pedido"]
    pedidoSeleccionado = Pedido.objects.get(id_bg=id_pedido)


    descripcion_bg = request.POST["descripcion_bg"]
    calorias_bg = request.POST["calorias_bg"]
    fecha_bg = request.POST["fecha_bg"]


    # Insertando datos mediante el ORM de DJANGO
    detalleEditar = DetallePlatillo.objects.get(id_bg=id_bg)
    detalleEditar.platillo_bg = platilloSeleccionado  # Corregido el nombre del campo
    detalleEditar.pedido_bg = pedidoSeleccionado  # Corregido el nombre del campo
    detalleEditar.descripcion_bg = descripcion_bg
    detalleEditar.calorias_bg = calorias_bg  # Corregido el nombre del campo
    detalleEditar.fecha_bg = fecha_bg
    detalleEditar.save()

    messages.success(request, 'DETALLE PLATILLO ACTUALIZADO CORRECTAMENTE')
    return redirect('/listadoDetalles/')


def listadoIngredientes(request):
    ingredientesBdd = Ingrediente.objects.all()
    return render(request, 'listadoIngredientes.html', {'ingredientes': ingredientesBdd})

def eliminarIngrediente(request,id_bg):
    ingredienteEliminar=Ingrediente.objects.get(id_bg=id_bg)
    ingredienteEliminar.delete()
    messages.success(request, 'INGREDIENTE ELIMINADO EXITOSAMENTE')
    return redirect('/listadoIngredientes/')


def guardarIngrediente(request):
    nombre_bg = request.POST["nombre_bg"]
    cantidad_disponible_bg=request.POST["cantidad_disponible_bg"]
    unidad_medida_bg=request.POST["unidad_medida_bg"]
    fecha_caducidad_bg=request.POST["fecha_caducidad_bg"]
    fotografia=request.FILES.get("fotografia")
    #Insertando datos mediante el ORM de django
    ingrediente =Ingrediente.objects.create(nombre_bg=nombre_bg,cantidad_disponible_bg=cantidad_disponible_bg,unidad_medida_bg=unidad_medida_bg,fecha_caducidad_bg=fecha_caducidad_bg,fotografia=fotografia)
    messages.success(request, 'INGREDIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoIngredientes')

def editarIngrediente(request, id_bg):
    ingredienteEditar=Ingrediente.objects.get(id_bg=id_bg)
    ingredientesBdd=Ingrediente.objects.all()
    return  render(request, 'editarIngrediente.html',{'ingrediente':ingredienteEditar,'ingredientes':ingredientesBdd})


def procesarActualizacionIngrediente(request):
    id_bg=request.POST["id_bg"]
    nombre_bg=request.POST["nombre_bg"]
    cantidad_disponible_bg=request.POST["cantidad_disponible_bg"]
    unidad_medida_bg=request.POST["unidad_medida_bg"]
    fecha_caducidad_bg=request.POST["fecha_caducidad_bg"]
    fotografia=request.POST["fotografia"]

    #Insertando datos mediante el ORM de DJANGO
    ingredienteEditar=Ingrediente.objects.get(id_bg=id_bg)
    ingredienteEditar.nombre_bg=nombre_bg
    ingredienteEditar.cantidad_disponible_bg=cantidad_disponible_bg
    ingredienteEditar.unidad_medida_bg=unidad_medida_bg
    ingredienteEditar.fecha_caducidad_bg=fecha_caducidad_bg
    ingredienteEditar.fotografia=fotografia
    ingredienteEditar.save()
    messages.success(request,
      'PROVINCIA ACTUALIZADA EXITOSAMENTE')
    return redirect('/listadoIngredientes/')


def listadoRecetas(request):
    recetasBdd = Receta.objects.all()

    ingredienteBdd = Ingrediente.objects.all()
    platilloBdd = Platillo.objects.all()

    return render(request, 'listadoRecetas.html', {'recetas': recetasBdd, 'ingredientes': ingredienteBdd,'platillos': platilloBdd})

def eliminarReceta(request,id_bg):
    recetaEliminar=Receta.objects.get(id_bg=id_bg)
    recetaEliminar.delete()
    messages.success(request, 'RECETA ELIMINADA EXITOSAMENTE')
    return redirect('/listadoRecetas/')


def guardarReceta(request):
    id_platillo=request.POST["id_platillo"]
    id_ingrediente=request.POST["id_ingrediente"]
    #capturando el tipo seleccionado por el usuario
    platilloSeleccionado=Platillo.objects.get(id_bg=id_platillo)
    ingredienteSeleccionado=Ingrediente.objects.get(id_bg=id_ingrediente)

    cantidad_bg=request.POST["cantidad_bg"]
    procedimiento_bg=request.POST["procedimiento_bg"]
    #Insertando datos mediante el ORM de django

    receta =Receta.objects.create(cantidad_bg=cantidad_bg,procedimiento_bg=procedimiento_bg,platillo_bg=platilloSeleccionado,ingrediente_bg=ingredienteSeleccionado)
    messages.success(request, 'RECETA DEL PLATILLO GUARDADO EXITOSAMENTE')
    return redirect('/listadoRecetas/')

def editarReceta(request, id_bg):
    recetaEditar=Receta.objects.get(id_bg=id_bg)
    recetasBdd=Receta.objects.all()
    platilloBdd=Platillo.objects.all()
    ingredienteBdd=Ingrediente.objects.all()
    return  render(request, 'editarReceta.html',{'receta':recetaEditar,'recetas':recetasBdd, 'platillos':platilloBdd, 'ingredientes':ingredienteBdd})

def procesarActualizacionReceta(request):
    id_bg = request.POST["id_bg"]
    id_platillo = request.POST["id_platillo"]
    platilloSeleccionado = Platillo.objects.get(id_bg=id_platillo)
    id_ingrediente = request.POST["id_ingrediente"]
    ingredienteSeleccionado = Ingrediente.objects.get(id_bg=id_ingrediente)


    cantidad_bg = request.POST["cantidad_bg"]
    procedimiento_bg = request.POST["procedimiento_bg"]


    # Insertando datos mediante el ORM de DJANGO
    recetaEditar = Receta.objects.get(id_bg=id_bg)
    recetaEditar.platillo_bg = platilloSeleccionado  # Corregido el nombre del campo
    recetaEditar.ingrediente_bg = ingredienteSeleccionado  # Corregido el nombre del campo
    recetaEditar.cantidad_bg = cantidad_bg
    recetaEditar.procedimiento_bg = procedimiento_bg  # Corregido el nombre del campo
    recetaEditar.save()

    messages.success(request, 'RECETA  ACTUALIZADA CORRECTAMENTE')
    return redirect('/listadoRecetas/')
