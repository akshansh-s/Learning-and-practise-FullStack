from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product, CartItem
import json

#serializers, decorators (this), generic, viewset
@csrf_exempt
def category_request(request, category_id=None):
    if request.method == 'GET':

        if category_id:
            categories = Category.objects.filter(id=category_id).values()
            if not categories:
                return JsonResponse({'error': 'Category not found'}, status=404)
            return JsonResponse({'categories': list(categories)}, safe=False)
        
        else:
            categories = list(Category.objects.values())
            return JsonResponse(categories, safe=False)

    if request.method == 'POST':

        data = json.loads(request.body)
        category = Category.objects.create(name=data['name'])
        return JsonResponse({'id': category.id, 'name': category.name}, status=201)

    category = Category.objects.filter(id=category_id)
    if not category.exists():
        return JsonResponse({'error': 'Category not found'}, status=404)
    #category = categories.first()

    if request.method == 'PUT':
        # categories = Category.objects.filter(id=category_id)
        # if categories.exists():
        #     category = categories.first()
        # return JsonResponse({'error': 'Category not found'}, status=404)
        data = json.loads(request.body)
        category.name = data.get('name', category.name)
        category.save()
        return JsonResponse({'id': category.id, 'name': category.name})

    if request.method == 'DELETE':
        # categories = Category.objects.filter(id=category_id)
        # if categories.exists():
        #     category = categories.first()
        # return JsonResponse({'error': 'Category not found'}, status=404)
        category.delete()
        return JsonResponse({'message': 'Category deleted'}, status=204)

@csrf_exempt
def product_request(request, product_id=None):
    # products = Product.objects.all()
    # return JsonResponse(list(products.values()), safe=False)
    if request.method == 'GET':
        if product_id:
        #     try:
        #         product = Product.objects.get(id=product_id)
        #     except Product.DoesNotExist:
        #         return JsonResponse({'error': 'Product not found'}, status=404)
        #     return JsonResponse({'id': product.id, 'name': product.name})
            products = Product.objects.filter(id=product_id).values('id', 'name', 'description', 'price', 'stock', 'category_id')
            #use serialzer
            if not products:
                return JsonResponse({'error': 'Product not found'}, status=404)
            return JsonResponse({'product': list(products)[0]})
        else:
            category_id = request.GET.get('category_id')
            products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
            return JsonResponse({'products': list(products.values())}, safe=False)

    data = json.loads(request.body)

    if request.method == 'POST':
        # if data['price'] <= 0 or data['stock'] < 0:
        #     return JsonResponse({'error': 'Invalid price or stock'}, status=400)
        
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock'],
            category_id=data['category_id']
        )
        return JsonResponse({'id': product.id, 'name': product.name}, status=201)

    product = Product.objects.filter(id=product_id).first()
    if not product:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'PUT':
        # Product.objects.filter(id=product_id).update(name=data['name'])
        # product.name = data.get('name', product.name)
        # product.description = data.get('description', product.description)
        # product.price = data.get('price', product.price)
        # product.stock = data.get('stock', product.stock)
        for field, value in data.items():
            setattr(product, field, value)
        product.save()
        return JsonResponse({'id': product.id, 'name': product.name})

    if request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product deleted'}, status=204)


@csrf_exempt
def cart_item_request(request, cart_item_id=None):
    if request.method == 'GET':
        if cart_item_id:
            cart_items = CartItem.objects.filter(id=cart_item_id).values('id', 'product_id', 'quantity')
            if not cart_items:
                return JsonResponse({'error': 'Cart item not found'}, status=404)
            return JsonResponse({'cart_item': list(cart_items)})
        else:
            cart_items = CartItem.objects.all()
            return JsonResponse({'cart_items': list(cart_items.values('id', 'product_id', 'quantity'))}, safe=False)

    #data = json.loads(request.body)

    if request.method == 'POST':
        # cart_item = CartItem.objects.create(
        #     product_id=data['product_id'],
        #     quantity=data['quantity']
        # )
        data = json.loads(request.body)
        product = Product.objects.filter(id=data['product_id']).first()
        if not product:
            return JsonResponse({'error': 'Product not found'}, status=404)
        if product.stock < data['quantity']:
            return JsonResponse({'error': 'Not enough stock available'}, status=400)
        product.stock-=data['quantity']
        product.save()
        cart_item = CartItem.objects.create(product=product, quantity=data['quantity'])
        return JsonResponse({'id': cart_item.id, 'product_id': cart_item.product_id, 'quantity': cart_item.quantity}, status=201)


    if cart_item_id:
        cart_item = CartItem.objects.filter(id=cart_item_id).first()
        if not cart_item:
            return JsonResponse({'error': 'Cart item not found'}, status=404)
        
    if request.method == 'PUT':
        # cart_item.quantity = data.get('quantity', cart_item.quantity)
        # cart_item.save()
        data = json.loads(request.body)
        new_quantity = data['quantity']
        if cart_item.product.stock + cart_item.quantity < new_quantity:
            return JsonResponse({'error': 'Not enough stock available'}, status=400)
            
        cart_item.product.stock += cart_item.quantity - new_quantity
        cart_item.product.save()

        cart_item.quantity = new_quantity
        cart_item.save()
        return JsonResponse({'id': cart_item.id, 'product_id': cart_item.product_id, 'quantity': cart_item.quantity})


    if request.method == 'DELETE':
        cart_item.product.stock += cart_item.quantity
        cart_item.product.save()
        
        cart_item.delete()
        return JsonResponse({'message': 'Cart item deleted'}, status=204)
