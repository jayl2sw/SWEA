### Set

`set` : `{}` 사용해서 만듬

* 인덱스를 제공하지 않음
* 순서의 개념이 없음
* 중복을 허용하지 않음

중복되지 않는 데이터를 만들기 위해 사용하는 자료구조

```python
data_set = {10, 20, 20, 30}
print(data_set) ==> {10, 20, 30}
```



#### 기본연산

`intersection() (&)` : 교집합 연산

`union() (|)` : 합집합 연산 => 중복없이 반환 

`difference() (-)` : 차집합 연산 



`data_set.add(n)` : 항목 n 하나 추가

`data_set.update({set})` : 셋을 뒤에 붙임

`data_set.remove(n)` : 항목 n 삭제

`data_set.pop()` : 첫 항목 제거 return 첫 항목

`data_set.clear()` : 모든 항목 삭제 `data_set = ()`



#### 항목 확인

`in` : set 안에 항목이 있으면 True  반환

`not in` : set 안에 항목이 없으면 True 반환

`a.issuperset(b)` : a가 b를 전부 포함하는 집합인지 확인

`a.issubset(b)` : b가 a를 전부 포함하는 집합인지 확인



### 셋 내포

```python
data_set1 = {1, 2, 3, 4, 5}
print("data_set1: {0}, {1}".format(type(data_set1), data_set1))

data_set2 = {item for item in data_set1}
print("data_set2: {0}, {1}".format(type(data_set2), data_set2))

data_set3 = {item for item in data_set1 if item % 2 == 1}
print("data_set3: {0}, {1}".format(type(data_set3), data_set3))
```



#### list, tuple,set 간의 변환

```python
data_str = "Hello"
data_list = list(data_str)
data_tuple = tuple(data_list)
data_set = set(data_tuple)
data_list = list(data_set)
```



---

### Dictionary

* **중괄호{} 안에 키: 값의 형식을 가진 유일한 데이터를 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형 중의 하나.**
  * 인덱스 제공 x 
  * 순서의 개념이 없음
  * 중복을 허용하지 않음



```python
data_dict1 = {
    "홍길동" : 20,
    "이순신" : 45,
    "강감찬" : 35,
}
print(data_dict1)

#키를 문자열로 적지 않는다.
data_dict2 = dict(홍길동 = 20, 이순신 = 45, 강감찬 = 35)
print(data_dict2)

data_tuple1 = (("홍길동", 20), ("이순신", 45), ("강감찬", 35))
data_dict3 = dict(data_tuple1)
```



