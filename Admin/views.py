from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from Admin.models import (
    UserProfile,
    OTP,
    Attendance,
    Timesheet,
    Leaveapplication,
    AddEvent,
    RecruitNotice,
    ResultPublish,
    Interview,
    Assignprojects
)
from django.core.mail import send_mail
import datetime
from django.conf import settings
# Create your views here.

def Login(request):
    Dict= {'message' : ''} 
    if request.method == "POST" :
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        data=authenticate(username=uname,password=pwd)
        if data !=None :
            login(request,data)
            return redirect('profile')
        msg= 'Incorrect Username or Password ' 
        Dict= {'message' : msg}  
    return render(request,"login.html", Dict)

def Logout(request):
    logout(request)
    return redirect('index')


def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        userType = request.POST.get('userType')
        profile_pic = request.FILES.get('pic')
        
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'signup.html',{'msg':msg})
        
        if len(contact)<10 or len(contact)>10:
            msg = 'Phone Number Should be equal to 10 digit'
            return render(request,'signup.html',{'msg':msg})

        try:
            user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        except:
            msg='Usename already exist.'
            return render(request,'signup.html',{'msg':msg})
        UserProfile.objects.create(user=user,profilePicture=profile_pic,contact_No=contact, address=address, dob=dob,userType=userType)
        return redirect('/login')
    return render(request, 'signup.html')

def AdminSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        profile_pic = request.FILES.get('pic')
        
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'adminsignup.html',{'msg':msg})
        
        if len(contact)<10 or len(contact)>10:
            msg = 'Phone Number Should be equal to 10 digit'
            return render(request,'adminsignup.html',{'msg':msg})

        try:
            user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        except:
            msg='Usename already exist.'
            return render(request,'adminsignup.html',{'msg':msg})
        UserProfile.objects.create(user=user,profilePicture=profile_pic,contact_No=contact, address=address, dob=dob, userType=Admin)
        return redirect('/login')
    return render(request, 'adminsignup.html')


def Profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,"profile.html") 

def ChangePass(request):
    if not request.user.is_authenticated:
        return redirect('login')
    msg =''
    if request.method == "POST":
        oldpass = request.POST.get('oldpass')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1!=password2:
            msg='Password should be same.'
            return render(request,'changepass.html', {'msg':msg})
        try:
            user = User.objects.get(username=request.user.username)
        except:
            msg='Invalid Username.'
            return render(request, 'changepass.html', {'msg':msg})
        
        t = user.check_password(oldpass)
        if t:
            user.set_password(password1)
            user.save()
            data=authenticate(username=request.user.username,password=password1)
            if data !=None :
                login(request,data)
                return redirect('profile')
        msg='Old Password is Incorrect.'
    return render(request,"changepass.html", {'msg':msg})      
    

def SendEmailForForgotPassword(request):
        if request.method == "POST":
          username = request.POST.get('username')

          try:
            user = User.objects.get(username=username)
          except:
            msg='Invalid Username.'
            return render(request, 'ForgotPassEmail.html', {'msg':msg})

        
          otp = OTP.objects.create(user=user)
        
          body = f'Forgot Password?? This is your OTP to get your password reset {otp.otp}'
          subject = 'Forgot Password for Your Account'
          from_email = settings.EMAIL_HOST_USER
          to_email = [user.email]
          send_mail(subject, body, from_email, to_email, fail_silently=True)
          return redirect('forgot-password')
        return render(request, 'ForgotPassEmail.html')

def ForgotPassword(request):
    msg =''
    if request.method == "POST":
        username = request.POST.get('username')
        user_otp = request.POST.get('otp')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1!=password2:
            msg='Password should be same.'
            return render(request,'ForgotPassEmail.html', {'msg':msg})
        try:
            user = User.objects.get(username=username)
        except:
            msg='Invalid Username.'
            return render(request, 'ForgotPassEmail.html', {'msg':msg})
        
        otp = OTP.objects.filter(user=user).order_by('-created_at').first()
        if str(otp.otp) == user_otp:
            user.set_password(password1)
            user.save()
            return redirect('/login')
        msg = 'Please Enter Correct OTP'
    return render(request, 'forgot-password.html', {'msg':msg})

def Addevent(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    if request.method == 'POST':
         date = request.POST.get('date')
         ename = request.POST.get('ename')
         venue = request.POST.get('venue')
         AddEvent.objects.create(
            user = UserProfile.objects.get(user=request.user),
            ename = ename,
            venue = venue,
            date = date,
         )      
         return redirect('/submitted')
    return render(request,'add-event.html')

def Assetmanage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'asset-manage.html')

