from django.shortcuts import render, redirect, get_object_or_404
from .models import AdharCardDetail
from .forms import AdharDetailForm, AdharDetailFirstForm
from googletrans import Translator

# Create your views here.


def index(request):
    
    data = '''Rajendra Kumar, chitarwai kala, khutar, singrauli, madhya pradesh
    contact: 9009112115
    '''
    return render(request, 'dasboard.html', {'data': "", 't':translate_to_hindi(data)})
    

def translate_to_hindi(text):
    try:
        translator = Translator()
        return translator.translate(text, dest='hi').text
    except AttributeError:
        return None


def adhar_form(request):

    if request.method == "POST":
        form = AdharDetailFirstForm(request.POST, request.FILES)
        
        name = request.POST.get('full_name')
        form.instance.full_name_hi = translate_to_hindi(name)
        # print(request.POST.get('relation'))

        if request.POST.get('relation') == "S/O":
            form.instance.relation_hi = translate_to_hindi("atmaj")
        elif form.instance.relation == "W/O":
            form.instance.relation_hi = translate_to_hindi("pati")
        else:
            form.instance.relation_hi = translate_to_hindi("putri")


        if request.POST.get('gender') == "MALE":
            form.instance.gender_hi = translate_to_hindi("purush")
        else :
            form.instance.gender_hi = translate_to_hindi("mahila")

        form.instance.relation_name_hi = translate_to_hindi(request.POST.get('relation_name'))
        form.instance.address_hi = translate_to_hindi(request.POST.get('address'))
        # print(form.instance.address_hi)
        form.instance.city_hi = translate_to_hindi(request.POST.get('city'))
        form.instance.state_hi = translate_to_hindi(request.POST.get('state'))

        # return render(request, 'uid/adhar_form.html', {'form': form})

        if form.is_valid():
            print("Form is vailidated and saved...")
            form.save()
            return redirect('adhar_list')
        else:
            return render(request, 'uid/adhar_form.html', {'form': form})
    else:
        form = AdharDetailFirstForm()
        return render(request, 'uid/adhar_form.html', {'form': form})


def adhar_list(request):
    
    adhar_list = AdharCardDetail.objects.all() 
    return render(request, 'uid/adhar_list.html', {'data': adhar_list})


def print_adhar(request, id):
    
    try:
        data = AdharCardDetail.objects.get(id=id)

        adhar_number = ""
        uid=str(data.uid)

        # this loop return the uid no in format which is in int uid no 
        for i in range(0,14):
            if i < 4:
                adhar_number += uid[i]
            elif i == 4 or i == 9:
                adhar_number += " "
            elif i < 9:
                adhar_number += uid[i-1]
            elif i < 15:
                adhar_number += uid[i-2]
            else:
                adhar_number.append("")

        return render(request, 'uid/print_adhar.html', {'data': data, 'uid': adhar_number})
        
    except AdharCardDetail.DoesNotExist:
        return render(request, 'uid/adhar_view.html', {'data': None})


def update_adhar(request, id):
    
    instance = get_object_or_404(AdharCardDetail, id=id)
    form = AdharDetailForm(request.POST or None, request.FILES or None, instance=instance)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("adhar_list")
        else:
            return render(request, "uid/adhar_updtae_form.html", {"form": form})
    return render(request, "uid/adhar_updtae_form.html", {"form": form})


def delete_adhar(request, id):
    
    try:
        data = AdharCardDetail.objects.get(id=id)
        data.delete()
        return redirect('adhar_list')
    except AdharCardDetail.DoesNotExist:
        print("Unable to delete")
        return redirect('adhar_list')

