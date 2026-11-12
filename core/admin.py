from django.contrib import admin

from .models import Aluguel, Categoria, Cliente, Veiculo


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "diaria")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "telefone", "criado_em")
    search_fields = ("nome", "cpf")


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("nome", "marca", "placa", "chassi", "categoria", "diaria", "ativo")
    search_fields = ("nome", "placa", "chassi")
    list_filter = ("categoria", "ativo")


@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "veiculo", "categoria", "diarias", "horas_atraso")
    list_filter = ("categoria",)
