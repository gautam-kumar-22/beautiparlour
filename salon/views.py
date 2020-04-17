from django.shortcuts import render
from django.views.generic import View, ListView

from .models import *

# Create your views here.
class HomeListView(ListView):

    model = Slider
    template_name = "index.html"
    context_object_name = 'slider_list'

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['service_list'] = Service.objects.all()[:4]
        context['aboutus'] = AboutUs.objects.all()[0]
        context['company_info'] = CompanyInfo.objects.all()[0]
        context['footer_info'] = Content.objects.filter(name="footer")[0]
        return context


class AboutListView(ListView):

    model = Passion
    template_name = "about.html"
    context_object_name = 'passion_list'

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(AboutListView, self).get_context_data(**kwargs)
        context['aboutus'] = AboutUs.objects.all()[0]
        context['company_info'] = CompanyInfo.objects.all()[0]
        context['footer_info'] = Content.objects.filter(name="footer")[0]
        context['content'] = Content.objects.filter(name="about")[0]
        return context


class ServiceListView(ListView):

    model = Service
    template_name = "service.html"
    context_object_name = 'service_list'

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['company_info'] = CompanyInfo.objects.all()[0]
        context['footer_info'] = Content.objects.filter(name="footer")[0]
        context['content'] = Content.objects.filter(name="service")[0]
        context['male_facilities_list'] = Facilities.objects.filter(gender="M")
        context['female_facilities_list'] = Facilities.objects.filter(gender="F")
        return context


class GalleryListView(ListView):

    model = Gallery
    template_name = "gallery.html"
    context_object_name = 'gallery_list'

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(GalleryListView, self).get_context_data(**kwargs)
        context['company_info'] = CompanyInfo.objects.all()[0]
        context['footer_info'] = Content.objects.filter(name="footer")[0]
        context['category_list'] = Category.objects.all()
        return context
