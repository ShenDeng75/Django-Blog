from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from author.forms import ProfileForm
from author.models import Author


@login_required
def profile(request):
    '''
    登录成功后
    '''
    user = request.user
    author = get_object_or_404(Author, user=user)
    if author.nick.strip() == "":   # 如果没有完善信息
        return HttpResponseRedirect(reverse('author:修改信息'))
    return HttpResponseRedirect(reverse('home:首页'))


@login_required
def profile_detail(request):
    '''
    显示个人信息页
    '''
    user = request.user
    try:
        author = Author.objects.get(user=user)
    except Exception:
        request.session.flush()
        return HttpResponseRedirect(reverse('home:首页'))   # 如果session失效
    if author.nick.strip() == "":
        return HttpResponseRedirect(reverse('author:修改信息'))
    return render(request, 'author/profile_detail.html', {'user': user})


@login_required
def profile_update(request):
    '''
    完善和修改信息
    '''
    user = request.user
    author = get_object_or_404(Author, user=user)
    status = "修改信息"
    if author.nick == "":
        status = "完善信息"
    if request.method == "POST":
        form = ProfileForm(request.POST, request=request)
        if form.is_valid():
            author.nick = form.cleaned_data['nick']
            author.tel = form.cleaned_data['tel']
            author.save()
            if status == "完善信息":
                return HttpResponseRedirect(reverse('home:首页'))
            return HttpResponseRedirect(reverse('author:显示个人信息'))
    else:
        form = ProfileForm(request=request)
    return render(request, 'author/profile_update.html', {'form': form, 'author': author, 'status': status})
