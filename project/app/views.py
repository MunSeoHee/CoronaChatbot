from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from .models import User

# Create your views here.
def keyboard(request):
    return redirect('/message/info')


@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    
    if return_str == '확진자 정보' :
      id = return_json_str["userRequest"]["user"]["id"]
      obj, create = User.objects.get_or_create(
        id = id,
        location = '확진자 정보'
      )
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
    
    if return_str == "블록" :
      return JsonResponse({
          "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": return_json_str['userRequest']['block']['id']
                    }
                }
            ]
        }
        })
    if return_str == "테스트" :
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
        "action": "block",
        "blockId":"info",
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

    if return_str == '그 외' :
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

    if return_str == '다른 지역' :
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
