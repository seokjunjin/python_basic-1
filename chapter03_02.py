# # chapter03_02
# # 파이썬 문자형

# # 문자열 생성
# str1 = "I am Python"
# str2 = 'python'
# str3 = """how are you?"""
# str4 = '''thank you!'''

# print(type(str1), type(str2), type(str3), type(str4))
# print(len(str1), len(str2), len(str3), len(str4))

# # 빈 문자열
# str1_t1 = ''
# str2_t2 = str() #str() 형식도 빈 문자열

# print(type(str1_t1), len(str1_t1))
# print(type(str2_t2), len(str2_t2))

# # 이스케이프 문자 사용
# # I'm boy

# print("I'm boy")
# print('I\'m boy')
# print('a \t b')
# print('a \"\" b')

# escape_str1 = "Do you have a \"retro games\"?"
# print(escape_str1)

# # 탭, 줄바꿈
# t_s1 = "Click \t Start!"
# t_s2 = "New Line \n Check!"

# print(t_s1)
# print(t_s2)
# print()

# # Raw String
# # 주로 경로를 표시할 때 사용
# raw_s1 = r'D:\python\test'
# print(raw_s1)

# # 멀티라인 출력: 역 슬래시 사용
# multi_str = \
# """
# Keyword arguments:
# argument -- description
# Return: return_description
# """

# print(multi_str)

# # # 문자열 연산
# # str_o1 = "python"
# # str_o2 = "Apple"
# # str_o3 = "How are you doing"
# # str_o4 = "Seoul Daejeon Busan Ulsan"

# # print(str_o1 * 3)
# # print(str_o1 + str_o2)
# # print('y' in str_o1)
# # print('z' in str_o2)
# # print('p' not in str_o2)

# # # 문자열 형변환
# # print(str(66), type(str(66)))
# # print(str(True), type(str(True)))

# # # 문자열 함수(upper, isalnum, stratswith, count, endswith, isalpha, ...)
# # print("Capitalize: ", str_o1.capitalize())
# # print("endwith? :", str_o2.endswith("e"))
# # print("replace", str_o1.replace("thon", "good"))
# # print("sorted:", sorted(str_o1))
# # print("split:", str_o4.split(' '))

# # # 반복(시퀀스)
# # im_str = "Good boy!"

# # print(dir(im_str))

# # # 출력
# # # for i in im_str:
# # #     print(i)


# 슬라이싱
str_s1 = "Nice Python"


# 슬라이싱 연습
print(str_s1[0:3]) # 인덱스 이므로 0, 1, 2에 해당하는 텍스트가 출력됨
print(str_s1[5:11]) # Python만 출력
print(str_s1[5:])
print(str_s1[:len(str_s1)-1])
print(str_s1[1:9:2]) # 3번째 인수는 건너뛰는 단위
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1]) # 문자열을 거꾸로 출력함! :D 

# 아스키 코드
a = 'z'
print(ord(a)) # 아스키 코드 값 출력
print(chr(122)) # 문자로 출력