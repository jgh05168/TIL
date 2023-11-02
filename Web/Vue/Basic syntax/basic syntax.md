d# Basic Syntax

- [Template Syntax](#Template-Syntax)

- [Dynamically data binding](#Dynamically-data-binding)

- [Event Handling](#Event-Handling)

- [Form Input Bindings](#Form-Input-Bindings)

<br>

## Template Syntax

: DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용

1. Text Interpolation

    ```html
    <p>Message: {{msg}}</p>
    ```

    - 데이터 바인딩의 가장 기본적인 형태

    - 이중 중괄호 구문(콧수염 구문)을 사용

    - 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체

    - msg 속성이 변경될 때마다 업데이트됨

2. Raw HTML
    
    ```html
    <div v-html='rawHtml'></div>

    const rawHtml = ref('<span style="color:red">This should be red.</span>')
    ```

    - 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야 함

3. Atrribute Bindings

    ```html
    <div v-bind:id='dynamicId'></div>

    const dynamicId = ref('my-id')
    ```

    - 콧수염 구문은 HTML 속성 내에서 값을 사용할 수 없기 때문에 v-bind를 사용

    - HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함

    - 바인딩 값이 null이나 undefined인 경우 렌더링 요소에서 제거된다.

4. JavaScript Expressions

    ```javascript
    {{ number + 1 }}
    {{ ok ? 'YES' : 'NO'}}
    {{ msg.split('').reverse().join('')}}
    <div :id="`list-${id}`"></div>
    ```

    - Vue는 모든 데이터 바인딩 내에서 JS 표현식의 모든 기능을 지원

    - Vue 템플릿에서 JS 표현식을 사용할 수 있는 위치

        1. 콧수염 구문 내부
        2. 모든 directive의 속성 값 (v-로 시작하는 특수 속성)

    - [주의]

        - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음 ( return 뒤에 사용할 수 있는 코드여야 함)

        - 흐름제어 역시 작동하지 않는다.(삼항 표현식 사용)

### Directive

: `v-` 접두사가 있는 특수 속성

- Directive의 속성 값은 단일 JS 표현식이여야 함 (v-for, v-on 제외)

- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용

- ex) 

    - v-if 는 seen 표현식 값의 T/F를 기반으로 <p> 요소를 제거/삽입

        ```html
        <p v-if="seen">Hi There</p>
        
        ...

        const seen = ref(True)
        ```

#### `v-on: submit.prevent="onSubmit"`

- `v-on` : Name
- `submit` : Argument
- `prevent` : Modifiers
- `"onSubmit"` : Value(JS 표현식)

#### Directive - Arguments

- 일부 directive는 directive 뒤에 콜론으로 표시되는 인자를 사용할 수 있음

- ex) HTML a 요소의 href 속성 값을 myUrl 값에 바인딩하도록 하는 v-bind의 인자

    - `<a v-bind:href="myUrl">Link</a>`

- ex) click은 이벤트 수신할 이벤트 이름을 작성하는 v-on 의 인자

    - `<button v-on:click="doSomething">Button</button>`

#### Directive - Modifiers

- .(dot)로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄

- ex) .prevent느 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 midifier

    ```html
    <form @submit.prevent="onSubmit">
        <input type="submit">
    </form>
    ```

#### Built-in Directives

- v-text
- v-show
- v-if
- v-for
- ...

<br>

## Dynamically data binding

`v-bind` : 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 <U>동적으로 바인딩</U>