def Recruitnotice(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
         title = request.POST.get('title')
         description = request.POST.get('description')
         RecruitNotice.objects.create(
            user = UserProfile.objects.get(user=request.user),
            title = title,
            description = description,
         )      
         return redirect('/submitted') 
    return render(request,'recruit-notice.html')

def Resultpublish(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    if request.method == 'POST':
         date = request.POST.get('date')
         ename = request.POST.get('ename')
         description = request.POST.get('description')
         ResultPublish.objects.create(
            user = UserProfile.objects.get(user=request.user),
            ename = ename,
            description = description,
            date = date,
         )      
         return redirect('/submitted')
    return render(request,'result-publish.html')

def ManageEmployee(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    employees = UserProfile.objects.filter(userType="Employee")
    return render(request, 'manage-employee.html', {'users':employees})
    
def AddEmployee(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        userType = request.POST.get('userType')

        
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'add-employee.html',{'msg':msg})
        
        if len(contact)<10 or len(contact)>10:
            msg = 'Phone Number Should be equal to 10 digit'
            return render(request,'add-employee.html',{'msg':msg})

        try:
            user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        except:
            msg='Usename already exist.'
            return render(request,'add-employee.html',{'msg':msg})
        UserProfile.objects.create(user=user,contact_No=contact, address=address, dob=dob,userType=userType)
        return redirect('/manage-employee')
    return render(request,'add-employee.html')


def Attendance1(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        date1 = request.POST.get('date')
        status = request.POST.get('status')
        in_time = request.POST.get('in_time')
        out_time = request.POST.get('out_time')

        print(type(datetime.date.today()))
        date = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        print(type(date))
        if datetime.date.today() == date:
            try:
                Attendance.objects.get(user=UserProfile.objects.get(
                    user=request.user), date=datetime.date.today())
                msg = "you have already Attended"
                return render(request, "attendance.html", {"msg": msg})
            except:
                Attendance.objects.create(
                    user=UserProfile.objects.get(user=request.user),
                    date=date1,
                    status=status,
                    in_time=in_time,
                    out_time=out_time
                )
                return redirect('/submitted')

        else:
            Attendance.objects.create(
                user=UserProfile.objects.get(user=request.user),
                date=date1,
                status=status,
                in_time=in_time,
                out_time=out_time
            )
            return redirect('/submitted')
    return render(request, 'attendance.html') 


def TimeSheet(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        month = request.POST.get('month')
        a = Attendance.objects.filter(user=UserProfile.objects.get(user=request.user), date__month=month)
        return render(request, 'user-timesheet.html',{'timesheet':a})
    return render(request,'timesheet.html') 



def LeaveApplication(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    if request.method == 'POST':
         from_date = request.POST.get('from_date')
         to_date = request.POST.get('to_date')
         leaveType = request.POST.get('leaveType')
         reasons = request.POST.get('reasons')
         Leaveapplication.objects.create(
            user = UserProfile.objects.get(user=request.user),
            from_date = from_date,
            to_date = to_date,
            leaveType = leaveType,
            reasons = reasons    
         )      
         return redirect('/submitted')
    return render(request,'leave-application.html')



def AssignInterview(request):
    if not request.user.is_authenticated:
        return redirect('login')
    u = UserProfile.objects.filter(userType="Manager")
    if request.method == 'POST':
         name = request.POST.get('name')
         manager = request.POST.get('manager')
         email = request.POST.get('email')
         description = request.POST.get('description')

         user = UserProfile.objects.get(id=int(manager))
         Interview.objects.create(
             user = user,
             candidate_name = name,
             candidate_email = email,
             candidate_description = description
         )
    return render(request, 'assign-interview.html', {'user':u})


def Interviews(request): 
    if not request.user.is_authenticated:
        return redirect('login')
    i = Interview.objects.filter(status="Pending")
    return render(request,'candidate-info.html',{'candidate':i})


def DeleteInterview(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    i = Interview.objects.get(id=id)
    i.delete()
    return redirect('search-candidate')


def DeleteWork(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    w = Assignprojects.objects.get(id=id)
    w.delete()
    return redirect('given-work')


def GivenWork(request):
    if not request.user.is_authenticated:
        return redirect('login')
    work = Assignprojects.objects.filter(manager=UserProfile.objects.get(user=request.user))
    return render(request, 'given-work.html', {'work':work})


def AddFeedback(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
         feedback = request.POST.get('feedback')
         if feedback is None:
            i = Interview.objects.filter(status="Pending")
            return render(request,'candidate-info.html',{'candidate':i})
         i = Interview.objects.get(id=id)
         i.feedback = feedback
         i.save()
         return redirect('interviews')


def SearchCandidate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
         email = request.POST.get('email')
         c = Interview.objects.filter(candidate_email__icontains=email)
         return render(request, 'candidate-info.html',{'candidate':c})
    return render(request, 'search-candidate.html')


def AcceptCandidate(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    i = Interview.objects.get(id=id)
    i.status = "Selected"
    i.save()
    return redirect('search-candidate')


def RejectedCandidate(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    i = Interview.objects.get(id=id)
    i.status = "Selected"
    i.save()
    return redirect('search-candidate')



def AssignWork(request) :
    if not request.user.is_authenticated:
        return redirect('login')
    employees = UserProfile.objects.filter(userType="Employee")
    if request.method == 'POST':
         pname = request.POST.get('pname')
         assignto = request.POST.get('assignto')
         date = request.POST.get('date')
         deadline = request.POST.get('deadline')
         description = request.POST.get('description')

         u = UserProfile.objects.get(id=int(assignto))

         Assignprojects.objects.create(
            manager = UserProfile.objects.get(user=request.user),
            user = u,
            pname = pname,
            description = description,
            date = date,
            deadline = deadline
         )      
         return redirect('/submitted') 
    return render(request,'assign-projects.html',{'users':employees})


def AssignedWork(request):
    if not request.user.is_authenticated:
        return redirect('login')
    a = Assignprojects.objects.filter(user=UserProfile.objects.get(user=request.user)).exclude(status="Completed")
    return render(request, 'work.html', {'work':a})


def StartWork(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    a = Assignprojects.objects.get(id=id)
    a.status = 'In Progress'
    a.save()
    return redirect('assigned-work')

def CompletedWork(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    a = Assignprojects.objects.get(id=id)
    a.status = 'Completed'
    a.save()
    return redirect('assigned-work')



def EditProfile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST" :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        pic = request.FILES.get('pic')
        u = UserProfile.objects.get(user=request.user)
        u.contact_No = contact
        u.address = address
        u.dob = dob
        if pic:
            u.profilePicture = pic
        u.user.first_name = first_name
        u.user.last_name = last_name
        u.user.email = email
        u.user.save()
        u.save()
        return redirect('profile')
    return render(request,'edit-profile.html')


def AllUsers(request):
    if not request.user.is_authenticated:
        return redirect('login')
    alluser = UserProfile.objects.all().exclude(user=request.user)
    return render(request, 'users.html', {'users':alluser})


def AllHr(request):
    if not request.user.is_authenticated:
        return redirect('login')
    allhr = UserProfile.objects.filter(userType="HR")
    return render(request, 'users.html', {'users':allhr})


def Employees(request):
    if not request.user.is_authenticated:
        return redirect('login')
    employees = UserProfile.objects.filter(userType="Employee")
    return render(request, 'users.html', {'users':employees})


def Managers(request):
    if not request.user.is_authenticated:
        return redirect('login')
    managers = UserProfile.objects.filter(userType="Manager")
    return render(request, 'users.html', {'users':managers})


def DeleteUser(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')


def UserDetails(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = UserProfile.objects.get(id=id)
    return render(request, 'userdetails.html', {"details":user})

def EditUser(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = UserProfile.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        pic = request.FILES.get('pic')
        
        user.contact_No = phone
        user.address = address
        user.dob = dob
        if pic:
            user.profilePicture = pic
        user.user.first_name=first_name
        user.user.last_name=last_name
        user.user.email = email
        
        user.user.save()
        user.save()
        return redirect('users')
    return render(request, 'edit-user.html', {"details":user})

def Submitted(request): 
    if not request.user.is_authenticated:
        return redirect('login')   
    return render(request, 'submitted.html')

def AttendanceDetails(request):
    if not request.user.is_authenticated:
        return redirect('login')
    alluser = Attendance.objects.all()
    return render(request, 'attendance-details.html', {'users':alluser})

def DeleteAttendance(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = Attendance.objects.get(id=id)
    user.delete()
    return redirect('/attendance-details')

def EditAttendance(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = Attendance.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        contact_No = request.POST.get('contact_No')
        date = request.POST.get('date')
        status = request.POST.get('status')
        in_time = request.POST.get('in_time')
        out_time = request.POST.get('out_time')

        user.contact_No = contact_No
        user.name = name
        user.date = date
        user.status = status
        user.in_time = in_time
        user.out_time = out_time

        user.save()
        return redirect('/attendance-details')
    return render(request, 'edit-attendance.html', {"details":user})


def TimesheetDetails(request):
    if not request.user.is_authenticated:
        return redirect('login')
    ts = Timesheet.objects.all()
    return render(request, 'timesheet-details.html', {'users':ts})

def DeleteTimesheet(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = Timesheet.objects.get(id=id)
    user.delete()
    return redirect('/timesheet-details')

def LaDetails(request):
    if not request.user.is_authenticated:
        return redirect('login')
    la = Leaveapplication.objects.filter(status="Pending")
    return render(request, 'la-details.html', {'users':la})


def Approve(request, id):
    if not request.user.is_authenticated:
        return redirect('login')    
    user = Leaveapplication.objects.get(id=id)
    user.status="Approved" 
    user.save()          
    body = ' Your Leave Application has been Approved.'
    subject = 'Leave Application Status'
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.user.user.email]
    send_mail(subject, body, from_email, to_email, fail_silently=True)
    return redirect('/la-details/')


def DeleteLa(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = Leaveapplication.objects.get(id=id)
    user.status="Rejected" 
    user.save()
    body = ' Your Leave Application has been Rejected.'
    subject = 'Leave Application Status'
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.user.user.email]
    send_mail(subject, body, from_email, to_email, fail_silently=True)
    return redirect('/la-details')
