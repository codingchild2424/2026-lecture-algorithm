# === Ex 1: 체이닝 해시 테이블 (Hash Table with Chaining) ===
# Week 10 해시 테이블 - 체이닝(연결 리스트) 방식의 충돌 해결
# 각 버킷이 리스트로 구현되어, 충돌 시 같은 버킷에 여러 항목을 저장
# 시간 복잡도: 평균 O(1), 최악 O(n) (모든 키가 같은 버킷에 해싱될 때)
# 공간 복잡도: O(n + m) - n은 저장된 항목 수, m은 테이블 크기
"""Hash Table with Chaining."""


class HashTableChaining:
    """체이닝 방식의 해시 테이블.

    충돌 해결: 같은 해시값을 가진 키들을 리스트(체인)에 저장
    적재율(load factor) = 저장된 항목 수 / 테이블 크기
    적재율이 높아질수록 체인이 길어져 성능이 저하됨
    """
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 각 버킷을 빈 리스트로 초기화
        self.count = 0  # 저장된 항목 수 추적

    def _hash(self, key):
        """해시 함수: 키를 테이블 인덱스로 변환한다.

        Python 내장 hash() 사용 후 테이블 크기로 나머지 연산
        결과: 0 ~ (size-1) 범위의 인덱스
        """
        return hash(key) % self.size

    def put(self, key, value):
        """키-값 쌍을 해시 테이블에 삽입한다.

        알고리즘:
        1. 해시 함수로 버킷 인덱스를 계산
        2. 해당 버킷의 체인을 순회하며 동일한 키가 있는지 확인
        3. 동일 키가 있으면 값을 갱신 (덮어쓰기)
        4. 없으면 체인 끝에 새 항목 추가

        시간 복잡도: 평균 O(1 + alpha), alpha = 적재율
        """
        idx = self._hash(key)
        # 기존 키가 있는지 체인을 순회하여 확인
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)  # 기존 키의 값 갱신
                return
        # 새로운 키이면 체인에 추가
        self.table[idx].append((key, value))
        self.count += 1

    def get(self, key):
        """키에 해당하는 값을 반환한다. 없으면 None.

        알고리즘:
        1. 해시 함수로 버킷 인덱스 계산
        2. 해당 버킷의 체인을 순회하며 키 탐색

        시간 복잡도: 평균 O(1 + alpha), alpha = 적재율
        """
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v  # 키를 찾으면 값 반환
        return None  # 키가 없으면 None 반환

    def delete(self, key):
        """키-값 쌍을 해시 테이블에서 삭제한다.

        알고리즘:
        1. 해시 함수로 버킷 인덱스 계산
        2. 해당 버킷의 체인에서 키를 찾아 제거

        시간 복잡도: 평균 O(1 + alpha)
        반환: 삭제 성공 시 True, 키가 없으면 False
        """
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx].pop(i)  # 체인에서 해당 항목 제거
                self.count -= 1
                return True
        return False

    def load_factor(self):
        """적재율(load factor)을 반환한다.

        적재율 = 저장된 항목 수 / 테이블 크기
        적재율이 1을 넘으면 평균적으로 각 버킷에 1개 이상의 항목이 있음
        일반적으로 적재율이 0.75를 넘으면 리사이징을 고려한다
        """
        return self.count / self.size


if __name__ == "__main__":
    ht = HashTableChaining(size=7)
    data = [("apple", 3), ("banana", 5), ("cherry", 2), ("date", 8), ("elderberry", 1)]

    # 삽입 및 적재율 변화 확인
    for k, v in data:
        ht.put(k, v)
        print(f"put('{k}', {v}) -> load_factor = {ht.load_factor():.2f}")

    # 검색 테스트
    print(f"\nget('cherry') = {ht.get('cherry')}")  # 존재하는 키
    print(f"get('fig') = {ht.get('fig')}")          # 존재하지 않는 키

    # 내부 버킷 구조 확인 - 체이닝 상태를 시각적으로 확인
    print("\nInternal table:")
    for i, bucket in enumerate(ht.table):
        print(f"  [{i}]: {bucket}")
