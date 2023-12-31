# MySQL

- [Database Modelling](#Database-Modelling)

- [개념적 데이터베이스 모델링](#개념적-데이터베이스-모델링)

- [논리적 데이터베이스 모델링](#논리적-데이터베이스-모델링)

- [물리적 데이터베이스 모델링](#물리적-데이터베이스-모델링)

- [동적 게시판 생성을 위한 모델링 실습](#동적-게시판-생성을-위한-모델링-실습)

<br>

## Database Modelling

- 정보화 시스템을 구축하기 위해 어떤 데이터가 존재하는지 또는 업무에 필요한 정보는 무엇인지 분석하는 방법

- 관계형 데이터베이스는 이 '표'의 개념을 사용하여 데이터를 구성하는 방법을 사용.

### 소프트웨어 개발 방법론(Software Development Life Cycle, SDLC)

1. 요구 분석

2. 시스템 명세

3. 설계

    - UI / UX 설계
    - **DB 설계(Modeling)**

4. 구현

5. 테스트

6. 유지보수

<br>

## 개념적 데이터베이스 모델링

: 업무분석 단계에서 얻어진 내용을 토대로 우선 Entity를 추출하고 Entity 내에 속성(Attribute)을 구성하며 Entity 간의 관계를 정의해서 ER-Diagram을 정의하는 단계

개체(class)(네모), 속성(property)(동그라미), 관계(method)(마름모)

- 개체(Entity)

    - 사용자와 관계가 있는 주요 객체로써 업무 수행을 위해 데이터로 관리되어져야 하는 사람, 사물, 장소, 사건 등

    - 영속적으로 존재하는 것

    - 새로 식별이 가능한 데이터 요소를 가짐

    - Entity는 반드시 Attribute를 가져야 함

- 속성(Attribute)

    - 저장할 필요가 있는 실체에 관한 정보

    - 개체(Entity)의 성질, 분류, 수량, 상태, 특성 등을 나타내는 세부사항

    - 개체에 포함되는 속성의 숫자는 10개 내외로 하는 것이 바람직함

    - 최종 DB 모델링 단계를 통해 테이블의 컬럼으로 활용

    - 속성의 유형

        - 기초 속성 : 원래 갖고 있는 속성으로 현업에서 기본적으로 사용되는 속성

        - 추출 속성 : 기초 속성으로부터 계산(가공)에 의해 얻어질 수 있는 속성

        - 설계 속성 : 실제로 존재하지 않으나 시스템의 호율성을 도모하기 위해 설계자가 임의로 부여하는 속성

- 식별자 : 한 개체(Entity) 내에서 인스턴스를 유일하게 구분할 수 있는 단일 속성 또는 속성 그룹

    - 후보키

    - 기본키 : 개체에서 각 인스턴스를 유일하게 식별하는데 가장 적합한 key

    - 대체키

    - 복합키

    - 대리

- 관계(relationship)

    - 두 Entity 간의 업무적인 연관성 또는 관련 사실

    - 각 Entity 간에 특정한 존재여부 결정

    - 현재의 관계 뿐만 아니라 장래에 용될 경우도 고려

    - E-R Diagram으로 관계를 설정하는 순서

        1. 관계가 있는 두 실체를 실선으로 연결하고 관계를 부여
        2. 관계 차수를 표현
        3. 선택성을 표