from django.contrib import admin
from django.urls import path
from config.views import main, burger_list

urlpatterns = [
    path("admin/", admin.site.urls), # views.py에 작성한 main 함수 불러오기
    path("", main), # 공백 (아무것도 입력하지 않은 경로)과 main 함수 연결
    path("burgers/", burger_list),
]