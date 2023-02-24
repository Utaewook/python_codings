# 파일명: myHashMap.py
# 작성자: 유태욱
# 작성일자: 2022-11-16
# 주요기능: 다양한 정보 레코드를 key를 이용해 신속하게 검색 할 수 있는 Hashmap 클래스
# 최종수정일자: 2022-11-16
# 수정내용: 최초작성

class Entry:  # key-value 쌍으로 데이터를 저장하는 클래스
    def __init__(self, k, v):  # 클래스 생성자
        # 생성자 파라미터로 받은 k,v값을 각각 key value 값에 저장
        self._key = k
        self._value = v

    def __str__(self):  # 객체의 문자열 반환 함수
        return str(self._value)  # value값을 문자열로 반환한다.


def CyclicShiftHashCode(str_key):  # key값을 hashing하는 함수
    mask = (1 << 32) - 1  # 32 비트의 정수 값으로 제한
    h = 0  # hashing된 값을 저장할 변수
    for ch in str_key:  # key의 철자 순회 반복문
        h = (h << 5 & mask) | (h >> 27)  # cyclic shift hash code
        h += ord(ch)
    return h  # 해시값을 반환


class Bucket(Entry):  # 같은 해시값을 가지는 Entry가 저장되는 클래스
    def __init__(self):  # 클래스 생성자
        self._bucket = []  # 리스트에 같은 해시값을 갖는 Entry를 저장한다.

    def _getitem(self, k):  # key값에 맞는 value를 반환해주는 함수
        for item in self._bucket:  # 리스트에 있는 아이템들 순회
            if k == item._key:  # 키 값이 입력받은 k값과 같다면
                return item._value  # 찾은 value값을 반환해준다
        return None  # 찾은 값이 없으면 None 반환해준다

    def _setitem(self, k, v):  # key값에 맞는 Entry의 value를 수정하는 함수
        for item in self._bucket:  # 리스트에 있는 아이템들 순회
            if k == item._key:  # 키 값이 입력받은 k값과 같다면
                item._value = v  # 찾은 value값을 v로 바꿔준다.
                return  # 함수를 끝낸다
        self._bucket.append(Entry(k, v))  # 리스트에 해당 키값을 갖는 Entry가 없다면 새로 추가해준다.

    def _delitem(self, k):  # key값에 맞는 Entry를 삭제하는 함수
        for j in range(len(self._bucket)):  # 리스트에 있는 아이템들 순회
            if k == self._bucket[j]._key:  # 키 값이 입력받은 k값과 같다면
                self._bucket.pop(j)  # 찾은 Entry를 pop해준다
                return 1  # 1개 삭제했음 반환
        return None  # 찾은 갑이 없으면 None을 반환해준다

    def __len__(self):  # 객체의 길이를 반환하는 함수
        return len(self._bucket)  # 리스트의 길이를 반환해준다.

    def __iter__(self):  # 순회 가능한 객체를 만들기 위해 iterater 반환
        for item in self._bucket:  # 리스트의 아이템들을 순회하며
            yield item._key  # 키값을 반환해준다.


class HashMap(Bucket):  # hashing된 키값으로 value를 저장하는 hashmap
    def __init__(self, capacity=11, prm=109345121):  # 클래스 생성자
        self._hash_table = capacity * [None]  # capacity만큼의 길이를 갖는 리스트 생성
        self._hash_table_size = capacity  # 해시 테이블의 길이 저장
        self._num_entry = 0  # Entry 갯수를 저장할 변수 선언
        self._prime = prm  # 해싱 알고리즘에 쓰일 소수 저장

    def _hash_value(self, k):  # 키 값을 해싱 후 반환해주는 함수
        return CyclicShiftHashCode(k) % self._prime % self._hash_table_size  # 해시 함수를 통해 값을 받아온뒤, 해시테이블 크기에 맞게 들어가게 하기위해 나머지 연산을 해준다.

    def __len__(self):  # 객체의 길이를 반환하는 함수
        return self._num_entry  # Entry의 개수를 반환한다.

    def _getitem(self, k):  # 해시 맵에서 key 값에 맞는 value 값을 반환 하는 함수
        hv = self._hash_value(k)  # 입력 받은 키 값을 해싱한다.
        bucket = self._hash_table[hv]  # 해싱된 키값을 테이블에 넣어 Bucket을 가져온다
        return bucket._getitem(k)  # bucket의 key값을 갖는 Entry를 찾아 value를 반환해준다

    def _setitem(self, k, v):  # 해시 맵에서 key값에 맞는 객체에 value값을 저장하는 함수
        hv = self._hash_value(k)  # 입력 받은 키 값을 해싱한다.
        if self._hash_table[hv] is None:  # 해시 테이블에 hv 위치에 Bucket이 None이라면(비어있다면)
            self._hash_table[hv] = Bucket()  # 새 Bucket을 생성한다
        bucket = self._hash_table[hv]  # 해시 테이블의 hv 위치의 bucket을 가져온다
        bucket._setitem(k, v)  # 가져온 bucket에 입력받은 k,v값으로 설정한다.

    def _delitem(self, k):  # 해시 맵에서 key 값에 맞는 객체를 삭제하는 함수
        hv = self._hash_value(k)  # 입력 받은 키 값을 해싱한다.
        bucket = self._hash_table[hv]  # 해시 테이블의 hv 위치의 bucket을 가져온다
        bucket._delitem(k)  # k 값에 해당하는 Entry를 삭제한다.
        self._num_entry -= 1  # Entry 개수를 1 줄인다.

    def __str__(self):  # 객체의 문자열 반환 함수
        s = ''  # 빈 문자열 선언
        for h in range(len(self._hash_table)):  # 해쉬 테이블의 길이만큼 순회하는 반복문
            bucket = self._hash_table[h]  # h 번째에 있는 Bucket을 가져온다
            if bucket is not None:  # 빈 Bucket이 아니라면
                s += " bucket[{:2d}] : ".format(h)  # 선언해 둔 문자열에 Bucket의 번호를 적고
                for item in bucket:  # Bucket내의 key 값들을
                    s += str(item) + ", "   # 문자열에 더해서 적어준다.
                s += "\n"  # 개행 삽입 후
        return s  # 문자열을 반환해준다.
