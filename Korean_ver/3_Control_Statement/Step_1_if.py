이번에는 제어문인 if문에 대해서 알아보자.

먼저 간단한 예제를 보며 익혀가도록 하자. 예제를 보고 이해하고 응용하는것은 매우 좋은 공부법이다.

>>> money = 1000               # money 라는 변수에 1000을 대입
>>> if money >= 1000:          # 만약 money 가 1000보다 크거나 같다면
...     print("버스 탑승 OK")   # 버스탑승 OK 를 출력하고
... else:                      # 그렇지 않다면
...     print("버스 탑승 불가") # 버스 탑승 불가 라는 문자열을 출력하라
버스 탑승 OK

>>> card = True                # 카드에 True 라는 Boolean 자료형을 입력
>>> if card:                   # 만약 card 가 True면
...     print("버스 탑승 OK")   # 버스 탑승OK 를 출력하고
... else:                      # 그렇지 않다면
...     print("버스 탑승 불가") # 버스 탑승 불가 라는 문자열을 출력하라
버스 탑승 OK

간단한 예제를 통해 if문에 대해 알아보았다. 참고로 if문에서는 위 예제와 같이 if문과 else문 다음의 수행할 문장은 앞에 들여쓰기를 해주어야 한다.
추가적으로 if, else 다음에 붙는 콜론을 절대 잊지말자!

비교 연산자는 boolean 자료형에서 다루었으므로, 아직 이해하지 못했다면 Datatypes 폴더의 boolean 자료형에 대해 읽고 오도록 하자.


- and, or, not

if문에서 배울 또다른 조건식으로는 and, or, not이 있다. 예제를 통해 익혀보도록 하자.

'돈이 1000원 있거나 버스카드가 있으면 버스에 탑승하거라'

>>> money = 500                   # money 라는 변수에 1000을 대입
>>> bus_card = True                # 카드에 True 라는 Boolean 자료형을 입력
>>> if money >= 1000 or bus_card:  # money가 1000보다 크거나 같거나 bus_card 가 True 라면
...     print("버스 탑승 OK")       # 버스 탑승 OK 를 출력
... else:                          # 그렇지 않다면
...     print("버스 탑승 불가")     # 버스 탑승 불가 를 출력
버스 탑승 OK

위 예제에서는 돈이 500원이 있지만, 버스카드가 있으므로 or 조건이 성립되면서 버스 탑승 OK가 출력이된다. 아, 버스카드에 돈이 부족할 일은 없으므로, 걱정
하지않아도 된다.
근데 만약 버스카드에 돈이 없다면 어찌될까. 다음 예제에서는 and 조건식에 대해 다룬다.

'버스카드를 갖고있는데, 버스카드에 1000원이상 들어있으면 버스에 타라!'

>>> bus_card = True                     # bus_card 가 True (버스카드를 소유하고있고)
>>> card_money = 900                    # card_money 는 900을 입력
>>> if bus_card and card_money >= 1000: # bus_card 가 True 이면서 card_money 가 1000 이상일때
...     print("버스 탑승 OK")            # 버스 탑승 OK 출력
... else:                               # 그렇지 않다면
...     print("버스 탑승 불가")           # 버스 탑승 불가 를 출력
버스 탑승 불가

위 예제같은 경우는 버스 카드는 True 지만 카드에 돈이 900원이 있어서 버스 탑승 불가 라는 문자열을 내놓는다.


다음 예제는 not 조건식에 대해 알아보자.

'공항 입국 수속을 밟을때, 반입 금지 물건이 없다면 입국 허가를 내어라.'

>>> danger_article = False
>>> if not danger_article:
...     print("입국 허가")
... else:
...     print("입국 금지")
입국 허가

위 예제는 not 조건식을 사용한 예제이다.
not 조건식은 x가 거짓(False) 라면 참이다 라는 뜻을 갖고있으므로, danger_article 은 False 라는 boolean 자료형을 갖고 있으므로, not 조건식을 사용
하면 True 로 인식되어 입국 허가 라는 문자열이 출력이 된다.


- in

이번에는 in 조건식에 대해 알아보도록 하자. 다시 말하지만 예제를 보며 이해하고 공부하는 방법은 프로그래밍을 공부하기엔 매우 좋은 방법이므로, 예제를
한번 보도록 하자. (물론 필자만 그렇게 생각하는 것 일수도 있다고 한다.)

>>> 5 in [5, 6, 7]        # 5가 5, 6, 7리스트에 있는가?
True

>>> 9 in [5, 6, 7]        # 9가 5, 6, 7 리스트에 있는가?
False

>>> 5 not in [5, 6, 7]    # 5가 5, 6, 7 리스트에 없는가?
False

>>> 9 not in (5, 6, 7)    # 9가 5, 6, 7 튜플에 없는가?  / 튜플 적용 가능
True

>>> 'h' in ('h', 'e', 'l', 'l', 'o')      # h가 튜플에 존재하는가
True

위 in 조건식을 익혔다면 다음 예제를 보며 응용해보도록 하자.

>>> room = ['bed', 'computer', 'books']     # room 이라는 리스트에 bed, computer, books 를 집어넣는다.
>>> if 'pencil' in room                     # pencil 이라는 문자열이 room 리스트에 있다면
...     print("방에 연필이 있군요.")         # 방에 연필이 있군요. 를 출력
... else:                                   # 그렇지 않다면
...     print("방에 연필이 없네요.")         # 방에 연필이 없네요. 를 출력
방에 연필이 없네요.

위 예제를 보아 room 리스트에 pencil이 없으니 방에 연필이 없네요 라는 문자열을 출력하는 것을 볼 수 있다.
다음에는 elif 에 대해서 알아보도록 하자.

'버스를 타야하는데 1000원이 있으면 버스를 타고, 돈이 없는데 카드가 있다면 버스를 타라.

>>> money = 900
>>> books = True
>>> card = False
>>> if money >= 1000:
...     print("버스 탑승 OK")
... elif card:
...     print("버스 탑승 OK")
... else:
...     print("버스 탑승 불가")

elif 는 else와 if 를 섞어서 만들어진 조건문이다 라고 생각하면 편할 것 이다. 다시말해 else 뒤에는 조건식이 붙지 않지만, elif 뒤에는 if문처럼
조건식이 붙는다.


여기까지 if문에 대해 알아보았다.