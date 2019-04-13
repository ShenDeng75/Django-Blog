from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.forms import BlogForm


def index(request):
    '''
    首页，显示所有博客
    '''
    is_superuser = 0
    try:
        username = request.user
        user = User.objects.get(username=username)
        is_superuser = user.is_superuser
    except:
        pass
    blogs = Blog.objects.all().order_by('-create_date')
    tags = tags_sort(Tag.objects.all())
    return render(request, 'blog/index.html', {'is_superuser': is_superuser, 'blogs': blogs, 'tags': tags, 'allcount': blogs.count()})


def tags_sort(tags):
    '''
    对标签重新排序
    '''
    tags_dict = {}
    tags_list = [t.name for t in tags]
    a = tags_list[1]
    tags_list.append(a)
    tags_list.pop(1)
    for t in tags_list:   # 获取数量
        tag = Tag.objects.get(name=t)
        tags_dict[t] = tag.blog_set.all().count()
    return tags_dict


def category(request, tag):
    '''
    分类显示
    '''
    if tag == "all":
        blogs = Blog.objects.all()
    else:
        obj_tag = Tag.objects.get(name=tag)
        blogs = obj_tag.blog_set.all()     # 多对多查询
    tags = tags_sort(Tag.objects.all())
    allcount = Blog.objects.all().count()
    return render(request, 'blog/index.html', {'blogs': blogs, 'is_superuser': 0, 'tags': tags, 'allcount': allcount})


@login_required
def create_blog(request):
    '''
    添加博客
    '''
    user = User.objects.get(username=request.user)
    is_superuser = user.is_superuser
    if not is_superuser:   # 只有超级用户能添加
        return HttpResponseRedirect(reverse('blog:首页'))
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.instance.belong_id = user.id   # 给外键赋值。
            form.save()
            return HttpResponseRedirect(reverse('blog:首页'))
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})


def detail(request, pk, slug):
    '''
    显示博客内容
    '''
    blog = get_object_or_404(Blog, pk=pk)
    blog.visited()
    blog_path = blog.title + '.html'
    return render(request, 'blog/detail.html', {'blog': blog, 'blog_path': blog_path})
