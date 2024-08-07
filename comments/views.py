from django.shortcuts import redirect, get_object_or_404
from .forms import CommentsForm, ReplyForm
from news.models import Latest_News, Trending_News, Articles, Headlines
from django.contrib import messages
from .models import Comments, Reply
# Create your views here.


def post_comments(request, slug):
    if not request.user.is_authenticated:
        messages.info(request,"You do not have permission to perform this action")
        return redirect('home')
    latest_news = Latest_News.objects.filter(slug=slug).first()
    trending_news = Trending_News.objects.filter(slug=slug).first()
    headlines = Headlines.objects.filter(slug=slug).first()
    articles = Articles.objects.filter(slug=slug).first()

    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            if articles:
                comment.articles = articles
            if latest_news:
                comment.latest_news = latest_news
            if headlines:
                comment.headlines = headlines
            if trending_news:
                comment.trending_news = trending_news
            comment.save()
            messages.success(request, "Comment posted successfully.")
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    return redirect('home')


def post_reply(request, slug, id):
    if not request.user.is_authenticated:
        messages.info(request,"You do not have permission to perform this action")
        return redirect('home')
    latest_news = Latest_News.objects.filter(slug=slug).first()
    trending_news = Trending_News.objects.filter(slug=slug).first()
    headlines = Headlines.objects.filter(slug=slug).first()
    articles = Articles.objects.filter(slug=slug).first()
    comment = comment = get_object_or_404(Comments, id=id)

    if request.method=="POST":
        form=ReplyForm(request.POST)
        if form.is_valid():
            likes_form=form.save(commit=False)
            likes_form.user=request.user
            likes_form.comment = comment
            if latest_news:
                likes_form.latest_news = latest_news
            if trending_news:
                likes_form.trending_news = trending_news
            if headlines:
                likes_form.headlines = headlines
            if articles:
                likes_form.articles = articles
            likes_form.save()
            messages.success(request,"Posted Successfully")
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        form=ReplyForm()
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    

def delete_comment(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, "You do not have permission to perform this action")
        return redirect('home')

    comment = get_object_or_404(Comments, id=id)

    if request.user != comment.user:
        messages.warning(request, "You do not have permission to perform this action")
        return redirect('home')
    comment.delete()
    messages.success(request, "Deleted successfully")
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def delete_reply(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, "You do not have permission to perform this action")
        return redirect('home')

    reply = get_object_or_404(Reply, id=id)

    if request.user != reply.user:
        messages.warning(request, "You do not have permission to perform this action")
        return redirect('home')
    reply.delete()
    messages.success(request, "Deleted successfully")
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def edit_comments(request, id, slug):
    if not request.user.is_authenticated:
        messages.warning(request,"You do not have permission to perform this action")
        return redirect('home')
    
    comment = get_object_or_404(Comments, id=id)
    latest_news = Latest_News.objects.filter(slug=slug).first()
    trending_news = Trending_News.objects.filter(slug=slug).first()
    headlines = Headlines.objects.filter(slug=slug).first()
    articles = Articles.objects.filter(slug=slug).first()

    if request.user != comment.user:
        messages.warning(request,"You do not have permission to perform this action")
        return redirect('home')
    
    if request.method=="POST":
        comment_name = request.POST['comment_name']
        comment.user=request.user
        comment.text=comment_name
        if latest_news:
            comment.latest_news = latest_news
        if trending_news:
            comment.trending_news = trending_news
        if headlines:
            comment.headlines = headlines
        if articles:
            comment.articles = articles
        comment.save()
        messages.success(request,"Updated Successfully")
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    return redirect(request.META.get('HTTP_REFERER', 'home'))



def update_reply(request, id,slug):
    if not request.user.is_authenticated:
        messages.warning(request,"You do not have permission to perform this action")
        return redirect('home')
    try:
        reply = get_object_or_404(Reply, id=id)
    except Reply.DoesNotExist:
        messages.error(request,"Not Found")
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    latest_news = Latest_News.objects.filter(slug=slug).first()
    trending_news = Trending_News.objects.filter(slug=slug).first()
    headlines = Headlines.objects.filter(slug=slug).first()
    articles = Articles.objects.filter(slug=slug).first()

    if request.user != reply.user:
        messages.warning(request,"You do not have permission to perform this action")
        return redirect('home')

    if request.method=="POST":
        name = request.POST['reply_name']
        reply.text=name
        reply.user=request.user
        if latest_news:
            reply.latest_news = latest_news
        if trending_news:
            reply.trending_news = trending_news
        if headlines:
            reply.headlines = headlines
        if articles:
            reply.articles = articles
        reply.save()
        messages.success(request,"Updated Successfully")
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    return redirect(request.META.get('HTTP_REFERER', 'home'))