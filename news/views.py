from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Latest_News, Articles, Trending_News, Headlines
from .forms import CategoryForm, Latest_News_Form, HeadlineForm, ArticlesForm, Trending_News_Form, UpdateNewsForm
from django.contrib import messages
from users.forms import LoginUserForm, UserSignUpform, CustomPasswordChangeForm, CustomPasswordResetForm, AdminSignUpform, UpdateUserForm
from django.contrib.auth.decorators import user_passes_test
import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.utils.html import strip_tags
from comments.forms import CommentsForm, ReplyForm
from comments.models import Comments, Reply
from users.models import CustomUser


# Create your views here.

def home(request):
    search_query = request.GET.get('news', '')
    categories = Category.objects.all()
    latest_news = Latest_News.objects.all().order_by('-publish_date')
    trending_news = Trending_News.objects.all().order_by('-publish_date')
    headlines = Headlines.objects.all().order_by('-publish_date')
    articles = Articles.objects.all().order_by('-publish_date')

    if search_query:
        latest_news = latest_news.filter(title__icontains=search_query)
        trending_news = trending_news.filter(title__icontains=search_query)
        headlines = headlines.filter(title__icontains=search_query)
        articles = articles.filter(title__icontains=search_query)

    news_content = list(latest_news) + list(trending_news) + list(headlines) + list (articles)

    news_sorted = sorted(news_content, key=lambda x: x.publish_date, reverse=True)
    category_form = CategoryForm()
    latest_news_form = Latest_News_Form()
    headline_form = HeadlineForm()
    article_form = ArticlesForm()
    trending_news_form = Trending_News_Form()
    login_user_form = LoginUserForm()
    user_register_form = UserSignUpform()
    update_news_form = UpdateNewsForm()
    password_change_form = CustomPasswordChangeForm(user=request.user)
    password_reset_form = CustomPasswordResetForm(user=None)
    admin_form = AdminSignUpform()

    return render(request, "home.html", {
        'category': categories,
        'latest_news': latest_news,
        'trending_news': trending_news,
        'headlines': headlines,
        'articles': articles,
        'news_sorted': news_sorted,
        'category_form': category_form,
        'Latest_News_Form': latest_news_form,
        'Headline_Form': headline_form,
        'article_form': article_form,
        'trending_news_form': trending_news_form,
        'login_user_form': login_user_form,
        'userregister_form': user_register_form,
        'adminsignupform': admin_form,
        'passwordChangeform': password_change_form,
        'password_reset_form': password_reset_form,
        'updatenewsform': update_news_form
    })


def full_latest_news_view(request, slug):
    if not request.user.is_authenticated:
        messages.info(request, "Please login to read news")
        return redirect("home")
    category=Category.objects.all()
    latest_news=get_object_or_404(Latest_News, slug=slug)
    category_form=CategoryForm()
    LatestNews_Form=Latest_News_Form()
    Headline_Form=HeadlineForm()
    article_form=ArticlesForm()
    trending_news_form=Trending_News_Form()
    commentsform=CommentsForm()
    login_user_form=LoginUserForm()
    reply_form=ReplyForm()
    userregister_form=UserSignUpform()
    comments=Comments.objects.filter(latest_news=latest_news).order_by('-id')
    for comment in comments:
        comment.replies = Reply.objects.filter(comment=comment)
    adminform=AdminSignUpform()
    updatenewsform=UpdateNewsForm()
    passwordresetform=CustomPasswordResetForm(user=None)
    passwordChangeform=CustomPasswordChangeForm(user=request.user)
    return render(request,"output.html",{'news':latest_news,'comments':comments,'reply_form':reply_form, 'commentsform':commentsform, 'category':category, 'category_form':category_form, 'Latest_News_Form': LatestNews_Form, 'Headline_Form':Headline_Form, 'article_form':article_form, 'trending_news_form':trending_news_form, 'login_user_form':login_user_form, 'userregister_form':userregister_form, 'passwordChangeform':passwordChangeform, 'adminsignupform':adminform,'password_reset_form':passwordresetform, 'updatenewsform':updatenewsform})


