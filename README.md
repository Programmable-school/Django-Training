# Django-Training

> Django + PostgreSQLでWeb開発

## 目次
- [環境構築](#環境構築)
- [Hello Worldを表示](#トレーニング)
- [ルーティング](#ルーティング)
- [リクエストメソッド](#リクエストメソッド)
- [静的ファイルの利用](#静的ファイルの利用)
- [HTMLのレンダリング](HTMLのレンダリング)
- DTLの利用
- Bootstrapの利用
- PostgreSQLの利用


## 開発環境
- Python 3.6
- Django 2.2.3

## 環境構築

djangoをインストールします。

```cmd
$ pip3 install django

$ django-admin --version
2.2.3
```

次に仮想環境へDjangoを導入します。

仮想環境は venv を用います。venv は軽量な仮想環境作成をサポートするツールです。

仮想環境用のディレクトリを作成し、仮想環境を作成します。

```cmd
$ mkdir djangoLesson
$ python3 -m venv djangoLesson
```

仮想環境が作成できたら、仮想環境を有効にするため bin/activate を実行します。

```cmd
$ cd djangoLesson
$ source bin/activate
```

仮想環境を有効化できたので、この状態でdjangoをインストールします。

```cmd
$ pip3 install django
```

以後、仮想環境からdjangoを利用する場合はあらかじめ bin/activate で仮想環境を有効化する必要があります。


次にWebアプリのプロジェクトを作成します。

```cmd
$ django-admin startproject djangoLesson
```

djangoLessonのディレクトリが生成されます。

```cmd
djangoLesson/
├── djangoLesson
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

|ファイル|説明|
|---|---|
|settings.py|アプリ全般の設定ファイルです。|
|urls.py|URLのルーティング設定を行うファイルです。|
|wsgi.py|アプリをデプロイするために必要なファイルです。|
|manage.py|アプリを起動するためのファイルです。開発者がこのファイルを編集することはありません。|


ローカルサーバーで起動します。 

```cmd
# manage.py があるディレクトリに移動する
$ cd djangoLesson

# ローカルサーバーを起動
$ python3 manage.py runserver
```

起動が成功すると、次のようなログがターミナル上に表示されます。

```cmd
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

August 16, 2019 - 23:21:27
Django version 2.2.4, using settings 'djangoLesson.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

ブラウザで http://127.0.0.1:8000/ を開くと、次の画面が表示されます。

<img src="./images/lesson0_top.png" width="50%">

環境構築はこれで完了です。

## トレーニング
Djangoフレームワークを学びます。サンプルコードを写経し実行した後、課題を進めてください。

### Hello Worldを表示

DjangoでHello Worldを表示させましょう。

djangoLesson/views.py を作成して、次のコードを実装します。

```python
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello World")
```

djangoLesson/urls.pyに次のコードを実装します。

```python
from django.contrib import admin
from django.urls import path

from . import views # 追加

urlpatterns = [
    path('', views.index), # 追加
    path('admin/', admin.site.urls),
]
```

urls.py では パス とルーティングで表示させたい view とを紐づけます。

この場合 http://127.0.0.1:8000/ と views.py で実装した index関数 が紐づきます。

index関数では HttpResponse を使って Hello World の文字列を返しているだけなので、アクセスすると画面上に Hello World が表示されます。

ブラウザで http://127.0.0.1:8000/ を開くと次の画面が表示されます。

<img src="./images/lesson1_helloWorld.png" width="50%">

### ルーティング

ページを追加する場合は、ルーティングの設定を行います。

djangoLesson/urls.py に追加したいページの パス を path() を使用して追加します。

2つのページを追加してみます。

djangoLesson/views.py に次の関数を追加します。

```python
def hoge(request):
  return HttpResponse("hoge")

def fuga(request):
  return HttpResponse("fuga")
```

djangoLesson/urls.py に hoge と fuga をルーティングへ追加します。

```python
urlpatterns = [
    path('', views.index),
    path('hoge/', views.hoge), # 追加
    path('fuga/', views.fuga), # 追加
    path('admin/', admin.site.urls),
]
```

ブラウザで http://127.0.0.1:8000/hoge/ と http://127.0.0.1:8000/fuga/ にアクセスするとページが表示されます。

##### パスごとに設定ファイルを分ける

特定のパスに対応する処理を追加することができます。「アプリケーションを追加する」と呼んでいます。

例えば http://127.0.0.1:8000/dapp/ というURLに対する処理を一括で追加することができます。

次のコマンドを入力して dapp アプリケーションを追加します。

```cmd
python3 manage.py startapp dapp
```

すると djangoLesson の同層に dapp　ディレクトリが追加されます。この中にDjangoアプリの雛形が入っています。

では、作成した dapp を動かせれるよう設定します。

dapp/views.py を次のように実装します。

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("dapp index")

def foo(request):
  return HttpResponse("dapp foo")
```

dapp/urls.py を作成して、次のように実装します。

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('foo', views.foo),
]
```

次に、djangoLesson から dapp を参照できるようにします。

djangoLesson/urls.py に dapp を追加します。

```python
from django.contrib import admin
from django.urls import path, include # include追加

from . import views

urlpatterns = [
    path('', views.index),
    path('dapp/', include('dapp.urls')), # 追加
    path('hoge/', views.hoge),
    path('fuga/', views.fuga),
    path('admin/', admin.site.urls),
]
```
http://127.0.0.1:8000/dapp/ や　http://127.0.0.1:8000/dapp/foo にアクセスできるようになります。


#### 課題 1

views.py に djangoDayo関数 実装して Django Dayo の文字列だけを表示するページを作成してください。

ブラウザで http://127.0.0.1:8000/djangoDayo/ を開いて確認できること。


### リクエストメソッド

HTTPでは同じパスに対して異なるメソッドを提供することができます。リクエストメソッドと呼ばれ、データのCRUD（作成、取得、更新、削除）操作に応じて処理を扱えることができます。

| メソッド | 用途 |
|:---|:---|
|GET | データの取得 |
|POST | データの作成 |
|PUT | データの更新 |
|DELETE | データの削除 |

requeset.method で送られてきたリクエストメソッドを判断できます。

djangoLesson/views.py に次のコードを追加します。

```python
from django.views.decorators.csrf import csrf_exempt # 追加

# 追加
@csrf_exempt
def crud(request):
  if request.method == 'POST':
    return HttpResponse('POST')
  elif request.method == 'GET':
    return HttpResponse('GET')
  elif request.method == 'PUT':
    return HttpResponse('PUT')
  elif request.method == 'DELETE':
    return HttpResponse('DELETE')
  else:
    return HttpResponse('Unknown')
```

djangoLesson/urls.py に crud のパスを追加します。

```python
urlpatterns = [
    path('', views.index),
    path('dapp/', include('dapp.urls')),
    path('hoge/', views.hoge),
    path('fuga/', views.fuga),
    path('crud/', views.crud),  # 追加
    path('admin/', admin.site.urls),
]
```

リクエストメソッド毎に実装通りの結果が返ってくるか確認します。

curl コマンドを用いて http://127.0.0.1:8000/crud/ へリクエストを送ります。

```cmd
$ curl http://127.0.0.1:8000/crud/
GET

$ curl -X GET http://127.0.0.1:8000/crud/
GET

$ curl -X POST http://127.0.0.1:8000/crud/
POST

$ curl -X DELETE http://127.0.0.1:8000/crud/
DELETE

$ curl -X PUT http://127.0.0.1:8000/crud/
PUT

$ curl -X A http://127.0.0.1:8000/crud/
Unknown
```

### 静的ファイルの利用

Webアプリケーションで画像・動画ファイル、JavaScript、CSS（スタイルシート）を配信できるようにしていきます。

djangoLesson/setting.py で基本設定を見ていきます。

django.contrib.staticfiles が設定されていることを確認してください。

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

STATIC_URL にディレクトリのパスが設定されていることを確認してください。

```python
STATIC_URL = '/static/'
```

配信するファイルを格納するディレクトリの絶対パスを設定します。

djangoLesson/setting.py の最後に次のコードを追加してください。

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

CSSを配信できるか確認します。

static ディレクトリを作成して次のCSSファイルを作成してください。

```cmd
$ mkdir static | touch ./static/style.css
$ ls
dapp            db.sqlite3      djangoLesson    manage.py       static
```

static/style.css に次のコードを追加してください。

```css
h1 {
  color: red;
}
```

djangoLesson/views.py に次のコードを追加します。

```python
def page1(request):
  return HttpResponse("""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="/static/style.css" />
      </head>
      <body>
        <h1>Page 1</h1>
      </body>
    </html>
  """)
```

djangoLesson/urls.py に page1 のパスを追加します。

```python
urlpatterns = [
    path('', views.index),
    path('dapp/', include('dapp.urls')),
    path('hoge/', views.hoge),
    path('fuga/', views.fuga),
    path('crud/', views.crud),
    path('page1/', views.page1),  # 追加
    path('admin/', admin.site.urls),
]
```

http://127.0.0.1:8000/page1/ を開くと次の画面が表示されます。

style.cssが反映されていることを確認できます。

<img src="./images/lesson4_page1.png" width="50%">

### HTMLのレンダリング



## 参考文献

[Python3 + Django2.0入門 - Pythonで作るWebアプリケーション開発入門 - その１](https://www.amazon.co.jp/gp/product/B07GNJW2QN)

[Python3 + Django2.0入門 - Pythonで作るWebアプリケーション開発入門 - その２](https://www.amazon.co.jp/gp/product/B07GNPK25J)
