from django.shortcuts import render
from website.models import Category, Website
from django.contrib.auth.decorators import login_required
from website.forms import WebsiteForm
from django.shortcuts import HttpResponseRedirect, reverse
from haystack.views import SearchView


def index(request, cate="all"):
    '''
    网址分享首页
    '''
    if cate == "all":
        website = Website.objects.all().order_by('-create_date')[:10]
    else:
        cate_obj = Category.objects.get(name=cate)
        website = cate_obj.website_set.all()
    category = cate_sort(Category.objects.all())
    allcount = Website.objects.all().count()
    return render(request, 'website/index.html', {'website': website, 'category': category, 'allcount': allcount})


class WebsiteSearch(SearchView):
    template = 'website/index.html'

    def extra_context(self):
        context = super(WebsiteSearch, self).extra_context()
        website = Website.objects.all().order_by('-create_date')[:10]
        category = cate_sort(Category.objects.all())
        allcount = Website.objects.all().count()
        context['website'] = website
        context['category'] = category
        context['allcount'] = allcount
        return context


def cate_sort(category):
    '''
    对网址标签计数
    '''
    category_dict = {}
    cate_name = [c.pk for c in category]
    for c in reversed(cate_name):
        cate = Category.objects.get(pk=c)
        category_dict[cate.name] = cate.website_set.all().count()
    return category_dict


@login_required
def create(request):
    '''
    添加网址
    '''
    user = request.user
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            # form.instance.belong_id = user.id
            website = form.save(commit=False)   # 当需要添加form中没有的字段时。
            website.belong = user
            website.save()
            form.save_m2m()   # 当使用了form.save(commit=False)时，并且模型中有多对多关系，就必须使用form.save_m2m()方法。
            return HttpResponseRedirect(reverse('website:首页', args={'all'}))
    else:
        form = WebsiteForm()
    return render(request, 'website/create_website.html', {'form': form})
