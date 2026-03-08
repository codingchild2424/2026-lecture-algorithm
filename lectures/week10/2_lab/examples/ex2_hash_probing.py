# === Ex 2: 선형 탐사 해시 테이블 (Hash Table with Linear Probing) ===
# Week 10 해시 테이블 - 개방 주소법(Open Addressing) 중 선형 탐사 방식
# 충돌 시 다음 빈 슬롯을 순차적으로 탐색하여 저장
# 시간 복잡도: 평균 O(1/(1-alpha)), 최악 O(n) - alpha는 적재율
# 공간 복잡도: O(m) - m은 테이블 크기 (체이닝과 달리 추가 리스트 없음)
"""Hash Table with Linear Probing (Open Addressing)."""


class HashTableProbing:
    """선형 탐사 방식의 해시 테이블.

    개방 주소법(Open Addressing): 모든 항목을 테이블 내부에 직접 저장
    선형 탐사: 충돌 시 h(k), h(k)+1, h(k)+2, ... 순서로 빈 슬롯 탐색
    클러스터링 문제: 연속된 슬롯이 채워지면 탐색 시간이 증가 (1차 클러스터링)
    적재율이 1에 가까워지면 성능이 급격히 저하됨
    """
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size    # 키 배열 (None이면 빈 슬롯)
        self.values = [None] * size  # 값 배열
        self.count = 0               # 저장된 항목 수

    def _hash(self, key):
        """해시 함수: 키를 테이블 인덱스로 변환한다.

        Python 내장 hash() 사용 후 테이블 크기로 나머지 연산
        결과: 0 ~ (size-1) 범위의 인덱스
        """
        return hash(key) % self.size

    def put(self, key, value):
        """키-값 쌍을 해시 테이블에 삽입한다.

        알고리즘:
        1. 해시 함수로 초기 인덱스를 계산
        2. 해당 슬롯이 비어있지 않고 다른 키가 저장되어 있으면
           다음 슬롯으로 이동 (선형 탐사: idx = (idx + 1) % size)
        3. 빈 슬롯 또는 동일 키 슬롯을 찾으면 값을 저장

        시간 복잡도: 평균 O(1/(1-alpha)), 테이블이 가득 차면 예외 발생
        """
        if self.count >= self.size:
            raise Exception("Hash table is full")  # 테이블이 가득 참
        idx = self._hash(key)
        # 선형 탐사: 빈 슬롯이나 동일 키를 찾을 때까지 다음 슬롯으로 이동
        while self.keys[idx] is not None and self.keys[idx] != key:
            idx = (idx + 1) % self.size  # 원형으로 다음 슬롯 탐색
        if self.keys[idx] is None:
            self.count += 1  # 새로운 키 삽입
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        """키에 해당하는 값을 반환한다. 없으면 None.

        알고리즘:
        1. 해시 함수로 초기 인덱스 계산
        2. 선형 탐사로 키를 탐색
        3. 빈 슬롯을 만나면 키가 없는 것으로 판단 (탐색 종료)
        4. 한 바퀴 돌아서 시작 위치로 돌아오면 키가 없음

        시간 복잡도: 평균 O(1/(1-alpha))
        """
        idx = self._hash(key)
        start = idx  # 시작 위치 기록 (한 바퀴 확인용)
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]  # 키를 찾음
            idx = (idx + 1) % self.size  # 다음 슬롯으로 이동
            if idx == start:
                break  # 한 바퀴 다 돌았으면 키 없음
        return None

    def load_factor(self):
        """적재율(load factor)을 반환한다.

        개방 주소법에서는 적재율이 절대 1을 초과할 수 없음 (테이블 크기 제한)
        일반적으로 적재율 0.5~0.7 이상이면 리사이징을 고려해야 함
        """
        return self.count / self.size


if __name__ == "__main__":
    ht = HashTableProbing(size=7)
    data = [("apple", 3), ("banana", 5), ("cherry", 2), ("date", 8), ("elderberry", 1)]

    # 삽입 및 적재율 변화 확인
    for k, v in data:
        ht.put(k, v)
        print(f"put('{k}', {v}) -> load_factor = {ht.load_factor():.2f}")

    # 검색 테스트
    print(f"\nget('cherry') = {ht.get('cherry')}")

    # 내부 테이블 구조 확인 - 선형 탐사로 인한 클러스터링 확인 가능
    print("\nInternal table:")
    for i in range(ht.size):
        print(f"  [{i}]: key={ht.keys[i]}, value={ht.values[i]}")
