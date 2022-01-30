from functools import reduce
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import AdharCardDetail
from .forms import AdharDetailForm, AdharDetailFirstForm
from googletrans import Translator
from datetime import datetime
from dateutil.relativedelta import relativedelta



def index(request):
    
    data = '''Rajendra Kumar, chitarwai kala, khutar, singrauli, madhya pradesh
    contact: 9009112115
    '''
    return render(request, 'dasboard.html', {'data': translate_to_hindi(data)})
    

def translate_to_hindi(text):
    try:
        translator = Translator()
        return translator.translate(text, dest='hi').text
    except AttributeError:
        return None


@login_required
def adhar_form(request):

    if request.method == "POST":
        form = AdharDetailFirstForm(request.POST, request.FILES)
        
        name = request.POST.get('full_name')
        form.instance.full_name_hi = translate_to_hindi(name)
        # print(request.POST.get('relation'))

        if request.POST.get('relation') == "S/O":
            form.instance.relation_hi = translate_to_hindi("atmaj")
        elif form.instance.relation == "W/O":
            form.instance.relation_hi = translate_to_hindi("ardhangani")
        else:
            form.instance.relation_hi = translate_to_hindi("aatmja")


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


@login_required
def adhar_list(request):
    
    adhar_list = AdharCardDetail.objects.all() 
    return render(request, 'uid/adhar_list.html', {'data': adhar_list})


@login_required
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

        download_date = datetime.now()
        issue_date = datetime.now() - relativedelta(years=3, days=8)
        string = str(data.uid) + " " + data.full_name + " " + data.relation + " " + data.relation_name + " " + str(data.date_of_birth) + " " + data.gender + " " + data.address + " " + data.city + " " + data.state + " " +data.full_name_hi + " " + data.relation_hi + " " + data.relation_name_hi + " " + data.gender_hi + " " + data.address_hi + " " + data.city_hi + " " + data.state_hi + " " + str(data.pin_code) + " " + str(data.image)
        string += " " + str(download_date) + str(issue_date)
        string += ", This is fack Adhar Download From Fack site 'Raj Infotech Printing Service' for any frod this site will not responsible"
        qr_text = reduce(lambda x, y: str(x)+str(y), map(ord,string))
        
        context = {
            'data': data, 
            'uid': adhar_number, 
            'qr_text': qr_text,
            'download_date': download_date,
            'issue_date': issue_date
        }

        return render(request, 'uid/print_adhar.html', context)
        
    except AdharCardDetail.DoesNotExist:
        return render(request, 'uid/adhar_view.html', {'data': None})


@login_required
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


@login_required
def delete_adhar(request, id):
    
    try:
        data = AdharCardDetail.objects.get(id=id)
        data.delete()
        return redirect('adhar_list')
    except AdharCardDetail.DoesNotExist:
        print("Unable to delete")
        return redirect('adhar_list')