def full_trending_news_view(request, slug):
    if not request.user.is_authenticated:
        messages.info(request, "Please login to read news")
        return redirect("home")
    category=Category.objects.all()
    trending_news=get_object_or_404(Trending_News, slug=slug)
    category_form=CategoryForm()
    LatestNews_Form=Latest_News_Form()
    Headline_Form=HeadlineForm()
    article_form=ArticlesForm()
    commentsform=CommentsForm()
    reply_form=ReplyForm()
    comments=Comments.objects.filter(trending_news=trending_news).order_by('-id')
    for comment in comments:
        comment.replies = Reply.objects.filter(comment=comment)
    trending_news_form=Trending_News_Form()
    login_user_form=LoginUserForm()
    adminform=AdminSignUpform()
    updatenewsform=UpdateNewsForm()
    userregister_form=UserSignUpform()
    passwordChangeform=CustomPasswordChangeForm(user=request.user)
    passwordresetform=CustomPasswordResetForm(user=None)
    return render(request,"output.html",{'news': trending_news,'reply_form':reply_form, 'comments':comments,'commentsform':commentsform, 'category':category, 'category_form':category_form, 'Latest_News_Form': LatestNews_Form, 'Headline_Form':Headline_Form, 'article_form':article_form, 'trending_news_form':trending_news_form, 'login_user_form':login_user_form, 'userregister_form':userregister_form, 'passwordChangeform':passwordChangeform, 'adminsignupform':adminform,'password_reset_form':passwordresetform, 'updatenewsform':updatenewsform})


def full_headlines_view(request, slug):
    if not request.user.is_authenticated:
        messages.info(request, "Please login to read news")
        return redirect("home")
    category=Category.objects.all()
    headlines=get_object_or_404(Headlines, slug=slug)
    category_form=CategoryForm()
    LatestNews_Form=Latest_News_Form()
    Headline_Form=HeadlineForm()
    adminform=AdminSignUpform()
    reply_form=ReplyForm()
    commentsform=CommentsForm()
    article_form=ArticlesForm()
    comments=Comments.objects.filter(headlines=headlines).order_by('-id')
    for comment in comments:
        comment.replies = Reply.objects.filter(comment=comment)
    trending_news_form=Trending_News_Form()
    login_user_form=LoginUserForm()
    userregister_form=UserSignUpform()
    updatenewsform=UpdateNewsForm()
    passwordChangeform=CustomPasswordChangeForm(user=request.user)
    passwordresetform=CustomPasswordResetForm(user=None)
    return render(request,"output.html",{'news':headlines, 'reply_form':reply_form, 'category':category,'comments':comments, 'commentsform':commentsform,'category_form':category_form, 'Latest_News_Form': LatestNews_Form, 'Headline_Form':Headline_Form, 'article_form':article_form, 'trending_news_form':trending_news_form, 'login_user_form':login_user_form, 'userregister_form':userregister_form, 'passwordChangeform':passwordChangeform, 'adminsignupform':adminform,'password_reset_form':passwordresetform, 'updatenewsform':updatenewsform})


def full_articles_view(request, slug):
    if not request.user.is_authenticated:
        messages.info(request, "Please login to read news")
        return redirect("home")
    category=Category.objects.all()
    articles=get_object_or_404(Articles, slug=slug)
    category_form=CategoryForm()
    LatestNews_Form=Latest_News_Form()
    Headline_Form=HeadlineForm()
    article_form=ArticlesForm()
    trending_news_form=Trending_News_Form()
    adminform=AdminSignUpform()
    login_user_form=LoginUserForm()
    reply_form=ReplyForm()
    comments=Comments.objects.filter(articles=articles).order_by('-id')
    for comment in comments:
        comment.replies = Reply.objects.filter(comment=comment)
    commentsform=CommentsForm()
    updatenewsform=UpdateNewsForm()
    userregister_form=UserSignUpform()
    passwordresetform=CustomPasswordResetForm(user=None)
    passwordChangeform=CustomPasswordChangeForm(user=request.user)
    return render(request,"output.html",{'news':articles,'comments':comments,'reply_form':reply_form,'category':category,'commentsform':commentsform, 'category_form':category_form, 'Latest_News_Form': LatestNews_Form, 'Headline_Form':Headline_Form, 'article_form':article_form, 'trending_news_form':trending_news_form, 'login_user_form':login_user_form, 'userregister_form':userregister_form, 'passwordChangeform':passwordChangeform, 'adminsignupform':adminform, 'password_reset_form':passwordresetform, 'updatenewsform':updatenewsform})

