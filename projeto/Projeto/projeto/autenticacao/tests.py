from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group

class AuthTests(TestCase):
    def setUp(self):
        # Configuração inicial antes dos testes: criação de um cliente, utilizador e grupo
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.group = Group.objects.create(name='Clientes')
        self.user.groups.add(self.group)  # Adiciona o utilizador ao grupo 'Clientes'
        self.user.save()

    def test_register_view(self):
        # Testa o carregamento da página de registro
        response = self.client.get(reverse('registo'))
        self.assertEqual(response.status_code, 200)  # Verifica se a página carrega corretamente
        self.assertTemplateUsed(response, 'registo.html')  # Garante que a template correto é usado

        # Testa o envio do formulário de registro
        response = self.client.post(reverse('registo'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)  # Confirma sucesso do registro

    def test_login_view(self):
        # Testa o login com credenciais válidas
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Espera redirecionamento após login
        self.assertRedirects(response, '/')  # Verifica o redirecionamento esperado

    def test_logout_view(self):
        # Testa o logout de um utilizador autenticado
        self.client.login(username='testuser', password='12345')  # Faz login do utilizador
        response = self.client.post(reverse('logout'))  # Envia requisição de logout
        self.assertEqual(response.status_code, 302)  # Confirma redirecionamento após logout

    def test_pagina_protegida_view(self):
        # Testa o acesso a uma página protegida após login
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('pagina_protegida'))
        self.assertEqual(response.status_code, 200)  # Verifica se a página carrega corretamente
        self.assertTemplateUsed(response, 'pagina_protegida.html')  # Garante que a template correto é usado

    def test_perfil_view(self):
        # Testa o acesso à página de perfil do utilizador
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('perfil'))
        self.assertEqual(response.status_code, 200)  # Verifica se a página carrega corretamente
        self.assertTemplateUsed(response, 'perfil.html')  # Garante que a template correto é usado

    def test_redefinir_senha_view(self):
        # Testa a funcionalidade de redefinição de senha
        self.client.login(username='testuser', password='12345')  # Faz login do utilizador
        response = self.client.post(reverse('redefinir_senha'), {
            'username': 'testuser',
            'nova_senha': 'newpassword123',
            'confirmar_senha': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Espera redirecionamento após redefinir a senha
        self.user.refresh_from_db()  # Atualiza os dados do utilizador
        self.assertTrue(self.user.check_password('newpassword123'))  # Verifica se a senha foi alterada

    def test_senha_redefinida_sucesso_view(self):
        # Testa a página de confirmação de senha redefinida
        response = self.client.get(reverse('senha_redefinida_sucesso'))
        self.assertEqual(response.status_code, 200)  # Verifica se a página carrega corretamente
        self.assertTemplateUsed(response, 'registration/senha_redefinida_sucesso.html')  # Confirma a template
