from django.db import models
import jdatetime  # کتابخانه jdatetime رو ایمپورت کنید

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Interaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.CharField(max_length=20, blank=True, null=True)  # اجازه بدید فیلد خالی باشه

    def save(self, *args, **kwargs):
        # اگر تاریخ وارد نشده، تاریخ فعلی رو به شمسی تبدیل کنید
        if not self.date:
            now = jdatetime.datetime.now()
            self.date = now.strftime('%Y/%m/%d %H:%M:%S')  # فرمت تاریخ شمسی
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Interaction with {self.customer.name} on {self.date}"