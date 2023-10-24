# 반복문(for, while)
# for : 반복 횟수가 정해져 있을 때(a 10번 출력해줘)
# while : 조건이 중요할 때 사용(10보다 작을 때 까지만 반복해줘)

#for 시작_0~9까지 출력
'''
for i0 in range(10):
    print("안녕하세요")
'''

#while 시작
'''
i = 0
while i < 10:
    print(i)
    i += 1
'''

i=0
while True:
    if i ==10:
        break
    print(i)
    i += 1

# 조건문