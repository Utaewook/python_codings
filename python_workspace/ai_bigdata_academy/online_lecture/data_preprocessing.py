import pandas as pd
import numpy as np
import copy

# # --------------- 데이터 프레임 생성---------------
# print('\n데이터 프레임 생성\n')
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
#
# print(df)
#
# dummy = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# df2 = pd.DataFrame(dummy)
#
# print(type(df2))
# print(df2)
#
# dummy2 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# df3 = pd.DataFrame(dummy2)
# print(df3)
#
# df3.columns = ['a', 'b', 'c']
# print(df3)
#
# a = {'company': ['acb', '회사', '152'], '직원수': [125, 1243, 75]}
# df_a = pd.DataFrame(a)
# print(df_a)
#
# # NaN값을 어떻게 넣을까?
# a['위치'] = ['Seoul', None, 'Busan']
# df_a = pd.DataFrame(a)
# print(df_a)
#
# # np.NaN을 사용
# a['위치'] = ['Seoul', np.NAN, 'Busan']
# df_a = pd.DataFrame(a)
# print(df_a)
#
# # --------------- 칼럼명 추출 변경 ---------------
#
# print('\n칼럼명 추출 변경\n')
# print(df.columns)
# print(df.columns[1])
#
# # 칼럼명 변경
# df.columns = ['d', 'e', 'f']
# print(df.columns)
#
# df.rename(columns={'d': '뒤'}, inplace=True)  # inplace true로 해줘야 변경된다.
# print(df.columns)
# print(df)
#
# # --------------- copy를 이용한 데이터 복사 ---------------
#
# print('\ncopy를 이용한 데이터 복사\n')
# df.columns = ['a', 'b', 'c']
#
# df2 = df  # 얕은 복사(ref 복사)
# print(df)
# print(df2)
# df.columns = ['d', 'e', 'f']
#
# print(df)
# print(df2)
#
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
# df2 = copy.deepcopy(df)
# df.columns = ['d', 'e', 'f']
# print(df)
# print(df2)
#
# # --------------- 시리즈 ---------------
#
# print('\n시리즈\n')
#
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
# print(df['a'])
#
# a = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(a)
#
# print(a['e'])
#
# print(a.unique())
#
# # --------------- loc, iloc ---------------
#
# print('\nloc, iloc\n')
#
# df = pd.DataFrame({'a': [i for i in range(1, 11)], 'b': [i for i in range(11, 21)], 'c': [i for i in range(21, 31)]})
#
# print(df)
#
# # 문제: a,b 열을 추출하시오
# print(df[['a', 'b']])
#
# # 문제: 첫번쨰 행을 출력
# print(df.loc[0])
#
# # 범위 추출
# print(df.loc[2:4])  # 파이썬의 슬라이싱과는 다르게 마지막 인덱스의 요소까지 불러온다!
#
# idx = ['a', 'b', 'c', 'c', 'e', 'f', 'g', 'h', 'i', 'j']
# df.index = idx
#
# print(df.loc['a':'c'])
# print(df.loc['c':])
#
# # 행-열 순서대로
# print(df.loc[['g', 'i'], ['a', 'c']])
#
# df = pd.DataFrame({'a': [i for i in range(1, 11)], 'b': [i for i in range(11, 21)], 'c': [i for i in range(21, 31)]})
#
# # iloc (index 로 location 접근) - 인덱스가 문자열 등 다른 걸로 대치 되어도 0부터 시작하는 인덱스로 접근 가능함
#
# print(df.iloc[:5, [0, 2]])
#
# # --------------- 조건에 맞는 데이터 추출 ---------------
#
# print('\n조건에 맞는 데이터 추출\n')
#
# print(df[df['a'] >= 3])
#
# print(df[df['a'] >= 3][['a', 'c']])
#
# print(df[(df['a'] >= 3) & (df['b'] <= 17)])
#
# print(df[(df['a'] <= 3) | (df['a'] >= 7)])
#
# print(df[(df['a'] >= 3) & ((df['b'] <= 16) | (df['c'] == 30))])
#
# # --------------- sort ---------------
#
# print('\nsort\n')
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, 5, 3], 'c': [1, 345, 2, 3, 5]})
#
# print(df)
#
# df.sort_index(ascending=False, inplace=True)
# print(df)
#
# df.reset_index(inplace=True, drop=True)
# print(df)
#
# df.sort_values(by=['b', 'c'], ascending=True, inplace=True)
# print(df)
#
# df.sort_values(by=['b', 'c'], ascending=[True, False], inplace=True)
# print(df)
#
# # --------------- 결측값 처리 ---------------
#
# print('\n결측값 처리\n')
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# print(df)
#
# print(df.isnull())
# print(df.isnull().sum())
#
# # 행 기준으로 결측지 삭제
# df.dropna(inplace=True)
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
#
# # 열 기준으로 결측치 삭제
# df.dropna(axis=1, inplace=True)
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# df.fillna(0, inplace=True)
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# df.fillna(method='bfill', inplace=True)  # 뒤에 값으로 채우기
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# df.fillna(method='ffill', inplace=True)  # 앞에 값으로 채우기
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# df.fillna(method='ffill', limit=1, inplace=True)  # 앞에 값을 한번만 채우기 (연쇄적으로는 안됨)
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# df.fillna(df.mean()['a'], inplace=True)  # a 열의 평균값으로 채우기
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# df.fillna(df.mean(), inplace=True)  # 각 열의 평균값으로 채우기
# print(df.mean())
# print(df)
#
# df = pd.DataFrame({'a': [2, 3, 2, 7, 4], 'b': [2, 1, 3, np.NAN, np.NAN], 'c': [1, np.NAN, 2, 3, 5]})
# df.fillna(df.mean()[['b','c']], inplace=True)  # b,c 열의 결측값들을 각 평균값으로 채우기
# print(df.mean())
# print(df)
#
#
# --------------- 타입 변환 ---------------
#
# print('\n타입 변환\n')
#
# df = pd.DataFrame({'판매일':['5/11/21','5/12/21','5/13/21','5/14/21','5/15/21'],
#                    '판매량':['10','15','20','25','30'],
#                    '방문자수':['10','-','17','23','25'],
#                    '기온':['24.1','24.3','24.8','25','25.4']})
# print(df)
# print(df.dtypes)
#
# df = df.astype({'판매량': 'int'})
#
# df['판매량 보정'] = df['판매량'] + 1
# print(df)
# print(df.dtypes)
#
# df['방문자수'] = pd.to_numeric(df['방문자수'],errors='coerce')
# print(df)
# print(df.dtypes)
#
# df.fillna(0,inplace=True)
# df = df.astype({'방문자수':'int'})
# print(df)
# print(df.dtypes)
#
# df['판매일'] = pd.to_datetime(df['판매일'],format='%m/%d/%y')
# print(df)
#
# --------------- 레코드, 칼럼 추가/삭제 ---------------
#
# print('\n레코드, 칼럼 추가/삭제\n')
#
# df = pd.DataFrame({'a': [1, 1, 3, 4, 5], 'b': [2, 3, 2, 3, 4], 'c': [3, 4, 7, 6, 4]})
#
# # 1,3,6,4,8로 이루어진 d 칼럼을 추가하기
# df['d'] = [1, 3, 6, 4, 8]
# print(df)
#
# # 1로 이루어진 e 칼럼 추가
# df['e'] = [1, 1, 1, 1, 1]
# print(df)
#
# df['f'] = 3
# print(df)
#
# df['g'] = df['a'] + df['b'] - df['c']
# print(df)
#
# df.drop(['d', 'e', 'f', 'g'], axis=1, inplace=True)
# print(df)
#
# # 레코드(행) 추가
#
# df = df.append({'a': 6, 'b': 7, 'c': 8}, ignore_index=True)
# print(df)
#
# df.loc[6] = [7, 8, 9]
# print(df)
#
# # 레코드 삭제
#
# df.drop(0, inplace=True)
# print(df)
#
# df = pd.DataFrame({'a': [1, 1, 3, 4, 5], 'b': [2, 3, 2, 3, 4], 'c': [3, 4, 7, 6, 4]})
# df.drop([i for i in range(4)], inplace=True)
# print(df)
#
# df = pd.DataFrame({'a': [1, 1, 3, 4, 5], 'b': [2, 3, 2, 3, 4], 'c': [3, 4, 7, 6, 4]})
# df.drop(df.index[:4], inplace=True)
# print(df)
#
# df = pd.DataFrame({'a': [1, 1, 3, 4, 5], 'b': [2, 3, 2, 3, 4], 'c': [3, 4, 7, 6, 4]})
# idx = df[df['a'] < 4].index
# df.drop(idx, inplace=True)
# print(df)
#
# # --------------- 데이터 변환 ---------------
#
# print('\n데이터 변환\n')
#
# df = pd.DataFrame({'a':[1,2,3,4,5]})
#
# df['b'] = 0
# pd.set_option('mode.chained_assignment',None)
#
# a = df[df['a']<2]
# print(a)
# df['b'][a.index] = '2미만'
#
#
# b = df[(df['a']<4)&(df['a']>=2)]
# print(b)
# df['b'][b.index] = '4미만'
#
# c = df[df['a']>=4]
# print(c)
# df['b'][c.index] = '4이상'
#
# print(df)
#
#
# def case_function(x):
#     if x<2:
#         return '2 미만'
#     elif x<4:
#         return '4 미만'
#     else:
#         return '4 이상'
#
# df['c'] = df['a'].apply(case_function)
# print(df)
#
# m = {1:'one',2:'two',3:'three',4:'four',5:'five'}
#
# df['d'] = df['a'].map(m)
# print(df)
#
# --------------- 데이터 프레임 결합 ---------------
#
# print('\n데이터 프레임 결합\n')
#
#
# # 상하 결합
# df1 = pd.DataFrame({'a':[1,2,3],'b':[11,12,13],'c':[21,22,23]})
# df2 = pd.DataFrame({'a':[4,5,6],'b':[14,15,16],'c':[24,25,26]})
#
# print(pd.concat([df1,df2]))
# print(pd.concat([df2,df1],ignore_index=True))
#
# df1 = pd.DataFrame({'a':[1,2,3],'b':[11,12,13],'c':[21,22,23],'d':[41,42,43]})
# df2 = pd.DataFrame({'a':[4,5,6],'b':[14,15,16],'c':[24,25,26],'e':[51,52,53]})
#
# print(pd.concat([df2,df1],ignore_index=True))
#
#
# df1 = pd.DataFrame({'a':[1,2,3],'b':[11,12,13],'c':[21,22,23],'d':[41,42,43]})
# df2 = pd.DataFrame({'a':[4,5,6],'b':[14,15,16],'c':[24,25,26],'e':[51,52,53]})
#
# print(pd.concat([df2,df1],join='outer',ignore_index=True))
#
# df1 = pd.DataFrame({'a':[1,2,3],'b':[11,12,13],'c':[21,22,23],'d':[41,42,43]})
# df2 = pd.DataFrame({'a':[4,5,6],'b':[14,15,16],'c':[24,25,26],'e':[51,52,53]})
#
# print(pd.concat([df2,df1],join='inner',ignore_index=True))
#
# # 좌우 결합
#
# df1 = pd.DataFrame({'a':[1,2,3],'b':[11,12,13],'c':[21,22,23],'d':[31,32,33]})
# df2 = pd.DataFrame({'e':[3,4,5],'f':[13,14,15],'g':[23,24,25],'h':[41,42,43]})
#
# print(pd.concat([df1,df2],axis=1))
#
# df1 = pd.DataFrame({'id':[1,2,3],'성별':['f','m','f'],'나이':[20,30,40]})
# df2 = pd.DataFrame({'id':[1,2,3],'키':[153.4,170.3,178.4],'몸무게':[52.1,63.4,81.4]})
#
# print(pd.concat([df1,df2],axis=1))
#
#
# df1 = pd.DataFrame({'id':[1,2,3,4,5],'성별':['f','m','f','m','f'],'나이':[20,30,40,34,19]})
# df2 = pd.DataFrame({'id':[3,4,5,6,7],'키':[153.4,170.3,178.4,150,169.1],'몸무게':[52.1,63.4,81.4,69,49]})
# print(pd.concat([df1,df2],axis=1))
#
# # 여러 join을 통한 merge
#
# print(pd.merge(df1,df2,how='left',on='id'))
# print(pd.merge(df1,df2,how='inner',on='id'))
# print(pd.merge(df1,df2,how='right',on='id'))
# print(pd.merge(df1,df2,how='outer',on='id'))
#
#
# df1 = pd.DataFrame({'id':[1,2,3,4,5],'성별':['f','m','f','m','f'],'나이':[20,30,40,34,19]})
# df2 = pd.DataFrame({'user_id':[3,4,5,6,7],'키':[153.4,170.3,178.4,150,169.1],'몸무게':[52.1,63.4,81.4,69,49]})
#
# print(pd.merge(df1,df2,how='outer',left_on='id',right_on='user_id'))
#
#
# df1 = pd.DataFrame({'ID' : [1, 2, 3, 4, 5], '가입일' : ['2021-01-02', '2021-01-04', '2021-01-10', '2021-02-10', '2021-02-24'], '성별' : ['F', 'M', 'F', 'M', 'M']})
# df2 = pd.DataFrame({'구매순서' : [1, 2, 3, 4, 5], 'ID' : [1, 1, 2, 4, 1], '구매월' : [1, 1, 2, 2, 3], '금액' : [1000, 1500, 2000, 3000, 4000]})
#
# print(pd.merge(df1,df2,how='left',on='ID'))

