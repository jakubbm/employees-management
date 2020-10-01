from django.shortcuts import redirect


def allowed_roles(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user_groups = [group.name for group in request.user.groups.all()]
            for group in user_groups:
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
            return redirect('Main:access_denied')
        return wrapper_func
    return decorator
