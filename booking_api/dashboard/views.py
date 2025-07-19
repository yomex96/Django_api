from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib.auth import logout


@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page after logout