# Week 05 Lab — 그리디 알고리즘

## 목표
- 그리디 알고리즘의 성공/실패 조건을 실험적으로 확인한다.
- 실제 스케줄링 문제에서 그리디가 어떻게 활용되는지 체험한다.

---

## Type A — 알고리즘 구현

### A-1: 동전 거스름돈 (10분)

`examples/coin_change.py`를 실행하여 그리디 알고리즘이 성공/실패하는 케이스를 확인합니다.

- 성공 케이스: coins = [500, 100, 50, 10]
- 실패 케이스: coins = [1, 3, 4], amount = 6

### A-2: 분할 가능 배낭 (10분)

`examples/fractional_knapsack.py`에서 분할 가능 배낭 문제를 그리디로 풀어봅니다.

- 단위 가치(value/weight) 기준으로 정렬 후 탐욕적 선택

### A-3: Huffman Coding (15분)

`examples/huffman.py`에서 Huffman 코딩을 구현합니다.

- 문자 빈도수 기반 트리 구성
- 인코딩 및 디코딩 검증

---

## Type B — 웹 코드 분석

### B-1: 회의실 예약 시스템 (15분)

`examples/web_scheduler/`의 Flask 앱을 실행합니다:

```bash
cd examples/web_scheduler
python app.py
```

Activity Selection 알고리즘이 적용된 스케줄러를 분석합니다.
- 회의 요청 목록에서 최대 몇 개의 회의를 배정할 수 있는지 확인
- 그리디 전략(끝나는 시간 기준 정렬)이 왜 최적인지 생각해봅니다.

---

## Homework 4
과제 상세는 `homework/README.md`를 참고하세요.
