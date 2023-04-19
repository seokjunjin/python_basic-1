# chapter02-1
# 파이썬 완전 기초
# print 사용 방법

print('python start')
print("python start")
print('''python start''')
print("""python start""")

# print('터미널 토글을 하려면 ctrl + ; 누릅니다') 

# # separator 옵션 사용
print('p', 'y','t','h','o','n', sep = '')

# 랜덤한 글자를 출력하는 코드 
import random

for i in range(1, 7):
    r = random.randrange(1, 44)
    print('%4d' % (r), end='')    