# django

# [Django Study] Chapter 1: Introduction

## 1. Django란 무엇인가?

- **정의**: 파이썬(Python) 기반의 오픈 소스 **풀스택 웹 프레임워크**입니다.
- **철학**: *"The web framework for perfectionists with deadlines"*
- **Batteries Included**: 웹 개발에 필요한 핵심 기능(로그인, 관리자 페이지 등)이 이미 내장되어 있습니다.

---

## 2. 왜 장고(Django)를 사용하는가?

### ① 압도적인 생산성

- 웹 서비스의 공통 기능(Auth, Admin, RSS 등)을 직접 구현할 필요가 없어 비즈니스 로직에만 집중 가능합니다.
- 파이썬의 간결한 문법을 그대로 활용합니다.

### ② 강력한 보안 (Secure by Default)

- SQL Injection, XSS, CSRF 등 주요 웹 취약점에 대한 방어 코드가 기본적으로 적용되어 있습니다.

### ③ 확장성과 신뢰성

- Instagram, Spotify, Dropbox 등 글로벌 대형 서비스에서 검증된 프레임워크입니다.

---

## 3. 장고의 장단점

| 구분 | 장점 (Pros) | 단점 (Cons) |
| --- | --- | --- |
| **기능성** | 관리자 페이지(Admin) 자동 생성 | 프레임워크 자체가 무겁고 메모리 점유율이 높음 |
| **개발 경험** | 강력한 ORM으로 DB 제어가 쉬움 | 장고 특유의 규칙(Convention)을 익히는 데 시간이 걸림 |
| **생태계** | 거대한 커뮤니티와 풍부한 써드파티 앱 | 비동기 처리(Async) 지원이 다른 프레임워크 대비 늦음 |

---

## 4. 장고의 핵심: MTV 패턴

장고는 소프트웨어 디자인 패턴인 MVC를 자신들만의 방식으로 구현한 **MTV 패턴**을 사용합니다.

1. **Model (M)**: 데이터 구조 정의 및 데이터베이스 관리 (ORM)
2. **Template (T)**: 사용자에게 보여지는 화면 디자인 (HTML)
3. **View (V)**: 요청을 받고 로직을 처리하여 응답을 반환 (핵심 컨트롤러 역할)

---

## 5. 결론

장고는 **"빠르게, 안전하게, 그리고 확장 가능하게"** 웹 서비스를 만들고 싶은 개발자에게 최고의 선택지입니다. 특히 데이터 모델링이 중요한 프로젝트에서 그 진가를 발휘합니다.

# [Django Study] Chapter 2: Model (MTV의 M)

## 1. 모델(Model)의 역할

- **데이터 설계도**: 데이터베이스의 구조(Schema)를 파이썬 클래스로 정의합니다.
- **ORM (Object-Relational Mapping)**: SQL 쿼리문 없이 파이썬 코드로 데이터베이스를 조작할 수 있게 합니다.
- **데이터 무결성**: 필드 타입과 옵션을 통해 올바른 데이터만 저장되도록 보장합니다.

---

## 2. 주요 모델 필드 (Model Fields)

이미지에서 확인한 필드들을 용도별로 분류한 핵심 리스트입니다.

### ① 문자열 (String)

- `CharField`: 이름, 제목 등 길이가 제한된 짧은 문자열 (max_length 필수)
- `TextField`: 게시글 본문, 댓글 등 길이가 긴 문자열
- `SlugField`: URL에 사용되는 문자, 숫자, 하이픈(-)의 조합

### ② 숫자 및 논리 (Numeric & Boolean)

- `IntegerField`: 정수 값
- `DecimalField / FloatField`: 소수점이 포함된 실수 값
- `BooleanField`: True / False 상태 저장

### ③ 날짜 및 시간 (Date & Time)

- `DateTimeField`: 날짜와 시간 모두 저장 (`auto_now_add=True` 설정 시 작성일 자동 생성)
- `DateField`: 날짜만 저장

### ④ 특수 및 유효성 검사 (Special & Validator)

- `EmailField`: 이메일 형식 여부 확인
- `URLField`: 웹 주소 형식 여부 확인
- `FileField / ImageField`: 파일 및 이미지 업로드 경로 관리

---

## 3. 모델 정의 예시 코드

