from django.shortcuts import render


# Create your views here.
def index(request):
    user = request.user
    menus = [
        {'title': "我的博客", 'url': "blog/", 'content': "学习总结，记录Bug", 'img': "images/blog.jpg"},
        {'title': "网址分享", 'url': "website/", 'content': "分享一些免费实用的网站", 'img': "images/webshare.jpg"},
        {'title': "实用脚本", 'url': "#", 'content': "用脚本解放双手", 'img': "images/tools.jpg"},
        {'title': "我的简历", 'url': "#", 'content': "我的学习历程", 'img': "images/resume.jpg"},
    ]
    return render(request, 'home/index.html', {'user': user, 'menus': menus})
