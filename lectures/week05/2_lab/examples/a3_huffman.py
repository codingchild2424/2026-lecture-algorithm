# === A-3: 허프만 코딩 (Huffman Coding) ===
# 그리디 알고리즘을 이용한 최적 접두어 코드 생성
#
# 핵심 개념:
# - 그리디 전략: 매 단계에서 빈도가 가장 낮은 두 노드를 합침
# - 최소 힙(우선순위 큐)을 사용하여 효율적으로 최솟값 추출
# - 빈도가 높은 문자일수록 짧은 코드 할당 -> 전체 비트 수 최소화
# - 접두어 코드 속성: 어떤 코드도 다른 코드의 접두어가 아님 -> 구분자 없이 디코딩 가능
# - 시간 복잡도: O(n log n) (n = 서로 다른 문자 수, 힙 연산 n-1회)
# - 공간 복잡도: O(n) (트리 노드 수)
"""
허프만 코딩 (Huffman Coding) 구현

그리디 전략: 빈도가 가장 낮은 두 노드를 반복적으로 합쳐서
최적의 접두어 코드(prefix code)를 생성한다.

구현 내용:
1. 빈도 테이블 구성
2. 최소 힙을 이용한 허프만 트리 구축
3. 코드 생성 (트리 순회)
4. 인코딩 / 디코딩
5. 압축률 계산
"""

import heapq
import math
from collections import Counter


class HuffmanNode:
    """허프만 트리의 노드."""

    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char      # 리프 노드의 문자 (내부 노드는 None)
        self.freq = freq      # 빈도
        self.left = left
        self.right = right

    def __lt__(self, other):
        """최소 힙에서 빈도 기준으로 비교."""
        return self.freq < other.freq

    def is_leaf(self):
        return self.left is None and self.right is None


def build_frequency_table(text):
    """텍스트의 문자별 빈도를 계산한다.

    Args:
        text: 입력 문자열

    Returns:
        {문자: 빈도} 딕셔너리 (빈도 내림차순 정렬)
    """
    return dict(Counter(text).most_common())


def build_huffman_tree(freq_table):
    """빈도 테이블로부터 허프만 트리를 구축한다.

    그리디 선택: 매 단계에서 빈도가 가장 낮은 두 노드를 합친다.

    Args:
        freq_table: {문자: 빈도} 딕셔너리

    Returns:
        허프만 트리의 루트 노드
    """
    # 각 문자를 리프 노드로 만들어 최소 힙에 삽입
    heap = []
    for char, freq in freq_table.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))

    # 문자가 1개뿐인 경우 처리
    if len(heap) == 1:
        node = heapq.heappop(heap)
        root = HuffmanNode(freq=node.freq, left=node)
        return root

    # 노드가 하나가 될 때까지 가장 작은 두 노드를 합침
    step = 0
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # 새 내부 노드 생성
        merged = HuffmanNode(
            freq=left.freq + right.freq,
            left=left,
            right=right,
        )
        heapq.heappush(heap, merged)

        step += 1
        left_label = repr(left.char) if left.is_leaf() else f"[{left.freq}]"
        right_label = repr(right.char) if right.is_leaf() else f"[{right.freq}]"
        print(f"    Step {step}: 합침 {left_label}({left.freq}) + "
              f"{right_label}({right.freq}) = [{merged.freq}]")

    return heapq.heappop(heap)


def generate_codes(root, prefix="", codes=None):
    """허프만 트리를 순회하여 각 문자의 코드를 생성한다.

    왼쪽 간선 = '0', 오른쪽 간선 = '1'

    Args:
        root: 허프만 트리의 루트 노드
        prefix: 현재까지의 코드 접두어
        codes: 코드 딕셔너리 (재귀 호출용)

    Returns:
        {문자: 이진 코드 문자열} 딕셔너리
    """
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.is_leaf():
        # 리프 노드 -- 코드 확정
        codes[root.char] = prefix if prefix else "0"
        return codes

    generate_codes(root.left, prefix + "0", codes)
    generate_codes(root.right, prefix + "1", codes)

    return codes


def encode(text, codes):
    """텍스트를 허프만 코드로 인코딩한다.

    Args:
        text: 원본 문자열
        codes: {문자: 이진 코드 문자열} 딕셔너리

    Returns:
        인코딩된 비트 문자열
    """
    return "".join(codes[char] for char in text)


def decode(encoded_text, root):
    """인코딩된 비트 문자열을 허프만 트리로 디코딩한다.

    Args:
        encoded_text: 인코딩된 비트 문자열
        root: 허프만 트리의 루트 노드

    Returns:
        디코딩된 문자열
    """
    decoded = []
    current = root

    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            decoded.append(current.char)
            current = root

    return "".join(decoded)


def print_tree(node, prefix="", is_left=True, is_root=True):
    """허프만 트리를 시각적으로 출력한다."""
    if node is None:
        return

    if is_root:
        connector = ""
    elif is_left:
        connector = "|-- (0) "
    else:
        connector = "`-- (1) "

    if node.is_leaf():
        label = f"{repr(node.char)} [{node.freq}]"
    else:
        label = f"[{node.freq}]"

    print(f"    {prefix}{connector}{label}")

    if not is_root:
        new_prefix = prefix + ("|       " if is_left else "        ")
    else:
        new_prefix = prefix

    if not node.is_leaf():
        print_tree(node.left, new_prefix, True, False)
        print_tree(node.right, new_prefix, False, False)