1. [Attribute Bindings](#Attribute-Bindings)

2. [Class and Style Bindings](#Class-and-Style-Bindings)

### Attribute Bindings

- HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되로록 함

```html
<img v-bind:src="imageSrc">
<a v-bind:href="myUrl">Move to url</a>
```

- v-bind 약어

    - `:`

- Dynamic attribute name

    - 대괄호로 감싸서 directive argument에 JS 표현식을 사용할 수도 있음

    - JavaScript 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨

    `<button :[key]="myValue"></button>`

    - <span style='color: crimson;'>대괄호 안에 작성하는 이름은 반드시 소문자로만 구성 가능</span>

### Class and Style Bindings

- 클래스와 스타일은 모두 속성이므로 v-bind를 사용하여 다른 속성과 마찬가지로 동적으로 문자열 값을 할당할 수 있음

- Vue는 클래스 및 스타일과 함께 v-bind를 사용할 때 객체 또는 배열을 활용한 개선 사항을 제공

- [Class and Style Bindings가 가능한 경우]

    1. Binding HTML Classes

        - Binding to Objects

            - 객체를 `:class`에 전달하여 클래스를 동적으로 전환할 수 있음

            ```html
            <style>
                .active {
                color: crimson;
                }
            </style>

            ...
            <div :class="{ active: isActive }">Text</div>
            <div class="static" :class="{ active: isActive, 'text-primary': hasInfo }">Text</div>   <!--이런 경우는 클래스가 하나로 합쳐진다.-->


            ...
            const isActive = ref(true)
            ```

        - Binding to Arrays

            - `:class`를 배열에 바인딩하여 클래스 목록을 적용할 수 있음

            - ex)
            ```html
            <div :class="[activeClass, infoClass]">Text</div>
            <div :class="[{ active: isActive }, infoClass]">Text</div>  <!--배열 안에 객체 역시 가능-->
            ```

    2. Binding Inline Styles

        - Binding to Objects

            - `:style`은 JS 객체 값에 대한 바인딩을 지원
        
                ```html
                <div :style="{ color: activeColor, fontSize: fontSize + 'px'}">Text</div>
                ```

            - 실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열도 지원

                ```html
                <div :style="{ 'font-size': fontSize + 'px'}">Text</div>
                ```

            - 템플릿을 더 깔끔하게 작성하려면 스타일 객체에 직접 바인딩하는 것을 권장.

                ```javascript
                const styleObj = ref({
                    color: activeColor, 
                    fontSize: fontSize.value + 'px'
                })
                
                <div :style="styleObj">Text</div>
                ```

        - BInding to Arrays

            - 여러 스타일 객체의 배열에 `:style`을 바인딩 할 수 있음

            - 작성한 객체는 병합되어 동일한 요소에 적용

            ```javascript
            const styleObj2 = ref({
                color: 'blue',
                border: '1px solid black'
            })

            <div :style="[styleObj, styleObj2]">Text</div>
            ```

<br>

## Event Handling

`v-on` : DOM 요소에 이벤트 리스너를 연결 및 수신

`v-on:event="handler"`

- handler 종류

    1. Inline handlers : 이벤트가 트리거 될 떄 실행될 JS 코드

        - 주로 간단한 상황에 사용

    2. Method handlers : 컴포넌트에 정의된 메서드 이름

        - Inline handlers로는 불가능한 대부분의 상황에서 사용

        - Method Handlers는 이를 트리거하는 기본 DOM Event 객체를 자동으로 수신

- v-on 약어

    - `@`
    - `@event="handler"`

- Inline Handlers에서의 메서드 호출

    - 메서드 이름에 직접 바인딩하는 대신 Inline Handlers에서 메서드를 호출할 수도 있음

    - 기본 이벤트 대신 사용자 지정 인자를 전달할 수 있음

    ```html
    <button @click="greeting('hello')">Say hello</button>
    ```

- Inline Handlers에서의 event 인자에 접근하기

    - Inline Handlers에서 원래 DOM 이벤트에 접근하기

    - $event 변수를 사용하여 메서드에 전달

    ```javascript
    const warning = function(message, event){
        console.log(message)
        console.log(event)
    }

    <button @click="warning('경고입니다', $event)">Submit</button>

- Event Modifiers

    - Vue는 v-on에 대한 Event Modifiers를 제공해 `event.preventDefault()`와 같은 구문을 메서드에서 작성하지 않도록 함

    - stop, prevent, self 등 다양한 modifiers를 제공

    -> 메서드는 DOM 이벤트에 대한 처리보다는 데이터에 관한 논리를 작성하는 것에 집중할 것

- Key Modifiers

    - Vue는 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음

    ```html
    <!--key가 Enter일 때만 onSubmit 이벤트를 호출하기-->
    <input type="text" @keyup.enter="onSubmit">
    ```

<br>

## Form Input Bindings

: form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JS 상태에 동기화해야 하는 경우 (양방향 바인딩)

[양방향 바인딩 방법]

1. v-bind와 v-on을 함께 사용

    - v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용

    - v-on을 사용하여 input 이벤트가 발생할 때마다 input 요소의 value 값을 별도 반응형 변수에 저장하는 핸들러를 호출

    ```javascript
    <div id="app">
        <p>{{ inputText1 }}</p>
        <input type="text" @input="onInput" :value="inputText1">

        <p>{{ inputText2 }}</p>
        <input type="text" v-model="inputText2">
    </div>
    ...

    const inputText1 = ref('')
    const inputText2 = ref('')
    const onInput = function (event) {
        inputText1.value = event.currentTarget.value
    }
    ```
2. v-model 사용

    : form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦

    - v-model을 사용하여 사용자 입력 데이터와 반응형 변수를 실시간 동기화

    ```javascript
    const inputText2 = ref('')

    <p> {{ inputText2 }}</p>
    <input v-model='inputText2'>
    ```

    - v-model은 단순 text input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능
    