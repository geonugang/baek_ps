grade_dict = {'A+':4.5,
              'A0':4.0,
              'B+':3.5,
              'B0':3.0,
              'C+':2.5,
              'C0':2.0,
              'D+':1.5,
              'D0':1.0,
              'F':0}                                # 인하대학교 컴퓨터공학과의 등급에 따른 과목평점
total = 0
result = 0
for i in range(20):                                 # 20번 전공과목의 과목명, 학점, 등급입력
    sub, grades, rate = input().split()
    grades = float(grades)                          # grades를 float형으로 변환
    if rate != 'P':                                 # rate가 p일 경우 계산에서 제외
        total += grades                             # total에 학점을 저장
        result += grades * grade_dict[rate]         # result에 학점과 등급에 맞는 학점을 곱한 후 저장

final = result/total                                # result에 total학점을 나누어 전공평점을 계산
print('{:.6f}'.format(final))                       # 소수점 6번째 까지 출력