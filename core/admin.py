from django.contrib import admin
from django.contrib.auth.models import User, Group
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import Site, SocialAccount
from .models import Item, OrderItem, Order, UserProfile


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered'
                    ]
    list_display_links = [
        'user',
    ]

    search_fields = [
        'user__username',
        'ref_code'
    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)
admin.site.unregister(Site)
admin.site.unregister(SocialAccount)
