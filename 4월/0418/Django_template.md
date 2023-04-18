# Django - Django Template

# 1. Template System

## django template system
> 데이터 **표현**을 제어하면서, **표현**과 관련된 로직을 담당

- ### HTML 의 특정 부분을 변수 값에 따라 바꾸고 싶다면?

```python
def index(request):
    context = {
        'name': 'Sophia',
    }
    return render(request, 'articles/index.html', context)
```

```html
<body>
    <h1>Hello, {{ name }}</h1>
</body>
```

## Django Template Language (DTL)
> Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

## DTL Syntax

1. Variable
2. Filters
3. Tags
4. Comments

---
### 1-1. Variable

- view 함수에서 render 함수의 세번째 인자로 딕셔너리 타입으로 넘겨 받을 수 있음
- 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
- dot(.)를 사용하여 변수 속성에 접근할 수 있음

```html
{{ variable }}
```


### 1-2. Filters

- 표시할 변수를 수정할 때 사용
- chained가 가능하며 일부 필터는 인자를 받기도 함
``` {{ name|truncatewords:30 }} ```
- 약 60개의 built-in template filters를 제공

```html
{{ variable | filter }}
```


### 1-3. Tags

- 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요 ``` {% if %} {% endif %} ```
- 약 24개의 built-in template tags를 제공
```html
{% tag %}
```


### 1-4. Comments

- DTL에서의 주석 표현

```html
<h1>Hello, {# name #}</h1>
```

```html
  {% comment %} 
    {% if name == 'Sophia' %}
    {% endif %} 
  {% endcomment %}
```

---

# 2. 템플릿 상속

### 만약 모든 템플릿에 bootstrap을 적용하려면? 
> 모든 템플릿에 CDN을 작성해야 할까?

## 템플릿 상속 (template inheritance)
> 페이지의 공통요소를 포함하고,  
하위 템플릿이 재정의 할 수 있는 공간을 정의하는  
기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축

- ### skeleton 역할 템플릿 작성

```html
<!-- articles/base.html -->
<!doctype html>
<html lang="en">
<head>
...
{% comment %} bootstrap CDN 생략 {% endcomment %}
</head>
<body>
  {% block content %}
  {% endblock content %}
{% comment %} CDN 생략 {% endcomment %}
</body>
</html>
```

- ### 기존 template의 변화

```html
<!-- articles/index.html -->
{% extends 'articles/base.html' %}

{% block style %}
  <style>
    h1 { 
      color: crimson;
    }
  </style>
{% endblock style %}

{% block content %}
  <h1>Hello, {{ name }}!!</h1>
{% endblock content %}
```

---

### 2-1. 'extends' tag

```html
{% extends 'path' %}
```

> 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
 - 반드시 템플릿 최상단에 작성되어야 함 (2개 이상 사용 불가)


### 2-2. 'block' tag

```html
{% block name %}{% endblock name %}
```

> 하위 템플릿에서 재정의(overridden)할 수 있는 블록을 정의
 - 하위 템플릿이 작성할 수 있는 공간을 지정

---

# 3. 요청과 응답 with HTML form

## 데이터를 보내고 가져오기
(sending and Retrieving form data)

> HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기  

> HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법

```html
<form action="#" method="GET">
    <div>
        <label for="name">아이디: </label>
        <input type="text" id="name">
    </div>
    <div>
        <label for="password">패스워드: </label>
        <input type="password" name="password" id="password">
    </div>
    <input type="submit" value="로그인">
</form>
```

---

## 3-1. 'form' element

> 사용자로부터 할당된 데이터를 서버로 전송  

- 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 제공


### **'action' & 'method'**

> form의 핵심 속성 2가지  

"데이터를 어디(**action**)로 어떤 방식(**method**)으로 보낼지"

- action
    - 입력 데이터가 전송될 URL을 지정 (목적지)
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

- method
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP request methods (GET, POST)를 지정


## 3-2. 'input' element

> 사용자의 데이터를 입력 받을 수 있는 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음

