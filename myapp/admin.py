from django.contrib import admin
from .models import (
    Category, Certificate, die_shop, Offer, OfferImage,
    PortfolioImage, PortfolioPage, ServicePage, TeamMember,
    BlogPost, BlogImage   # yangi qo‘shilganlar
)

# --- Portfolio uchun rasm inline ---
class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

@admin.register(PortfolioPage)
class PortfolioPageAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]


# --- Offer uchun galereya ---
class OfferImageInline(admin.TabularInline):
    model = OfferImage
    extra = 1

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferImageInline]


# --- Blog uchun rasm inline ---
class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title",)
    list_filter = ("date",)
    inlines = [BlogImageInline]


# Oddiy ro‘yxatdan o‘tkazilganlar
admin.site.register(TeamMember)
admin.site.register(PortfolioImage)
admin.site.register(die_shop)
admin.site.register(Category)
admin.site.register(Certificate)
admin.site.register(ServicePage)
