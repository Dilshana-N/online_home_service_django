from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ohs_app.forms import login_form, worker_form, cus_register, FeedbackForm,ScheduleForm,Work_form,addbill_form,Creditcard_form
from ohs_app.models import worker_register, Register, complaints, Login,schedule,work,take_appoinments,Bill,CreditCard



# Create your views here.





           ######################## NOTES ########################

# "return redirect" for urls   , "return render" for .html pages
# ---.is_valid(): for checking validation which we defined in form
#commit=False for adding extra data and save it
# "objects.filter" = for filtering a specific one among a group


# home page of the website
def index(request):
    return render(request, "index.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("admin_base")
            if user.is_customer:
                return redirect("customer_base")
            if user.is_worker:
                return redirect("worker_base")
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, "login.html")
# log out function
def logout_view(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
# the dashboard

def dashboard(request):
    return render(request, "dashboard.html")


def customer_registration(request):
    form1 = login_form()
    form2 = cus_register()
    if request.method == 'POST':
        form1 = login_form(request.POST)
        form2 = cus_register(request.POST)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request, "customer.html", {'form1': form1, 'form2': form2})

def worker_registration(request):
    form1 = login_form()
    form2 = worker_form()
    if request.method == 'POST':
        form1 = login_form(request.POST)
        form2 = worker_form(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_worker = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request, "workers.html", {'form1': form1, 'form2': form2})







          ######################## ADMIN ########################

@login_required(login_url='login_page')
def admin_base(request):
    return render(request, "admin/admin_base_.html")

@login_required(login_url='login_page')
# customers data which we fetched through model "Register"
# "Register"=model created for customer registration
def customers_data(request):
    data = Register.objects.all()
    print(data)
    return render(request, "admin/customers_data.html", {'data': data})

@login_required(login_url='login_page')
# workers data which we fetched through model "worker_register"
# "worker_register"=model created for workerer registration
def workers_data(request):
    data = worker_register.objects.all()
    print(data)
    return render(request, "admin/workers_data.html", {'data': data})

@login_required(login_url='login_page')
# delete function fot workers data
#  data fetch through models,and mention this function as urls in workers_data.html
def delete(request, id):
    wm = worker_register.objects.get(id=id)
    wm.delete()
    return redirect("workers_data")

@login_required(login_url='login_page')
# delete function fot customers data
#  data fetch through models,and mention this funct
#  ion as urls in customers_data.html
# use different function name for same delete()
def delete_it(request, id):
    wm = Register.objects.get(id=id)
    wm.delete()
    return redirect("customers_data")

@login_required(login_url='login_page')
# update function for workers data
# "instance"=in updates an eding
#            we can access the data at the moment like what we edited or updated
def update(request, id):
    a = worker_register.objects.get(id=id)
    form = worker_form(instance=a)
    if request.method == 'POST':
       form = worker_form(request.POST,request.FILES, instance=a)
       if form.is_valid():
            form.save()
            return redirect("workers_data")
    return render(request, "admin/update.html", {'form': form})

@login_required(login_url='login_page')
# view feedback details with a reply feedback link
def feedbacks(request):
    n = complaints.objects.all
    return  render(request,"admin/feedbacks.html",{"feedbacks":n})

@login_required(login_url='login_page')
# admin replying feedback here
#what is reply)????????????
def reply_feedback(request,id):
    feedback=complaints.objects.get(id=id)
    if request.method== 'POST' :
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('feedbacks')
    return render(request,'admin/reply_feedback.html',{'feedback':feedback})

@login_required(login_url='login_page')
# view  worker added schedule by admin
def view_schedule_admin (request):
    n = schedule.objects.all
    return  render(request,"admin/view_schedule.html",{"view_schedule":n})

@login_required(login_url='login_page')
# delete schedules which worker added
# add this function's url in view shedule for admin as button
# admin can delete schedule
def delete_worker_schedule(request, id):
    wm = schedule.objects.get(id=id)
    wm.delete()
    return redirect("view_schedule_admin")

@login_required(login_url='login_page')
# work adding by admin,so worker can add their work which is defined by admin
def work_add(request):
    form=Work_form()
    if request.method=='POST':
        form=Work_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work_view")
    return render(request,'admin/work_add_admin.html',{'form':form})

@login_required(login_url='login_page')
# for viewing added work
# create a extra "work_view_admin.html" for work view and add delete and update button
def work_view(request):
    data=work.objects.all()
    return render(request,'admin/work_view_admin.html',{'data':data})

