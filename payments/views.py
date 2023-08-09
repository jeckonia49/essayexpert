from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from assignments.models import Order
from accounts.models import Profile, AccountUser
from .models import Transaction
from django.http import JsonResponse
from django.contrib.auth import login


class TransactionView(generic.TemplateView):
    template_name = "payments/index.html"
    
    def get_object(self, **kwargs):
        return get_object_or_404(Order, pk=kwargs.get("pk"), slug=kwargs.get("slug"))
    
    def get_context_data(self, **kwargs):
        context = super(TransactionView, self).get_context_data(**kwargs)
        context['order'] = self.get_object(**kwargs)
        # print(context)
        return context
    
    def post(self, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get("pk"), slug=kwargs.get("slug"))
        email=email=self.request.POST.get("email")
        user = AccountUser.objects.filter(email=email).first()
        if user is None:
            return redirect(order)
        
        
        if user and user.is_authenticated:
            # login(self.request, user)
            transaction = Transaction.objects.create(
                client=user.user_profile,
                email_address=email,
                order=order,
                price=order.price,
                completed=True
            )
            transaction.save()
            print(user, "Another save")
        if user and not user.is_authenticated:
            login(self.request, user)
            transaction = Transaction.objects.create(
                client=user.user_profile,
                email_address=email,
                order=order,
                price=order.price,
                completed=True
            )
            transaction.save()
        print(self.request.POST)
        return redirect(order)
        
        


    


    

    

