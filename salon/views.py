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
        if Service.objects.all():
            context['service_list'] = Service.objects.all()[:4]
        if AboutUs.objects.all():
            context['aboutus'] = AboutUs.objects.all()[0]
        if CompanyInfo.objects.all():
            context['company_info'] = CompanyInfo.objects.all()[0]
        if Content.objects.filter(name="footer"):
            context['footer_info'] = Content.objects.filter(name="footer")[0]
        return context


class AboutListView(ListView):

    model = Passion
    template_name = "about.html"
    context_object_name = 'passion_list'

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(AboutListView, self).get_context_data(**kwargs)
        if AboutUs.objects.all():
            context['aboutus'] = AboutUs.objects.all()[0]
        if CompanyInfo.objects.all():
            context['company_info'] = CompanyInfo.objects.all()[0]
        if Content.objects.filter(name="footer"):
            context['footer_info'] = Content.objects.filter(name="footer")[0]
        if Content.objects.filter(name="about"):
            context['content'] = Content.objects.filter(name="about")[0]
        return context


class ServiceListView(ListView):

    model = Service
    template_name = "service.html"
    context_object_name = 'service_list'

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(ServiceListView, self).get_context_data(**kwargs)
        if CompanyInfo.objects.all():
            context['company_info'] = CompanyInfo.objects.all()[0]
        if Content.objects.filter(name="footer"):
            context['footer_info'] = Content.objects.filter(name="footer")[0]
        if Content.objects.filter(name="service"):
            context['content'] = Content.objects.filter(name="service")[0]
        if Facilities.objects.filter(gender="M"):
            context['male_facilities_list'] = Facilities.objects.filter(gender="M")
        if Facilities.objects.filter(gender="F"):
            context['female_facilities_list'] = Facilities.objects.filter(gender="F")
        return context


class GalleryListView(ListView):

    model = Gallery
    template_name = "gallery.html"
    context_object_name = 'gallery_list'

    def get_context_data(self, **kwargs):
        """Add section data in context."""
        context = super(GalleryListView, self).get_context_data(**kwargs)
        if CompanyInfo.objects.all():
            context['company_info'] = CompanyInfo.objects.all()[0]
        if Content.objects.filter(name="footer"):
            context['footer_info'] = Content.objects.filter(name="footer")[0]
        context['category_list'] = Category.objects.all()
        return context
