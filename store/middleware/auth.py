from django.shortcuts import redirect
from django.contrib import messages 

def authmiddleware(get_response):
    def middleware(request):
        # print(request.META['PATH_INFO'])
        if not request.session.get("customer_id"):
            messages.success(request, 'Please Login')
            return redirect("home")
        # print("middleware")
        response=get_response(request)
        return response
    
    return middleware