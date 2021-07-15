"""EmployeeManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from public.views import Index,About,Contact,Services
from Admin.views import (
    Login,
    Logout,
    Signup,
    AdminSignup,
    SendEmailForForgotPassword,
    ForgotPassword,
    ChangePass,
    Addevent,
    Assetmanage,
    Recruitnotice,
    Resultpublish,
    ManageEmployee,
    Attendance1,
    TimeSheet,
    LeaveApplication,

    AssignInterview,
    SearchCandidate,
    AcceptCandidate,
    RejectedCandidate,
    Interviews,
    DeleteInterview,
    AddFeedback,
    AssignWork,
    GivenWork,
    AssignedWork,
    StartWork,
    DeleteWork,
    CompletedWork,
    Profile,
    EditProfile,
    AllUsers,
    AllHr,
    Managers,
    Employees,
    UserDetails,
    DeleteUser,
    EditUser,
    Submitted,
    AddEmployee,
    AttendanceDetails,
    DeleteAttendance,
    EditAttendance,
    TimesheetDetails,
    DeleteTimesheet,
    LaDetails,
    Approve,
    DeleteLa
)

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index, name='index'),
    path('about/',About),
    path('contact/',Contact),
    path('services/',Services),
    path('login/',Login, name='login'),
   

    path('profile/',Profile, name = 'profile'),
    path('edit-profile/',EditProfile, name = 'edit-profile'),
    path('users/', AllUsers, name='users'),
    path('all-hr/', AllHr, name='all-hr'),
    path('managers/', Managers, name='managers'),
    path('employees/', Employees, name='employees'),
    path("user-details/<int:id>/", UserDetails, name="user-details"),
    path('edit-user/<int:id>/', EditUser, name="edit-user"),
    path('delete-user/<int:id>/', DeleteUser, name='delete-user'),
    path('add-event/',Addevent, name= 'add-event'),
    path('asset-manage/',Assetmanage, name='asset-manage'),
    path('attendance/',Attendance1, name='attendance'),
    path('attendance-details/',AttendanceDetails, name='attendance-details'),
    path('delete-attendance/<int:id>/', DeleteAttendance, name='delete-attendance'),
    path('edit-attendance/<int:id>/', EditAttendance, name="edit-attendance"),
    path('submitted/',Submitted, name='submitted'),
    path('timesheet/',TimeSheet, name='timesheet'),
    path('timesheet-details/',TimesheetDetails, name='timesheet-details'),
    path('delete-timesheet/<int:id>/', DeleteTimesheet, name='delete-timesheet'),
    path('leave-application/',LeaveApplication, name= 'leave-application'),
    path('la-details/',LaDetails, name='la-details'),
    path('delete-la/<int:id>/', DeleteLa, name='delete-la'),
    path("approve/<int:id>/", Approve, name="approve"),

    path('assign-interview/', AssignInterview, name='assign-interview'),
    path('search-candidate/', SearchCandidate, name='search-candidate'),
    path('interviews/',Interviews, name= 'interviews'),
    path('add-feedback/<int:id>/', AddFeedback, name='add-feedback'),
    path('accept-candidate/<int:id>/', AcceptCandidate, name='accept-candidate'),
    path('reject-candidate/<int:id>/', RejectedCandidate, name='reject-candidate'),
    path('delete-interview/<int:id>/', DeleteInterview, name='delete-interview'),

    path('assign-work/',AssignWork, name= 'assign-work'),
    path('assigned-work/', AssignedWork, name='assigned-work'),
    path('given-work/', GivenWork, name='given-work'),
    path('delete-work/<int:id>/', DeleteWork, name='delete-work'),

    path('start-work/<int:id>/', StartWork, name='start-work'),
    path('completed-work/<int:id>/', CompletedWork, name='completed-work'),

    path('manage-employee/',ManageEmployee, name='manage-employee'),
    path('add-employee/',AddEmployee, name='add-employee'),
    path('result-publish/',Resultpublish, name='result-publish'),
    path('recruit-notice/',Recruitnotice, name='recruit-notice'),
    path('changepass/',ChangePass, name ='changepass'),
    path('logout/',Logout),
    path('signup/',Signup),
    path('adminsignup/',AdminSignup, name= 'adminsignup'),
    path('email-forgotpassword/',SendEmailForForgotPassword, name='email-forgotpassword'),
    path('forgot-password/', ForgotPassword, name='forgot-password'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

