from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		# obj = RestaurantLocation.objects.create(
		# 	name = form.cleaned_data.get('name'),
		# 	location = form.cleaned_data.get('location'),
		# 	category = form.cleaned_data.get('category'))

		return HttpResponseRedirect("/restaurants/")

		if form.errors:
			errors = form.errors
		
	template_name = 'restaurants/form.html'
	context = { "form": form, "errors": errors }

	return render(request, template_name, context)



def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list": queryset,
	}
	return render(request, template_name, context)


class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) | 
				Q(category__icontains=slug)
				)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset



class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all() #filter(category__iexact='kuhinja')


		
		