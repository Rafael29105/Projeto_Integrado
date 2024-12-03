from django.test import TestCase
from django.urls import reverse  
from django.contrib.auth.models import User  
from .models import Order, MenuItem  
from django.core.exceptions import ValidationError

class OrderModelTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(name="Pizza", price=20.0)

    def test_total_price_calculation(self):
        # Testa o cálculo correto do preço total de um pedido.
        order = Order.objects.create(
            customer_name="João Silva",
            menu_item=self.menu_item,
            quantity=2,
            status="Pendente"  
        )
        self.assertEqual(order.total_price, 40.0)

    def test_invalid_order_fields(self):
        order = Order(customer_name="", menu_item=self.menu_item, quantity=0, status="Pendente")
        with self.assertRaises(ValidationError):
            order.full_clean()

# Testes para as views de pedido 
class OrderViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.menu_item = MenuItem.objects.create(name="Pizza", price=20.0)
        cls.order = Order.objects.create(
            customer_name="João Silva",
            menu_item=cls.menu_item, 
            quantity=2, 
            status="Pendente"
        )

    def test_order_list_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "João Silva")

    def test_order_list_unauthenticated_redirect(self):
        response = self.client.get(reverse('order_list'))
        self.assertRedirects(response, '/accounts/login/?next=/orders/orders/')

# Testes para a view de criação de pedido
class OrderCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_order_authenticated(self):
        # Testa se um utilizador autenticado consegue criar um pedido com sucesso.
        self.client.login(username='testuser', password='12345')
        menu_item = MenuItem.objects.create(name="Pizza", price=20.0)
        response = self.client.post(reverse('order_create'), {
            'customer_name': 'Maria Oliveira',
            'menu_item': menu_item.id,
            'quantity': 3,
            'status': 'Pendente',
        })
        self.assertEqual(response.status_code, 302)

# Testes para a view de atualização de pedido
class OrderUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.menu_item = MenuItem.objects.create(name="Pizza", price=20.0)
        cls.order = Order.objects.create(
            customer_name="João Silva",
            menu_item=cls.menu_item,
            quantity=2,
            status="Pendente"
        )

    def test_update_order(self):
        # Testa a atualização de um pedido existente.
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('order_update', args=[self.order.pk]), {
            'customer_name': 'João Silva',
            'menu_item': self.menu_item.id,
            'quantity': 3,
            'status': 'Concluído',
        })
        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.customer_name, 'João Silva')

    def test_update_nonexistent_order(self):
        # Testa a tentativa de atualizar um pedido inexistente 
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('order_update', args=[999]))
        self.assertEqual(response.status_code, 404)

# Testes para a view de exclusão de pedido
class OrderDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.menu_item = MenuItem.objects.create(name="Pizza", price=20.0)
        cls.order = Order.objects.create(
            customer_name="João Silva",
            menu_item=cls.menu_item,
            quantity=2,
            status="Pendente"
        )

    def test_delete_order(self):
        # Testa a exclusão de um pedido existente.
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('order_delete', args=[self.order.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())
