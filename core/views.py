from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def index(request):
    return render(request, 'core/index.html')


def contact_us(request):
    context={}
    if request.method == 'POST':
        name=request.POST.get("name")
        em=request.POST.get("email")
        sub=request.POST.get("subject")
        msz=request.POST.get("message")

        obj=Contact(name=name,email=em,subject=sub,message=msz)
        obj.save()
        context['message']=f"Dear {name},Thnks for your time!"
        # return HttpResponse("dear {} Thanks for regisetring")

    return render(request,'contact.html',context)
