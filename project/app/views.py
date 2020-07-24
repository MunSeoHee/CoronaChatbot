#-*- coding:utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from .models import User
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
# read Seoul Data


# Create your views here.
def keyboard(request):
    return JsonResponse({
"version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "무엇을 알고싶으신가요?"
        }
      }
    ],
    "quickReplies": [
      {
        "messageText": "확진자 정보",
        "action": "message",
        "label": "확진자 정보"
      },
      {
        "messageText": "마스크 약국 현황",
        "action": "message",
        "label": "근처 약국 현황"
      },
      {
        "messageText": "위탁병원 정보",
        "action": "message",
        "label": "위탁 병원 정보"
      }
    ]
  }
})


@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']



    if return_str == '도봉구' or return_str == '동대문구' or return_str == '동작구' or return_str == '은평구' or return_str == '강북구' or return_str == '강동구' or return_str == '강남구' or return_str == '강서구' or return_str == '금천구' or return_str == '구로구' or return_str == '관악구' or return_str == '광진구' or return_str == '종로구' or return_str == '중구' or return_str == '중랑구' or  return_str == '마포구' or return_str == '노원구'or return_str == '서초구' or  return_str == '서대문구' or return_str == '성북구' or return_str == '성동구' or return_str == '송파구' or return_str == '양천구' or return_str == '영등포구' or return_str == '용산구':
      id = return_json_str["userRequest"]["user"]["id"]
      choice = User.objects.get(userId=id)
      if choice.location == '확진자 정보':
        if return_str == '도봉구':
          x = "도봉구	어린이집	2020-06-24	격리 중\n도봉구	어린이집	2020-06-23	격리 중\n도봉구	어린이집	2020-06-23	격리 중\n도봉구	어린이집	2020-06-23	격리 중\n도봉구	어린이집	2020-06-21	격리 중\n도봉구	어린이집	2020-06-20	격리 중\n도봉구	어린이집	2020-06-20	격리 중\n도봉구	어린이집	2020-06-19	격리 중\n도봉구	어린이집	2020-06-19	격리 중\n도봉구	어린이집	2020-06-18	격리 중"
        elif return_str == '동대문구':
          x = "동대문구	강남 역삼동 모임	2020-06-27	격리 중\n동대문구	강남 역삼동 모임	2020-06-26	격리 중\n동대문구	해외 유입	2020-06-19	격리 중\n동대문구	리치웨이	2020-06-05	격리해제\n동대문구	이태원 클럽	2020-05-14	격리해제\n동대문구	이태원 클럽	2020-05-12	격리해제\n동대문구	이태원 클럽	2020-05-10	격리해제\n동대문구	해외 유입	2020-04-07	격리해제\n동대문구	확진자 접촉	2020-04-04	격리해제\n동대문구	해외 유입	2020-04-04	격리해제"
        elif return_str == '강남구':
          x = "강남구	강남 역삼동 모임	2020-06-27	격리 중\n강남구	확진자 접촉	2020-06-24	격리 중\n강남구	리치웨이	2020-06-22	격리 중\n강남구	리치웨이	2020-06-17	격리 중\n강남구	리치웨이	2020-06-16	격리 중\n강남구	리치웨이	2020-06-03	격리해제\n강남구	삼성화재	2020-06-03	격리 중\n강남구	확인불가	2020-06-02	격리 중\n강남구	해외 유입	2020-05-31	격리해제\n강남구	구리 집단감염	2020-05-29	격리해제"
        elif return_str == '강동구':
          x = "강동구	확진자 접촉	2020-06-22	격리 중\n강동구	확인불가	2020-06-22	격리 중\n강동구	확인불가	2020-06-12	격리해제\n강동구	해외 유입	2020-06-11	격리 중\n강동구	리치웨이	2020-06-07	격리 중\n강동구	리치웨이	2020-06-05	격리해제\n강동구	리치웨이	2020-06-05	격리 중\n강동구	리치웨이	2020-06-04	격리해제\n강동구	용인 Brothers	2020-06-04	격리해제\n강동구	해외 유입	2020-06-02	격리해제"
        elif return_str == '강북구':
          x = "강북구	확인불가	2020-06-18	격리 중\n강북구	리치웨이	2020-06-13	격리해제\n강북구	어린이집	2020-06-12	격리 중\n강북구	어린이집	2020-06-12	격리 중\n강북구	양천 탁구클럽	2020-06-07	격리해제\n강북구	양천 탁구클럽	2020-06-06	격리해제\n강북구	리치웨이	2020-06-05	격리해제\n강북구	확인불가	2020-06-03	격리 중\n강북구	서초 Family	2020-06-02	격리해제\n강북구	KB 생명	2020-06-02	격리해제"
        elif return_str == '강서구':
          x = "강서구	확진자 접촉	2020-06-25	격리 중\n강서구	리치웨이	2020-06-22	격리 중\n강서구	확인불가	2020-06-21	격리 중\n강서구	대자연	2020-06-20	격리 중\n강서구	금천구 쌀 제조공장	2020-06-19	격리 중\n강서구	금천구 쌀 제조공장	2020-06-18	격리 중\n강서구	확인불가	2020-06-18	격리 중\n강서구	SMR	2020-06-17	격리 중\n강서구	대자연	2020-06-17	격리 중\n강서구	양천 탁구클럽	2020-06-13	격리 중"
        elif return_str == '관악구':
          x = "관악구	확진자 접촉	2020-06-28	격리 중\n관악구	왕성교회	2020-06-27	격리 중\n관악구	왕성교회	2020-06-27	격리 중\n관악구	확인불가	2020-06-27	격리 중\n관악구	왕성교회	2020-06-27	격리 중\n관악구	왕성교회	2020-06-27	격리 중\n관악구	왕성교회	2020-06-26	격리 중\n관악구	왕성교회	2020-06-26	격리 중\n관악구	왕성교회	2020-06-26	격리 중\n관악구	왕성교회	2020-06-26	격리 중"
        elif return_str == '광진구':
          x = "광진구	강남 역삼동 모임	2020-06-26	격리 중\n광진구	리치웨이	2020-06-18	격리 중\n광진구	리치웨이	2020-06-10	격리해제\n광진구	이태원 클럽	2020-05-27	격리해제\n광진구	이태원 클럽	2020-05-21	격리해제\n광진구	이태원 클럽	2020-05-14	격리해제\n광진구	이태원 클럽	2020-05-10	격리해제\n광진구	이태원 클럽	2020-05-09	격리해제\n광진구	이태원 클럽	2020-05-09	격리해제\n광진구	해외 유입	2020-04-09	격리해제"
        elif return_str == '구로구':
          x = "구로구	왕성교회	2020-06-28	격리 중\n구로구	확진자 접촉	2020-06-27	격리 중\n구로구	확진자 접촉	2020-06-26	격리 중\n구로구	확진자 접촉	2020-06-25	격리 중\n구로구	확진자 접촉	2020-06-24	격리 중\n구로구	확인불가	2020-06-23	격리 중\n구로구	리치웨이	2020-06-21	격리 중\n구로구	리치웨이	2020-06-21	격리 중\n구로구	확진자 접촉	2020-06-21	격리 중\n구로구	리치웨이	2020-06-21	격리 중"
        elif return_str == '금천구':
          x = "금천구	확진자 접촉	2020-06-29	격리 중\n금천구	확인불가	2020-06-24	격리 중\n금천구	리치웨이	2020-06-15	격리 중\n금천구	리치웨이	2020-06-12	격리 중\n금천구	리치웨이	2020-06-13	격리 중\n금천구	양천 탁구클럽	2020-06-11	격리 중\n금천구	리치웨이	2020-06-11	격리해제\n금천구	리치웨이	2020-06-11	격리 중\n금천구	리치웨이	2020-06-10	격리해제\n금천구	리치웨이	2020-06-10	격리 중"
        elif return_str == '노원구':
          x = "노원구	해외 유입	2020-06-29	격리 중\n노원구	왕성교회	2020-06-28	격리 중\n노원구	왕성교회	2020-06-26	격리 중\n노원구	확진자 접촉	2020-06-25	격리 중\n노원구	리치웨이	2020-06-20	격리 중\n노원구	리치웨이	2020-06-20	격리 중\n노원구	리치웨이	2020-06-12	격리 중\n노원구	리치웨이	2020-06-11	격리 중\n노원구	해외 유입	2020-06-10	격리해제\n노원구	확진자 접촉	2020-06-05	격리 중"
        elif return_str == '동작구':
          x = "동작구	왕성교회	2020-06-26	격리 중\n동작구	확진자 접촉	2020-06-26	격리 중\n동작구	왕성교회	2020-06-25	격리 중\n동작구	확인불가	2020-06-20	격리 중\n동작구	대전 방문 판매	2020-06-19	격리 중\n동작구	리치웨이	2020-06-16	격리 중\n동작구	확진자 접촉	2020-06-16	격리해제\n동작구	리치웨이	2020-06-15	격리 중\n동작구	리치웨이	2020-06-10	격리해제\n동작구	확인불가	2020-06-09	격리 중"
        elif return_str == '마포구':
          x = "마포구	리치웨이	2020-06-29	격리 중\n마포구	리치웨이	2020-06-29	격리 중\n마포구	리치웨이	2020-06-27	격리 중\n마포구	리치웨이	2020-06-29	격리 중\n마포구	확인불가	2020-06-19	격리 중\n마포구	확진자 접촉	2020-06-18	격리 중\n마포구	기타	2020-06-16	격리해제\n마포구	리치웨이	2020-06-09	격리해제\n마포구	리치웨이	2020-06-06	격리 중\n마포구	삼성화재	2020-06-04	격리해제"
        elif return_str == '서대문구':
          x = "서대문구	오렌지 라이프	2020-06-19	격리 중\n서대문구	해외 유입	2020-06-18	격리 중\n서대문구	SMR	2020-06-15	격리해제\n서대문구	해외 유입	2020-06-14	격리 중\n서대문구	확인불가	2020-06-08	deceased\n서대문구	서초 Family	2020-06-02	격리해제\n서대문구	서초 Family	2020-06-02	격리해제\n서대문구	SMR	2020-06-01	격리해제\n서대문구	해외 유입	2020-05-30	격리해제\n서대문구	연아나 뉴스 클래스	2020-05-29	격리해제"
        elif return_str == '서초구':
          x = "서초구	해외 유입	2020-06-28	격리 중\n서초구	왕성교회	2020-06-26	격리 중\n서초구	의왕 물류 센터	2020-06-20	격리 중\n서초구	리치웨이	2020-06-19	격리 중\n서초구	리치웨이	2020-06-18	격리해제\n서초구	리치웨이	2020-06-16	격리해제\n서초구	확진자 접촉	2020-06-17	격리 중\n서초구	확인불가	2020-06-14	격리해제\n서초구	리치웨이	2020-06-13	격리 중\n서초구	리치웨이	2020-06-11	격리해제"
        elif return_str == '성동구':
          x = "성동구	금천구 쌀 제조공장	2020-06-20	격리 중\n성동구	금천구 쌀 제조공장	2020-06-20	격리 중\n성동구	확인불가	2020-06-09	격리해제\n성동구	확인불가	2020-06-07	격리해제\n성동구	이태원 클럽	2020-06-07	격리해제\n성동구	이태원 클럽	2020-06-06	격리 중\n성동구	확인불가	2020-06-06	격리해제\n성동구	이태원 클럽	2020-06-05	격리해제\n성동구	해외 유입	2020-06-02	격리해제\n성동구	확인불가	2020-05-29	격리해제"
        elif return_str == '성북구':
          x = "성북구	해외 유입	2020-06-21	격리 중\n성북구	확인불가	2020-06-18	격리 중\n성북구	리치웨이	2020-06-10	격리해제\n성북구	확인불가	2020-06-12	격리해제\n성북구	확인불가	2020-05-29	격리해제\n성북구	이태원 클럽	2020-05-18	격리해제\n성북구	이태원 클럽	2020-05-10	격리해제\n성북구	이태원 클럽	2020-05-09	격리해제\n성북구	이태원 클럽	2020-05-08	격리해제\n성북구	해외 유입	2020-04-27	격리해제"
        elif return_str == '송파구':
          x = "송파구	왕성교회	2020-06-28	격리 중\n송파구	강남 역삼동 모임	2020-06-27	격리 중\n송파구	확인불가	2020-06-21	격리 중\n송파구	해외 유입	2020-06-16	격리 중\n송파구	쿠팡 물류센터	2020-06-10	격리해제\n송파구	양천 탁구클럽	2020-06-05	격리해제\n송파구	확인불가	2020-06-01	격리해제\n송파구	성서 연구 모임	2020-05-29	격리해제\n송파구	성서 연구 모임	2020-05-28	격리해제\n송파구	쿠팡 물류센터	2020-05-27	격리 중"
        elif return_str == '양천구':
          x = "양천구	해외 유입	2020-06-27	격리 중\n양천구	양천 탁구클럽	2020-06-19	격리 중\n양천구	양천 탁구클럽	2020-06-19	격리 중\n양천구	확인불가	2020-06-18	격리 중\n양천구	대자연	2020-06-18	격리 중\n양천구	SMR	2020-06-12	격리 중\n양천구	확인불가	2020-06-12	격리해제\n양천구	리치웨이	2020-06-11	격리 중\n양천구	양천 탁구클럽	2020-06-10	격리해제\n양천구	리치웨이	2020-06-10	격리 중"
        elif return_str == '영등포구':
          x = "영등포구	왕성교회	2020-06-27	격리 중\n영등포구	확인불가	2020-06-27	격리 중\n영등포구	해외 유입	2020-06-23	격리 중\n영등포구	시청역 안전요원	2020-06-20	격리 중\n영등포구	시청역 안전요원	2020-06-20	격리 중\n영등포구	의왕 물류 센터	2020-06-20	격리 중\n영등포구	시청역 안전요원	2020-06-19	격리 중\n영등포구	확진자 접촉	2020-06-19	격리 중\n영등포구	리치웨이	2020-06-18	격리 중\n영등포구	리치웨이	2020-06-17	격리 중"
        elif return_str == '용산구':
          x = "용산구	확진자 접촉	2020-06-28	격리 중\n용산구	확인불가	2020-06-27	격리 중\n용산구	리치웨이	2020-06-15	격리 중\n용산구	리치웨이	2020-06-15	격리 중\n용산구	리치웨이	2020-06-14	격리 중\n용산구	리치웨이	2020-06-06	격리 중\n용산구	리치웨이	2020-06-12	격리해제\n용산구	리치웨이	2020-06-06	격리해제\n용산구	리치웨이	2020-06-05	격리 중\n용산구	리치웨이	2020-06-05	격리 중"
        elif return_str == '은평구':
          x = "은평구	확인불가	2020-06-29	격리 중\n은평구	해외 유입	2020-06-26	격리 중\n은평구	확진자 접촉	2020-06-19	격리 중\n은평구	리치웨이	2020-06-18	격리 중\n은평구	확인불가	2020-06-17	격리 중\n은평구	양천 탁구클럽	2020-06-17	격리 중\n은평구	확인불가	2020-06-16	격리해제\n은평구	확인불가	2020-06-16	격리해제\n은평구	양천 탁구클럽	2020-06-16	격리 중\n은평구	확인불가	2020-06-15	격리 중"
        elif return_str == '종로구':
          x = "종로구	해외 유입	2020-06-24	격리 중\n종로구	확인불가	2020-06-13	격리 중\n종로구	한국 캠퍼스 십자군	2020-06-12	격리해제\n종로구	한국 캠퍼스 십자군	2020-05-29	격리해제\n종로구	해외 유입	2020-05-17	격리해제\n종로구	이태원 클럽	2020-05-08	격리해제\n종로구	해외 유입	2020-04-02	격리해제\n종로구	해외 유입	2020-03-31	격리해제\n종로구	해외 유입	2020-03-31	격리해제\n종로구	확진자 접촉	2020-03-24	격리해제"
        elif return_str == '중구':
          x = "중구	해외 유입	2020-06-26	격리 중\n중구	리치웨이	2020-06-18	격리 중\n중구	양천 탁구클럽	2020-06-09	격리 중\n중구	KB 생명	2020-05-28	격리해제\n중구	이태원 클럽	2020-05-11	격리해제\n중구	이태원 클럽	2020-05-08	격리해제\n중구	확진자 접촉	2020-04-15	격리해제\n중구	확진자 접촉	2020-03-31	격리해제\n중구	확진자 접촉	2020-03-30	격리해제\n중구	해외 유입	2020-03-28	격리해제"
        elif return_str == '중랑구':
          x = "중랑구	강남 역삼동 모임	2020-06-26	격리 중\n중랑구	해외 유입	2020-06-25	격리 중\n중랑구	확인불가	2020-06-19	격리 중\n중랑구	리치웨이	2020-06-23	격리 중\n중랑구	어린이집	2020-06-18	격리 중\n중랑구	양천 탁구클럽	2020-06-16	격리 중\n중랑구	리치웨이	2020-06-13	격리해제\n중랑구	확인불가	2020-06-12	격리 중\n중랑구	확인불가	2020-06-12	격리 중\n중랑구	리치웨이	2020-06-12	격리해제"


        return JsonResponse({
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text":x
                }
            }
        ], 
        "quickReplies": [
      {
        "messageText": "확진자 정보",
        "action": "message",
        "label": "확진자 정보"
      },
      {
        "messageText": "마스크 약국 현황",
        "action": "message",
        "label": "근처 약국 현황"
      },
      {
        "messageText": "위탁병원 정보",
        "action": "message",
        "label": "위탁 병원 정보"
      }
    ]
    }
})
      elif choice.location == '마스크 약국 현황':
        #sadasd


        addr = []


        open_url='http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=wR48WNzLvEyNkXNTpr3%2Fn62V29gWjkmqZluf%2BSurBS1GC9RRm9BGj6BF%2FBqQvUWSH5LU5NG%2BzKxrGYokLgq2%2Fg%3D%3D&Q0=서울특별&Q1='+return_str+'&ORD=NAME&pageNo=1&numOfRows=10'


        res= requests.get(open_url)

        yak= BeautifulSoup(res.content,'html.parser')

        data=yak.find_all('item')

        for item in data:
            addr.append(item.find('dutytel1').get_text())




        #sdaasdasd
        return JsonResponse({
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[0]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[1]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[2]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[3]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[4]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[5]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[6]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[7]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[8]
                }
              ]
            },
             {
              "title": "약국",
              "description": "근처약국을 알려드려요",

              "buttons": [
                {
                  "action":  "webLink",
                  "label": "지도보기",
                  "webLinkUrl": "https://map.naver.com/v5/search/"+addr[9]
                }
              ]
            }
          ]
        }
      }
    ],
    "quickReplies": [
      {
        "messageText": "확진자 정보",
        "action": "message",
        "label": "확진자 정보"
      },
      {
        "messageText": "마스크 약국 현황",
        "action": "message",
        "label": "근처 약국 현황"
      },
      {
        "messageText": "위탁병원 정보",
        "action": "message",
        "label": "위탁 병원 정보"
      }
    ]
  }
})
      elif choice.location == '위탁병원 정보':
        if return_str == '도봉구':
          x = "도봉병원 02)3492-3250 서울특별시 도봉구 도봉로 720 (방학동)"
        elif return_str == '동대문구':
          x = "서울나은병원 1544-6003 서울특별시 동대문구 왕산로 137(제기동)\n현대중앙의원 02)2244-9600 서울특별시 동대문구 사가정로 110 (전농동)"
        elif return_str == '강남구':
          x = "강남베드로병원 02-1544-7522 남부순환로 2633(도곡동 914-2)"
        elif return_str == '강동구':
          x = "강동성모요양병원 02)488-0020 서울특별시 강동구 올림픽로80길31"
        elif return_str == '강북구':
          x = "신일병원 02)903-5121 서울특별시 강북구 덕릉로 73 (수유동)"
        elif return_str == '강서구':
          x = "강서연세병원 02)2658-5114 서울특별시 강서구 양천로 712 (염창동)\n강서힘찬병원 1899-2228 서울시 강서구 강서로56길 38(등촌동)"
        elif return_str == '관악구':
          x = "사랑의병원 02)880-0114 서울특별시 관악구 남부순환로 1860 (봉천동)"
        elif return_str == '광진구':
          x = "김종웅내과의원 02)455-4038 서울시 광진구 용마산로 44"
        elif return_str == '구로구':
          x = "권내과의원 02)2685-6612 서울시 구로구 경안로40길 34(개봉동)"
        elif return_str == '금천구':
          x = "연세조내과 02)803-2134 서울특별시 금천구 시흥대로58길 5 (시흥동)\n서울으뜸정형외과의원 02)807-0111 서울시 금천구 독산로 210, 2층"
        elif return_str == '노원구':
          x = "밝은미래안과 02)939-3075 서울특별시 노원구 동일로 1548, 세일빌딩 4층 (상계동)\n삼성드림이비인후과 02)935-1365 서울특별시 노원구 노해로 482, 덕영빌딩 4층 (상계동)\n새서울병원 02)930-5858 서울특별시 노원구 동일로 1678 (상계동)\n어비뇨기과 02)930-013 서울특별시 노원구 동일로 1401 (상계동)"
        elif return_str == '동작구':
          x = "의료법인성석의료재단 동작경희병원 02)822-8112 서울특별시 동작구 상도로 146"
        elif return_str == '마포구':
          x = "박상수내과의원 02)332-5460 서울특별시 마포구 독막로 22 (합정동)\n예담정형외과의원 02-335-2500 서울 마포구 독막로 22(합정동 청명빌딩 3층)\n서울본내과의원 02)3143-2220 서울특별시 마포구 양화로133"
        elif return_str == '서대문구':
          x = "한양그린내과의원 02)379-3377 서울특별시 서대문구 통일로 413, 화인빌딩 2층 (홍제동)"
        elif return_str == '서초구':
          x = "김일중내과 02)3473-1356 서울특별시 서초구 효령로 396 (서초동)"
        elif return_str == '성동구':
          x = "9988병원 02)2297-9988 서울특별시 성동구 왕십리로269"
        elif return_str == '성북구':
          x = "서울척병원 1599-0033 서울특별시 성북구 동소문로 47길 8\n의료법인 유라의료재단 온누리요양병원 02)919-2700 서울특별시 성북구 화랑로 271 (장위동)"
        elif return_str == '송파구':
          x = "서울수내과의원 02)414-9919 서울특별시 송파구 송파대로 389, 2층 (석촌동)"
        elif return_str == '양천구':
          x = "메디힐병원 02)2604-7551 서울특별시 양천구 남부순환로 331 (신월동)"
        elif return_str == '영등포구':
          x = "jc빛소망 안과 02)785-1068 서울특별시 영등포구 국제금융로 6길 33, 6층(여의도동)\n아이비이비인후과 02)784-7533 서울 영등포구 여의도동 43-4\n윤문수비뇨기과 02)2069-0221 서울특별시 영등포구 영중로 46, 4층 (영등포동5가)\n의료법인 영등포병원 02)2632-0013 서울 영등포구 당산로 31길 10\n김종률내과의원 02)831-1585 서울 영등포구 신길로 28"
        elif return_str == '용산구':
          x = "김내과의원 02)703-2226 서울특별시 용산구 백범로 281 (효창동)"
        elif return_str == '은평구':
          x = "본서부병원 02)3156-5020 서울특별시 은평구 은평로133"
        elif return_str == '종로구':
          x = "서울적십자병원 02)2002-8000 서울특별시 종로구 새문안로 9 (평동)"
        elif return_str == '중구':
          x = "삼성푸른의원 02)2231-4154 서울특별시 중구 다산로42길 80 (신당동)"
        elif return_str == '중랑구':
          x = "팔팔(88)병원 1899-8875 서울특별시 중랑구 동일로 679\n건강한 성심의원 02-437-6152 서울특별시 중랑구 용마산로 503"
        return JsonResponse({
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": x
                }
            }
        ],
        "quickReplies": [
      {
        "messageText": "확진자 정보",
        "action": "message",
        "label": "확진자 정보"
      },
      {
        "messageText": "마스크 약국 현황",
        "action": "message",
        "label": "근처 약국 현황"
      },
      {
        "messageText": "위탁병원 정보",
        "action": "message",
        "label": "위탁 병원 정보"
      }
    ]


    }
})




    elif return_str == '확진자 정보' or return_str == '지역선택' or  return_str=='마스크 약국 현황' or return_str =='위탁병원 정보' :
        if return_str ==  '확진자 정보':
          x = '확진자 정보'

        elif return_str == '마스크 약국 현황':
          x = '마스크 약국 현황'

        elif return_str == '위탁병원 정보':
          x = '위탁병원 정보'

        elif return_str == '지역선택':
          x = '지역선택'

        id = return_json_str["userRequest"]["user"]["id"]

        obj, create = User.objects.get_or_create(userId = id)
        obj.location = x
        obj.save()

        return JsonResponse({
          "version": "2.0",
            "template": {
              "outputs": [
                {
                  "simpleText": {
                    "text": "지역을 선택해주세요"
                  }
                }
              ],
              "quickReplies": [
                {
                  "messageText": "강남구",
                  "action": "message",
                  "label": "강남구"
                },
                {
                  "messageText": "강동구",
                  "action": "message",
                  "label": "강동구"
                },
                {
                  "messageText": "강북구",
                  "action": "message",
                  "label": "강북구"
                },
                {
                  "messageText": "강서구",
                  "action": "message",
                  "label": "강서구"
                },
                {
                  "messageText": "관악구",
                  "action": "message",
                  "label": "관악구"
                },
                {
                  "messageText": "광진구",
                  "action": "message",
                  "label": "광진구"
                },
                {
                  "messageText": "구로구",
                  "action": "message",
                  "label": "구로구"
                },
                {
                  "messageText": "금천구",
                  "action": "message",
                  "label": "금천구"
                },
                {
                  "messageText": "노원구",
                  "action": "message",
                  "label": "노원구"
                },
                {
                  "messageText": "그 외",
                  "action": "message",
                  "label": "그 외"
                }
              ]
            }
          })




    elif return_str == '그 외' :
      return JsonResponse({
"version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "지역을 선택해주세요"
        }
      }
    ],
    "quickReplies": [
      {
        "messageText": "도봉구",
        "action": "message",
        "label": "도봉구"
      },
      {
        "messageText": "동대문구",
        "action": "message",
        "label": "동대문구"
      },
      {
        "messageText": "동작구",
        "action": "message",
        "label": "동작구"
      },
      {
        "messageText": "마포구",
        "action": "message",
        "label": "마포구"
      },
      {
        "messageText": "서대문구",
        "action": "message",
        "label": "서대문구"
      },
      {
        "messageText": "서초구",
        "action": "message",
        "label": "서초구"
      },
      {
        "messageText": "성동구",
        "action": "message",
        "label": "성동구"
      },
      {
        "messageText": "성북구",
        "action": "message",
        "label": "성북구"
      },
      {
        "messageText": "송파구",
        "action": "message",
        "label": "송파구"
      },
      {
        "messageText": "다른 지역",
        "action": "message",
        "label": "다른 지역"
      }
    ]
  }
})

    elif return_str == '다른 지역' :
      return JsonResponse({
    "version": "2.0",
      "template": {
        "outputs": [
          {
            "simpleText": {
              "text": "지역을 선택해주세요"
            }
          }
        ],
        "quickReplies": [
          {
            "messageText": "양천구",
            "action": "message",
            "label": "양천구"
          },
          {
            "messageText": "영등포구",
            "action": "message",
            "label": "영등포구"
          },
          {
            "messageText": "용산구",
            "action": "message",
            "label": "용산구"
          },
          {
            "messageText": "은평구",
            "action": "message",
            "label": "은평구"
          },
          {
            "messageText": "종로구",
            "action": "message",
            "label": "종로구"
          },
          {
            "messageText": "중구",
            "action": "message",
            "label": "중구"
          },
          {
            "messageText": "중랑구",
            "action": "message",
            "label": "중랑구"
          },
          {
            "messageText": "지역 선택",
            "action": "message",
            "label": "지역 선택"
          }
        ]
      }
    })

    else:
        return JsonResponse({
"version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "무엇을 알고싶으신가요?"
        }
      }
    ],
    "quickReplies": [
      {
        "messageText": "확진자 정보",
        "action": "message",
        "label": "확진자 정보"
      },
      {
        "messageText": "마스크 약국 현황",
        "action": "message",
        "label": "근처 약국 현황"
      },
      {
        "messageText": "위탁병원 정보",
        "action": "message",
        "label": "위탁 병원 정보"
      }
    ]
  }
})
