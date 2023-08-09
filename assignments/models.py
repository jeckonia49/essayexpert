from django.db import models
from django.utils import timezone
import datetime
from accounts.models import Profile
from django.utils.text import slugify
import random
import string
from django.urls import reverse
from .utils import (
    Discipline,
    SubDiscipline,
    PaperType,
    PowerPoint,
    PAPER_TYPE_CHOICES,
    DISCIPLINE_CHOICES,
    POWERPOINT_CHOICES,
)






class Order(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_client")
    topic = models.CharField(max_length=100, help_text="Tell us your topic")
    slug = models.SlugField(max_length=100)
    type_of_paper = models.CharField(choices=PAPER_TYPE_CHOICES, max_length=100, default="Type of paper")
    discipline = models.CharField(max_length=100, choices=DISCIPLINE_CHOICES, default="discipline")
    pages = models.PositiveBigIntegerField(default=1)
    words = models.PositiveBigIntegerField(default=275)
    academic_level = models.CharField(choices=(
        ("DA", "Dont Apply"),
        ("HS", "High School"),
        ("CG", "College"),
        ("UG", "Undergraduate"),
        ("MS/PDH", "Masters/Phd"),
    ), default="UG", max_length=10)
    deadline_date = models.DateField(default=timezone.now)
    deadline_time = models.TimeField(default=timezone.now, help_text="H:M")
    paper_instruction = models.TextField(blank=True, null=True)
    files = models.FileField(upload_to="orders/", blank=True, null=True)
    paper_format = models.CharField(max_length=100, choices=(
        ("APA", (("APA6", "APA 6"), ("APA7", "APA 7"), ("APA9", "APA 9"),)),
        ("MLA", "MLA"),
        ("CHICAGO", "Chicago/Turabian"),
        ("NA", "Not Applicable"),
        ("HARVARD", "Harvard"),
        ("OTHER", "OTHER"),
    ), default="APA")
    type_of_service = models.CharField(max_length=10, choices=(
        ("SW", "Sample Writing"),
        ("ER", "Editting Rewriting"),
        ("CALC", "Calculations"),
        ("IT", "Programming")
    ), default="SW")
    reference_copies = models.BooleanField(default=False)
    sms_update = models.BooleanField(default=False)
    turnitin_report = models.BooleanField(default=False)
    writer_choice = models.CharField(max_length=2, choices=(
        ("RW", "Regular Writer"),
        ("FW", "First Writer"),
        ("PW", "Professional Writer")
    ), default="RW")
    ppt = models.IntegerField(default=0)
    software_tools = models.BooleanField(default=False)
    software_tool_description = models.TextField(blank=True, null=True)
    weekly = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(blank=True, null=True, max_length=12)
    is_daily = models.BooleanField(default=True)
    price = models.FloatField(default=1.34)
    
    class Meta:
        get_latest_by = "createdAt"
    
    def __str__(self):
        return self.topic

    @property
    def order_id_code(self):
        res = random.choices([string.ascii_lowercase + string.digits], k=10)
        result = random.choice(res)
        random.shuffle(list(result))
        result = "".join(random.choices(result, k=10))
        return result
    
    # @property
    # def expected_delivery(self):
    
    
    def get_absolute_url(self):
        return reverse("payments:payments_order_detail", kwargs={
            "pk":self.pk,
            "slug":self.slug,
        })
    
    
    

    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        self.order_id = self.order_id_code
        self.slug=self.topic
        return super(Order, self).save(*args, **kwargs)


class WeeklyAssigment(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    school_id = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    moodle_account_link =models.URLField(max_length=255)
    number_of_subjects = models.PositiveIntegerField(default=1)
    login_details_username = models.CharField(max_length=300, help_text="username for the moodle account")
    login_details_password = models.CharField(max_length=300, help_text="password for the moodle account")
    subjects_details = models.TextField(help_text="Subject details eg, subject title and code")
    duration = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    
    def __str__(self):
        
        return self.full_name
    


    
