import csv
from reportlab.pdfgen import canvas
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from .forms import UploadFileForm, NameForm, AuthorForm
from .somewhere import handle_uploaded_file

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'blog/thanks.html', {'form': form.cleaned_data})
    else:
        form = NameForm()
    return render(request, 'blog/name.html', {'form': form})

def get_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            return render(request, 'blog/thanks.html', {'form': form.cleaned_data})
    else:
        form = AuthorForm()
    return render(request, 'blog/name.html', {'form': form})

def some_view_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second Row', 'A', 'B', 'C', '"Testing"'])
    return response

def test(request):
    response = HttpResponse("Welcome to the blog page!")
    response['Age'] = 120
    return response

def some_view_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    return response


def upload_file(request):
    if request.methos == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'forms': form})


def get_html(request):
    form = {'name': 'LYH', 'sex': 'male', 'age': '26'}
    return render(request, 'blog/extends-base.html', {'forms': form})