# --------------- 그룹화 ---------------

print('\n그룹화\n')

df1 = pd.DataFrame(
    {'ID': [1, 2, 3, 4, 5], '가입일': ['2021-01-02', '2021-01-04', '2021-01-10', '2021-02-10', '2021-02-24'],
     '성별': ['F', 'M', 'F', 'M', 'M']})
df2 = pd.DataFrame(
    {'구매순서': [1, 2, 3, 4, 5], 'ID': [1, 1, 2, 4, 1], '구매월': [1, 1, 2, 2, 3], '금액': [1000, 1500, 2000, 3000, 4000]})

print(df2.groupby(by=['ID'])['금액'].sum())
s2 = df2.groupby(by=['ID'])['금액'].sum()

print(pd.merge(df1, s2, how='left', on='ID'))

s3 = df2.groupby(by=['ID','구매월'])['금액'].sum()
print(s3)
print(pd.merge(df1,s3, how='left',on='ID'))

s4 = df2.groupby(by=['ID','구매월'],as_index=False)['금액'].sum()
print(s4)
print(pd.merge(df1,s4, how='left',on='ID'))

df = pd.DataFrame({'구매순서' : [1, 2, 3, 4, 5], 'ID' : [1, 1, 2, 4, 1], '구매월' : [1, 1, 2, 2, 3], '금액' : [1000, 1500, 2000, 3000, 4000], '수수료' : [100, 150, 200, 300, 400]})
print(df.groupby(by = ['ID'])['금액'].agg([sum, len]))
print(df.groupby(by = ['ID'], as_index = False)['금액'].agg([sum, len]))
df2 = df.groupby(by = ['ID'])['금액'].agg([sum, len])
df2.reset_index(inplace = True)
print(df2)


print(df.groupby(by = ['ID']).agg({'금액' : [max, min], '수수료' : min}))
df2 = df.groupby(by = ['ID']).agg({'금액' : [max, min], '수수료' : min})
df2.reset_index()
print(df2)
print(df2.columns)
print(df2.columns.values)

df2.columns = ['_'.join(col) for col in df2.columns.values]
df2.reset_index(inplace=True)
print(df2)