# Week 01 Lab — 환경 설정 & 코딩 에이전트

## 목표
- 개발 환경을 설정하고, 코딩 에이전트를 알고리즘 학습에 활용하는 방법을 익힌다.

## 사전 준비
- Python 3.10+ 설치 확인
- 텍스트 에디터 또는 IDE (VS Code 권장)

---

## Task 1: 코딩 에이전트 설치 (10분)

아래 중 하나를 설치합니다:
- **Claude Code**: `npm install -g @anthropic-ai/claude-code`
- **Gemini CLI**: `npm install -g @anthropic-ai/gemini-cli` (또는 공식 문서 참고)
- **OpenCode**: `go install github.com/opencode-ai/opencode@latest`

설치 후 터미널에서 실행하여 정상 작동을 확인합니다.

## Task 2: 개발 환경 확인 & 온라인 저지 계정 (10분)

1. Python 버전 확인:
   ```bash
   python3 --version
   ```

2. 필수 패키지 설치:
   ```bash
   pip install matplotlib
   ```

3. [Baekjoon Online Judge](https://www.acmicpc.net/) 계정 생성

## Task 3: 에이전트로 이진 탐색 구현 (15분)

RALPH 기법을 적용하여 코딩 에이전트에게 이진 탐색 구현을 요청합니다.

**RALPH 기법이란?**
- **R**ole: 역할 부여 ("너는 알고리즘 튜터야")
- **A**sk: 요청 ("이진 탐색을 Python으로 구현해줘")
- **L**imit: 제약 조건 ("재귀 버전과 반복 버전 둘 다")
- **P**rovide: 입력 제공 ("정렬된 리스트 [1,3,5,7,9,11]에서 7을 찾아")
- **H**int: 힌트 ("시간복잡도가 O(log n)인 이유도 설명해")

**실습**: `examples/binary_search.py`를 참고하여 직접 구현해보고, 에이전트의 코드와 비교합니다.

## Task 4: 알고리즘 시각화 스크립트 만들기 (10분)

에이전트에게 요청하여, 이진 탐색의 탐색 과정을 시각적으로 보여주는 스크립트를 만듭니다.

예시 프롬프트:
> "이진 탐색이 동작하는 과정을 단계별로 출력하는 Python 스크립트를 만들어줘. 각 단계에서 현재 탐색 범위와 mid 값을 보여줘."

## Task 5: 첫 Baekjoon 문제 풀기 (5분)

- [BOJ 1920 — 수 찾기](https://www.acmicpc.net/problem/1920)
- 에이전트를 활용하여 풀이 전략을 세우고, 직접 제출합니다.
