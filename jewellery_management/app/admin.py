from django.contrib import admin

from app.models import (
    Store,
    StorePhoneNumber,
    Jewellery,
    Category,
    Supplier,
    SupplierPhoneNumber,
    Customer,
    CustomerPhoneNumber,
    Order,
    Payment,
    StoreSeller,
)

admin.site.register(Store)
admin.site.register(StorePhoneNumber)
admin.site.register(Jewellery)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(SupplierPhoneNumber)
admin.site.register(Customer)
admin.site.register(CustomerPhoneNumber)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(StoreSeller)
