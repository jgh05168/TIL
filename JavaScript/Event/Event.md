# Controlling event

[- Event(이벤트)](#Event(이벤트))

[- Event Handler 활용](#Event-Handler-활용)

<br>

## Event(이벤트)

: 무언가 일어났다는 신호, 사건 

-> 모든 DOM 요소는 이러한 event를 만들어 냄

event object : DOM에서 이벤트가 발생했을 떄 생성되는 객체

    ex) mouse, input, keyboard, ...

#### DOM 요소는 event를 받고 받은 event를 `처리(event handler)` 할 수 있음

<br>

## Event Handler 활용

: 이벤트가 발생했을 때 실행되는 함수

-> 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

### `addEventListener()`

: 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출

- EventTarget.addEventListener(type, handler)

    - EventTarget : DOM 요소(대상)

    - type : 수신할 이벤트(특정 이벤트)

        - 문자열로 작성

    - handler : 콜백 함수(지정한 이벤트를 받아서 할 일)

        - 콜백 함수는 발생한 event object를 유일한 매개변수로 받음

        - 콜백 함수는 반환값이 없음

    ! 주의 !

        - 콜백 함수로 화살표함수를 사용할 경우 콜백함수 내부 this는 Window를 가리킨다.

[활용]

- 버튼을 클릭하면 버튼 요소 출력하기 -> 버튼에 이벤트 처리기를 부착하여 클릭 이벤트가 발생하면 이벤트가 발생한 버튼 정보를 출력

```javascript
// <button id="btn">버튼</button>  :  외부에 존재하는 버튼 태그

// 1. 버튼 선택
const btn = document.querySelector('#btn')

// 2. 콜백 함수
const detectClick = function (event) {
    console.log(event)
    // 아래 3개는 모두 같은 역할
    console.log(event.target)
    console.log(event.currentTarget)
    console.log(this)
}

// 3. 버튼에 이벤트 핸들러를 부착
btn.addEventListener('click', detectClick)
```

### 버블링

: 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상

: 가장 최상단의 조상 요소(document)를 만날 떄까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작

-> 실제 이벤트가 어디서 발생했는지 알고자 한다.

1. event.target

    - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성

    - 실제 이벤트가 시작된 target 요소

    - 버블링이 진행되어도 변하지 않음

2. event currentTarget

    - <U>현재 요소</U>

    - 항상 이벤트 핸들러가 연결(부착)된 요소만을 참조하는 속성(EventTarget)

    - 'this'와 같음 -> `this == event.currentTarget`

    - 항상 EventTarget(최상단 요소)를 가리킨다.

    [주의 사항]

    - console.log()로 event 객체를 출력할 경우 currentTarget 키의 값은 null을 가짐

    - currentTarget은 이벤트가 처리되는 동안에만 사용할 수 있기 때문

    - 대신 console.log(event.currentTarget)을 사용하여 콘솔에서 확인 가능

    - currentTarget 이후의 속성 값들은 <U>target</U>을 참고해서 사용하기

