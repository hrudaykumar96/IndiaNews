from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from .forms import UserSignUpform, LoginUserForm, CustomPasswordChangeForm, CustomPasswordResetForm, AdminSignUpform, UserUpdateForm, UpdateUserForm
from django.contrib import messages
from news.models import Category
from news.forms import CategoryForm, Latest_News_Form, HeadlineForm, ArticlesForm, Trending_News_Form
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser
import datetime
from django.utils import timezone
from django.utils.text import slugify

# Create your views here.

def loginuser(request):
    if request.method=="POST":
        form=LoginUserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"You are Logged in successfully")
            return redirect('home')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f' {error}')
        return redirect('home')
    form=LoginUserForm()
    return redirect('home')


def signupuser(request):
    if request.method=="POST":
        form = UserSignUpform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Email registered successfully")
            return redirect('home')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f' {error}')
        return redirect('home')
    form=UserSignUpform()
    return redirect('home')


def signout(request):
    logout(request)
    messages.success(request,"You are Logged out Successfully")
    return redirect('home')


def change_password(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password updated successfully')
                return redirect('home')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{error}')
                return redirect('home')
        else:
            messages.info(request,"You are not logged in")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return redirect('home')


def reset_password(request):
    if request.method=="POST":
        form=CustomPasswordResetForm(user=None,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password changed successfully")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
            return redirect('home')
    else:
        form=CustomPasswordResetForm(user=None)
        return redirect('home')
    
@user_passes_test(lambda u: u.role==CustomUser.ADMIN, login_url='home')
def create_editor(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            if request.user.role==CustomUser.ADMIN:
                form=AdminSignUpform(request.POST)
                if form.is_valid():
                    user=form.save(commit=False)
                    user.set_unusable_password()
                    user.role=CustomUser.EDITOR
                    user.save()
                    messages.success(request,"Admin user created successfully")
                    return redirect('home')
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{error}')
                return redirect('home')
            messages.warning(request,"You are not authorized to create admin user")
            return redirect('home')
        messages.warning(request,"You are not logged in")
        return redirect('home')
    form=AdminSignUpform()
    return redirect('home')

@user_passes_test(lambda u: u.role==CustomUser.ADMIN, login_url='home')
def user_management(request):
    if request.user.role != CustomUser.ADMIN:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect('home')

    category = Category.objects.all()
    category_form = CategoryForm()
    LatestNews_Form = Latest_News_Form()
    Headline_Form = HeadlineForm()
    article_form = ArticlesForm()
    userupdateform=UserUpdateForm()
    trending_news_form = Trending_News_Form()
    passwordChangeform = CustomPasswordChangeForm(user=request.user)
    userregister_form = UserSignUpform()
    adminform = AdminSignUpform()

    # Filtering
    name_query = request.GET.get('name', '')
    email_query = request.GET.get('email', '')
    role_query = request.GET.get('role', '')
    from_date = request.GET.get('from_date', '')
    to_date = request.GET.get('to_date', '')

    users = CustomUser.objects.all()

    if name_query:
        users = users.filter(name__icontains=name_query)

    if email_query:
        users = users.filter(email__icontains=email_query)

    if role_query:
        if role_query == 'admin':
            users = users.filter(role='admin')
        elif role_query == 'user':
            users = users.filter(role='user')
        elif role_query == 'editor':
            users = users.filter(role='editor')

    if from_date and to_date:
        from_date = timezone.make_aware(datetime.datetime.strptime(from_date, '%Y-%m-%d'))
        to_date = timezone.make_aware(datetime.datetime.strptime(to_date, '%Y-%m-%d')) + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
        users = users.filter(date_joined__range=(from_date, to_date))

    users = users.order_by('name')

    return render(request, "usermanagement.html", {
        'category': category,
        'category_form': category_form,
        'Latest_News_Form': LatestNews_Form,
        'Headline_Form': Headline_Form,
        'article_form': article_form,
        'trending_news_form': trending_news_form,
        'passwordChangeform': passwordChangeform,
        'userregister_form': userregister_form,
        'users': users,
        'adminsignupform': adminform,
        'userupdateform':userupdateform
    })


@user_passes_test(lambda u: u.role==CustomUser.ADMIN, login_url='home')
def delete_users(request, slug):
    if request.user.role != CustomUser.ADMIN:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect("home")
    if request.method=="POST":
        try:
            users=CustomUser.objects.get(slug=slug)
            if users==request.user:
                messages.info(request,"Cannot delete your own account")
                return redirect("user_management")
            users.delete()
            messages.success(request,"User deleted successfully")
            return redirect('user_management')
        except users.DoesNotExist:
            messages.info(request,"User does not esist")
            return redirect("user_management")
    return redirect('user_management')


@user_passes_test(lambda u: u.role==CustomUser.ADMIN, login_url='home')
def update_user(request, slug):
    if request.user.role!=CustomUser.ADMIN:
        messages.warning(request,"You are nnot authorized to perform this action")
        return redirect('home')
    if request.method=="POST":
        user=CustomUser.objects.get(slug=slug)
        form=UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            if user==request.user:
                messages.info(request,"Cannot update own Account")
                return redirect('user_management')
            users=form.save(commit=False)
            users.slug=slugify(form.cleaned_data['email'])
            role = form.cleaned_data['role']
            if role == 'admin':
                users.role = role
                users.is_superuser=True
                users.is_staff=True
            elif role == 'editor':
                users.role = role
                users.is_superuser=False
                users.is_staff=True
            elif role == 'user':
                users.role = role
                users.is_superuser=False
                users.is_staff=False

            users.save()
            messages.success(request,"Data Updated Successfully")
            return redirect('user_management')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f' {error}')
        return redirect('user_management')
    form=UserUpdateForm(instance=user)
    return redirect('user_management')


def update_profile(request,user_id):
    user = CustomUser.objects.get(user_id = user_id)
    if request.user.user_id != user_id:
        messages.warning(request,"you cannot update other's profile")
        return redirect('home')
    if request.method == "POST":
        form = UpdateUserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            userform = form.save(commit=False)
            userform.user_id = form.cleaned_data['email'].split('@')[0]
            userform.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f' {error}')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        form = UpdateUserForm(instance=user)
        return redirect(request.META.get('HTTP_REFERER', 'home'))