# Router

- [Routing](#Routing)

- [Vue Router](#Vue-Router)

- [Navigation Guard](#Navigation-Guard)

## Routing

: 네트워크에서 경로를 선택하는 프로세스

-> 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술

- CSR / SPA에서의 Routing

    - SPA에서 routing은 브라우저의 클라이언트 측에서 수행

    - 클라이언트 측 JS가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드 하지 않음

    - 페이지는 1개이지만, 링크에 따라 여러 컴포넌트를 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 함

<br>

## Vue Router

: Vue 공식 라우터

`Vite로 프로젝트 생성 시 Router 추가`

### Vue 프로젝트 구조 변화

1. App.vue 코드 변화

2. router 폴더 생성

3. views 폴더 생성

- RouterLink

    - 페이지를 다시 로드 하지 않고 URL을 변경하고 URL 생성 및 관련 로직을 처리

    - HTML의 a태그를 렌더링

    ```vue
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    ```

- RouterView

    - URL에 해당하는 컴포넌트를 표시
    - 어디에나 배치하여 레이아웃에 맞출 수 있음

    ```vue
    <RouterView />
    ```

- router/index.js

    - 라우팅에 관련된 정보 및 설정이 작성되는 곳

    - router에 URL과 컴포넌트를 매핑

- views

    - RouterView 위치에 렌더링 할 컴포넌트를 배치

    - 기존 components 폴더와 기능적으로 다른 것은 없으며 단순 분류의 의미로 구성됨

    **-> 일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장**


### Basic Routing

[라우팅 기본]

1. index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)

2. RouterLink의 `to` 속성으로 index.js에서 정의한 주소 속성 값(path)을 사용

### Named Routes

: 경로에 이름을 지정하는 라우팅

- 장점

    - 하드 코딩 된 URL을 사용하지 않아도 됨

    - URL 입력 시 오타 방지

### Dynamic Route Matching with Params

#### 매개 변수를 사용한 동적 경로 매칭

- 주어진 패턴 경로를 동일한 컴포넌트에 매핑 해야 하는 경우 활용

1. /views/UserView.vue 컴포넌트 작성

2. index.js에 UserView 컴포넌트 라우트 작성

    - 매개변수는 콜론(`:`)으로 표기

3. 라우트의 매개변수는 컴포넌트에서 `$route.params`로 참조 가능

    다만 다음과 같이 Composition API 방식으로 작성하는 것을 권장

    ```vue
    <!-- UserView.vue -->
    <script setup>
    import { ref } from 'vue';
    import { useRoute } from 'vue-router';

    const route = useRoute()
    const userId = ref(route.params.id)
    </script>

    <template>
        {{userId}}
    </template>
    ```

### Programmatic Navigation

- router의 인스턴스 메서드를 사용해 RouterLink로 a 태그를 만드는 것 처럼 프로그래밍으로 네비게이션 관련 작업을 수행할 수 있음

1. 다른 위치로 이동하기

    `router.push()`

    - 다른 URL로 이동하는 메서드

    - 새 항목을 history stack에 push 하므로 사용자가 브라우저 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음

    |선언적|프로그래밍적|
    |---|---|
    |`<RouterLink :to='...'>`|`router.push()`|

2. 현재 위치 바꾸기

    `router.replace()`

    - push 메서드와 달리 history stack에 새로운 항목을 push하지 않고 다른 URL로 이동

    |선언적|프로그래밍적|
    |---|---|
    |`<RouterLink :to='...' replace>`|`router.replace(...)`|

<br>

## Navigation Guard

: Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 취소하여 네비게이션을 보호

1. Globally (전역 가드)

    - 애플리케이션 전역에서 동작
    - index.js에서 정의

2. Per-route (라우터 가드)

    - 특정 route에서만 동작
    - index.js의 각 routes에 정의

3. In-component (컴포넌트 가드)

    - 특정 컴포넌트 내에서만 동작
    - 컴포넌트 Script에 정의

### Globally (전역 가드)

#### `router.beforeEach()` : 다른 URL로 이동하기 직전에 실행되는 함수. Global Before Guards

```javascript
router.beforeEach((to, from) => {
    ...
    return false
})
```

- to : 이동 할 URL 정보가 담긴 Route 객체
- from : 현재 URL 정보가 담긴 Route 객체
- 선택적 반환(return)값
    1. false
        - 현재 내비게이션을 취소
        - 브라우저 URL이 변경된 경우(사용자가 수동으로 / 뒤로 버튼을 통해) from 경로의 URL로 재설정
    2. Route Location
        - `router.push()`를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect

- <span style='color: red;'>! return이 없다면 'to' URL Route 객체로 이동</span>

### Per-route (라우터 가드)

#### `router.beforeEnter()` : route에 진입했을 때만 실행되는 함수

-> 매개변수, 쿼리 값이 변경될 떄는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨

```javascript
{
    path: '/user/:id',
    name: 'user',
    component: UserView,
    beforeEnter: (to, from) => {        // 진입하기 전 수행
        ...,
        return false
    }
}
```

### In-component (컴포넌트 가드)

#### `onBeforeRouteLeave()`

- 현재 라우트에서 다른 라우트로 이동하기 전에 실행

    -> 사용자가 현재 페이지를 떠나는 동작에 대한 로직을 처리

#### `onBeforeRouteUpdate()`

- 이미 렌더링된 컴포넌트가 *같은 라우트 내*에서 업데이트되기 전에 실행

    -> 라우트 업데이트 시 추가적인 로직을 처리

두 명령 모두 사용 전 import 필요