from django.shortcuts import render
import matplotlib.pyplot as plt
# io : 입출력 연산을 위한 Python 표준 라이브러리
from io import BytesIO
'''
BytesIO : 이진 데이터를 다루기 위한 버퍼를 제공
버퍼 : 임시 저장 공간
파일 시스템과 유사하지만 실제로 파일로 만들지 않고 메모리 단에서 작업할 수 있다.
'''
import base64       # 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈

'''
[참고]
PLT를 만드는 곳에 화면에 그리는 곳이 달라서 오류가 날 수 있다고 경고를 준다.
-> 백엔드를 Agg로 설정하여 해결
'''
plt.switch_backend('Agg')

# Create your views here.
def index(request):
    x = [1, 2, 3, 4]
    y = [2, 4, 9, 16]

    plt.plot(x, y)
    plt.title("Graph")
    plt.ylabel('y label')
    plt.xlabel('x label')

    buffer = BytesIO()      # 비어있는 버퍼 생성
    plt.savefig(buffer, format='png')       # 버퍼에 그래프를 저장

    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()      # 버퍼 닫기



    context = {
        # '''
        # 이미지를 웹 페이지에 표시하기 위해
        # URL 형식(주소형식)으로 만들어진 문자열을 생성
        # '''

        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'examples/index.html', context)



import pandas as pd
csv_path = 'C:/Users/SSAFY/Desktop/관통/my/PJT04/matplotlib_django/pjt04Example/data/austin_weather.csv'

def example(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }

    return render(request, 'examples/example.html', context)