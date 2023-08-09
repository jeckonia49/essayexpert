from django.shortcuts import render, redirect
from django.urls import is_valid_path
from django.views import generic
from .forms import AssignmentForm, WeeklyForm
from .models import Order
from django.utils import timezone
import datetime
from django.http import JsonResponse

class HomeTemplateView(generic.TemplateView):
    template_name ="index.html"
    

class AssignmentOrderView(generic.TemplateView):
    template_name = "assignments/place_order.html"
    form_class = AssignmentForm
    
    def get_context_data(self, **kwargs):
        context = super(AssignmentOrderView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(initial={"ppt":0})
        return context
    
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
        except:
            user=None

        form = self.form_class(request.POST, request.FILES)
        
        options = request.POST.getlist("checks[]")
        files = request.FILES.getlist("files")
        
        if form.is_valid():
            
            print(form.cleaned_data)
            form.save()
            order = Order.objects.all().last()
            if len(options) > 0:
             
             for _ in options:
                if "reference_copies" in options:
                    order.reference_copies=True
                    order.price += 0.95
                
                if  "sms_update"  in options:
                    order.sms_update=True
                    order.price += 0.95
                    
                if  "turnitin_report"  in options:
                    order.turnitin_report=True
                    order.price += 0.05
                
                if  "software_tools"  in options:
                    order.software_tools=True
                    order.price+=0.95
                
            if user is not None and user.is_authenticated:
                order.client=user.user_profile
            order.price += order.pages*1.34
            order.topic = request.POST.get("topic")
            
            if files:
                for file in files:
                    order.files=file
            order.save()
            print(order)
            return redirect(order)
        context = {
            "form":form
        }
        print(form.errors)
        return render(request, self.template_name, context)
    


class WeeklyAssignemntView(generic.TemplateView):
    template_name = "assignments/weekly_order.html"
    form_class = WeeklyForm
    
    def get_context_data(self, **kwargs):
        context = super(WeeklyAssignemntView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.client = request.user.user_profile
            instance.save()
            instance.price=form.cleaned_data.get("number_of_subjects")*0.3
            form.save()
            return JsonResponse({"message": "Message"})
        self.get_context_data(**kwargs).update({
            "form": form
        })
        return render(request, self.template_name, self.get_context_data(**kwargs))
