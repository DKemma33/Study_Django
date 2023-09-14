from django.test import TestCase

from cart.models import Cart
from member.models import Member
from product.models import Product


# Create your tests here.
class Product(TestCase):

    product = Product.objects.create(product_name='박카스', product_price='3000', product_stock='20')
    member = Member.objects.get(id=10)
    Cart.objects.create(product=product, member=member, product_count=3)
    pass