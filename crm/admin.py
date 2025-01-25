from django.contrib import admin
from .models import Customer, Interaction
import jdatetime  # کتابخانه jdatetime رو ایمپورت کنید
from django.utils import timezone

class CustomerAdmin(admin.ModelAdmin):
    # فیلدهایی که می‌خواید قابل جست‌وجو باشن
    search_fields = ['name', 'email', 'phone']

    # فیلترها
    list_filter = ['created_at']

    # فیلدهایی که می‌خواید در لیست نمایش داده بشن
    list_display = ['name', 'email', 'phone', 'jalali_created_at', 'interaction_count']  # نمایش تاریخ شمسی

    # (اختیاری) تعداد آیتم‌های نمایش‌داده‌شده در هر صفحه
    list_per_page = 20

    # Actions (عملیات گروهی)
    actions = ['send_email']

    def send_email(self, request, queryset):
        # ارسال ایمیل به مشتریان انتخاب‌شده
        for customer in queryset:
            # کد ارسال ایمیل (مثال ساده)
            print(f"Email sent to {customer.email}")
        self.message_user(request, f"Emails sent to {queryset.count()} customers.")
    send_email.short_description = "Send email to selected customers"

    # فیلد محاسباتی: تعداد تعاملات هر مشتری
    def interaction_count(self, obj):
        return obj.interaction_set.count()
    interaction_count.short_description = "Interaction Count"

    # فیلد محاسباتی: نمایش تاریخ ایجاد به صورت شمسی
    def jalali_created_at(self, obj):
        # تبدیل زمان UTC به منطقه زمانی Tehran
        local_time = timezone.localtime(obj.created_at, timezone=timezone.get_current_timezone())
        jalali_date = jdatetime.datetime.fromgregorian(datetime=local_time)
        return jalali_date.strftime('%Y/%m/%d %H:%M:%S')
    jalali_created_at.short_description = 'تاریخ ایجاد'
    # تاریخ‌چه سلسله‌مراتبی
    date_hierarchy = 'created_at'

    # ویرایش سریع
    list_editable = ['email', 'phone']

class InteractionAdmin(admin.ModelAdmin):
    # فیلدهایی که می‌خواید قابل جست‌وجو باشن
    search_fields = ['customer__name', 'description']

    # فیلترها
    list_filter = ['date']

    # فیلدهایی که می‌خواید در لیست نمایش داده بشن
    list_display = ['customer', 'short_description', 'date']

    # (اختیاری) تعداد آیتم‌های نمایش‌داده‌شده در هر صفحه
    list_per_page = 20

    # پیش‌نمایش توضیحات
    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    short_description.short_description = "Description Preview"

# ثبت مدل‌ها با کلاس‌های Admin سفارشی
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Interaction, InteractionAdmin)