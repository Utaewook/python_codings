numbers=[('abc',2),('def',3),('ghi',4),('jkl',5),('mno',6),('pqrs',7),('tuv',8),('wxyz',9)]
num_map={c:v for k,v in numbers for c in k}
s=input("문자열을 입력하지오: ")
result="".join(str(num_map.get(v)) for v in s.lower())
print(result)