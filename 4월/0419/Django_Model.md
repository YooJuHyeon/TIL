# Django - Django Model
---
# 1. Model

## 1-1. django Model

> DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공

- 테이블 구조를 설계하는 **'청사진(blueprint)'**
---

## 1-2. model 클래스 작성

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```
---

## 1-3. model 클래스 이해하기

- ### 모델 클래스 == 테이블 스키마
    - id 필드는 자동 생성

- ### django.db.models 모듈의 Model이라는 부모 클래스를 상속받아 작성 **(models.Model)**

- ### model 기능에 관련된 모든 설정이 담긴 클래스
    - https://github.com/django/django/blob/main/django/db/models/base.py
    - 개발자는 테이블 구조를 어떻게 설계할 지에 대한 코드만 작성하도록 하기 위함

- ###  클래스 변수명 **(title, content,...)**
    - 테이블의 각 "필드 이름"

-  ### model Field 클래스 **(CharField, TextField,...)**
    - 테이블 필드의 "데이터 타입"
    - https://docs.djangoproject.com/en/3.2/ref/models/fields/

-  ### model Field 클래스의 키워드 인자 (필드 옵션)
    - 테이블 필드의 "제약조건" 관련 설정
    - https://docs.djangoproject.com/en/3.2/ref/models/fields/

---
---

# 2. Migrations

## Migrations

> model 클래스의 변경사항 (필드 생성, 추가 수정 등)을 DB에 최종 반영하는 방법

---
## 2-1. Migrations 과정

```
model class(설계도 초안)
```

**↓ makemigrations ↓**

```
migration 파일 (최종 설계도)
```

**↓ migrate ↓**

```
db.sqlite3
```
---

## 2-2. Migrations 핵심 명령어

```python
$ python manage.py makemigrations
```
> model class를 기반으로 설계도 (migration) 작성  


```python
$ python manage.py migrate
```
> 만들어진 설계도를 DB에 전달하여 반영
---

## 2-3. 추가 모델 필드 작성

이미 생성된 테이블에 필드를 추가해야 한다면?

> model class에 변경사항이 생겼다면,  
반드시 새로운 설계도를 생성하고,  
이를 DB에 반영해야 한다.

1. model class 작성 및 수정
2. makemigrations
3. migrate

---
## 2-4. model Field 클래스

### CharField()
> 길이의 제한이 있는 문자열을 넣을 때 사용
- 필드의 최대 길이를 결정하는 max_length는 필수 인자


### TextField()
> 글자의 수가 많을 때 사용


### DateTimeField()
> 날짜와 시간을 넣을 때 사용
- DateTimeField의 선택 인자
    - auto_mow : 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
    - auto_now_add : 데이터가 처음 생성될 때만 자동으로 현재 날짜 시간을 저장

---
---

# 3. Admin site

## Automatic admin interface

> django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
- 데이터 관련 테스트 및 확인을 하기에 매우 유용

---

## 3-1. admin 계정 생성

```
$ python manage.py createsuperuser
```

- email은 선택사항이기 때문에 입력하지 않고 진행 가능
- 비밀번호 생성 시 보안상 터미널에 출력되지 않으니 무시하고 입력을 이어가도록 함

---

## 3-2. DB에 생성된 admin 계정 확인

> db.sqlite3 > auth_user 에서 확인

---

## 3-3. admin에 모델 클래스 등록

> admin.py에 등록하지 않으면 admin site에서 확인 할 수 없음

```python
# articles/admin.py

from django.contrib import admin
# 명시적 상대경로
from .models import Article

# 암기 꿀팁 : "admin site 에 등록(register) 하겠다"
admin.site.register(Article)
```
---

## 3-4. 서버 로그인 후 등록된 모델 클래스 확인

---

## 3-5. 서버에서 데이터 CRUD 테스트 후, 실제 테이블에 저장되었다는 것도 확인

---
---

# 4. 참고

## 4-1. 데이터베이스 초기화

1. migration 파일 삭제
2. db.sqlite3 파일 삭제
- migrations 폴더를 지우지 않도록 주의!

---

## 4-2. Migrations 기타 명령어

```
$ python manage.py showmigrations
```
- migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
- [X] 표시가 있으면 migrate가 완료되었음을 의미

```
$ python manage.py sqlmigrate articles 0001
```
- 해당 migrations 파일이 SQL 문으로 어떻게 해석되어 DB에 전달되는지 확인하는 용도

---

## 4-3. 첫 migrate 시 출력 내용이 많은 이유는?

> 기본적으로 Django 프로젝트가 동작하기 위해 작성되어 있는  
기본 내장 app들에 대한 migration 파일들이 함께 migrate 되기 때문