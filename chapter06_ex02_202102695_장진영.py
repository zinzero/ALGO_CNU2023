# 문자열 매칭에 사용되는 호스풀 알고리즘을 구현한 프로그램
# 시간복잡도 : O(mn) -> O(n)
# 비교하는 패턴의 비해 텍스트의 길이가 아주 커지면 패턴의 크기 보다 텍스트의 크기가 영향을 더 미치기 때문에
# 시간복잡도가 O(n)이 된다.
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간
NO_OF_CHARS = 128


# 전처리를 위한 shift table
def shift_table(pat):
    m = len(pat)  # 패턴 문자열의 길이
    tbl = [m] * NO_OF_CHARS  # 테이블을 패턴 문자열의 길이와의 곱으로 테이블 초기화

    for i in range(m - 1):  # m -1 만큼 반복한다
        # ord()함수를 이용해서 패턴의 해당하는 char를 유니코 포인트로 변환한다.
        # 변환한 결과 값인 정수를 인덱스로 사용해서
        # 해당 인덱스의 값을 저장한다.
        tbl[ord(pat[i])] = m - 1 - i

    return tbl


# 호스풀 함수
def search_horspool(T, P):
    m = len(P)  # 패턴 문자열의 길이
    n = len(T)  # 텍스트 문자열의 길이
    t = shift_table(P)  # shift_table 호출 -> 전처리 하기
    i = m - 1  # 패턴 문자열의 끝 번호 인덱스 값
    while i <= n - 1:  # 인덱스 범위가 텍스트 문자열의 길이보다 작을 때 까지 반복한다.
        k = 0
        # k가 패턴의 길이보다 작고 패턴과 문자열을 뒤에서 부터 비교해서 일치한다면
        while k <= m - 1 and P[m - 1 - k] == T[i - k]:
            k += 1  # k의 값을 증가 시킨다.
        if k == m:  # k와 m의 길이가 일치하면
            return i - m + 1  # 패턴의 시작 위치를 반환
        else:
            # 아닌경우 쉬프트 테이블에서 텍스트의 유니코드를 이용하여 해당하는 테이블 값을 tc에 저장
            tc = t[ord(T[i - k])]
            i += tc - k  # tc - k 값을 i에 더해준다.
    return -1  # 패턴의 시작 위치를 찾지 못하면 -1을 반환


text = input()  # 텍스트 입력받기
pattern = input()  # 패턴 입력받기

end_time = time.time()  # 프로그램 종료 시간

print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
print("패턴의 위치 :", search_horspool(text, pattern))  # 호스풀 알고리즘 결과 출력
