# Week 03 Lab — 정렬 알고리즘 구현 & 벤치마크

## 목표
- 기본 정렬 알고리즘을 직접 구현하고, 성능을 비교한다.
- 웹 애플리케이션에서 정렬 알고리즘 선택이 사용자 경험에 미치는 영향을 체험한다.

---

## Type A — 알고리즘 구현

### A-1: 기본 정렬 구현 (10분)

`examples/basic_sorts.py`의 TODO를 채워 Selection Sort, Bubble Sort, Insertion Sort를 구현하세요.

각 함수는 리스트를 받아 정렬된 새 리스트를 반환합니다.

테스트:
```bash
python examples/basic_sorts.py
```

### A-2: 고급 정렬 구현 (15분)

`examples/advanced_sorts.py`의 TODO를 채워 Merge Sort, Quick Sort를 구현하세요.

### A-3: 벤치마크 (10분)

`examples/sort_benchmark.py`를 실행하여 모든 정렬 알고리즘의 성능을 비교합니다.

```bash
python examples/sort_benchmark.py
```

N=100, 1000, 10000, 100000에서 각 알고리즘의 실행 시간을 측정하고 그래프를 확인하세요.

**질문**: O(n²) 알고리즘과 O(n log n) 알고리즘의 차이가 언제부터 눈에 띄나요?

---

## Type B — 웹 코드 분석

### B-1: 미니 쇼핑몰 정렬 비교 (15분)

`examples/web_sort_demo/`의 Flask 앱을 실행합니다:

```bash
cd examples/web_sort_demo
pip install flask
python app.py
```

브라우저에서 `http://localhost:5000`을 열어:
1. "Bubble Sort로 정렬" 버튼을 클릭하고 로딩 시간을 확인
2. "Quick Sort로 정렬" 버튼을 클릭하고 로딩 시간을 확인
3. 상품 수를 1000 → 10000 → 50000으로 변경하며 차이를 체감

**질문**: 실제 쇼핑몰에서 O(n²) 정렬을 쓰면 어떤 일이 벌어질까요?

---

## Homework 2
과제 상세는 `homework/README.md`를 참고하세요.
