from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, template_name="common/index.html", context=context)