### **'name'**

> input의 핵심 속성

- 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근할 수 있음


## 3-3. fake Naver 실습

```html
<!-- articles/search.html -->
{% extends 'articles/base.html' %}

{% block content %}
  <h1>Form 실습</h1>
  <form action="https://search.naver.com/search.naver" method="GET">
    <label for="message">검색어 : </label>
    <input type="text" name="query" id="message">
    <input type="submit">
  </form>
{% endblock content %}
```


## 3-4. Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 텅해 넘기는 방법
- 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며, 기본 URL과 물음표(?)로 구분됨
- 예시 
    - http://host:port/path?**key=value&key=value**



---

# 4. 요청과 응답 활용

## 사용자 입력 데이터를 받아 그대로 출력하는 서비스 제작하기

### 4-1. view 함수는 몇 개가 필요할까?

- ### throw 작성

```python
# urls.py
urlpatterns = [
    path('throw/', views.throw),
]
```

```python
# views.py
def throw(request):
    return render(request, 'articles/throw.html')
```

```html
<!-- articles/throw.html -->
{% extends 'articles/base.html' %}

{% block content %}
  <h1>Throw</h1>
  <form action="/catch/" method="GET">
    <input type="text" name="message">
    <input type="submit">
  </form>
{% endblock content %}
```

- ### catch 작성

```python
# urls.py
urlpatterns = [
    path('catch/', views.catch),
]
```

```python
# views.py
def catch(request):
    ???
    return render(request, 'articles/catch.html')
```

```html
<!-- articles/catch.html -->
{% extends 'articles/base.html' %}

{% block content %}
  <h1>Catch</h1>
  <h1>{{ ??? }}를 받았습니다!</h1>
{% endblock content %}
```

### 4-2. form 데이터는 어디에 들어 있을까?

> 모든 요청 데이터는 **HTTP request** 객체에 들어 있음  
(view 함수의 첫번째 인자)

- ### request 객체 살펴보기

```python
def catch(request):
    print(request)
    print(type(request)) 
    print(dir(request))
    print(request.GET)
    print(request.GET.get('message'))

    return render(request, 'articles/catch.html')
```
↓
```python
# dir() 내장함수를 써서 해당 객체가 어떤 변수와 메서드를 가지고 있는지 조회 후 GET 메서드를 사용해보기
request.GET
# 출력결과 (딕셔너리 형태로 출력됨)
<QueryDict: {'message': ['안녕!']}>


# 딕셔너리의 get 메서드를 사용해 키 값 조회
request.GET.get('message')
# 출력 결과 (키 값 출력)
안녕!
```


### 4-3. catch 작성 마무리

```python
# urls.py
urlpatterns = [
    path('catch/', views.catch),
]
```

```python
# views.py
def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)
```

```html
<!-- articles/catch.html -->
{% extends 'articles/base.html' %}

{% block content %}
  <h1>Catch</h1>
  <h1>{{ message }}를 받았습니다!</h1>
{% endblock content %}
```

---

# 5. 참고

## 5-1. 추가 템플릿 경로 지정
1. BASE_DIR 지정
```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

↓

2. base.html의 새로운 템플릿 경로 생성 
```  
최상단에 templates폴더 만든 후, 그안에 base.html
```

↓

3. extends 경로 수정
```html
{% extends 'base.html' %}
```

### **BASE_DIR**
- settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정 해놓은 변수

```python
#  settings.py
BASE_DIR = Path(__file__).resolve().parent.parent
```
- [참고/python의 객체 지향 파일 시스템 경로](https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib)



## 5-2. DTL 주의사항

- Python처럼 일부 프로그래밍 구조(if, for 등)을 사용할 수 있지만  
명칭을 그렇게 설계했을 뿐이지 Python 코드로 실행되는 것이 아니며  
Python과 아무런 관련이 없음

- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심할 것
    - 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리



## 5-3. DTL 학습

- 공식 문서를 참고해 다양한 태그와 필터 사용해복
    - [공식문서](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/)