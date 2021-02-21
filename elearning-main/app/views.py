from django.shortcuts import render

# Create your views here.
def renderLogin(request):
    return render(request,'login.html')
def renderFaculityHome(request):
    return render(request,'faculityHome.html')
def renderFaculityQueries(request):
    return render(request,'faculityManageQueries.html')
def renderFaculityChats(request):
    return render(request,'faculityChatRequests.html')
def renderFaculityProfile(request):
    return render(request,'faculityProfile.html')
def renderStudentHome(request):
    return render(request,'studentHome.html')
def renderStudentMaterials(request):
    return render(request,'studentMaterials.html')
def renderStudentChats(request):
    return render(request,'studentChats.html')
def renderStudentProfile(request):
    return render(request,'studentProfile.html')
