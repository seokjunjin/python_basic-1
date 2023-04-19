# chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)

# object reference
# 변수값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)

# 예2)
n = 777
print(n, type(n))

m = n
print(m, n)

# id(identify) 확인
m = 800
n = 600
print(id(m))
print(id(n))

# 같은 오브젝트 참조
m = 800
n = 800
print(id(m))
print(id(n))

#다양한 변수 선언
#Camel Case : numberOfCollegeGraduates -> Method
#Pascal Case : NumberOfCollegGraduates -> Class
#Snake Case : number_of_colleague_graduates

#reservered keyword는 변수에 사용할 수 없음
#_, $ 등을 붙여서 변수 선언을 할 수는 있음