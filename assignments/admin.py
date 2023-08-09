from django.contrib import admin
from .models import (
Discipline,
SubDiscipline,
PaperType,
PowerPoint,
Order,


WeeklyAssigment,
)


class SubDisciplineInlineAdmin(admin.StackedInline):
    model = SubDiscipline
    extra=0

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        SubDisciplineInlineAdmin,
    ]


@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(PowerPoint)
class PowerPointAdmin(admin.ModelAdmin):
    list_display = ['count', 'get_amount', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["client", "topic","type_of_paper",'order_id_code',"deadline_date","deadline_time", 'price', "pages","words","academic_level","paper_format","type_of_service","reference_copies","sms_update","turnitin_report","writer_choice","ppt","software_tools",]
    search_fields = ['topic', 'type_of_paper', 'discipline', "client"]
    list_filter = [
        "client",
        'discipline',
        'academic_level',
        'paper_format',
        'writer_choice',
        "deadline_date",
        "weekly"
    ]
    list_per_page = 10
    prepopulated_fields = {"slug":("topic",)}


@admin.register(WeeklyAssigment)
class AdminWeeklyAssigment(admin.ModelAdmin):
    list_display = [
        "client", "full_name","school_id","school_name","moodle_account_link",
        "number_of_subjects","login_details_username","login_details_password", "subjects_details","duration",
        ]
    
    


