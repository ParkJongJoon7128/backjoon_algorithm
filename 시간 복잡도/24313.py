a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# f(n) = 7n + 7, g(n) = n, c = 8, n0 = 1이다. f(1) = 14, c × g(1) = 8

if(((a1 * n0) + a0 <= (c * n0)) and (a1 <= c)):
    print(1)
else:
    print(0)

