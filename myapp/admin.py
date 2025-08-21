from django.contrib import admin
from .models import (
    Category, Certificate, die_shop, Offer, OfferImage,
    PortfolioImage, PortfolioPage, TeamMember
)

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioPageAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]

# --- Offer uchun galereya ---
class OfferImageInline(admin.TabularInline):
    model = OfferImage
    extra = 1

class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferImageInline]

admin.site.register(TeamMember)
admin.site.register(PortfolioPage, PortfolioPageAdmin)
admin.site.register(PortfolioImage)
admin.site.register(die_shop)
admin.site.register(Offer, OfferAdmin)  
admin.site.register(Category)
admin.site.register(Certificate)
