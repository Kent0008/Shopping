from django.contrib import admin
from .models import Products, Brand, Comment, Cart, Order
from django.utils.safestring import mark_safe

from modeltranslation.admin import TranslationAdmin

# Register your models here.

class ProductsAdmin(TranslationAdmin):
  
  list_display = ['name', 'brand', 'price', 'size', 'quant']
  list_filter = ["gender", "brand", "size", ]
  search_fields = ('name',)
  readonly_fields = ('get_image', )

  def get_image(self, obj):
    
    return mark_safe(f'<img src={obj.image.url} width="40" height="40" >')
  
  fieldsets = (

        ('Главное', {"fields" : (
                    ("name",),
                    ("descriptions",),
                    ("price",),
                    ("size",),
                    ("gender",),
                    ("quant",),
        )}),

        ("Бренд", {
            "classes" : ("callapse"),
            "fields" : (
                ( "brand",),
                ( "image", "get_image", ),

            )
        }

        )




    )
  




admin.site.register(Products, ProductsAdmin)

class BrandAdmin(admin.ModelAdmin):
  list_filter = ("name", )
  search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)

class CommentAdmin(admin.ModelAdmin):
  list_filter = ("username", "comment" )
  search_fields = ('username',)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Cart)
  
admin.site.register(Order)