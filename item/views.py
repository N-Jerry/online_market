from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

from .models import Item, Category
from .forms import NewItemForm, EditItemForm

# Create your views here.
def browse(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold = False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        #Q is to be able to search in multiple feilds
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/browse.html', {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id': int(category_id)})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {'item':item, 'related_items':related_items})

class edit(UpdateView):
    model = Item
    fields = ['name', 'description', 'price']


# @login_required
# def edit(request, pk):
#     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#     item = get_object_or_404(Item, pk=pk, created_by=request.user)
#     print(item)
#     if request.method == 'POST':
#         #To edit the image, add request.FILES as attribute
#         form = EditItemForm(request.POST, instance=item)
        
#         if form.is_valid():
#             form.save()
#             return redirect('item:detail', pk=item.id)
#     else:
#         #When we get here, we the form will be empty so to avoid that
#         #we add the instance attribute to the current item

#         form = EditItemForm(instance=item)
#         print("hry thr")
#     return render(request, 'item/form.html', { 'form': form, 'title': 'Edit Item'})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'item/form.html', { 'form': form, 'title': 'New Item'})

@login_required
def delete(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')