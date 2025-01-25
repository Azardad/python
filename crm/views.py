from django.shortcuts import render, get_object_or_404
from django.urls import reverse  # این خط رو اضافه کنید
from .models import Customer, Interaction  # مدل‌های Customer و Interaction رو ایمپورت کنید

def customer_list(request):
    customers = Customer.objects.all()  # همه‌ی مشتریان رو از دیتابیس بگیرید
    return render(request, 'crm/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)  # مشتری رو بر اساس ID بگیرید
    interactions = Interaction.objects.filter(customer=customer)  # تعاملات مربوط به مشتری رو بگیرید
    return render(request, 'crm/customer_detail.html', {'customer': customer, 'interactions': interactions})

def home(request):
    # لینک‌های مورد نیاز
    admin_url = reverse('admin:index')  # لینک به صفحه ادمین
    customer_list_url = reverse('customer_list')  # لینک به لیست مشتری‌ها

    context = {
        'admin_url': admin_url,
        'customer_list_url': customer_list_url,
    }
    return render(request, 'crm/home.html', context)