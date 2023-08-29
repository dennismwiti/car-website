from django.shortcuts import render, redirect
from .models import Inquiry
from django.contrib import messages, auth
# from django.contrib.auth.models import User


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        # message = request.POST['message']

        inquiry = Inquiry(car_id=car_id, car_title=car_title, user_id=user_id,
                          first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city,
                          state=state, email=email, phone=phone)
        # message = message
        # Inquiry.objects.order_by('user_id').filter(user_id=request.user.id))
        inquiry.save()

        # inquiries = request.session.get('inquiries', [])
        # inquiries.append({
        #     'car_title': car_title,
        #
        # })
        # request.session['inquiries'] = inquiries

        messages.success(request, 'Inquiry submitted successfully.')

        return redirect('dashboard')

    else:
        return render(request, 'accounts/cars.html')

    #     data = {
    #         'inquiries': inquiries,
    #     }
    #     return render(request, 'accounts/dashboard.html', data)
    # else:
    #     return render(request, 'accounts/inquiry.html')


def dashboard(request):

    # inquiries = request.session.get('inquiries', [])
    #
    # data = {
    #     'inquiries': inquiries,
    # }
    # return render(request, 'accounts/dashboard.html', data)

    inquiries = Inquiry.objects.all()  # Retrieve all inquiries from the database

    data = {
        'inquiries': inquiries,
    }
    return render(request, 'accounts/dashboard.html', data)


def delete_inquiry(request, inquiry_id):
    try:
        inquiry = Inquiry.objects.get(pk=inquiry_id)

        inquiry.delete()

        messages.success(request, 'Inquiry has been deleted successfully.')
    except Inquiry.DoesNotExist:

        messages.error(request, 'Inquiry deos not exist.')

    return redirect('dashboard')

