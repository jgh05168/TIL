# Asynchronous

- [비동기(Asynchronous)](#비동기(Asynchronous))

- [JavaScript와 비동기](#JavaScript와-비동기)

- [AJAX](#AJAX)

- [Callback과 Promise](#Callback과-Promise)

<br>

## 비동기(Asynchronous)

: 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식

-> 작업의 완료 여부를 신경쓰지 않고 <U>동시에 다른 작업들을 수행할 수 있음</U>

- 특징

    1. 병렬적 수행

    2. 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

- ex)

    ```javascript
    const slowRequest = function(callback) {
        setTimeout( function() {    // 3초를 기다렸다가 콜백 함수를 호출하는 함수
            callback()
        }, 3000)        
    } 

    slowRequest(myCallback)
    ```

<br>

## JavaScript와 비동기

[들어가기 전]

### Thread란 ?
    
-> 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread 라면 업무를 수행할 수 있는 주체가 여러 개라는 의미

however, JavaScript는 한번에 여러 일을 수행할 수 없다.

### JavaScript Runtime

- JavaScript가 동작할 수 있는 환경(Runtime)
- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
- JS에서 비동기 관련 작업은 브라우저 or Node와 같은 환경에서 처리

### 브라우저 환경에서의 JS 비동기 처리 관련 요소

1. JavaScript Engine의 <span style='color:crimson;'>Call Stack</span>
    
    : 모든 작업은 Call Stack(LIFO)로 들어간 후 처리된다.

    - 요청이 들어올 때 마다 순차적으로 처리하는 Stack
    - 기본적인 JS의 Single Thread 작업 처리
    
2. <span style='color:crimson;'>Web API</span>

    : 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도록 처리하도록 한다.

    - JS 엔진이 아닌 브라우저에서 제공하는 runtime 환경
    - 시간이 소요되는 작업을 처리(setTimeout, DOM Event, AJAX 요청 등)

3. <span style='color:crimson;'>Task Queue</span>

    : Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue(FIFO)에 순서대로 들어간다.

    - 비동기 처리된 Callback 함수가 대기하는 Queue
    
4. <span style='color:crimson;'>Event Loop</span>

    : Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 작업을 Call Stack으로 보낸다.

    - 태스크(작업)가 들어오길 기다렸다가 태스크가 들어오면 이를 처리하고, 처리할 태스크가 없는 경우에는 잠드는, 끊임없이 돌아가는 자바스크립트 내 루프
    - Call Stack과 Task Queue를 지속적으로 모니터링
    - Call Stack이 비어있는 지 확인 후 비어있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

[정리]

- JS는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 진행
- 하지만 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 됨

<br>

## AJAX

: Asynchronous JavaScript + XML

: JS의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술

(최근은 XML보다 가벼운 용량과 JS의 일부인 JSON 형식을 더 많이 사용)

### XMLHttpRequest 객체

: 서버와 상호작용할 때 사용하며 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있음

-> 사용자의 작업을 방해하지 않고 페이지의 일부를 업데이트

-> 주로 AJAX 프로그래밍에 많이 사용됨

-> JavaScript를 사용하여 서버에 HTTP 요청을 할 수 있는 객체

### Axios

: JavaScript에서 사용되는 <U>Promise 기반</U> HTTP 클라이언트 라이브러리

-> 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구

- 구조

    - get, post 등 여러 http request method 사용 가능
    - then 메서드를 사용해서 "**성공하면 수행할 로직**"을 작성
    - catch 메서드를 사용해서 "***실패하면 수행할 로직**"을 작성

    ```javascript
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

    axios({
        method = 'post',
        url = '/user/12345',
        data: {
            firstName: 'Fred',
            lastName: 'Flintstone'
        }
    })
        .then(요청에 성공하면 수행할 콜백함수)
        .catch(요청에 실패하면 수행할 콜백함수)
    ```

[정리]

- axios는 브라우저에서 비동기로 데이터 통신을 가능하게 하는 라이브러리
    - 브라우저를 위해 XMLHttpRequest 생성
- 같은 방식으로 DRF로 만든 API 서버로 요청을 보내서 데이터를 받아온 후 처리할 수 있도록 함


<br>

## Callback과 Promise

[비동기 처리의 단점]

- 작업이 완료되는 순서에 따라 처리한다.
- 코드의 실행 순서가 불명확하다.

### 비동기 콜백

: 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수

: 연쇄적으로 발생하는 비동기 작업을 <U>순차적으로 동작</U>할 수 있게 함

-> 작업의 순서와 동작을 제어하거나 결과를 처리하는데 사용

- 콜백 함수 정리

    - 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직
    - 비동기 코드를 작성하다 보면 콜백 함수로 인한 콜백 지옥은 빈번히 나타나는 문제임
    - 이는 코드의 가독성을 해치고 유지 보수가 어려워짐

    -> promise 사용

### Promise

: JS에서 비동기 작업의 결과를 나타내는 객체

-> 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능을 제공

- "작업이 끝나면 실행 시켜 줄게" 라는 약속
- 비동기 작업의 완료 또는 실패를 나타내는 객체
- ex) Axios 라이브러리의 .then(), .catch()

```javascript
work1()
    .then((result1) => {
        // work 2
        return result2
    })
    .then((result2) => {
        // work3
        return result3
    })
    .catch((error) => {
        //error handling
    })
```

- `.then(callback)`
    - 요청한 작업이 성공하면 callback 실행
    - callback은 이전 작업의 성공 결과를 인자로 전달받음

- `.catch(callback)`
    - then()이 하나라도 실패하면 callback 실행
    - callback은 이전 작업의 실패 객체를 인자로 전달받음

- then과 catch는 모두 항상 promise 객체를 반환. -> 계속해서 chaining 가능

    - chaining의 장점
        1. 가독성
            - 비동기 작업의 순서와 의존 관계를 명확히 표현할 수 있음

        2. 에러 처리
            - 각각의 비동기 작업 단계에서 발생하는 에러를 분할 처리 가능
        
        3. 유연성
            - 각 단계마다 필요한 데이터를 가공하거나 다른 비동기 작업을 수행할 수 있어서 더 복잡한 비동기 흐름을 구성할 수 있음

        4. 코드 관리 
            - 비동기 작업을 분리하여 구성하면 코드를 관리하기 용이

- 첫번째 then 콜백함수의 반환값이 이어지는 then 콜백함수의 인자로 전달된다.