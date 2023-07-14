from django.shortcuts import render
from .forms import RestaurantFilterForm
from .models import Restaurant


def filter_restaurants(request):
    if request.method == 'POST':
        form = RestaurantFilterForm(request.POST)
        if form.is_valid():
            selected_prices = form.cleaned_data.get('price_range')
            # Perform the filtering based on selected_prices
            if 'cheap' in selected_prices:
                restaurants = Restaurant.objects.filter(price__lt=10.00)
            elif 'moderate' in selected_prices:
                restaurants = Restaurant.objects.filter(price__range=[10.00, 30.00])
            elif 'expensive' in selected_prices:
                restaurants = Restaurant.objects.filter(price__gt=30.00)
            else:
                restaurants = Restaurant.objects.all()
    else:
        form = RestaurantFilterForm()
        restaurants = Restaurant.objects.all()

    context = {
        'form': form,
        'restaurants': restaurants
    }
    return render(request, 'filter.html', context)
