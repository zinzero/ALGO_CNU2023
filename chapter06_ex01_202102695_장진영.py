# 기수정렬 알고리즘을 구현한 프로그램
# 시간복잡도
# 수의 자릿수 d, 리스트의 길이 n -> O(dn)
# 수의 자릿수는 리스트의 길이가 충분히 커지면 무시할 수 있으므로 -> O(n)

from queue import Queue  # 버킷을 FIFO 형태로 이용하기 위해 사용하는 모듈
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 실행시간을 알아보기 위한 모듈


# 기수정렬
def radix_sort(A):
    queues = []  # 정렬을 위한 리스트
    for i in range(BUCKETS):  # 버킷의 길이 만큼
        queues.append(Queue())  # 리스트의 큐를 append한다.

    n = len(A)  # 정렬하는 리스트의 길이
    factor = 1  # 자리수를 구분하기 위한 정수
    for d in range(DIGITS):  # 자릿수 만큼 반복하면서
        for i in range(n):  # 정렬할 리스트의 길이만큼 반복한다.
            # 정렬할 리스트의 데이터와 factor를 나누고 10으로 모듈러 연산을 하면 1의자리 수가 된다.
            # 해당 자리수의 값을 인덱스로 사용해서 값을 넣어준다.
            queues[(A[i]//factor) % 10].put(A[i])
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()  # 큐의 값을 가져와서 리스트의 정렬하면서 저장한다.
                j += 1
            factor *= 10  # factor의 값을 10을 곱해서 다음 자릿수로 넘어가도록 한다.


data = list(map(int, input().split()))  # 숫자를 입력받아서 리스트로 저장

end_time = time.time()  # 프로그램 종료 시간

BUCKETS = 10  # 0 ~ 9 까지를 의미하는 버킷
DIGITS = 4  # 입력 받는 숫자의 자릿수
radix_sort(data)  # 기수정렬 시작
print("실행시간 : ", end_time - start_time)  # 프로그램 실행 시간 출력
print("Radix: ", data)  # 결과물 출력
