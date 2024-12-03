from django.apps import AppConfig

# Definindo a configuração da aplicação 'orders'
class OrdersConfig(AppConfig):
    # Configuração padrão para o tipo de campo auto-incremental
    default_auto_field = 'django.db.models.BigAutoField'
    # Nome da aplicação
    name = 'orders'
