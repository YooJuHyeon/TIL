# Django - django URLs

# 1. URL dispatcher

> URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

---

# 2. 변수와 URL

### 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면   
### 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까?

```python
urlpatterns = [
    path('articles/1/', ...),
    path('articles/2/', ...),
    path('articles/3/', ...),
    path('articles/4/', ...),
    path('articles/5/', ...),
    ...,
]
```

##  Variable Routing

> URL 일부에 변수를 포함시키는 것  
  (변수는 view 함수의 인자로 전달 할 수 있음)


## Variable routing 작성법

- **<path_converter:variable_name>**

```python
urlpatterns = [
    path('articles/<int:num>/', views.hello),
    path('hello/<str:name>/', views.greeting),
]
```


## Path converters

> URL 변수의 타입을 지정  
(str, int 등 5가지 타입 지원)


## Variable routing 실습

```python
# urls.py
urlpatterns = [
    path('articles/<int:num>/', views.detail),
]
```

```python
# views.py
def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)
```

```html
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Detail</h1>
  <h3>지금은 {{ num }}번 글입니다.</h3>
{% endblock content %}
```

---

# 3. App의 URL

## App URL mapping

> 각 앱에 URL을 정의하는 것
- 프로젝트와 각각의 앱이 URL을 나누어 관리하여 주소관리를 편하게 하기 위함

```python
# firstpjt/urls.py

from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('<int:num>/', views.detail),
    path('hello/<str:name>/', views.greeting),
]
```

```python
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
]
```

## include()

> 다른 URL들을 참조할 수 있도록 돕는 함수
- URL의 그 시점까지 일치하는 부분을 잘라내고,   
남은 문자열 부분을 후속 처리를 위해 include된 URL로 전달

---

# 4. URL 이름 지정

```python
# firstpjt/urls.py

path('articles/', include('articles.urls')),
```

```python
# articles/urls.py

path('index/', views.index),
```
- 기존 'articles/' 주소가 'articles/index/'로 변경됨  
- 기존에 articles/ 주소를 사용했던 모든 위치를 찾아 변경해야 함

## Naming URL patterns

> URL에 이름을 지정하는 것
- path 함수의 name 인자를 정의해서 사용


## name 인자 작성

```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('articles/<int:num>/', views.detail, name='detail'),

]
```

```python
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('hello/<str:name>/', views.greeting, name='greeting'),
]
```

## URL 표기 변화

> herf 속성 값 뿐만 아니라 form의 action 속성처럼 url을 작성하는 모든 위치에서 변경

```html
<!-- articles/index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Hello, {{ name }}!!</h1>
  <a href="/dinner/">dinner</a>
  <a href="/search/">search</a>
  <a href="/throw/">throw</a>
{% endblock content %}
```
↓  ↓  ↓
```html
<!-- articles/index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Hello, {{ name }}!!</h1>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'search' %}">search</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock content %}
```

## 'url' tag

> 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

```python
{% url 'url-name' arg1 arg2 %}
```

---

# 5. URL Namespace

## URL 이름 지정 후 남은 문제

> articles 앱의 url 이름과 pages 앱의 url이름이 같음  

> 단순히 이름만으로는 분리가 어려운 상황

```python
# articles/urls.py

path('index/', views.index, name='index'),
```

```python
# pages/urls.py

path('index/', views.index, name='index'),
```


## app_name 속성 지정

> url 이름 + app 이름표 붙이기
```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
]
```

```python
# pages/urls.py

app_name = 'pages'
urlpatterns = [
    ...,
]
```


## URL tag의 변화

```python
{% url 'index' %}
```
↓   ↓   ↓   
```python
{% url 'articles:index' %}
```

---

# 6. 참고

## Trailing Slashes

- django는 URL 끝에 '/'가 없다면 자동으로 붙임
- django의 url 설계 철학
    - "기술적 측면에서, foo.com/bar와 foo.com/bar/는 서로 다른 URL이다."
- 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이 두 주소를 서로 다른 페이지로 봄
- 그래서 django는 검색 엔진이 혼동하지 않게 하기 위해 사용
- 그러나 모든 프레임워크가 이렇게 작동하는 것은 아님