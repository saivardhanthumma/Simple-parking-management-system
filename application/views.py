from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Sum
from django.db.models.functions import Cast

def login1(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

            return redirect('dashboard')
            
        else:
            
            messages.info(request,"Username or Password is incorrect")
            
            return redirect('home')
    else:
       
        return redirect('home')

def home(request):
    return render(request,'index.html')

@login_required(login_url='home')
def dashboard(request):
    if request.user.is_authenticated:
        total_parked_cars=Add_Vehicle.objects.filter(status=1).count()
      
        departed_parked_cars=Add_Vehicle.objects.filter(status=0).count()
        
        category_count=Category.objects.all().count()
       
        total_vehicle_records=Add_Vehicle.objects.all().count()
        
        total_earnings = Add_Vehicle.objects.filter(status=False).aggregate(Sum('parking_charge'))["parking_charge__sum"]
        total_limit = Category.objects.all().aggregate(Sum('vehicle_limit'))["vehicle_limit__sum"]
        total_limit=int(total_limit)
        total_parked_cars = Add_Vehicle.objects.filter(status=True).count()
   
        context={'tp':total_parked_cars,
                 'dp':departed_parked_cars,
                 'cc':category_count,
                 'tv':total_vehicle_records,
                 'tl':total_limit,
                 'total_earnings':total_earnings ,
                 

                 
        }
        return render(request,'dashboard.html',context)
    else:
        return  redirect('home')



@login_required(login_url='home')
def category(request):
     data1=Category.objects.all()
     data=Category.objects.all()

     context={
        'data':data,
        'data1':data1,
    }
     return render(request,"category.html", context)

@login_required(login_url='home')
# def vehicleEntry(request):
#     data=Category.objects.all()
#     data1 = Add_Vehicle.objects.all() 
    
    
#     context = {
#         'data':data,
#         'data1': data1,
        
#     }
#     return render(request, 'vehicleEntry.html', context)
@login_required(login_url='home')
def vehicleEntry(request):
    
    categories = Category.objects.all()
    data1 = Add_Vehicle.objects.all() 
    
    remaining_limits = {}
    
    
    for category in categories:
      
        # Count how many vehicles are currently parked in each category
        parked_cars_count = Add_Vehicle.objects.filter(vehicle_type=category.vehicle_type, status=True).count()
        
    
        # Calculate remaining spaces
        remaining_limits[category.vehicle_type] = int(category.vehicle_limit) - parked_cars_count
       
    
    
    # Create a list of dictionaries, each containing category info and the remaining limit
    data = []
    
    for category in categories:
        data.append({
            'vehicle_type': category.vehicle_type,
            'vehicle_limit': category.vehicle_limit,
            'remaining_limit': remaining_limits[category.vehicle_type]
        })
   
    context = {
        'data': data,
        'data1':data1,
        'category':categories
    }
   
    return render(request, 'vehicleEntry.html', context)
    

@never_cache
@login_required(login_url='home')
def managevehicle(request):
    
    vehicles1 = Add_Vehicle.objects.all()  # Get all vehicles if no search query
    
    context = {
        'data1': vehicles1,
        
    }
    return render(request, 'managevehicles.html', context)
    
    
@never_cache
@login_required(login_url='home')
def searchdata(request):
    vehicles = Add_Vehicle.objects.all()
    # if request.method == "POST":
    #     search_query1 = request.POST.get('search')
    #     if search_query1:
    #         vehicles = vehicles.filter(vehicle_no=search_query1)
    return render(request, 'search.html', {"vehicles": vehicles})


@login_required(login_url='home')
def Account(request):
    if request.method == 'POST':
        currentpswd = request.POST.get('CurrentPassword')
        newpswd = request.POST.get('NewPassword')
        
        
        # Assuming the user is already logged in, you can get their username from the request
        username = request.user.username
        
        # Authenticate the user
        user = auth.authenticate(username=username, password=currentpswd)
        print(user)
        if user is not None:
            user.set_password(newpswd)
            user.save()
                    # It's a good practice to log the user out after changing their password
            auth.logout(request)
            messages.success(request, "Your password has been changed successfully. Please log in again.")
            return redirect('home')
            
            
        else:
            messages.error(request,'please enter valid password')
       
    
    return render(request, 'Account.html')

def login1(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:

            auth.login(request,user)
            
            return redirect('dashboard')
            
        else:
            
            messages.info(request,"Username or Password is incorrect")
            
            return redirect('home')
    else:
       
        return redirect('home')

@never_cache
@login_required(login_url='home')
def categoryEntry(request):
    data=Category.objects.all()
    try:
        if  request.method=='POST':
            parking_area_no=request.POST.get('ParkingAreaNumber')
            vehicle_type=request.POST.get('VehicleType')
            vehicle_limit=request.POST.get('VehicleLimit')
            parking_charge=request.POST.get('ParkingCharge')
            
            
        

            Category.objects.create(
                parking_area_no=parking_area_no,
                vehicle_type=vehicle_type,
                vehicle_limit=vehicle_limit,
                parking_charge=parking_charge,
            
                )
            # data=Category.objects.all()
            # ,{'data':data}
            messages.success(request,'Data added successfully!')
            
            return redirect('category')
        else:
            return redirect( "category" )
    except :
        messages.error(request,"you are enter duplicate values")
        return redirect('category')
@never_cache
@login_required(login_url='home')
def vehicleEntryregister(request):
    if  request.method=='POST':
        vehicle_no=request.POST.get('VehicleNumber')
        parking_area_no=request.POST.get('ParkingAreaNumberEntry')
      
        parking_charge=request.POST.get('ParkingChargeEntry')
        vehicle_type_name = request.POST.get('VehicleTypeEntry')
       
        parking_charge=float(parking_charge[1:])
    
        

        Add_Vehicle.objects.create(
                vehicle_no = vehicle_no,
                parking_area_no=parking_area_no,
                vehicle_type=vehicle_type_name,
                parking_charge=parking_charge,
            
                )
        
        
        
        return redirect( "vehicleEntry" )
    else:
        
        return redirect( "vehicleEntry" )

@login_required(login_url='home')  
def deactivate_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.status = False  # Assuming 'status' is a BooleanField
    category.save()
    return redirect('category')  

@login_required(login_url='home')
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('category')  # Redirect to the list view or wherever appropriate

@login_required(login_url='home')
def DoneBtn(request,vehicleid):
    print(vehicleid)
    add_Vehicle= Add_Vehicle.objects.get(id=vehicleid)
    add_Vehicle.status=False
    add_Vehicle.save()
    print(555)
    
    return redirect('managevehicle')

def edit_category(request,category_id):
    
    if request.method == 'POST':
        parking_area_no=request.POST.get('parking_area_no')
        vehicle_type=request.POST.get('vehicle_type')
        vehicle_limit=request.POST.get('vehicle_limit')
        parking_charge=request.POST.get('parking_charge')
        print(parking_area_no)
        print(vehicle_limit)
        print(vehicle_type)
        print(parking_charge) 
        Category.objects.filter(id=category_id).update(parking_area_no=parking_area_no, vehicle_type=vehicle_type, vehicle_limit=vehicle_limit,parking_charge=parking_charge)
        # category = Category.objects.get(id=specific_id)
        # category.name = 'New Name'
        # category.vehicle_type = 'New Vehicle Type'
        # category.vehicle_limit = 10
        # category.save()


        return redirect('category')
    return  redirect('category')
def logout1(request):
    auth.logout(request)
    
    return redirect('/')