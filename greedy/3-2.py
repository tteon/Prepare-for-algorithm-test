'''

# N, M, K 를 공백으고 구분하여 입력받기
print('plz input the condition () , () , ()')
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K 번 더하기
        if m == 0 : # m 이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할때마다 1씩 빼기
    if m == 0 : # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력

'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
### 핵심 파트 , 반복되는 수열을 구함.
count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second
print(result)