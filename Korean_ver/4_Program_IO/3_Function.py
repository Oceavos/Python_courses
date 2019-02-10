이번에는 함수에 대해 알아보도록 하자.

함수에 대해서 간단히 설명을 해보자면, 우리는 음료수를 얼음판에 붓고 냉동실에 얼려서 얼음판을 털어내서 사각형, 별모양 등등 많은 모양의 얼음을 만들어낸다.
이때 여기서 얼음판을 파이썬에서는 함수라고 한다.

즉 주어진 일을 수행한뒤 그에대한 결과값을 내놓는게 함수이다.
쉽게 말하면 계속 반복해서 사용해야 하는데, 똑같은 코드를 입력하기에는 가독성 외 여러가지 문제가 생길 수 있으므로 함수를 사용하게 된다.

자 그럼 함수에 대해 간단히 예제를 보자.

>>> def addition(a, b)
...     return a + b

>>> addition(5, 5)
10

눈치가 빠르다면 위 예제를 바로 이해했을 것이다.

addition 이라는 함수의 매개변수 a, b에 각각 5를 대입해서 addition 함수내의 return a + b의 명령을 수행하면 10을 반환한다.

쉽게 말하자면 addition 이라는 함수에 있는 변수 a, b에 5, 5를 각각 대입하고 return 함수를 이용해서 결과값을 반환한 것 이다.

그럼 이제 사칙연산을 만들어보자.

>>> def addition(a, b):
...   	return a + b

>>> def subtraction(a, b):
...   	return a - b

>>> def multiplication(a, b):
...   	return a * b

>>> def division(a, b):
...    	return a / b

>>> addition(5, 5)
10
>>> subtraction(10, 5)
5
>>> multiplication(5, 5)
25
>>> division(5, 5)
1.0

자 근데 여기서 일부 독자는 궁금해 하는것이 있을 수 있다.

꼭 함수 옆에는 매개변수를 입력해주어야 하는가에 대한 답변은 물론 아니다. 아래 예제를 통해 알아보자.

>>> def print_me():
...     return 'YES!!'

>>> print_me()
'YES!!'

위처럼 print_me 함수를 만드는데 매개변수를 사용하지 않았다. 그리고 그에대한 결과값은 'YES!!' 라는 문자열을 반환하게 된다.
그러므로 print_me() 라는 명령을 입력하면 'YES!!' 라는 문자열이 바로 나오게된다.

그리고 함수내 매개변수에서 값을 변수를 선언하듯이 설정할 수 있다. 아래 예제를 보도록 하자.

>>> def my_hobby(name, hobby, age=20):
...    	print('제 이름은 %s 입니다.' % name)
...    	print('제 취미는 %s 입니다.' % hobby)
...    	print('제 나이는 %d 입니다.' % age)

	
>>> my_hobby('홍성진', '프로그래밍')
제 이름은 홍성진 입니다.
제 취미는 프로그래밍 입니다.
제 나이는 20 입니다.

위처럼 매개변수내의 age 변수의 초기값을 20으로 지정해준 모습이다. 위 예제처럼 매개변수의 값을 처음부터 설정할 수 있다.