from django.shortcuts import render, redirect

def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            user_groups = [group.name for group in request.user.groups.all()]
            users_groups_quantity = len(user_groups)
            
            for group in user_groups:
                if group in allowed_roles:
                    return view_func(request,*args,**kwargs)
                elif user_groups.index(group) == users_groups_quantity:
                    return redirect('Main:access_denied')
        return wrapper_func
    return decorator
    
    