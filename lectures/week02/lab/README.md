# Week 02 Lab — 복잡도 분석 실습

## 목표
- 시간 복잡도를 실험적으로 측정하고, 이론적 분석과 비교한다.
- 웹 API에서 알고리즘 선택이 응답 시간에 미치는 영향을 체험한다.

---

## Type A — 알고리즘 구현

### A-1: 시간 측정 유틸 작성 (10분)

`examples/timer_util.py`를 참고하여 실행 시간을 측정하는 유틸을 작성합니다.

### A-2: 중복 원소 찾기 — O(n²) → O(n) 개선 (15분)

**문제**: 정수 배열이 주어졌을 때, 중복된 원소가 있는지 판별하시오.

1. **O(n²) 풀이**: 이중 for문으로 모든 쌍을 비교
2. **O(n) 풀이**: 해시셋(set)을 이용

`examples/find_duplicate.py`를 참고하세요.

두 풀이의 실행 시간을 N=100, 1000, 10000, 100000에서 비교합니다.

### A-3: 실행 시간 그래프 (10분)

`examples/complexity_plot.py`를 실행하여 O(1), O(n), O(n log n), O(n²)의 실행 시간 그래프를 그립니다.

---

## Type B — 웹 코드 분석

### B-1: 상품 검색 API 비교 (15분)

`examples/web_search_api/` 폴더의 Flask 앱을 실행합니다:

```bash
cd examples/web_search_api
pip install flask
python app.py
```

두 가지 검색 엔드포인트를 비교합니다:
- `GET /search/linear?q=상품명` — 선형 탐색 O(n)
- `GET /search/binary?q=상품명` — 이진 탐색 O(log n)

N=100, 10000, 1000000 상품에서 응답 시간을 측정하고 비교합니다.

**질문**: 데이터가 커질수록 두 방식의 차이가 어떻게 변하나요?

---

## Homework 1
과제 상세는 `homework/README.md`를 참고하세요.
