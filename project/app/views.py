from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
 

    if return_str == "강남구":
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
        "label": "마스크 약국 현황"
      },
      {
        "messageText": "위탁병원 정보",
        "action": "message",
        "label": "위탁 병원 정보"
      }
    ]
  }
})
    if return_str == '테스트':
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
        "messageText": "중구",
        "action": "message",
        "label": "중구"
      },
      {
        "messageText": "서초구",
        "action": "message",
        "label": "서초구"
      },
      {
        "messageText": "송파구",
        "action": "message",
        "label": "송파구"
      }
    ]
  }
})