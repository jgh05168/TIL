b# Comopnent State Flow

- [Passing Props](#Passing-Props)

- [Component Events](#Component-Events)

## Passing Props

"부모는 자식에게 데이터를 전달(Pass Props) 하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)"

### Props 

: 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성

- 부모 속성이 업데이트되면 자식으로 흐르지만 그 반대는 안됨

- 즉, 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능

- 또한 부모 컴포넌트가 업데이트 될 때마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨

-> 부모 컴포넌트에서만 변경되고 이를 내려 받는 자식 컴포넌트는 자연스럽게 갱신

#### One-Way Data Flow 

: 모든 props는 자식 속성과 부모 속성 사이에 `하향식 단방향 바인딩`을 형성

- 단방향인 이유

    : 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함

### Props 선언

: 부모 컴포넌트에서 보낸 props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요

1. 부모 컴포넌트 Parent에서 자식 컴포넌트 ParentChild에 보낼 props 작성

    `<ParentChild my-msg="message"/>`

    1. 문자열 배열을 사용한 선언

        `defineProps(['문자열'])`

    2. **객체를 사용한 선언(권장)**

        `defineProps({myMsg: String})`

### prop 데이터 사용

- 템플릿에서 반응형 변수와 같은 방식으로 활용

- props를 객체로 변환하므로 필요한 경우 JS 에서 접근 가능

```javascript
const props = defindProps({
    myMsg: String,
})
console.log(props.myMsg)
```

### 한 단계 더 prop 내려 보내기

1. ParentChild 컴포넌트를 부모로 갖는 ParentGrandChild 컴포넌트 생성 및 등록

2. ParentChild 컴포넌트에서 Parent 로부터 받은 prop인 myMsg를 ParentGrandChild에게 전달

3. 출력 결과 확인

### Props 세부사항

1. Props Name Casing (Props 이름 컨벤션)

    - 선언 및 템플릿 참조 시 : camelCase

    - 자식 컴포넌트로 전달 시 : kebab-case

2. Static Props & Dynamic Props

    - v-bind를 사용하여 <U>동적으로 할당된 props</U>를 사용할 수 있음

<br>

## Component Events

"부모가 prop 데이터를 변경하도록 소리쳐야 한다!"

### `$emit()`

: 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드

`$emit(event, ...args)` 

- event : 커스텀 이벤트

- args : 추가 인자

#### 이벤트 발신 및 수신(Emitting and Listening to Events)

- $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신

    `<button @click="%emit('someEvent')">클릭</button>`

- 그러면 부모는 `v-on`을 사용하여 수신할 수 있음

    `<parentComp @some-event="someCallback" />`

1. ParentChild에서 someEvent라는 이름의 사용자 정의 이벤트를 발신

2. ParentChild의 부모 Parent는 v-on을 사용하여 발신된 이벤트를 수신

    - 수신 후 처리할 로직 및 콜백함수 호출

#### Emit 이벤트 선언

- `defineEmits()를 사용하여 명시적으로 발신할 이벤트를 선언할 수 있음

- script에서 `$emit` 메서드를 접근할 수 없기 떄문에 `defineEmits()`는 $emit 대신 사용할 수 있는 동등한 함수를 반환

```javascript
const emit = defineEmits(['someEvent', 'myFocus'])

const buttonClick = function() {
    emit('someEvent')
}
```

### Event 인자

: 이벤트 발신 시 추가 인자를 전달하여 값을 제공할 수 있음

1. ParentChild에서 이벤트를 발신하여 Parent로 추가 인자 전달하기

2. ParentChild에서 발신한 이벤트를 Parent에서 수신

### Event 세부사항

#### Event Name Casing

- 선언 및 발신 시 : camelCase

- 부모 컴포넌트에서 수신 시 : kebab-case

[참고]

- 정적 & 동적 props 주의사항

```vue
<!-- 정적 props로 문자열로써의 '1'을 전달 -->
<SomeComponent num-props="1" />

<!-- 동적 props로 숫자로써의 1을 전달 -->
<someComponent :num-props="1" />
```

- Prop 선언을 객체 선언 문법으로 권장하는 이유

    - prop에 타입을 지정하는 것은 컴포넌트를 가독성이 좋게 문서화하는데 도움이 되며, 다른 개발자가 잘못된 유형을 전달할 때에 브라우저 콘솔에 경고를 출력하도록 함

    - 추가로 prop에 대한 "유효성 검사"로 활용 가능