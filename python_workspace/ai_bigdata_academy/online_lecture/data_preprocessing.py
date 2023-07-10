import pandas as pd
import numpy as np
import copy

# --------------- 데이터 프레임 생성---------------
print('\n데이터 프레임 생성\n')
df = pd.DataFrame({'a': [1,2,3], 'b':[4,5,6], 'c':[7,8,9]})

print(df)


dummy = {'a': [1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
df2 = pd.DataFrame(dummy)

print(type(df2))
print(df2)

dummy2 = [[1,4,7],[2,5,8],[3,6,9]]
df3 = pd.DataFrame(dummy2)
print(df3)

df3.columns = ['a','b','c']
print(df3)

a = {'company':['acb','회사','152'], '직원수':[125,1243,75]}
df_a = pd.DataFrame(a)
print(df_a)


# NaN값을 어떻게 넣을까?
a['위치'] = ['Seoul',None,'Busan']
df_a = pd.DataFrame(a)
print(df_a)

# np.NaN을 사용
a['위치'] = ['Seoul',np.NAN,'Busan']
df_a = pd.DataFrame(a)
print(df_a)

# --------------- 칼럼명 추출 변경 ---------------

print('\n칼럼명 추출 변경\n')
print(df.columns)
print(df.columns[1])

# 칼럼명 변경
df.columns = ['d','e','f']
print(df.columns)

df.rename(columns={'d':'뒤'},inplace=True) # inplace true로 해줘야 변경된다.
print(df.columns)
print(df)

# --------------- copy를 이용한 데이터 복사 ---------------

print('\ncopy를 이용한 데이터 복사\n')
df.columns = ['a','b','c']

df2 = df  # 얕은 복사(ref 복사)
print(df)
print(df2)
df.columns = ['d','e','f']

print(df)
print(df2)


df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})
df2 = copy.deepcopy(df)
df.columns = ['d','e','f']
print(df)
print(df2)

# --------------- 시리즈 ---------------

print('\n시리즈\n')


df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})
print(df['a'])

a = pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])
print(a)

print(a['e'])
