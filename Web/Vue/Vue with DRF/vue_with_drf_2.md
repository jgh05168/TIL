# Vue with DRF 2

- [DRF Authentication](#DRF-Authentication)

- [Authentication with Vue](#Authentication-with-Vue)

<br>

## DRF Authentication 

[시작하기 전에]

- User 모델 관련 코드 활성화

- user ForeignKey 주석 해제

- article_list view 함수에서 게시글 생성 시 user 정보도 저장될 수 있도록

### Authentication

**: 인증, 수신된 요청을 해당 요청의 사용자 또는 자격 증명과 연결하는 매커니즘**

- if, 유효한 인증 자격 증명이 없는 경우

    - HTTP 401 Unauthorized

#### Permission

**: 권한, 요청에 대한 접근 허용 또는 거부 여부를 결정**

- if, 권한이 없는 경우

    - HTTP 403 Forbidden (Permission Denied)

    - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있다.

인증이 먼저 진행되며 수신 요청을 해당 요청의 사용자 또는 해당 요청이 서명된 토큰과 같은 일련의 자격 증명과 연결

다음 권한 및 제한 정책은 인증이 완료된 해당 자격 증명을 사용하여 요청 허용 여부를 결정

#### 인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 <U>자격 증명만 식별한다는 점에 유의</U>.

### 인증 체계 설정 방법

1. 전역 설정

    - settings.py에 `DEFAULT_AUTHENTICATION_CLASSES`를 사용.

2. View 함수 별 설정

    - `authentication_classes 데코레이터` 사용

    1. BasicAuthentication

    2. [<span style="color: red;">TokenAuthentication</span>](#TokenAuthentication)

        - 간단한 token 기반 HTTP 인즈 체계

        - 기본 데스크톱 및 모바일 클라이언트와 같은 클라이언트-서버 설정에 적합

        -> 서버가 사용자에게 <U>토큰을 발급</U>하여 사용자는 매 요청마다 <U>발급받은 토큰을 다음 요청과 함께 보내</U> 인증 과정을 거침

    3. SessionAuthentication

    4. RemoteUserAuthentication

### TokenAuthentication

1. 인증 클래스 설정

    - 기본적으로 모든 view 함수가 토큰 기반 인증이 진행될 수 있도록 설정하는 것
    
    ```python
    # settings.py

    REST_FRAMEWORK = {
        # Authentication
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ],
    }
    ```

2. INSTALLED_APPS 추가

    ```python 
    # settings.py
    INSTALLED_APPS = [
        ... ,
        'rest_framework.authtoken',
        ...
    ]
    ```

3. Migrate 진행

4. 토큰 생성 코드 작성

    - `accounts/signals.py`

    - 모든 사용자가 자동으로 생성된 코튼을 가지도록 하는 역할

### Dj-Rest-Auth 라이브러리

- 인증 특화 라이브러리

    - 회원가입, 인증(SNS 인증 포함), 비밀번호 재설정 등 다양한 인증 관련 기능을 제공


- Registration(등록) 기능 추가 설정 필요

    1. 패키지 추가 설치

    2. 추가 App 등록

    3. 추가 URL 등록

    4. Migration

### Token 발급 및 활용

- 회원가입 후 로그인 진행하면 토큰 생성

-> <span style="color: red;">생성된 토큰을 Vue에서 별도로 저장하여 매 요청마다 함께 보내야 인증됨</span>

#### 토큰 활용

- Postman의 Headers에 발급받은 Token 작성 후 요청 성공 확인

    - Key: 'Authorization'

    - Value: `Token "키 값"` 

        - 위 양식을 꼭 지켜줘야한다.

    #### 클라이언트가 Token으로 인증 받는 방법

    1. `Authorization` HTTP Header에 포함

    2. 키 앞에는 문자열 `Token`이 와야 하며 `공백으로 두 문자열을 구분해야 함`

[정리]

#### 발급 받은 Token을 인증이 필요한 요청마다 함께 보내야 함

### 권한 정책 설정

1. 전역 설정

    - `DEFAULT_PERMISSION_CLASSES` 사용

2. View 함수 별 설정

    - `permission_classes` 데코레이터를 사용

#### IsAuthenticated 권한

- 인증되지 않은 사용자에 대한 권한을 거부하고 그렇지 않은 경우 권한을 허용

- 등록된 사용자만 API에 액세스 할 수 있도록 하려는 경우에 적합


<br>

## Authentication with Vue

[시작하기 전에]

- 정상 작동하던 게시글 조회 불가능

- 401 status code 확인

- token을 보내지 않고 있기 때문이라 수정 필요

1. 회원가입

2. 로그인

    - 토큰 정보 저장

### 토큰이 필요한 요청

1. 게시글 전체 목록 조회

2. 게시글 작성

### 사용자의 인증(로그인) 여부에 따른 추가 기능 구현

1. 인증되지 않은 사용자 

    -> 메인 페이지 접근 제한

    - 전역 네비게이션 가드 `beforeEach`를 활용해 다른 주소에서 메인 페이지로 이동 시 인증 되지 않은 사용자라면 로그인 페이지로 이동시키기

    ```js
    // index.js

    import { useCounterStore } from '@/stores/counter'

    router.beforeEach((to, from) => {
    const store = useCounterStore()

    if (to.name === 'ArticleView' && !store.isLogin) {
        window.alert('Login Required')
        return { name: 'LogInView' }
    }

    })
    ```

2. 인증 된 사용자

    -> 회원가입 및 로그인 페이지에 접근 제한

    - 다른 주소에서 회원가입 또는 로그인 페이지로 이동 시 이미 인증 된 사용자라면 메인 페이지로 이동시키기

    ```js
    // index.js

    import { useCounterStore } from '@/stores/counter'

    router.beforeEach((to, from) => {
    const store = useCounterStore()

    if ((to.name === 'SignUpView' || to.name === 'LoginView') && store.isLogin) {
        window.alert('Already Logined')
        return { name: 'ArticleView'}
    }
    })
    ```