def get_news_bycategory(request,slug):
    category = Category.objects.all()
    current_category = get_object_or_404(Category, slug=slug)
    latest_news = Latest_News.objects.filter(category__slug=slug).order_by('-publish_date')
    trending_news = Trending_News.objects.filter(category__slug=slug).order_by('-publish_date')
    headlines = Headlines.objects.filter(category__slug=slug).order_by('-publish_date')
    articles = Articles.objects.filter(category__slug=slug).order_by('-publish_date')
    selected_category = get_object_or_404(Category, slug=slug)
    all_news_content = list(latest_news) + list(trending_news) + list(headlines) + list(articles)
    for item in all_news_content:
        item.class_name = item.__class__.__name__
    news_sorted = sorted(all_news_content, key=lambda x: x.publish_date, reverse=True)
    category_form=CategoryForm()
    LatestNews_Form=Latest_News_Form()
    updatenewsform=UpdateNewsForm()
    Headline_Form=HeadlineForm()
    article_form=ArticlesForm()
    trending_news_form=Trending_News_Form()
    adminform=AdminSignUpform()
    login_user_form=LoginUserForm()
    passwordresetform=CustomPasswordResetForm(user=None)
    passwordChangeform=CustomPasswordChangeForm(user=request.user)
    userregister_form=UserSignUpform()
    return render(request, "categorydata.html", {
        'category': category,
        'latest_news': latest_news,
        'trending_news': trending_news,
        'headlines': headlines,
        'articles': articles,
        'news_sorted': news_sorted,
        'selected_category':selected_category,
        'category_form':category_form,
        'Latest_News_Form':LatestNews_Form,
        'Headline_Form':Headline_Form,
        'article_form':article_form,
        'trending_news_form':trending_news_form,
        'current_category':current_category,
        'current_category_slug':current_category.slug,
        'login_user_form':login_user_form,
        'userregister_form':userregister_form,
        'adminsignupform':adminform,
        'passwordChangeform':passwordChangeform,
        'password_reset_form':passwordresetform,
        'updatenewsform':updatenewsform
    })


@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def create_category(request):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect("home")
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            if Category.objects.filter(name__iexact=form.cleaned_data['name']).exists():
                messages.info(request,"Category name already exists")
                return redirect('home')
            categoryform=form.save(commit=False)
            categoryform.user=request.user
            categoryform.save()
            messages.success(request,"Category added successfully")
            return redirect('home')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
        return redirect('home')
    form=CategoryForm()
    return redirect('home')

@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def create_latest_news(request):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect("home")
    if request.method=="POST":
        form=Latest_News_Form(request.POST, request.FILES)
        if form.is_valid():
            if Latest_News.objects.filter(title__iexact=form.cleaned_data['title']).exists():
                messages.info(request,"News with title already exists")
                return redirect('home')
            latest_news_form=form.save(commit=False)
            latest_news_form.user=request.user
            latest_news_form.save()
            messages.success(request,"News posted successfully")
            return redirect('home')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
        return redirect('home')
    form=Latest_News_Form()
    return redirect('home')

