
# 파일명: hw3_1.py
# 작성자: 유태욱
# 작성일자: 2022-09-15
# 주요기능: 16진수 데이터 입력, 정수로 저장 bit wise AND/OR/XOR 계산후 출력
# 최종수정일자: 2022-09-15
# 수정내용: 최초작성

a,b = input("input two hexadecimal numbers (예: 0xA3 0x3A) : ").split() # 2개의 16진수 데이터 문자열 입력
a,b = int(a,16),int(b,16) # 입력받은 두 16진수 데이터를 10진수(정수)로 저장

print(f"a = {hex(a)} = 0b{format(a,'08b')}") # 첫 번째로 입력받은 값을 16진수와 2진수로 출력
print(f"b = {hex(b)} = 0b{format(b,'08b')}") # 두 번째로 입력받은 값을 16진수와 2진수로 출력
print(f"a & b = {hex(a&b)} = 0b{format(a&b,'08b')}") # 두 값의 bit wise AND 계산값을 16진수와 2진수로 출력
print(f"a | b = {hex(a|b)} = 0b{format(a|b,'08b')}") # 두 값의 bit wise OR 계산값을 16진수와 2진수로 출력
print(f"a ^ b = {hex(a^b)} = 0b{format(a^b,'08b')}") # 두 값의 bit wise XOR 계산값을 16진수와 2진수로 출력