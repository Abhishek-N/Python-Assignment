from app.forms import UsersForm
from django.shortcuts import redirect, render
from django.http import JsonResponse
from app.models import User
from django.http import QueryDict

def create_user(request):
    if request.method=="POST":
        form = UsersForm(request.POST)
        try:
            form.save()
            return JsonResponse({'sts': True, 'msg': "User added"})
        except ValueError: 
            return JsonResponse({'sts': False, 'msg': "Failed adding user due to ValueError"}, status=400)

    else:        
        return render(request, 'index.html', {'nbar' : 'home'})

def view_users(request):
    if request.method == "GET":
        users = User.objects.all()
        return render(request, 'users.html', {'nbar': 'users', 'users': users})

def modify_user(request, id):
    if request.method == "GET":
        user = User.objects.get(id=id)
        return render(request, 'edit.html', {'nbar' : 'edit', 'user': user})
    elif request.method == "PUT":
        data = QueryDict(request.body)
        form = UsersForm(data)
        if form.is_valid():
            try:
                user = User.objects.filter(id=id).update(email=data.get('email'), first_name=data.get('first_name'), last_name=data.get('last_name'))
                return JsonResponse({'sts': True, 'msg': "Successfully updated user"})
            except:
                return JsonResponse({'sts': False, 'msg': "Failed to update user"}, status=500)
        else:
            return JsonResponse({'sts': False, 'msg': "Failed to update user"}, status=400)
    elif request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse({'sts': True, 'msg': "User successfully deleted"})
        except:
            return JsonResponse({'sts': False, 'msg': "Failed to delete user"}, status=400)

        