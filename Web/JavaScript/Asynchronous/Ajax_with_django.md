# Ajax with Django

- [Ajax와 서버](#Ajax와-서버)

- [Ajax with follow](#Ajax-with-follow)

- [Ajax with likes](#Ajax-with-likes)

## Ajax와 서버

- 클라이언트 : XHR 객체 생성 및 요청
- 서버 : JSON 반환

[서버 간 동작 원리]

<span style="color: crimson;">클라이언트</span> / 서버

<span style="color: crimson;">이벤트 발생</span> -> <span style="color: crimson;">XHR 객체 생성 및 요청</span> -> Ajax 요청 처리 -> 응답 데이터 생성 -> JSON 데이터 응답 -> <span style="color: crimson;">응답 데이터를 활용해 DOM 조작</span>

(웹 페이지의 일부분 만을 다시 로딩)

[08-ajax-with-django 폴더의 파일을 사용하여 실습형태로 공부]

<br>

## Ajax with follow

1. form 요소 선택을 위해 id 속성 지정 및 선택. (action과 method 속성은 삭제 : axios로 대체되기 때문)

    (이후 과정은 event handler의 콜백 함수에 포함되어 있음)

2. form 요소에 이벤트 핸들러 작성 및 submit 이벤트의 기본 동작 취소
    
    이벤트의 기본 동작 취소 : `event.preventDefault()`

3. axios 요청 작성

    - url에 작성한 user.pk는 어떻게 작성되야 할까?

        ```javascript
        <form id="follow-form" data-user-id="{{ person.pk }}">
            ...
        </form>

        const userId = formTag.dataset.userId
        ```

        - <U>'data-*' 속성</U>
        
            : 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환 할 수 있는 방법

            - 모든 사용자 지정 데이터는 JS에서 **dataset** 속성을 통해 사용

            [주의사항]

            1. 대소문자 여부에 상관없이 'xml' 문자로 시작 불가
            2. 세미콜론 포함 불가
            3. 대문자 포함 불가

    - csrf_token은 어떻게 보내야 할까?

        : csrf 값을 가진 input 요소를 직접 선택 후 axios에 작성하기.

        ```javascript
        // Ajax 관련 Django 공식문서 참고
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

        ```

    ```javascript
    // axios 작성
    axios({
        url: `/accounts/${userId}/follow/`,
        method: 'post',
        headers: {'X-CSRFToken': csrftoken},
      })
    ```

4. Django의 view 함수에서 팔로우 여부를 파악할 수 있는 변수를 추가로 생성해 JSON 타입으로 응답하기

    - 팔로우 상태 여부를 JS에게 전달할 데이터 작성

    - 응답은 더 이상 HTML 문서가 아닌 JSON 데이터로 응답

    ```python
    from django.http import JsonResponse
    
    @login_required
    def follow(request, user_pk):
        User = get_user_model()
        you = User.objects.get(pk=user_pk)
        me = request.user

        if me != you:
            if me in you.followers.all():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followings_count': you.followings.count(),
                'followers_count': you.followers.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    ```

5. 응답 데이터 is_followed에 따라 팔로우 버튼 토글하기

    ```javascript
    const isFollowed = response.data.is_followed

    if (isFollowed === true) {
            followBtn.value = 'Unfollow'
          } else {
            followBtn.value = 'Follow'
          }
    ```

6. 팔로워 / 팔로잉 수 조작

    ```javascript
    const followingsCountTag = document.querySelector('#followings-count')
    const followersCountTag = document.querySelector('#followers-count')
          
    followingsCountTag.textContent = response.data.followings_count
    followersCountTag.textContent = response.data.followers_count
    ```

<br>

## Ajax with likes

[유의사항]

- AJax 적용은 팔로우와 모두 동일

- 단, 팔로우와 달리 좋아요 버튼은 "한 페이지에 여러 개" 존재.

    1. forEach()

        ```javascript
        formTags.forEach((formTag) => { 
            formTag.addEventListener('submit', function (event) {
                event.preventDefault()

                const articleId = formTag.dataset.articleId

                axios({
                url: `/articles/${articleId}/likes/`,
                method: 'post',
                headers: {'X-CSRFToken': csrftoken},
                })
                .then((response) => {
                    // console.log(response.data.is_liked)
                    const isLiked = response.data.is_liked
                    const likeBtn = document.querySelector(`#like-${articleId}`)

                    if (isLiked === true) {
                    likeBtn.value = '좋아요 취소'
                    } else {
                    likeBtn.value = '좋아요'
                    }
                })
                .catch((error) => {
                    console.log(error)
                })
            })
        })
        ```

    2. querySelectorAll()

        ```javascript
        const formTags = document.querySelectorAll('.likes-forms')
        ```