이번에는 리스트 자료형에 대해 알아보겠습니다.

전에 문자열과 숫자형에 알아보았는데, 문자열과 숫자열만으로 하나의 집합을 만들어서 프로그래밍을 하기에는 너무 힘들기때문에 이러한 집합을 만들어주기 위해
리스트자료형을 사용한다.

리스트라 하면 보통 영수증을 받을때 물건의 리스트를 확인한다 라고 하는 경우가 있는데,
그 리스트를 파이썬에서 한번 프로그래밍 해보도록 하자.

- 리스트를 만들어보자

>>> buy = [1000, 2000, 3000, 4000]

위와같이
리스트이름 = [요소A, 요소B, 요소C] 형태로 리스트를 만들 수 있다.

그리고 리스트내에는 문자열과 문자도 넣을 수 있다!

>>> test = ["Hello, World!", "Hello", 1]
이런식으로 리스트내에 문자열과 문자, 숫자형을 입력해보았다. 물론 오류없이 정상적으로 작동하는 명령어임을 알 수 있다.

결론적으로 보자면, 리스트내에는 자료형 무엇이든 넣을 수 있다.

그리고 한가지 흥미로운점은 리스트내에 리스트를 요소값으로 갖을 수 있다. 아래 예제를 보자.

>>> test2 = [1, 2, [1, 2]]

test2 리스트내에 1, 2와 [1, 2] 요소를 추가하였다. 이렇게 리스트내에는 자료형 무엇이든 넣을 수 있다.

추가적으로

>>> binbin = [] 

이런형태의 비어있는 리스트도 만들 수 있다.


이제 우리는 리스트를 등록 해보았다. 이제 리스트에 등록된 값을 원하는값만 빼고 잘라보자. 전에 해보았던 인덱싱과 슬라이싱을 해보는 것 이다.

- 인덱싱

>>> test = [1, 2, 3]      # test 리스트에 [1, 2, 3]값 설정
>>> test                  # test 리스트 반환
[1, 2, 3]

>>> test[0]               # 0번째 즉 test 리스트에서 첫번째 값을 반환
1
>>> test[-1]              # -1번째 즉 test 리스트에서 가장 끝에서 첫번째 값을 반환
3
>>> test[0] + test[-1]    # 0번째와 -1번째 값을 더해라
4

리스트안에 넣은 리스트를 인덱싱해보자.

>>> test[1, 2, [1, 2]]    # test 리스트내에 1,2, [1, 2]값 설정

>>> test[-1]              # test 리스트에서 가장 끝에서 첫번째 값을 반환
[1, 2]

가장 끝에서 첫번째 값을 반환해야 하므로 test내에 있는 값중 가장 끝에있는 값은 [1, 2] 가 되므로 [1, 2] 를 반환하게 된다.
그럼 여기서 [1, 2] 에 있는 값 2를 반환하고 싶을때는 어떻게 할까?

>>> test[-1][-1]
2

이런식으로 뒤에 대괄호를 하나더 추가해주면서 리스트내에 리스트에 접근할 수 있었다.
다시 말하지만 리스트내에는 문자열과 문자 등 자료형 모두를 값으로 설정이 가능하다. 꼭 다른 자료형으로 한번씩 실습을 해보도록 하자.

추가적으로
>>> test[1, 2, [1, 2, [1,2]]]

이런식으로 리스트안에 리스트안에 리스트가 되어있는 경우도 대괄호를 세개를 사용함으로써 인덱싱이 가능하다
>>> test[-1][-1][-1]
2

- 리스트 슬라이싱
방금은 리스트를 인덱싱(Indexing) 해보았다. 이번에는 원하는 리스트만큼을 잘라내기 위한 슬라이싱을 해보도록 하자.

>>> test = [1, 2, 3, 4, 5]            # test 리스트에 1, 2, 3, 4, 5 값 설정
>>> test[0:2]                         # test 리스트에 0번째부터 1번째까지의 값을 반환 - 참고로 전에서 알아보았지만 뒤의 :2 뜻은 2는 미포함이다.
[1, 2]

>>> test[:1]          # test 리스트에서 1번째를 미포함한 1번째 미만의 값을 몽땅 반환한다.
[1]

>>> test[3:]          # test 리스트에서 3번째를 포함한 뒤의 값을 몽땅 반환한다.
[4, 5]


- 리스트 값의 제어

- 리스트 값 수정
>>> test = [1, 2, 3]
>>> test[0] = 5
>>> test
[5, 2, 3]

- 리스트 값 삭제
>>> test = [1, 2, 3]
>>> del test[0]
>>> test
[2, 3]

del <리스트이름>[제거 원하는 위치]
의 형태로 리스트내 값을 제거할 수 있었다. 물론 슬라이싱을 이용해 한번에 삭제할 수 있다.

>>> del test[1:]
>>> test
[1]

여기까지 리스트, 리스트의 인덱싱과 슬라이싱에 대해 알아보았다. 다음에는 리스트 함수를 공부해보자.