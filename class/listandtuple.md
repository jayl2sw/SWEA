# Sequence형

* `시퀀스형` : 데이터에 대해 순서를 가진 자료구조 총칭

### list

* `list` : `[]`안에 **서로 다른 자료형**의 값을 콤마로 구분해 하나이상 저장할 수 있는 컬렉션 자료형
  * index 사용하여 접근
  * 저장된 항목 변경 가능
  * 유효한 Index가 아닐 경우 IndexError 발생

```python
data_list = [10, 21.5, "Python", True]
print("{} {}".format(type(data_list),data_list))

[결과]
<class 'list'> [10, 21.5, 'Python', True]

IndexError: list index out ouf range

# 처음부터 마지막 전까지
data_list[0:3] => [data_list[0], data_list[1], data_list[2]]

# +를 사용하여 새 list 생성 가능
data_list1, data_list2 = [10, 20, 30], [40, 50]
data_list = data_list1 + data_list2
data_list = [10, 20, 30, 40, 50]

# *를 사용하여 새 list 생성 가능 
data_list = data_list1 * 2
data_list = [10, 20, 30, 10, 20, 30]
```



### list 조작법 

#### 추가

* `data_list.append(a)` : 뒤에 a 추가
* `data_list.insert(a, b)` : a번째 index에 b추가
* `data_list.extend([a, b])` : 뒤에 a, b 리스트 붙여서 연장
* `data_list.append([a, b])` :  뒤에 [a,b] 리스트를 항목으로 추가

```python
data_list = [10, 20, 30, 40]

data_list.append(50)
data_list = [10, 20, 30, 40, 50]

data_list.insert(2, 20)
data_list = [10, 20, 20, 30, 40, 50]

data_list.extend([60, 70]) 
data_list = [10, 20, 20, 30, 40, 50, 60, 70]

data_list.append([80, 90]) 
data_list = [10, 20, 20, 30, 40, 50, 60, 70, [80, 90]]

data_list = [10, 20, 30, 40]

data_list[2] = 29
data_list = [10, 20, 29, 40]

data_list[1:3] = [12, 15]		# 범위 연산자의 마지막은 포함되지 않음
data_list = [10, 12, 15, 40] 

data_list[1:3] = [12, 15, 20]		
data_list = [10, 12, 15, 20, 40] 

data_list[2:3] = [31, 25]		
data_list = [10, 12, 31, 25, 20, 40] 
```



#### 제거

* `del data_list[i]`: index가 i인 항목 제거 
* `data_list.pop(i)`: index가 i인 항목이 제거
* `data_list.remove(x)` : x값을 가지는 제일 처음 항목 삭제
* `data_list.clear()` : 모든 항목을 제거해 빈 리스트 객체 생성



#### 항목 확인

* `x in data_list` : data_list 내에 x가 있으면 `True` 반환
* `x not in data_list` : data_list 내에 x가 없으면 `True` 반환
* `data_list.count(x)` : 인자로 전달된 항목의 개수 확인 (x의 개수)



#### List와 for문

`data_list = list(range(0, 11, 2))`

`for item in data_list:`  항목정보를 매 반복마다 item에 저장

`for idx, item in enumerate(data_list):` 인덱스와 항목정보를 매 반복마다 idx와 item에 저장



#### 리스트 내포

```python 
data_list1 = [1, 2, 3, 4, 5]

data_list2 = []

for item in data_list1:
    data_list2.append(item)
    
data_list3 = [item for item in data_list1]

data_list1 = data_list2 = data_list3
```





---



* `tuple` :
* 

