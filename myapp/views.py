import django.db
from django.shortcuts import render, get_object_or_404
from .models import (BlogPost, Category, Certificate, die_shop, Offer, PortfolioPage, ServicePage,
    TeamMember)
import random


def home(request):
    person1 = TeamMember.objects.filter(
        name__iexact='Srajidinov Alisher Taxirovich',
        role__iexact='Deputy Chairman of the Management Board Chief Operating Officer'
    ).first()

    person2 = TeamMember.objects.filter(
        name__iexact='Hosilov Shaxrizod',
        role__iexact='Director of AKFA EXTRUSIONS LLC'
    ).first()

    person3 = TeamMember.objects.filter(
        name__iexact='Jalolov Mehriddin',
        role__iexact='Deputy Director for the Production of Aluminum Profiles'
    ).first()

    person4 = TeamMember.objects.filter(
        name__iexact='Alisher Kaharov',
        role__iexact='Chief Manager for Administrative Issues of Aluminum Profiles Production'
    ).first()

    team_members = TeamMember.objects.all()
    services = ServicePage.objects.prefetch_related("accordions").all()

    # 🔥 Yangi qo‘shilgan qism: Random yangiliklar
    posts = list(BlogPost.objects.all())
    random_posts = random.sample(posts, min(len(posts), 3))  # 3 tasini tanlaydi

    context = {
        'person1': person1,
        'person2': person2,
        'person3': person3,
        'person4': person4,
        'team_members': team_members,
        'services': services,
        'random_posts': random_posts,  # yangiliklarni ham contextga qo‘shdik
    }

    return render(request, 'home-1.html', context)

def home2(request):
    return render(request, 'home-2.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog2(request):
    return render(request, 'blog-inner.html')

def not_found(request):
    return render(request, '404.html')

def portfolio1(request):
    portfolio_13 = PortfolioPage.objects.all()
    context = {'portfolio_13' : portfolio_13}
    return render(request, 'portfolio-1.html', context)

def portfolio2(request):
    return render(request, 'portfolio-2.html')

def portfolio3(request):
    return render(request, 'portfolio-3.html')

def project1(request):
    return render(request, 'project-1.html')

def project2(request):
    return render(request, 'project-2.html')

def project3(request):
    return render(request, 'project-3.html')

def project4(request):
    return render(request, 'project-4.html')

def project5(request):
    return render(request, 'project-5.html')

def project6(request):
    return render(request, 'project-6.html')

def publication(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    # Boshqa postlardan random tanlash (shu postni o‘zini chiqarib tashlaymiz)
    other_posts = list(BlogPost.objects.exclude(pk=pk))
    similar_posts = random.sample(other_posts, min(len(other_posts), 2))  # faqat 2 tasini chiqaramiz

    return render(request, 'publication.html', {
        'post': post,
        'similar_posts': similar_posts
    })

def service(request):
    return render(request, 'service.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')

def certificates(request):
    category = Category.objects.filter(blocked=False)
    certificates = Certificate.objects.all()
    context = {
        'category': category,
        'certificates': certificates,
    }
    return render(request, 'certificates.html', context)

def team_view(request):
    team_members = TeamMember.objects.all()  
    context = {'team_members': team_members}  
    return render(request, 'team.html', context)  

def team_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    context = {'member': member}  # Bu yer context
    return render(request, 'home-2.html', context)
    
    
def portfolio_detail(request, id):
    project = get_object_or_404(PortfolioPage, id=id)
    context = {'project': project}
    return render(request, 'project-3.html', context)

def die_shop_list(request):
    products = die_shop.objects.all().order_by('id')
    return render(request, 'portfolio-2.html', {'products': products})

def die_shop_detail(request, id):
    dieshop = get_object_or_404(die_shop, id=id)

    # Prev / Next (id bo‘yicha)
    prev_shop = die_shop.objects.filter(id__lt=dieshop.id).order_by('-id').first()
    next_shop = die_shop.objects.filter(id__gt=dieshop.id).order_by('id').first()

    context = {
        'die_shop': dieshop,
        'prev_shop': prev_shop,
        'next_shop': next_shop,
    }
    return render(request, 'project-1.html', context)


def offer_list(request):
    offers = Offer.objects.all()
    context = {'offers': offers}
    return render(request, 'portfolio-3.html', context)


def project5(request, id):
    offer = get_object_or_404(Offer, id=id)
    return render(request, 'project-5.html', {'offer': offer})


def service_detail(request, pk):
    service = get_object_or_404(ServicePage, pk=pk)
    accordions = service.accordions.all()
    return render(request, "service.html", {
        "service": service,
        "accordions": accordions
    })
    
def blog_inner(request):
    posts = BlogPost.objects.all().order_by('-date')
    return render(request, 'blog-inner.html', {'posts': posts})