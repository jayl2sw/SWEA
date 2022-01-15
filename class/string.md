# string

### 문자열의 연결

* `+` : 두개 이상의 문자열을 합쳐 하나의 문자열 만듬

```python
message = "안녕하세요"
guest = "홍길동"

greeting = guest + "님, " + message
```



### 문자열의 반복

문자열 

```python
print("string"*times, ends = '') # end로 인해 줄바꿈 x
```



### 문자의 선택

```python
data_str = "안녕하세요, 파이썬입니다."
idx= 0 
cnt = len(data_str)
while True:
    print(data_str[idx]=> )
```



### 문자열의 범위 선택

```python 
data_str = "와우! 안녕하세요, 파이썬입니다."

start = input("시작 인덱스를 입력하세요: ")
end = input("종료 인덱스를 입력하세요: ")

try:
    start = int(start)
except ValueError:
    start = None

try:
    end = int(end)
except ValueError:
    end = None

print("{}".format(data_str[start:end]))
```



## 문자열 함수

` count()` : 문자열 개수를 반환하는 함수 

`len()` : 문자열의 길이를 반환하는 함수

`find()` : 원하는 문자열을 찾아서 인덱스를 반환하는 함수 못 찾을 시 -1 반환(왼쪽에서 오른쪽)

`rfind()` : 원하는 문자열을 찾아서 인덱스를 반환하는 함수 못찾을 시 -1 반환 (오른쪽에서 왼쪽)

`index()` : 원하는 문자열을 찾아서 인덱스를 반환하는 함수 못찾을 시 ValueError 발생

`join()` : 

`capitalize()` : 첫번째 문자를 대문자로 하는 새로운 문자열 반환

`lower()` : 모든 문자를 소문자로 한 새로운 문자열 반환

`upper()` : 모든 문자를 대문자로 한 새로운 문자열 반환

`lstrip("제거할 문자열")` : 왼쪽에서 문자열을 제거 

`rstip("제거할 문자열")` : 오른쪽에서 문자열을 제거

`strip("제거할 문자열")` : 양쪽에서 제거 

`replace(찾을 문자열, 교체 문자열)` : 문자열 교체 

`split("기준 문자열")` : 문자열을 나누어 list 형태로 반환

```python
data_str = "Have a nice day!"
input_str = "nice"
print(data_str.count(input_str))
```

```python
len(data_str)
```

```python
idx = data_str.find(input_str)
```

```python
data_str = "가나다라마바사아자차카타파하"
comma_space = ", "

output = comma_space.join(data_str)
print(output)
<class 'str'> 가, 나, 다, 라, 마, 바, 사, 아, 자, 차, 카, 타, 파, 하
```

```python
data_str =  "10, 20, 3o, 40, 50"

data_str = data_str.replace(" ", "")
print(data_str)

data_list = data_str.split(",")
for val in data_list:
    print(val, end=" ")
    if not val.isdigit():
        print("<= ", end="")
    print()
```

