from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'price', 'quantity']
    ordering = ['-price', 'name']
    list_filter = ['date_product', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию продукта'
    actions = [reset_quantity]

    """Отдельный продукт."""
    readonly_fields = ['date_product']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Дата создания',
                'fields': ['date_product']
            }
        ),
    ]



class ClientAdmin(admin.ModelAdmin):
    """Список клиентов."""
    list_display = ['name', 'email', 'phone', 'address']
    ordering = ['name', 'address']
    list_filter = ['date_reg']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'

    """Отдельный клиент."""
    readonly_fields = ['date_reg']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контактная информация',
            {
                'fields': ['email', 'phone', 'address'],
            },
        ),
        (
            'Прочее',
            {
                'classes': ['collapse'],
                'description': 'Дата регистрации',
                'fields': ['date_reg']
            }
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
