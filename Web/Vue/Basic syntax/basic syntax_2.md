# Basic Syntax 2

- [Cumputed Properties](#Cumputed-Properties)

- [Conditional Rendering](#Conditional-Rendering)

- [List Rendering](#List-Rendering)

- [Watchers](#Watchers)

- [Lifecycle Hooks](#Lifecycle-Hooks)

- [Vue Style Guide](#Vue-Style-Guide)

## Cumputed Properties

### `computed()` : 계산된 속성을 정의하는 함수

-> 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임

! 반응성 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산

[특징]

- 반환되는 값은 computed ref이며 일반 refs와 유사하게 계산관 결과를 `.value`로 참조할 수 있음(템플릿에서는 .value 생략 가능)

- computed 속성은 의존된 반응형 데이터를 <span style='color:crimson;'>자동으로 추적</span>

- 의존하는 데이터가 변경될 때만 재평가

### Computed vs Methods

#### computed와 method 차이

- computed 속성은 <span style='color:crimson;'>의존된 반응형 데이터를 기반으로 캐시(cashed) 된다.</span>

- 의존하는 데이터가 변경된 경우에만 재평가됨

- 의존된 반응형 데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조는 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환

-> 반면, method 호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행

#### Cache (캐시)

- 데이터나 결과를 일시적으로 저장해두는 임시 저장소

- 이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함

#### computed와 method의 적절한 사용처

|computed|method|
|---|---|
|의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용|단순히 특정 동작을 수행하는 함수를 정의할 때 사용|
|동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지|데이터에 의존하는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수|

[정리]

computed : 의존된 데이터가 변경되면 자동으로 업데이트

method : 호출해야만 실행됨

-> 무조건 computed만 사용하는 것이 아니라 사용 목적과 상황에 맞게 computed와 method를 적절히 조합하여 사용

<br>

## Conditional Rendering

### `v-if` : 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링

- `v-else` directive를 사용하여 v-if에 대한 else 블록을 나타낼 수 있음

- false로 평가받았을 경우 렌더링조차 하지 않는다.

- `v-else-if` 구문을 사용하여 else if 역시 조건을 걸어줄 수 있다.

```javascript
// 예시
<p v-if="isSeen">true일때 보여요</p>
<p v-else>false일때 보여요</p>
```

#### HTML <template> element

- 페이지가 로드 될 때 렌더링 되지 않지만 JS를 사용하여 나중에 문서에서 사용할 수 있도록 하는 HTML을 보유하기 위한 메커니즘

- "보이지 않는 wrapper 역할"

### `v-if` vs `v-show`

공통점 : 조건부 렌더링

`v-show` : 표현식 값의 T/F를 기반으로 <U?>요소의 가시성(visibility)을 전환</U>

![Alt text](image.png)

-> 렌더링은 하지만 보여질 지 말 지를 확인한다.

|v-if|v-show|
|---|---|
|초기 조건이 false인 경우 아무 작업도 수행하지 않음|초기 조건에 관계 없이 항상 렌더링|
|토글 비용이 높음|초기 렌더링 비용이 더 높음|

-> <U>무언가를 매우 자주 전환해야 하는 경우에는 `v-show`를, 실행 중에 조건이 변경되지 않는 경우에는 `v-if`를 권장</U>

<br>

## List Rendering

### `v-for` : 소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링

[v-for 구조]

- `v-for`는 <span style="color: crimson;">alias in expression</span> 형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭(alias)을 제공

- 같은 렌더링이 반복적으로 수행된다.

```html
<div v-for="item in items">
    {{item.text}}
</div>
```

- 인덱스(객체에서는 키)에 대한 별칭을 지정할 수 있음

```html
<div v-for="(item, index) in items"></div>
<div v-for="value in object"></div>
<div v-for="(value, key) in object"></div>
<div v-for="(value, key, index) in object"></div>
```
#### 여러 요소에 대한 `v-for` 적용

- template 요소에 `v-for`를 사용하여 하나 이상의 요소에 대해 반복 렌더링 할 수 있음

```html
<ul>
    <template v-for="item in myArr">
        <li>{{item.name}}</li>
        <li>{{item.age}}</li>
    <hr>
    </template>
</ul>
```
#### 중첩된 `v-for`

- 각 `v-for` 범위는 상위 범위에 접근할 수 있음

```html
<!-- const myInfo = ref([
          { name: 'Alice', age: 20, friends: ['Bella', 'Cathy', 'Dan'] },
          { name: 'Bella', age: 21, friends: ['Alice', 'Cathy'] }
        ]) -->

<ul v-for="item in myInfo">
    <li v-for="friend in item.friends">
        {{friend}}
    </li>
</ul>
```

### `v-for` with key

**<U>반드시 v-for와 key를 함께 사용한다</U>**

: 내부 컴포넌트의 상태를 일관되게 유지

-> 데이터의 예측 가능한 행동을 유지(Vue 내부 동작 관련)

- key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 있는 식별자여야 함

### `v-for` with `v-if`

**<U>동일 요소에 v-for와 v-if를 함께 사용하지 안는다.</U>**

: 동일한 요소에서 v-if가 v-for보다 <U>우선순위가 더 높기 때문</U>

-> v-if 조건은 v-for 범위의 변수에 접근할 수 없음

<br>

## Watchers

### `watch()` : <U>반응형 데이터를 감시</U>하고, 감시하는 데이터가 변경되면 <U>콜백 함수를 호출</U>

[watch 구조]

```javascript
watch(variable, (newValue, oldValue) => {
    //do something
})
```

- variable

    - 감시하는 변수

- newValue

    - 감시하는 변수가 변화된 값
    - 콜백 함수의 첫번째 인자

- oldValue

    - 콜백 함수의 두번째 인자

#### Computed와 Watchers

||Computed|watchers|
|---|---|---|
|공통점|데이터의 변화를 감지하고 처리||
|동작|의존하는 데이터 속성의 계산된 값을 반환|특정 데이터 속성의 변화를 감시하고 작업을 수행|
|사용 목적|템플릿 내에서 사용되는 데이터 연산용|데이터 변경에 따른 특정 작업 처리용|
|사용 예시|연산된 길이, 필터링 된 목록 계산 등|비동기 API 요청, 연관 데이터 업데이트 등|

<span style='color: red;'>!! computed와 watch 모두 의존(감시)하는 원본 데이터를 직접 변경하지 않음 !!</span>

<br>

## Lifecycle Hooks

: Vue 인스턴스의 생애주기 동안 특정 시점에 실행되는 함수

-> 개발자가 특정 단계에서 의도하는 로직이 실행될 수 있도록 함

[예시]

1. Vue 컴포넌트 인스턴스가 초기 렌더링 및 DOM 요소 생성이 완료된 후 특정 로직을 수행하기.

2. 반응형 데이터의 변경으로 인해 컴포넌트의 DOM이 업데이트된 후 특정 로직을 수행하기
