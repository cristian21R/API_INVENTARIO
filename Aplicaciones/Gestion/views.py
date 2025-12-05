from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Categoria, Producto


@csrf_exempt
def categoriaEndpoint(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            nombre = data.get("nombre")
            descripcion = data.get("descripcion", "")
            marca = data.get("marca", "")
            color = data.get("color", "")
            modelo = data.get("modelo", "")

            if not nombre:
                return JsonResponse({"error": "Nombre es obligatorio"}, status=400)

            categoria = Categoria.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                marca=marca,
                color=color,
                modelo=modelo
            )
            return JsonResponse({"mensaje": "Categoría creada", "id": categoria.id}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "GET":
        categorias = Categoria.objects.all().values()
        return JsonResponse(list(categorias), safe=False)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body.decode("utf-8"))
            categoria_id = data.get("id")
            if not categoria_id:
                return JsonResponse({"error": "ID requerido"}, status=400)

            try:
                categoria = Categoria.objects.get(id=categoria_id)
            except Categoria.DoesNotExist:
                return JsonResponse({"error": "Categoría no encontrada"}, status=404)

            categoria.nombre = data.get("nombre", categoria.nombre)
            categoria.descripcion = data.get("descripcion", categoria.descripcion)
            categoria.marca = data.get("marca", categoria.marca)
            categoria.color = data.get("color", categoria.color)
            categoria.modelo = data.get("modelo", categoria.modelo)
            categoria.save()

            return JsonResponse({"mensaje": "Categoría actualizada"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "DELETE":
        try:
            data = json.loads(request.body.decode("utf-8"))
            categoria_id = data.get("id")
            if not categoria_id:
                return JsonResponse({"error": "ID requerido"}, status=400)

            Categoria.objects.filter(id=categoria_id).delete()
            return JsonResponse({"mensaje": "Categoría eliminada"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def productoEndpoint(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            nombre = data.get("nombre")
            descripcion = data.get("descripcion", "")
            precio = data.get("precio")
            categoria_id = data.get("categoria")
            stock = data.get("stock", 0)

            if not nombre or precio is None or categoria_id is None:
                return JsonResponse({"error": "Nombre, precio y categoría son obligatorios"}, status=400)

            try:
                categoria = Categoria.objects.get(id=categoria_id)
            except Categoria.DoesNotExist:
                return JsonResponse({"error": "Categoría no encontrada"}, status=404)

            producto = Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                categoria=categoria,
                stock=stock
            )

            return JsonResponse({"mensaje": "Producto creado", "id": producto.id}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "GET":
        productos = Producto.objects.all().values(
            'id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria_id'
        )
        return JsonResponse(list(productos), safe=False)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body.decode("utf-8"))
            producto_id = data.get("id")
            if not producto_id:
                return JsonResponse({"error": "ID requerido"}, status=400)

            try:
                producto = Producto.objects.get(id=producto_id)
            except Producto.DoesNotExist:
                return JsonResponse({"error": "Producto no encontrado"}, status=404)

            producto.nombre = data.get("nombre", producto.nombre)
            producto.descripcion = data.get("descripcion", producto.descripcion)
            producto.precio = data.get("precio", producto.precio)
            producto.stock = data.get("stock", producto.stock)

            if "categoria" in data:
                try:
                    categoria = Categoria.objects.get(id=data["categoria"])
                    producto.categoria = categoria
                except Categoria.DoesNotExist:
                    return JsonResponse({"error": "Categoría no encontrada"}, status=404)

            producto.save()
            return JsonResponse({"mensaje": "Producto actualizado"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "DELETE":
        try:
            data = json.loads(request.body.decode("utf-8"))
            producto_id = data.get("id")
            if not producto_id:
                return JsonResponse({"error": "ID requerido"}, status=400)

            Producto.objects.filter(id=producto_id).delete()
            return JsonResponse({"mensaje": "Producto eliminado"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)