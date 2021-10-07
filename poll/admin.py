from django.contrib import admin
from .models import Question
# 클래스 테이블(객체) 등록
admin.site.register(Question)