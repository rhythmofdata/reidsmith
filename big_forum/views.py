from django.shortcuts import render, get_object_or_404, redirect
from .models import  Category, BF_Post, Author,Comment, Reply
from .utils import update_views
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden



# Create your views here.
User = get_user_model()


def bigForumHome(request):
    forums = Category.objects.all()
    num_posts = BF_Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    
    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories
    }
    return render(request,"big_forum_home.html", context)





def bigForumDetail(request,slug):
    post = get_object_or_404(BF_Post,slug=slug)
    # Ensure there is a logged-in user before accessing request.user
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to perform this action.")
    
    # Use get_object_or_404 to retrieve the user or raise a 404 if not found
    author = get_object_or_404(User, username=request.user.username)

    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user= author, content=comment)
        post.comments.add(new_comment.id)


    context = {
        "post":post
    }
    update_views(request,post)
    return render(request,"big_forum_detail.html", context)



def bigForumPosts(request, slug):
    category = get_object_or_404(Category,slug=slug)
    posts = BF_Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "forum": category,
        "title": "OZONE: Posts"
    }

    return render(request, "big_forum_posts.html", context)




@login_required
def create_post(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.Author
            post.author = request.POST.get('Author')  
            post.save()
            #form.save_m2m()
            return redirect('big_forum_home')  # Redirect to the forum index or another page after creating a post
    
    else:
        form = PostForm()
    context.update({
        "form":form,
        "title": "Create New Post"})

    return render(request,"big_forum_create_post.html",context)







