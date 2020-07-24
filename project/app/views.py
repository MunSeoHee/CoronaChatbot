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

    if return_str == '테스트':
        return JsonResponse({
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "보물상자",
          "description": "보물상자 안에는 뭐가 있을까",
          "thumbnail": {
            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
          },
          "profile": {
            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
            "nickname": "보물상자"
          },
          "social": {
            "like": 1238,
            "comment": 8,
            "share": 780
          },
          "buttons": [
            {
              "action": "message",
              "label": "열어보기",
              "messageText": "짜잔! 우리가 찾던 보물입니다"
            },
            {
              "action":  "webLink",
              "label": "구경하기",
              "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
            }
          ]
        }
      }
    ]
  }
})