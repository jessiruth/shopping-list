from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Jessica Ruth Damai Yanti Manurung',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
