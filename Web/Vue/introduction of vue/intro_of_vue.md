# Introduction of Vue

- [Frond-end Development](#Frond-end-Development)

- [Vue.js](#Vue.js)

<br>

## Frond-end Development

: 웹사이트와 웹 애플리케이션의 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인하는 것

-> HTML, CSS, JS 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발

### Client-side frameworks

: 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JS 기반 프레임워크

#### 필요한 이유

"웹에서 하는 일이 많아졌다."

1. 단순히 무언가를 읽는 곳 -> 무언가를 하는 곳
    
    - 웹 애플리케이션

    - 동적인 대화형 애플리케이션을 훨씬 더 쉽게 구축할 수 있게 됨

2. 다루는 데이터가 많아졌다.

    - 애플리케이션의 기본 데이터를 안정적으로 추적하고 업데이트(랜더링, 추가, 삭제 등)하는 도구가 필요

    - <span style='color: crimson;'>애플리케이션의 상태를 변경할 때마다 일치하도록 UI를 업데이트해야 한다는 것</span>

### SPA

: Single Page Application - 페이지 한 개로 구성된 웹 애플리케이션

: 웹 애플리케이션의 초기 로딩 후 새로운 페이지 요청 없이 동적으로 화면을 갱신하며 사용자와 상호작용하는 웹 애플리케이션 

-> [CSR 방식](#CSR)

![Alt text](image.png)

1. 서버로부터 필요한 모든 정적 HTML을 처음에 한번 가져옴

2. 브라우저가 페이지를 로드하면 Vue 프레임워크는 각 HTML 요소에 적절한 JS 코드를 실행(이벤트에 응답, 데이터 요청 후 UI 업데이트 등)

    - ex) 페이지 간 이동 시, 페이지 갱신에 필요한 데이터만을 JSON으로 전달받아 페이지 일부 갱신

    - Google maps, 인스타그램 등의 서비스에서 갱신 시 새로고침이 없는 이유

### CSR

: Client-side Rendering :클라이언트에서 화면을 랜더링하는 방식

1. 브라우저는 페이지에 필요한 최소한의 HTML 페이지와 JS를 다운로드

2. JS를 사용하여 DOM을 업데이트하고 페이지를 랜더링

![Alt text](image2.png)

-  장점

    1. 빠른 속도

        - 페이지의 일부를 다시 렌더링할 수 있으므로 동일한 웹사이트의 다른 페이지로 이동하는 것이 일반적으로 더 빠름

        - 서버로 전송되는 데이터 양을 최소화

    2. 사용자 경험

        - 새로고침이 발생하지 않아 네이티브 앱과 유사한 사용자 경험을 제공

    3. Front-end와 Back-end의 명확한 분리

        - Front-end는 UI 렌더링 및 사용자 상호 작용 처리를 담당 & Back-end는 데이터 및 API 제공을 담당

        - 대규모 애플리케이션을 더 쉽게 개발하고 유지 관리 가능

- 단점

    1. 초기 구동 속도가 느림

        - 전체 페이지를 보기 전에 약간의 지연을 느낄 수 있음

        - JS가 다운로드, 구문 분석 및 실행될 때까지 페이지가 완전히 렌더링되지 않기 때문

    2. SEO(검색 엔진 최적화) 문제

        - 페이지를 나중에 그려나가는 것이기 때문에 검색에 잘 노출되지 않을 수 있음

<br>

## Vue.js

- Vue란 ?

    - 사용자 인터페이스를 구축하기 위한 JS 프레임워크
    - 2023년 기준 최신 버전은 'Vue3'

- Vue를 학습하는 이유

    1. 쉬운 학습 곡선 및 간편한 문법
    2. 반응성 시스템 
    3. 모듈화 및 유연한 구조

1. 선언적 렌더링(Declarative Rendering)

    - HTML을 확장하는 템플릿 구문을 사용하여 HTML이 JS 데이터를 기반으로 어떻게 보이는지 설명할 수 있음

2. 반응형(Reactivity)

    - JS 상태 변경사항을 자동으로 추적하고 변경사항이 발생할 때 DOM을 효율적으로 업데이트

### Vue 튜토리얼

    1. 'CDN' 방식

    2. 'NPM' 설치 방식

- Application Instance

    - 모든 Vue 애플리케이션은 createApp 함수로 새 Application instance를 생성하는 것으로 시작

    ```html
    // 기본 구조(틀)
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <script>
    const { createApp } = Vue

    const app = createApp({
        ...
    })
    </script>
    ```

- `app.mount()`

    - 컨테이너 요소에 애플리케이션 인스턴스를 탑재(연결)

    - 각 앱 인스턴스에 대해 mount()는 한 번만 호출할 수 있음

- `ref()` : 반응형 상태(데이터)를 선언하는 함수

    - 반응형울 가지는 참조 변수를 만드는 것

    - 인자를 받아 .value 속성이 있는 ref 객체로 래핑하여 반환

    - ref로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트

    - 어떠한 타입도 가능

    ```javascript
    const { ..., ref } = Vue

    const app = createApp({
        setup () {
            const message = ref('hello vue!')
            console.log(message)
            return {
                message,
            }
        }
    })
    ```

- [Vue 기본 구조]

    - createApp()에 전달되는 객체는 Vue 컴포넌트
    - 컴포넌트의 상태는 setup() 함수 내에서 선언되어야 하며 <span style='color: crimson;'>객체를 반환해야 함</span>

- 템플릿 렌더링

    - 반환된 객체의 속성은 템플릿에서 사용할 수 있음

    - Mustache syntax(콧수염 구문)를 사용하여 메세지 값을 기반으로 동적 텍스트를 렌더링

    - 콘텐츠는 식별자나 경로에만 국한되지 않으며 유효한 JS 표현식을 사용할 수 있음

- Event Listeners in Vue

    - 'v-on' directive를 사용하여 DOM 이벤트를 수신할 수 있음

    - 함수 내에서 refs를 변경하여 구성 요소 상태를 업데이트

