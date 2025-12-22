from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView,CreateView
from .models import Item, MEAL_TYPE
from django.urls import reverse_lazy
from .models import Order, Item
from .forms import OrderForm


class MenuList(generic.ListView):
    queryset = Item.objects.order_by('-date_created')
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"


class AboutView(TemplateView):
    template_name = "about.html"


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order.html"

    def form_valid(self, form):
        item = Item.objects.get(pk=self.kwargs['pk'])
        form.instance.item = item
        response = super().form_valid(form)

        # set popup flag
        self.request.session['order_success'] = True
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # read + remove popup flag
        context['order_success'] = self.request.session.pop(
            'order_success', False
        )
        return context

    def get_success_url(self):
        # reload same page so popup can appear
        return self.request.path