from django.shortcuts import render
from .models import Member
# Create your views here.
def members(request):
    myMembers = Member.objects.all()
    return render(request, 'all_members.html',{'myMembers' : myMembers})