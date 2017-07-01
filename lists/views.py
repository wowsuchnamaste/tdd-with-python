from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    """Renders the front page.

    """
    return render(request, 'home.html')


def view_list(request):
    """Checks that we can view a list.

    """
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    """Checks that we can create a new list.

    :param request: http request
    :return: http redirects or assertion failure.
    """
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