@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def create_headline(request):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect("home")
    if request.method=="POST":
        form=HeadlineForm(request.POST,request.FILES)
        if form.is_valid():
            if Headlines.objects.filter(title__iexact=form.cleaned_data['title']).exists():
                messages.info(request, "News with title already exists")
                return redirect('home')
            headline_form=form.save(commit=False)
            headline_form.user=request.user
            headline_form.save()
            messages.success(request,"News posted successfully")
            return redirect('home')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
        return redirect('home')
    form=HeadlineForm()
    return redirect('home')

@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def create_article(request):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect("home")
    if request.method=="POST":
        form=ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            if Articles.objects.filter(title__iexact=form.cleaned_data['title']).exists():
                messages.info(request, "News with title already exists")
                return redirect('home')
            article_form=form.save(commit=False)
            article_form.user=request.user
            article_form.save()
            messages.success(request,"News posted successfully")
            return redirect('home')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
        return redirect('home')
    form=ArticlesForm()
    return redirect('home')   

@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def create_trending_news(request):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect("home")
    if request.method=="POST":
        form=Trending_News_Form(request.POST, request.FILES)
        if form.is_valid():
            if Trending_News.objects.filter(title__iexact=form.cleaned_data['title']).exists():
                messages.info(request, "News with title already exists")
                return redirect('home')
            trending_news_form=form.save(commit=False)
            trending_news_form.user=request.user
            trending_news_form.save()
            messages.success(request,"News posted successfully")
            return redirect('home')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
        return redirect('home')
    form=Trending_News_Form()
    return redirect('home')

@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def news_management(request):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request, "You are not authorized to perform this action")
        return redirect('home')
    
    category = Category.objects.all()
    category_form = CategoryForm()
    LatestNews_Form = Latest_News_Form()
    Headline_Form = HeadlineForm()
    adminform = AdminSignUpform()
    article_form = ArticlesForm()
    trending_news_form = Trending_News_Form()
    passwordChangeform = CustomPasswordChangeForm(user=request.user)
    userregister_form = UserSignUpform()
    updatenewsform=UpdateNewsForm()

    if request.user.role == CustomUser.EDITOR:
        latest_news = Latest_News.objects.filter(user=request.user)
        trending_news = Trending_News.objects.filter(user=request.user)
        headlines = Headlines.objects.filter(user=request.user)
        articles = Articles.objects.filter(user=request.user)    
    elif request.user.role == CustomUser.ADMIN:
        latest_news = Latest_News.objects.all()
        trending_news = Trending_News.objects.all()
        headlines = Headlines.objects.all()
        articles = Articles.objects.all()  

    title_query = request.GET.get('title', '')
    category_query = request.GET.get('category', '')
    news_user = request.GET.get('news_user', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')

    if title_query:
        latest_news = latest_news.filter(title__icontains=title_query)
        trending_news = trending_news.filter(title__icontains=title_query)
        headlines = headlines.filter(title__icontains=title_query)
        articles = articles.filter(title__icontains=title_query)

    if news_user:
        try:
            users = CustomUser.objects.filter(name__icontains=news_user)
            latest_news = latest_news.filter(user__in=users)
            trending_news = trending_news.filter(user__in=users)
            headlines = headlines.filter(user__in=users)
            articles = articles.filter(user__in=users)
        except CustomUser.DoesNotExist:
            latest_news = latest_news.none()
            trending_news = trending_news.none()
            headlines = headlines.none()
            articles = articles.none()

    if category_query:
        latest_news = latest_news.filter(category__id=category_query)
        trending_news = trending_news.filter(category__id=category_query)
        headlines = headlines.filter(category__id=category_query)
        articles = articles.filter(category__id=category_query)
      

    if date_from and date_to:
        date_from = timezone.make_aware(datetime.datetime.strptime(date_from, '%Y-%m-%d'))
        date_to = timezone.make_aware(datetime.datetime.strptime(date_to, '%Y-%m-%d')) + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
        latest_news = latest_news.filter(publish_date__range=(date_from, date_to))
        trending_news = trending_news.filter(publish_date__range=(date_from, date_to))
        headlines = headlines.filter(publish_date__range=(date_from, date_to))
        articles = articles.filter(publish_date__range=(date_from, date_to))

    all_news_content = list(latest_news) + list(trending_news) + list(headlines) + list(articles)
    for item in all_news_content:
        item.class_name = item.__class__.__name__
    all_news_sorted = sorted(all_news_content, key=lambda x: x.publish_date, reverse=True)
    
    total_count = len(all_news_sorted)
    total_news = len(trending_news) + len(latest_news)
    total_headline = len(headlines)
    total_articles = len(articles)

    return render(request, "newsmanagement.html", {
        'category': category,
        'category_form': category_form,
        'Latest_News_Form': LatestNews_Form,
        'Headline_Form': Headline_Form,
        'updatenewsform':updatenewsform,
        'article_form': article_form,
        'trending_news_form': trending_news_form,
        'passwordChangeform': passwordChangeform,
        'userregister_form': userregister_form,
        'adminsignupform': adminform,
        'news': all_news_sorted,
        'total_count': total_count,
        'total_latest_news': total_news,
        'total_headline': total_headline,
        'total_articles': total_articles,
    })


@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def category_management(request):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request,"You are not authorized to perform this action")
        return redirect('home')
    if request.user.role == CustomUser.EDITOR:
        category=Category.objects.filter(user=request.user).order_by('name')
    elif request.user.role == CustomUser.ADMIN:
        category=Category.objects.all().order_by('name')


    category_form=CategoryForm()
    LatestNews_Form=Latest_News_Form()
    Headline_Form=HeadlineForm()
    article_form=ArticlesForm()
    trending_news_form=Trending_News_Form()
    passwordChangeform=CustomPasswordChangeForm(user=request.user)
    userregister_form=UserSignUpform()
    adminform=AdminSignUpform()
    return render(request,"categorymanagement.html",{
        'category':category,
        'category_form':category_form,
        'Latest_News_Form':LatestNews_Form,
        'Headline_Form':Headline_Form,
        'adminsignupform':adminform,
        'article_form':article_form,
        'trending_news_form':trending_news_form,
        'passwordChangeform':passwordChangeform,
        'userregister_form':userregister_form,
    })



