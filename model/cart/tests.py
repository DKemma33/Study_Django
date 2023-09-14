from django.test import TestCase

from cart.models import Cart
from member.models import Member


# Create your tests here.
class CartTest(TestCase):
    # print(Cart.objects.values("member__member_name").query)
    # print(Cart.objects.values("product__product_name").query)
    print(Member.objects.values("cart__product_count").query)