def huffman_coding(text):
    """허프만 코딩의 전체 과정을 수행한다.

    Args:
        text: 인코딩할 문자열

    Returns:
        (인코딩된 비트열, 허프만 코드 테이블, 트리 루트)
    """
    # 1. 빈도 테이블 구성
    print("\n  [1단계] 빈도 테이블 구성")
    freq_table = build_frequency_table(text)
    print(f"    {'문자':<8} {'빈도':>6} {'비율':>8}")
    print(f"    {'-'*24}")
    for char, freq in freq_table.items():
        ratio = freq / len(text) * 100
        print(f"    {repr(char):<8} {freq:>6} {ratio:>7.1f}%")

    # 2. 허프만 트리 구축
    print(f"\n  [2단계] 허프만 트리 구축 (그리디: 빈도 최소 2개씩 합침)")
    root = build_huffman_tree(freq_table)

    # 트리 시각화
    print(f"\n  [2-1] 허프만 트리:")
    print_tree(root)

    # 3. 코드 생성
    print(f"\n  [3단계] 허프만 코드 생성")
    codes = generate_codes(root)
    # 코드 길이 순 정렬
    sorted_codes = sorted(codes.items(), key=lambda x: (len(x[1]), x[1]))
    print(f"    {'문자':<8} {'코드':<15} {'길이':>4} {'빈도':>6}")
    print(f"    {'-'*36}")
    for char, code in sorted_codes:
        print(f"    {repr(char):<8} {code:<15} {len(code):>4} {freq_table[char]:>6}")

    # 접두어 코드 검증
    print(f"\n  [3-1] 접두어 코드 검증:")
    is_prefix_free = True
    code_list = list(codes.values())
    for i in range(len(code_list)):
        for j in range(len(code_list)):
            if i != j and code_list[j].startswith(code_list[i]):
                is_prefix_free = False
                break
    print(f"    접두어 코드 속성: {'통과' if is_prefix_free else '실패'}")

    # 4. 인코딩
    print(f"\n  [4단계] 인코딩")
    encoded = encode(text, codes)
    text_display = repr(text[:80]) + ("..." if len(text) > 80 else "")
    print(f"    원본: {text_display}")
    display_encoded = encoded[:80]
    print(f"    인코딩: {display_encoded}{'...' if len(encoded) > 80 else ''}")

    # 5. 디코딩 검증
    print(f"\n  [5단계] 디코딩 검증")
    decoded = decode(encoded, root)
    is_correct = decoded == text
    decoded_display = repr(decoded[:80]) + ("..." if len(decoded) > 80 else "")
    print(f"    디코딩 결과: {decoded_display}")
    print(f"    원본 일치: {'통과' if is_correct else '실패'}")

    # 6. 압축률 계산
    print(f"\n  [6단계] 압축률 계산")
    original_bits = len(text) * 8  # ASCII 기준 8비트
    encoded_bits = len(encoded)
    compression_ratio = (1 - encoded_bits / original_bits) * 100

    # 고정 길이 코드와 비교
    num_chars = len(freq_table)
    fixed_bits_per_char = math.ceil(math.log2(num_chars)) if num_chars > 1 else 1
    fixed_total_bits = len(text) * fixed_bits_per_char

    # 허프만 평균 비트
    avg_huffman_bits = encoded_bits / len(text)

    # 엔트로피 (이론적 하한)
    entropy = 0
    for freq in freq_table.values():
        p = freq / len(text)
        if p > 0:
            entropy -= p * math.log2(p)

    print(f"    원본 크기 (ASCII 8bit):     {original_bits:>8} bits ({original_bits // 8} bytes)")
    print(f"    고정 길이 코드 ({fixed_bits_per_char}bit):    {fixed_total_bits:>8} bits")
    print(f"    허프만 코딩:                {encoded_bits:>8} bits")
    print(f"    이론적 하한 (엔트로피):      {len(text) * entropy:>8.0f} bits")
    print(f"")
    print(f"    허프만 평균 비트/문자:       {avg_huffman_bits:.3f}")
    print(f"    엔트로피:                   {entropy:.3f}")
    print(f"    ASCII 대비 압축률:          {compression_ratio:.1f}%")
    print(f"    고정 길이 대비 압축률:       {(1 - encoded_bits / fixed_total_bits) * 100:.1f}%")

    return encoded, codes, root


if __name__ == "__main__":
    print("=" * 65)
    print(" 허프만 코딩 (Huffman Coding)")
    print("=" * 65)

    # 예제 1: 간단한 텍스트
    print("\n" + "=" * 65)
    print("[예제 1] 간단한 텍스트")
    print("=" * 65)

    text1 = "abracadabra"
    huffman_coding(text1)

    # 예제 2: 영어 문장
    print("\n" + "=" * 65)
    print("[예제 2] 영어 문장")
    print("=" * 65)

    text2 = "the quick brown fox jumps over the lazy dog"
    huffman_coding(text2)

    # 예제 3: 빈도 편향이 큰 텍스트
    print("\n" + "=" * 65)
    print("[예제 3] 빈도 편향이 큰 텍스트 (압축 효과가 큰 경우)")
    print("=" * 65)

    text3 = "aaaaaaaabbbbccdd"
    huffman_coding(text3)

    # 요약
    print("\n" + "=" * 65)
    print(" 요약")
    print("=" * 65)
    print("""
  허프만 코딩의 그리디 전략:
  - 매 단계에서 빈도가 가장 낮은 두 노드를 합친다
  - 이 전략이 최적의 접두어 코드를 생성함이 증명되어 있다

  시간 복잡도: O(n log n)
  - n = 서로 다른 문자의 수
  - 최소 힙 연산 (삽입/삭제)이 O(log n)이고, n-1번 합침

  핵심 속성:
  - 접두어 코드: 어떤 코드도 다른 코드의 접두어가 아님
  - 이를 통해 구분자 없이 디코딩 가능
  - 빈도가 높을수록 짧은 코드 할당 -> 전체 비트 수 최소화
""")
