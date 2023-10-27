from django.urls import path
from . import views

app_name = 'weathers'
urlpatterns = [
    
    # 1. 날씨 API 테스트
    path('', views.index, name='index'),
    # 2. 서울의 5일 치 예보 데이터 확인
    path('save-data/', views.save_data, name='save_data'),
    # 3. 예보 데이터 중 원하는 데이터만 DB에 저장
    path('list-data/', views.list_data, name='list_data'),
    # 4. 저장된 데이터 전체 조회
    # 5. 특정 조건 데이터 확인(ex. 섭씨 30도 이상 시간대 조회)
    
]