@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def delete_news(request, slug):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request, 'You are not authorized to perform this action')
        return redirect('home')
    if request.method == "POST":
        news_items = [
            Latest_News.objects.filter(slug=slug).first(),
            Trending_News.objects.filter(slug=slug).first(),
            Headlines.objects.filter(slug=slug).first(),
            Articles.objects.filter(slug=slug).first()
        ]
        news_items = [item for item in news_items if item is not None]
        if not news_items:
            messages.info(request, "News does not exist")
        else:
            for item in news_items:
                item.delete()
            messages.success(request, "News Deleted Successfully")
        return redirect('news_management')
    return redirect('news_management')


@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def update_category(request,slug):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request,"You are not authorized to perform this action")
        return redirect('home')
    category_name=Category.objects.get(slug=slug)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=category_name)
        if form.is_valid():
            category=form.save(commit=False)
            category.slug=slugify(form.cleaned_data['name'])
            category.save()
            messages.success(request,"Category Updated Succesfully")
            return redirect('category_management')
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f' {error}')
        return redirect('category_management')
    form=CategoryForm(instance=category_name)
    return redirect('category_management')


@user_passes_test(lambda u: u.role in [CustomUser.ADMIN, CustomUser.EDITOR], login_url='home')
def update_news(request, slug):
    if request.user.role not in [CustomUser.ADMIN, CustomUser.EDITOR]:
        messages.warning(request,"You are not authorized to perform this action")
        return redirect('home')
    news_item = (
        Latest_News.objects.filter(slug=slug).first() or
        Trending_News.objects.filter(slug=slug).first() or
        Headlines.objects.filter(slug=slug).first() or
        Articles.objects.filter(slug=slug).first()
    )
    
    if not news_item:
        messages.error(request, "News item does not exist")
        return redirect('news_management')
    
    category_choices = Category.objects.all().values_list('id', 'name')

    if request.method == "POST":
        form = UpdateNewsForm(request.POST, request.FILES, category_choices=category_choices)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            is_acknowledge = form.cleaned_data['is_acknowledge']

            news_item.title = title
            news_item.description = description
            news_item.content = strip_tags(description)
            news_item.slug = slugify(title)
            news_item.category_id = category
            news_item.is_acknowledge = is_acknowledge
            
            if image:
                news_item.image = image
            
            news_item.save()

            messages.success(request, "News Updated Successfully")
            return redirect('news_management')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UpdateNewsForm(
            initial={
                'title': news_item.title,
                'description': news_item.description,
                'category': news_item.category_id,
                'is_acknowledge': news_item.is_acknowledge
            },
            category_choices=category_choices
        )

    return redirect('news_management')


