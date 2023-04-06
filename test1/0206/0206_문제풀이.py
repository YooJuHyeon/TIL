# 백준 2839번 : 설탕 배달
# 5kg봉지처럼 3kg봉지도 계속 몫과 나머지로 계산하려고 했었다.
# N에서 계속해서 3 빼주는 걸 생각하기까지 너무 오래 걸렸다.
# 사람들은 어떻게 이런 생각을 하지...
# 이래서 문제를 많이 풀어봐야 하는구나 싶다.

N = int(input())

if N % 5 == 0:           # N이 5로 나눠지면(나머지가 0이면)
    print(N//5)          # N을 5로 나눈 몫 출력

else:                    # N이 5로 바로 나눠지지 않는다면,
    cnt = 0              # 봉지 수 카운트할 변수 0으로 만들기

    while N > 0:         # N이 0보다 클때까지 while 반복문 돌리기
        N -= 3           # (N이 5의 배수가 될 때까지) 반복해서 3 빼기
        cnt +=1          # 3kg 봉지 뺐으니까 카운트변수에 1 추가

        if N % 5 == 0:     # N이 5로 나눠지면
            cnt += N // 5  # 카운트 변수에 N을 5로 나눈 몫 담기
            print(cnt)     # 카운트 변수 출력하고 멈추기
            break

        else:                # 아니면(N이 5로 나눈 나머지가 0이 아니라면)
            if N == 0:       # N이 0이라면
                print(cnt)   # 카운트 변수 출력하고 멈추기
                break

            elif 0< N < 3:    # N이 1 또는 2라면 (정확하게 봉지로 나눌 수 없음)
                print('-1')   # -1 출력하고 멈추기
                break