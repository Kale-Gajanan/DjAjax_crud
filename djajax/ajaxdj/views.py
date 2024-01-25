# views.py
import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Item
from .forms import ItemForm, BookForm


def item_list(request):
    items = Item.objects.all()
    #return redirect('item_list_json')
    print("i",items)
    return render(request,'item_list.html',)

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
def item_list_json(request):
    if request.method == 'GET':
        items = Item.objects.all()
        print("ij",items)
        data = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]
        # Convert to JSON and handle non-serializable values
        response_data={'data': data}
        json_data = json.dumps(response_data, default=str)

        return JsonResponse(json.loads(json_data), safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description})
        else:
            return JsonResponse({'error': 'Invalid form data'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description})
        else:
            return JsonResponse({'error': 'Invalid form data'})
    else:
        form = ItemForm(instance=item)
        return render(request, 'edit_item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})

from django.http import JsonResponse

def get_data(request):
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)


from django.shortcuts import render, redirect
from ajaxdj.forms import EmployeeForm
from ajaxdj.models import Employee


# Create your views here.
def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

"""
def index(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})

"""
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Book


@require_GET
def index(request):
    # DataTables parameters
    print("index")
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 100))
    order_column_index = int(request.GET.get('order[0][column]', 0))
    order_direction = request.GET.get('order[0][dir]', 'asc')
    search_value = request.GET.get('search[value]', '')

    # Actual total number of records (replace with your total count logic)
    total_records = Employee.objects.all().count()

    # Define the sort column based on DataTables parameters
    order_columns = [field.name for field in Employee._meta.fields]
    sort_column = order_columns[order_column_index]

    # Define the sort direction
    sort_direction = '' if order_direction == 'asc' else '-'

    # Fetch data from the Book model with sorting, searching, and pagination
    query_params = {}

    # Apply specific search conditions for the "title" field
    if search_value:
        query_params['name__icontains'] = search_value

    books = Employee.objects.filter(**query_params).order_by(f"{sort_direction}{sort_column}").values()[
            start:start + length]

    # Convert QuerySet to list for proper JSON serialization
    books_list = list(books)

    # Prepare the response data in the DataTables format
    response_data = {
        'draw': draw,
        'recordsTotal': total_records,
        'recordsFiltered': total_records,  # Replace with the actual filtered count
        'data': books_list,
    }

    return JsonResponse(response_data, safe=False)

"""
def index(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            print("ajax req")
            # If it's an AJAX request, return JSON response
            employee_list = []
            for employee in employees:
                employee_data = {
                    'id': employee.id,
                    'name': employee.name,
                    'email': employee.email,
                    'contact': employee.contact,
                    # Add other fields as needed
                }
                employee_list.append(employee_data)

            return JsonResponse({'employees': employee_list}, safe=False)
        else:
            # If it's a regular GET request, render the HTML template
            return render(request, "show.html", {'employees': employees})
    else:
        # Handle other HTTP methods if needed
        return HttpResponseNotAllowed(['GET'])

"""
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")

# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Book

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Book


@require_GET
def get_books(request):
    # DataTables parameters
    print("dddd")
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 100))
    order_column_index = int(request.GET.get('order[0][column]', 0))
    order_direction = request.GET.get('order[0][dir]', 'asc')
    search_value = request.GET.get('search[value]', '')

    # Actual total number of records (replace with your total count logic)
    total_records = Book.objects.all().count()

    # Define the sort column based on DataTables parameters
    order_columns = [field.name for field in Book._meta.fields]
    sort_column = order_columns[order_column_index]

    # Define the sort direction
    sort_direction = '' if order_direction == 'asc' else '-'

    # Fetch data from the Book model with sorting, searching, and pagination
    query_params = {}

    # Apply specific search conditions for the "title" field
    if search_value:
        query_params['title__icontains'] = search_value

    books = Book.objects.filter(**query_params).order_by(f"{sort_direction}{sort_column}").values()[
            start:start + length]

    # Convert QuerySet to list for proper JSON serialization
    books_list = list(books)

    # Prepare the response data in the DataTables format
    response_data = {
        'draw': draw,
        'recordsTotal': total_records,
        'recordsFiltered': total_records,  # Replace with the actual filtered count
        'data': books_list,
    }

    return JsonResponse(response_data, safe=False)

def show(request):
    return render(request,'show.html')
def show1(request):
    return render(request,'show1.html')
def books(request):
    return render(request,'books.html')


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def book_delete(request, pk):
    print("delete")
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books')