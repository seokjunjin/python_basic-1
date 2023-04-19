print('python', 'google.com', sep='@')

# # end 옵션
print('welcome to', end=' ')
print('IT news', end=' ')
print('web site')

# #file option
# #출력된 내용을 파일로 저장
import sys

# print('Learn Python', file=sys.stdout)

# #format (d(digit), s(string), f(float))
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) 
# 배열은 0부터 시작,  따라서 1은 두 번째이므로 two가 매핑되고 0이 첫번째이므로 one이 매핑되는 것임

# %s
print('%10s' % ('nice')) # 끝에서부터 채우고 앞 자리를 공백으로 채움
print('{:>10}'.format('nice')) # 끝에서부터 채우고 앞 자리를 공백으로 채움

print('%-10s' % ('nice')) #오른쪽을 공백으로 채움
print('{:10}'.format('nice')) #오른쪽을 공백으로 채움


print('{:$>10}'.format('nice')) # > 앞에 들어갈 수 있는 글자는 한 글자
print('{:^10}'.format('nice')) # 중앙 정렬
print('%.5s' % ('pythonstudy')) 
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%01.8f' % (3.141435611354))
print('%6.2f' % (123131.141435611354))
print('%06.2f' % (123131.141435611354))
print('{:06.2f}'.format(2.34567)) ### 2.35 -> 소수점 3자리가 반올림해서 출력됨