def delete_category(request, slug):
    if request.user.role != CustomUser.ADMIN:
        messages.warning(request,"You are not authorized to perform this action")
        return redirect('home')
    if request.method=="POST":
        try:
            category = get_object_or_404(Category, slug=slug)
            category.delete()
            messages.success(request,"Category Deleted Successfully")
            return redirect('category_management')
        except Category.DoesNotExist:
            messages.error(request,"Category Not Found")
            return redirect('category_management')
    else:
        return redirect('category_management')
    

def profile(request, user_id):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login to perform this action")
        return redirect('home')
    userdata = get_object_or_404(CustomUser,user_id=user_id)

    search_query = request.GET.get('news', '')
    categories = Category.objects.all()
    latest_news = Latest_News.objects.filter(user=userdata).order_by('-publish_date')
    trending_news = Trending_News.objects.filter(user=userdata).order_by('-publish_date')
    headlines = Headlines.objects.filter(user=userdata).order_by('-publish_date')
    articles = Articles.objects.filter(user=userdata).order_by('-publish_date')

    if search_query:
        latest_news = latest_news.filter(title__icontains=search_query)
        trending_news = trending_news.filter(title__icontains=search_query)
        headlines = headlines.filter(title__icontains=search_query)
        articles = articles.filter(title__icontains=search_query)

    news_content = list(latest_news) + list(trending_news) + list(headlines) + list (articles)
    for item in news_content:
        item.class_name = item.__class__.__name__
    total_count = len(news_content)
    total_articles = len(articles)
    total_news = len(latest_news) + len(trending_news)
    total_headlines = len(headlines)
    news_sorted = sorted(news_content, key=lambda x: x.publish_date, reverse=True)
    category_form = CategoryForm()
    latest_news_form = Latest_News_Form()
    headline_form = HeadlineForm()
    article_form = ArticlesForm()
    trending_news_form = Trending_News_Form()
    login_user_form = LoginUserForm()
    user_register_form = UserSignUpform()
    update_news_form = UpdateNewsForm()
    password_change_form = CustomPasswordChangeForm(user=request.user)
    password_reset_form = CustomPasswordResetForm(user=None)
    admin_form = AdminSignUpform()
    profileupdateform=UpdateUserForm()

    return render(request, "profile.html", {
        'category': categories,
        'latest_news': latest_news,
        'trending_news': trending_news,
        'headlines': headlines,
        'articles': articles,
        'news_sorted': news_sorted,
        'category_form': category_form,
        'Latest_News_Form': latest_news_form,
        'Headline_Form': headline_form,
        'article_form': article_form,
        'trending_news_form': trending_news_form,
        'login_user_form': login_user_form,
        'userregister_form': user_register_form,
        'adminsignupform': admin_form,
        'passwordChangeform': password_change_form,
        'password_reset_form': password_reset_form,
        'updatenewsform': update_news_form,
        'total_count':total_count,
        'total_news':total_news,
        'total_headlines':total_headlines,
        'total_articles':total_articles,
        'profileupdateform':profileupdateform,
        'userdata':userdata
    })