@login_required(login_url='login_page')
# add this function's url in delete button and update button
# delete work by admin
def delete_work(request, id):
    wm = work.objects.get(id=id)
    wm.delete()
    return redirect("work_view")

@login_required(login_url='login_page')
# update work by admin
# get the instance data-  'instance='
# work=model
# get the same form as update form(Work_form)
def update_work(request, id):
    a = work.objects.get(id=id)
    form = Work_form(instance=a)
    if request.method == 'POST':
        form = Work_form(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return redirect("work_view")
    return render(request, "admin/update_workdata.html", {'form': form})

@login_required(login_url='login_page')
# view appoinment by admin
def appoinmentview_admin(request):
    a=take_appoinments.objects.all()
    return render(request,"admin/viewappointment_admin.html",{"a":a})

@login_required(login_url='login_page')
# appointment approval function by admin
# if status=1 ,approve
def approve_appointment(request,id):
    n = take_appoinments.objects.get(id=id)
    n.status=1
    n.save()
    messages.info(request,'Appointment confirmed')
    return redirect('appoinmentview_admin')

@login_required(login_url='login_page')
# appointment rejection function by admin
# if status=2 ,reject
def reject_appointment(request,id):
    n=take_appoinments.objects.get(id=id)
    n.status=2
    n.save()
    messages.info(request,'Appointment Rejected')
    return redirect('appoinmentview_admin')

@login_required(login_url='login_page')
# for adding bill details like amount,date.....
def create_bill(request):
    form=addbill_form()
    if request.method=='POST':
        form=addbill_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')
    return render(request,'admin/generate_bill.html',{'form':form})

@login_required(login_url='login_page')
# view bill details what admin enter
def view_bill(request):
    bill=Bill.objects.all()
    print(bill)
    return render(request,'admin/view_payment_details.html',{'bill':bill})



















        ######################## WORKER ########################

@login_required(login_url='login_page')
def worker_base(request):
    return render(request, "worker/worker_base_.html")
@login_required(login_url='login_page')
def workerdata_view_by_worker(request):
    data = worker_register.objects.all()
    print(data)
    return render(request, "worker/workerdata_worker.html", {'data': data})

@login_required(login_url='login_page')
# add schedule by worker
def addschedule(request):
    form = ScheduleForm()
    # u = request.user
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.worker = worker_register.objects.get(user=request.user)
            obj.save()
            return redirect("view_filtered_schedule")
    return render(request, "worker/add_schedule.html", {"form": form})

@login_required(login_url='login_page')
# view schedules which added by worker
def view_schedule_worker(request):
    n = schedule.objects.all
    return render(request, "worker/viewschedule_worker.html", {"view_schedule": n})

@login_required(login_url='login_page')
def view_filtered_schedule(request):
        u = worker_register.objects.get(user=request.user)
        a = schedule.objects.filter(worker=u)
        return render(request, "worker/viewschedule_worker.html", {"view_schedule": a})


@login_required(login_url='login_page')
# schedule
# not fully created
def appoinmentview_worker(request):
    c = request.user.id
    print(c)
    s = take_appoinments.objects.filter(schedule__worker__user=c)
    print(s)
    return render(request, "worker/viewappointment_worker.html", {"s": s})

@login_required(login_url='login_page')
def workers_work(request):
    c = request.user.id
    print(c)
    s = take_appoinments.objects.filter(schedule__worker__user=c)
    print(s)
    return render(request, "worker/workby_worker.html", {"s": s})




@login_required(login_url='login_page')
def workerdata_worker(request):
    data = worker_register.objects.all()
    print(data)
    return render(request, "worker/data_view.html", {'data': data})

@login_required(login_url='login_page')
def update_worker_data(request, id):
    a = worker_register.objects.get(id=id)
    form = worker_form(instance=a)
    if request.method == 'POST':
        form = worker_form(request.POST,request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return redirect("workerdata_view_by_worker_filtered")
    return render(request, "worker/update_worker.html", {'form': form})

@login_required(login_url='login_page')
def workerdata_view_by_worker_filtered(request):
    data = worker_register.objects.filter(user=request.user)
    print(data)
    return render(request, "worker/update_worker_page.html", {'data': data})















    ######################## CUSTOMER ########################

@login_required(login_url='login_page')
# create dashboard function for customer
def customer_base(request):
    return render(request, "customer/customer_base_.html")


#add feedback for customer
# (commit=False) for adding "u" in it ,for knowing which one is feedbacked

@login_required(login_url='login_page')
def feedback(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect("feedback")
    return render(request, "customer/feedback.html", {"form": form})

@login_required(login_url='login_page')
# for viewing feedback
def view(request):
    data = complaints.objects.filter(user = request.user)
    print(data)
    return render(request, "customer/view.html", {"data": data})

@login_required(login_url='login_page')
# view schedule by customer
def view_schedule_customer (request):
    n = schedule.objects.all
    return  render(request,"customer/viewschedule_customer.html",{"view_schedule":n})

@login_required(login_url='login_page')
# book appoinment by customer
# add this url in button for booking appointment
def book_appoinment(request, id):
    wm = schedule.objects.get(id=id)
    wm.delete()
    return redirect("view_schedule_customer")

@login_required(login_url='login_page')
# view worker's data by customer
# create a seperate html page without update and delete button same as admin
# take datas from model "worker_register"
def view_workersdatacustomer(request):
    data = worker_register.objects.all()
    print(data)
    return render(request, "customer/view_worker_data_by_customer.html", {'data': data})

@login_required(login_url='login_page')
# function for take appoinment to customer
# u=customer
def appoinment_take_bycustomer(request,id):
    s = schedule.objects.get(id=id)
    u=Register.objects.get(user=request.user)
    appo=take_appoinments.objects.filter(user=u,schedule=s)
#     if already take appointment  we can't book
    if appo.exists():
        messages.info(request,"already booked")
        return redirect("view_schedule_customer")
# if appoinment not takened
    else:
        if request.method=="POST":
            obj=take_appoinments()
            obj.user=u
            obj.schedule=s
            obj.save()
            messages.info(request,"Appointment successfull")
            return redirect("appoinment_view")
    return render(request,"customer/take_appointment.html",{"s":s})

@login_required(login_url='login_page')
# view appoinment by customer only what he booked
def appoinment_view(request):
    u=Register.objects.get(user = request.user)
    a=take_appoinments.objects.filter(user=u)
    return render(request,"customer/viewappoinment_customer.html",{"a":a})

@login_required(login_url='login_page')
def appointment_side_profile(request):
    u=Register.objects.get(user = request.user)
    a=take_appoinments.objects.filter(user=u)
    return render(request,"customer/appointment side.html",{"a":a})

@login_required(login_url='login_page')
# view payment details by customer
#same as admin
# button change in admin
# in this html create a payment method button
def view_payment_by_customer(request):
    u = Register.objects.get(user=request.user)
    a = Bill.objects.filter(name=u)
    return render(request,'customer/view_payment_det_customer.html',{'a':a})

@login_required(login_url='login_page')
# for paying cash on delivery
# call the status
# status=2 for direct payment
def pay_in_direct(request,id):
    n = Bill.objects.get(id=id)
    n.status=2
    n.save()
    messages.info(request,'Choosed to pay direct')
    return redirect('view_payment_by_customer')

@login_required(login_url='login_page')
# for pay in online delivery
# status=1
def pay_bill_online(request,id):
    b=Bill.objects.get(id=id)
    form=Creditcard_form()
    if request.method == 'POST':
        card = request.POST.get('card')
        c=request.POST.get('cvv')
        d=request.POST.get('exp.')
        CreditCard(card_no=card,card_cvv=c,expiry_date=d).save
        b.status=1
        b.save()
        messages.info(request,"Bill Paided Successfully")
        return redirect("view_payment_by_customer")
    return render(request,"customer/pay_bill.html",{'form': form})

@login_required(login_url='login_page')
# bill history
# only confirmed not cancelled
def bill_history(request):
    u=Register.objects.get(user=request.user)
    bill=Bill.objects.filter(name=u,status__in=[1,2])
    return render(request,"customer/view_bill_history_customer.html",{'bill':bill})

@login_required(login_url='login_page')
def update_customer_data(request,id):
    a = Register.objects.get(id=id)
    form = cus_register(instance=a)
    if request.method == 'POST':
        form = cus_register(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect("customerdata_view_by_customer_filtered")
    return render(request, "customer/update_customer.html", {'form': form})

@login_required(login_url='login_page')
def customerdata_view_by_customer_filtered(request):
    data = Register.objects.filter(user=request.user)
    print(data)
    return render(request, "customer/update_customer_page.html", {'data': data})










