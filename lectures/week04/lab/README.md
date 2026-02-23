# Week 04 Lab — 분할 정복 심화

## 목표
- 분할 정복 알고리즘의 재귀 구조를 이해하고 트레이싱한다.
- 웹 애플리케이션에서 분할 정복이 활용되는 사례를 분석한다.

---

## Type A — 알고리즘 구현

### A-1: Merge Sort 트레이싱 (10분)

`examples/merge_sort_trace.py`를 실행하여 Merge Sort의 재귀 호출 트리를 관찰합니다.

각 재귀 호출에서 배열이 어떻게 분할되고 병합되는지 확인하세요.

### A-2: k번째 작은 수 찾기 (15분)

`examples/kth_smallest.py`를 참고하여 Randomized Select 알고리즘을 구현합니다.

- 평균 O(n) 시간에 k번째 작은 수를 찾는 알고리즘
- Quick Sort의 파티션을 활용

### A-3: 최근접 점의 쌍 (10분)

`examples/closest_pair.py`를 참고하여 분할 정복으로 최근접 점의 쌍을 찾습니다.

- 브루트포스 O(n²) vs 분할정복 O(n log n) 비교

---

## Type B — 웹 코드 분석

### B-1: 자동완성 API (15분)

`examples/web_autocomplete/` 폴더의 Flask 앱을 실행합니다:

```bash
cd examples/web_autocomplete
python app.py
```

10만 단어 사전에서 prefix 검색:
- `GET /autocomplete/linear?q=pre` — 순차 탐색
- `GET /autocomplete/binary?q=pre` — 정렬 + 이진 탐색

글자를 입력하며 응답 시간 차이를 체험합니다.

---

## Homework 3
과제 상세는 `homework/README.md`를 참고하세요.
