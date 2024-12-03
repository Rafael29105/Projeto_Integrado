from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MenuItem

class MenuItemModelTest(TestCase):
    
    # Configura o ambiente de teste criando um item de menu antes de cada teste.
    def setUp(self):
        self.item = MenuItem.objects.create(
            name="Bacalhau à Brás",
            description="Prato tradicional português.",
            price=12.50,
            is_available=True,
        )

    # Testa se os campos do modelo MenuItem estão sendo armazenados corretamente.
    def test_model_fields(self):
        self.assertEqual(self.item.name, "Bacalhau à Brás")
        self.assertEqual(self.item.description, "Prato tradicional português.")
        self.assertEqual(self.item.price, 12.50)
        self.assertTrue(self.item.is_available)

    # Testa a validação do preço para garantir que valores negativos sejam rejeitados.
    def test_price_validation(self):
        item = MenuItem(name="Item Negativo", description="Preço negativo", price=-5.00, is_available=True)
        with self.assertRaises(Exception):
            item.full_clean()

# Testes para as views relacionadas ao MenuItem
class MenuItemViewTest(TestCase):
    
    # Configura o ambiente de teste criando um utilizador e um item de menu antes de cada teste.
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')  
        self.item = MenuItem.objects.create(
            name="Bacalhau à Brás",
            description="Prato tradicional português.",
            price=12.50,
            is_available=True,
        )

    # Testa a visualização da lista de itens do menu para utilizadores autenticados.
    def test_menu_list_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 403)

    # Testa a visualização da lista de itens do menu para utilizadores sem permissões.
    def test_menu_list_view_no_permission(self):
        user_without_permission = User.objects.create_user(username='user_no_permission', password='password')
        self.client.login(username='user_no_permission', password='password')
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 403)

    # Testa a visualização de criação de um item do menu para utilizadores autenticados.
    def test_menu_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('menu_create'))
        self.assertEqual(response.status_code, 302)

    # Testa a visualização de criação de um item do menu para utilizadores sem permissões.
    def test_menu_create_view_permission_denied(self):
        user_no_permission = User.objects.create_user(username='no_permission_user', password='password')
        self.client.login(username='no_permission_user', password='password')
        response = self.client.get(reverse('menu_create'))
        self.assertEqual(response.status_code, 302)

    # Testa a visualização de edição de um item do menu.
    def test_menu_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('menu_update', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)

    # Testa a visualização de edição de um item do menu para utilizadores sem permissões.
    def test_menu_update_view_permission_denied(self):
        user_no_permission = User.objects.create_user(username='no_permission_user', password='password')
        self.client.login(username='no_permission_user', password='password')
        response = self.client.get(reverse('menu_update', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)

    # Testa a visualização de exclusão de um item do menu.
    def test_menu_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('menu_delete', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)

    # Testa a visualização de exclusão de um item do menu para utilizadores sem permissões.
    def test_menu_delete_view_permission_denied(self):
        user_no_permission = User.objects.create_user(username='no_permission_user', password='password')
        self.client.login(username='no_permission_user', password='password')
        response = self.client.get(reverse('menu_delete', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)