`models.py`에 작성하는 표준 구조입니다.

```python
from django.db import models

class StudyNote(models.Model):
    # 필드 정의
    title = models.CharField(max_length=200)       # 제목
    content = models.TextField()                    # 내용
    author_email = models.EmailField()              # 작성자 이메일 (Validator)
    created_at = models.DateTimeField(auto_now_add=True) # 생성일
    is_public = models.BooleanField(default=True)   # 공개 여부

    def __str__(self):
        return self.title
```

# [Django Study] Chapter 3: Template (MTV의 T) - Deep Dive

## 1. 템플릿(Template)의 개념

- **정의**: 데이터가 들어갈 자리가 비어 있는 HTML 파일입니다.
- **목적**: 데이터(Python)와 디자인(HTML)을 분리하여 협업과 유지보수를 용이하게 합니다.
- **엔진**: 장고는 기본적으로 **DTL (Django Template Language)**이라는 강력한 템플릿 엔진을 사용합니다.

---

## 2. DTL (Django Template Language) 문법

### ① 변수 (Variables)

- **형식**: `{{ variable_name }}`
- **설명**: View에서 전달된 파이썬 객체의 값을 출력합니다.
- **Dot(.) 연산자**: 객체의 속성이나 딕셔너리의 키, 리스트의 인덱스에 접근할 수 있습니다.
    - 예: `{{ user.name }}`, `{{ posts.0.title }}`

### ② 태그 (Tags)

- **형식**: `{% tag_name %}`
- **설명**: 렌더링 과정에서 복잡한 로직을 수행합니다. 반드시 닫는 태그가 필요한 경우가 많습니다.
- **주요 태그**:
    - `{% for item in list %}` ... `{% endfor %}`: 리스트 순회
    - `{% if condition %}` ... `{% else %}` ... `{% endif %}`: 조건문
    - `{% url 'path_name' %}`: 하드코딩 없이 URL 경로 생성
    - `{% csrf_token %}`: POST 요청 시 보안을 위한 토큰 생성 (필수)

### ③ 필터 (Filters)

- **형식**: `{{ value|filter_name }}`
- **설명**: 변수의 값을 화면에 표시하기 전에 변형합니다. 파이프(`|`) 기호를 사용합니다.
- **주요 필터**:
    - `|length`: 리스트나 문자열의 길이 반환
    - `|lower` / `|upper`: 대소문자 변환
    - `|truncatechars:20`: 20자까지만 보여주고 생략
    - `|default:"내용 없음"`: 값이 비어있을 때 기본값 출력

---

# [Django Study] Chapter 4: View (MTV의 V) - Deep Dive

## 1. 뷰(View)의 개념

- **비즈니스 로직의 중심**: 사용자의 요청(Request)을 받아 처리하고, 결과물(Response)을 돌려주는 '실행자'입니다.
- **중재자**: 모델(M)을 통해 데이터를 조회/저장하고, 템플릿(T)을 통해 완성된 화면을 사용자에게 보냅니다.

---

## 2. 뷰의 동작 메커니즘

사용자가 특정 페이지를 요청했을 때 발생하는 순서입니다.

1. **Request**: 웹 브라우저가 특정 URL로 접속합니다.
2. **URL Dispatching**: `urls.py`가 요청된 URL을 분석하여 알맞은 **View** 함수/클래스를 찾아냅니다.
3. **Process**: **View**는 필요한 데이터를 **Model**에 요청하거나 파이썬 로직을 수행합니다.
4. **Response**: 처리된 데이터를 **Template**에 결합하거나, JSON 데이터 혹은 리다이렉트 응답을 반환합니다.

[Image of Django request response cycle flow including URLconf, View, Model and Template]

---

## 3. 뷰의 한 가지 작성 방식

### ① 함수형 뷰 (FBV: Function Based View)

- **특징**: 파이썬 함수로 작성하며 직관적이고 이해하기 쉽습니다.
- **장점**: 코드의 흐름을 한눈에 파악할 수 있어 기초 스터디에 가장 적합합니다.

```
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, post_id):
    # 1. 데이터 조회 (Model)
    post = get_object_or_404(Post, pk=post_id)
    # 2. 로직 처리 및 화면 전달 (Template)
    return render(request, 'blog/detail.html', {'post': post})
```