# Text Editor

- [Text Editor 개요](#Text-Editor-개요)

- [gedit](#gedit)

- [vi 체험](#vi-체험)

- [vim 다루기](#vim-다루기)

- [vi를 메모장 처럼](#vi를-메모장-처럼)

## Text Editor 개요

리눅스의 대표적인 Editor

1. GUI : gedit
    - 단순 체험 정도

2. **CLI : vi**

    - <U>임베디드 환경의 리눅스에는 vi 밖에 없는 경우가 많다.</U>

    - <span style="color: crimson;">메모장처럼 빠르게 다룰 수 있게 훈련이 필요함</span>

[연습 순서]

1. gedit 연습
2. vi 연습
3. vim - 다양한 extension 설치 및 세팅

## gedit

: 우분투의 대표적인 GUI editor

- 메모장과 사용방법이 거의 똑같음

[자주 사용하는 키]

- 복사 / 붙여넣기 : ctrl + insert / shift + insert 

- Insert 키를 누르면, 커서가 두꺼워지면서 덮어쓰기가 된다.

- home : 한 줄 맨 앞 이동

- end : 한 줄 맨 뒤 이동

- page up / down : 페이지 이동

#### 터미널에서 프로그램을 실행

1. `gedit ./파일이름` : foreground 실행
    - 입력한 명령어 실행의 결과가 나올 때까지 기다리는 방식
    - 터미널이 입력만 되고 동작하지 않음.
    - gedit을 종료해야 터미널을 이어서 사용 가능
    - 간단한 작업 시 사용

2. **`gedit ./파일이름 &` : background 실행**
    - 하나의 터미널에서 여러 개의 프로세스를 실행할 수 있는 방식
    - 터미널도, gedit도 잘 동작함
    - 시간이 오래 걸리는 작업 시사용

#### 찾기 : Ctrl + F

- 화살표 버튼 : 다음 / 이전 찾기

#### 바꾸기 : Ctrl + H

- 찾은 다음 바꾸기

<br>

## vi 체험

### vi : <span style='color: red;'>vi</span>sual editor

임베디드 리눅스란 ? 

-> 임베디드 환경에서 동작하는 리눅스를 통틀어서 말하는 것

<span style='color: red;'>특징 : 경량, 안쓰는 기능들 모두 제거 </span>

### 터미널 창에서 vi 실행

`vi "텍스트파일 이름".txt

### 글 입력하기

1. ESC를 여러번 일단 눌러준다.

2. i를 한 번 누른다. (vi가 글자 Insert 모드로 변함)

3. 원하는 글을 입력한다.

### 종료하기

1. ESC를 여러번 눌러준다.

2. 콜론 ":"을 입력한다.

3. q! 를 입력 후 엔터를 누른다.

### 파일 저장하기

1. ESC를 여러번 눌러준다.

2. 콜론 ":"을 입력한다.

3. wq 를 입력 후 엔터를 누른다.

4. ls로 저장이 되었는지 확인

<br>

## vim 다루기

: VI iMproved

: vs code의 원조, 플러그인 설치 가능하도록 vi의 업그레이드 판

! 통상 전부 vi라고 불린다.

### vim 설치

1. 버전 확인하기 : `vi --version`

2. Vim8 Huge 버전 설치

    `sudo apt install vim -y`

[응용 : Hello World 작성 후 복붙]

1. i 키 입력 : insert(edit) 모드로 변경

2. Hello world 입력

3. esc 키 입력 : 커맨드 모드로 변경

4. p / shift + p (커맨드 모드에서만 가능)

5. h/j/k/l 로 방향키 이동하기

### Command Mode

1. vi를 시작할 때 진입하는 모드

2. ESC를 한 번 누르면 진입하면 모드

- 저장, 읽기, 닫기
- 커서 이동, page up / down
- `:`를 눌러 문자열로 명령어 입력이 가능

#### 단축키

- `gg` : 글 처음으로 이동하는 명령어
    - 원하는 줄로 이동 : `원하는 줄 + gg`

- `G` : 글 맨 마지막으로 이동하는 명령어

- `dd` : 한 줄 삭제

### Edit(Insert) 모드

- 타이밍 가능 모드
- command 모드에서 `i`를 눌러 모드 진입이 가능하다.
- `i` : 커서 앞쪽으로 insert 모드
- `a` : 커서 뒷쪽으로 insert 모드

<br>

## vi를 메모장 처럼

[사전 준비]

- Line number 넣기 : `set nu`

- Line number 빼기 : `set nonu`

[반드시 알아야 하는 기능]

- 저장, 불러오기

- 맨 위로 이동, 맨 아래로 이동 : gg / shift + g

- <span style='color: red;'>복사 붙여넣기</span>

    - 복사 : Visual Mode에서 영역을 선택한 후 `y`를 누르기
        - 한 줄 복사 : `yy`
        - 여러 줄 복사 : `복사하고자 하는 줄 개수 + yy`
    - 붙여넣기 : Visual Mode에서 `p`를 누르면 커서 뒷쪽에 붙여넣기가 된다.

        - `shift + p` : 커서 앞쪽으로 붙여넣기

- <span style='color: red;'>실행 취소, 다시 실행</span>

    - 실행 취소 : `u`

    - 다시 실행 : `Ctrl + r`

- <span style='color: red;'>찾기, 치환</span>

    - 찾기 : command mode에서 `/찾을단어`
        - 문자열의 앞 쪽에 커서 위치
    - 다음 검색 : `n`
    - 이전 검색 : `N`

    - 치환 : command line의 명령어 사용

        `:%s/찾을단어/바꿀단어/바꾸고자 하는 것들 선택`
        
        - g : global. 파일 전체의 단어를 바꾼다.

        - c : 어떤 방식으로 바꿀지 선택

- <span style='color: red;'>한 줄 삭제</span>

    - `dd`

    - 여러 줄 삭제 : `삭제하고자 하는 줄 개수 + dd`

### Visual Mode

- 블록을 잡는 모드

- Command 모드에서 `v`를 눌러 Visual 모드로 진입한다.

#### Home / End : `shift + 4 / shift + 6`