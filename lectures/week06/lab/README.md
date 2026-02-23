# Week 06 Lab — 동적 계획법

## 목표
- DP의 핵심 패턴(memoization, tabulation)을 이해하고 구현한다.
- 웹 애플리케이션에서 DP가 활용되는 실제 사례를 분석한다.

---

## Type A — 알고리즘 구현

### A-1: 피보나치 비교 (10분)

`examples/fibonacci.py`를 실행하여 세 가지 방식의 성능을 비교합니다:
- Naive 재귀: O(2^n)
- Memoization: O(n)
- Tabulation: O(n)

### A-2: LCS + DP 테이블 시각화 (15분)

`examples/lcs.py`에서 Longest Common Subsequence를 구현하고, DP 테이블을 출력합니다.

### A-3: 0-1 Knapsack + 역추적 (10분)

`examples/knapsack.py`에서 0-1 배낭 문제를 풀고, 어떤 물건을 선택했는지 역추적합니다.

---

## Type B — 웹 코드 분석

### B-1: 텍스트 Diff 뷰어 (15분)

`examples/web_diff/`의 Flask 앱을 실행합니다:

```bash
cd examples/web_diff
python app.py
```

두 텍스트를 입력하면 LCS 기반으로 변경된 부분을 하이라이트합니다.
- GitHub의 diff 기능이 이와 같은 원리로 동작합니다.

---

## Homework 5 (마지막 과제)
과제 상세는 `homework/README.md`를 참고하세요.
