# 02_pjt - ver1_금융

## 넷플릭스 주가 데이터 분석

프로젝트 풀이 계획 

    1. 데이터는 csv 파일로 주어짐

    2. 데이터가 Table 형식을 띄고 있었기 때문에 numpy를 사용하는 대신 pandas library를 사용하였다.

    3. matplotlib를 사용하여 그래프 도식화 진행


### A. 데이터 전처리 - 2021년 이후의 종가 데이터 출력하기

#### 학습한 내용 

1. pandas 를 사용하여 csv 파일을 DataFrame으로 읽어오는 과정 수행.

2. DataFrame으로 읽어오는 과정 진행 중 특정 열의 정보만을 불러오는 과정(usecols)을 사용하여 특정 정보에 대한 데이터만을 가져옴


```python
data = pd.read_csv("NFLX.csv", encoding='cp949', usecols=range(0, 5))
```

- cp949 : 한국어판 MS Windows의 기본 코드 페이지로, 한글 인코딩의 한 종류이며 EUC-KR의 확장형[IT위키 참조]

- 총 column 7개 중 Adj close와 Volume은 사용하지 않았기 때문에 range()를 사용하여 Date 부터 Close까지의 정보를 불러왔다.


#### 어려웠던 부분

- pandas의 기본이 되는 csv 파일을 불러오는 과정이기 떄문에 어려움 없이 수행할 수 있었다.


### B. 데이터 전처리 - 2021년 이후의 종가 데이터 출력하기

#### 학습한 내용 

1. 불러온 csv DataFrame의 열 정보를 활용하는 방법.
    불러온_csv_file_변수.(['열 이름'])

2. to_datetime() 함수를 활용하여 object 형을 datetime 형으로 형변환 시켜주는 과정

```python
data_after_2021 = data[data['Date'] > "2021-01-01"]
```

3. matplotlib의 다양한 메서드들을 활용하여 2021년 이후 종가 데이터를 도식화

```python
plt.plot(data_after_2021['Date'], data_after_2021['Close'])

plt.title("NFLX Close Price")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)
plt.show()
```

#### 어려웠던 부분

- datetime 형에 익숙하지 않아 어떠한 방식으로 타입이 구성되는지 이해가 필요함


### C. 데이터 분석 - 2021년 이후 최고, 최저 종가 출력하기

#### 학습한 내용

1. 각 열의 전체 데이터들에 대해 min(), max() 메서드를 사용할 수 있음

```python
max_price = data_after_2021['Close'].max()
min_price = data_after_2021['Close'].min()
```

#### 어려웠던 부분

- min(), max() 메서드는 자주 쓰이기 떄문에 어려움 없이 사용했음


### D. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기

#### 학습한 내용

1. 본 문제는 datetime 형에 대한 이해가 필요함

    1-1. 일 정보는 필요하지 않으므로, Date_m이라는 새로운 열 변수를 만들어 주어 연, 월 정보만을 사용한 새로운 열 생성

        datetime 형은 "%y-%m-%d"로 구성되어 있는데 이 중 y, m 정보를 사용

        dt.strftime() 메서드를 통해 필요한 정보를 불러와 새로운 열 생성

    ```python
    data_after_2021['Date_m'] = data_after_2021['Date'].dt.strftime("%Y-%m")
    ```

2. 같은 달 정보에 대해 하나의 그룹으로 묶어주는 과정이 필요

    2-1. groupby() 메서드를 사용하여 같은 그룹에 있는 Close 값들에 대해 mean() 메서드를 사용하여 평균내어줌

    ```python
    data_after_2021.groupby('Date_m')['Close'].mean()
    ```

#### 어려웠던 부분

- problem B와 마찬가지로 datetime 형에 대한 이해가 필요함

- pandas 메서드인 groupby()를 인지하고 있어야 하며 동작에 대한 이해가 필요함


### E. 데이터 시각화 - 2022년 이후 최고, 최저, 종가 시각화하기

#### 학습한 내용 

1. 여러 개의 plot을 도식화 하는 과정에 있어서 어떤 plot을 나타내는지에 대한 정보를 제공해야함

    1-1. plot()을 진행할 때 label=""을 통해 어떤 정보에 대한 plot인지 labeling 과정을 진행

    1-2. matplotlib에서 제공하는 legend() 메서드를 사용하여 그래프에 나타내줌

```python
plt.plot(data_after_2022['Date'], data_after_2022['High'], label='High')
plt.plot(data_after_2022['Date'], data_after_2022['Low'], label='Low')
plt.plot(data_after_2022['Date'], data_after_2022['Close'], label='Close')

plt.legend()
```

#### 어려웠던 부분

- matplotlib 을 사용하여 여러 개의 그래프를 plot 해 줄 때는 matlab과 다르게 hold on 을 해 줄 필요가 없음


## 관통 프로젝트를 진행하며 새로 배운 것들 및 느낀점

- 데이터 사이언스에 사용되는 대표적인 라이브러리인 pandas와 matplotlib에 대한 간단한 실습을 통해 친숙해질 수 있었다.

- Table 형 자료에 대해 전처리를 진행할 경우 pandas 라이브러리를 사용. 배열 연산을 수행할 경우 numpy 라이브러리를 사용

- pandas document를 확인해 본다면 매우 다양한 기능들을 제공하고 있는데, 추가적인 실습을 통해 익혀나가면 좋을 것 같다.

