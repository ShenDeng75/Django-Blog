"""
Django settings for shendeng project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目根目录的绝对路径


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k6@a+7l2-xm=s6dreh^41eo13ogx#)25&e1!#tx4x0+f+!07w8'    # 加密盐

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["www.shendeng520.top", "127.0.0.1"]   # 允许的域名，防止攻击


# Application definition
# ***注册app
INSTALLED_APPS = [
    # 框架app
    'django.contrib.admin',   # 强大的后台管理。
    'django.contrib.auth',    # 用户，权限，组。
    'django.contrib.contenttypes',
    'django.contrib.sessions',   # session处理。
    'django.contrib.messages',
    # 'django.contrib.staticfiles',   # 静态文件处理。  # 会默认在该app下的static文件夹中寻找静态文件。
    # 第三方app
    'django.contrib.sites',
    'allauth',  # allauth对于django.contrib.sites有依赖。
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',   # 需要的第三方providers。
    'widget_tweaks',   # 可以给前端表单添加类，用来美化界面。
    'ckeditor',   # 富文本编辑器
    'ckeditor_uploader',   # 文件上传
    'haystack',    # 全文搜索
    # 自己的app
    'author',
    'blog',
    'home',
    'website',
]
SITE_ID = 1   # 用了django.contrib.sites要设置SITE_ID。

# ***使用了第三方登录
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'   # 指定登录方式。用户名或email
ACCOUNT_EMAIL_REQUIRED = True      # 用户必须填邮箱。
LOGIN_REDIRECT_URL = '/author/profile/'   # 登录成功后跳转的连接。
ACCOUNT_SIGNUP_FORM_CLASS = 'author.forms.SignupForm'   # 使用自定义的注册表单。必须加这一句，否者Author不会与User一起保存到数据库。

AUTHENTICATION_BACKENDS = (   # 使用的后端。用来兼容不同数据库。
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 当没有登录而访问需要登录的连接时跳转的连接。也可以在login_required中设置。
LOGIN_URL = "/account/login/"

# ***邮箱设定
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465    # 最好用465，因为在部署时有些服务器会禁用25端口。
EMAIL_HOST_USER = '3255803596@qq.com'  # 你的 QQ 账号和授权码。
EMAIL_HOST_PASSWORD = 'mlykcfxqbmcddbgb'
EMAIL_USE_SSL = True  # 这里必须是 SSL，否则部署后发送不成功。
DEFAULT_FROM_EMAIL = '平凡的神灯<3255803596@qq.com>'

# ***富文本编辑器设置
# 如果要让富文本编辑器在admin外显示，需要更改/
# site-packages/ckeditor_uploader/urls.py中的内容/
# 把staff_member_required 改为login_required
CKEDITOR_UPLOAD_PATH = 'upload/'    # 保存上传文件的文件夹；位于media文件夹中
CKEDITOR_JQUERY_URL = 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'    # python图形处理库。依赖库
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_CONFIGS = {
           'default': {
               'toolbar': (['Source', '-',  'Preview', '-', ],   # 设置工具栏
                           ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', ],
                           ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat', '-',
                            "CodeSnippet", 'Subscript', 'Superscript'],
                           ['NumberedList', 'BulletedList', '-', 'Blockquote'],
                           ['Link', 'Unlink', ],
                           ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', ],
                           ['Format', 'Font', 'FontSize', 'TextColor', 'BGColor', ],
                           ['Bold', 'Italic', 'Underline', 'Strike', ],
                           ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                           ),
               'extraPlugins': 'codesnippet',   # 插入代码/
               'width': 'auto',         # 还需要在static/ckeditor/ckeditor/config.js中添加config.extraPlugins="codesnippet"
               'height': 400,
               'allowedContent': True,   # 禁止ckeditor格式化自己插入的HTML源码。
           }
}

# ***全文搜索设置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'website.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 设置每页显示的数目，默认为20，可以自己修改
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
# 自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# ***中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shendeng.urls'   # 主路由文件

# ***模板文件设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',    # 用项目中的templates来覆盖allauth中的templates
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'blog_files')],  # blog_files用来找到博客的html文件
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'shendeng.contexts.lang',  # 全局模板变量。
            ],
        },
    },
]

WSGI_APPLICATION = 'shendeng.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# ***数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shendeng',
        'USER': 'root',
        'PASSWORD': 'shendeng75',   # @ShenDeng75
        'HOST': 'localhost',
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'   # 设置时区

DATE_FORMAT = 'Y-m-d'   # 设置时间显示格式，会被下面的USE_I18N覆盖。
DATETIME_FORMAT = 'Y-m-d H:i:s'

USE_I18N = True    # 使用本地时间显示格式

USE_L10N = True
# 如果TIME_ZONE = 'UTC'则需要设置以下参数。但是最好设置本地时区。
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'  # 静态文件
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'   # 媒体文件
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
