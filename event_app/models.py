from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event_management(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_free = models.BooleanField()

    def __str__(self):
        return self.title

class Speaker_management(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    linkedin_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Participant_management(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Schedule_management(models.Model):
    event = models.ForeignKey(Event_management, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    topic = models.CharField(max_length=150)
    speaker = models.ForeignKey(Speaker_management, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.topic

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('PAID', 'Paid'),
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed')
    ]

    participant = models.ForeignKey(Participant_management, on_delete=models.CASCADE)
    event = models.ForeignKey(Event_management, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return self.transaction_id
    
