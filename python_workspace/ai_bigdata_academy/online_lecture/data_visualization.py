import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def one_data_one_graph():  # 하나의 데이터를 하나의 차트에 그리기
    x = [1, 2, 3]
    y = [4, 5, 6]

    plt.figure()  # 도화지 만들기 (생략 가능함)

    plt.plot(x, y)  # 그래프를 그리는 함수 (세번째 문자열 매개변수를 통해 색상, 선 종류 변경 가능)
    # linewidth = 선 굵기, color = 그래프 색상, marker = 마커 생성, linestyle = 선 종류

    # plt.plot(y) # y값만 매개변수로 줘도 그려짐(index가 x값으로 되는듯?)

    plt.title("graph")  # 그래프의 이름을 정할 수 있음 -> fontsize를 통해 크기 조정 가능

    # x,y 축의 이름을 지정해줄 수 있음 -> fontsize를 통해 크기 조정 가능
    plt.xlabel('x')
    plt.ylabel('y')

    plt.grid(True)  # 격자 생성 axis 옵션으로 가로 세로 격자선만 생성가능

    # x범위 y범위를 지정해서 그래프의 구간을 정해 줄 수있다
    plt.xlim([2, 4])
    plt.ylim([5, 6])
    # axis를 통해 그래프의 구간을 정해 줄 수도 있음
    plt.axis([1, 2, 4, 5])

    # 축의 폰트 크기 조정
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=25)

    # 그래프의 특정 위치에 텍스트 삽입
    plt.text(1.2, 4.4, 'text', fontsize=10)

    plt.show()


def multi_data_one_graph():  # 여러 데이터를 한 차트에 그리기
    x1 = [1, 2, 3]
    x2 = [1, 2, 3]
    y1 = [1, 2, 3]
    y2 = [1, 4, 7]

    plt.plot(x1, y1, color='red')
    plt.plot(x2, y2, color='blue')

    # or

    # plt.plot(x1,x1,'b',x2,y2,'r')

    plt.legend(['data1', 'data2'], loc='upper right')  # plot에서 지정한 lable을 범례로 추가(혹은 직접 추가 가능)
    # loc = 위치 조절 / fontsize = 범례 글자 크기

    y2 = [1, 100, 200]  # 엄청 크기가 큰 값 대입
    plt.plot(x2, y2, color='blue')

    plt.show()


def multi_data_multi_graph():  # 다중 값으로 여러 그래프 그리기
    x1 = [1, 2, 3]
    y1 = [1, 2, 3]
    x2 = [1, 2, 3]
    y2 = [1, 50, 200]

    # 1. subplot을 통해 그리기
    # subplot(행의 수, 열의 수, 해당 그래프가 그려질 위치)

    # # 가로로 두 개의 그래프
    # plt.subplot(1,2,1)
    # plt.plot(x1,y1)
    # plt.title('data1')
    #
    # plt.subplot(1,2,2)
    # plt.plot(x2,y2)
    # plt.title('data2')

    # # 세로로 두 개의 그래프
    # plt.subplot(2, 1, 1)
    # plt.plot(x1, y1)
    # plt.title('data1')
    #
    # plt.subplot(2, 1, 2)
    # plt.plot(x2, y2)
    # plt.title('data2')
    # plt.tight_layout()  #글자 겹치고 그러는거 방지-레이아웃 자동 설정
    #
    #
    # # 2. subplots를 통해 그리기 -> (row,col) 구조로 다중 그래프 그리기 가능!
    # fig, axe1 = plt.subplots(nrows=2, ncols=2)
    #
    # axe1[0][0].plot(x1,y1,color='blue')
    # axe1[0][1].plot(x1,y2,color='red')
    # axe1[1][0].plot(x2,y1,color='green')
    # axe1[1][1].plot(x2,y2,color='black')

    # 3. 두 개의 데이터를 한 그래프 안에 그리기 -> y축을 두 개 사용
    fig, axe1 = plt.subplots()

    axe2 = axe1.twinx()
    chart1 = axe1.plot(x1, y1, color='red', label='data1')
    chart2 = axe2.plot(x2, y2, color='blue', label='data2')

    axe1.set_xlabel('x', fontsize=15)
    axe1.set_ylabel('y1', fontsize=15)
    axe2.set_ylabel('y2', fontsize=15)

    # 범례 표시하기
    chart = chart1 + chart2
    axe1.legend(chart, ['data1', 'data2'])

    plt.show()


def dataset_loading():
    df = sns.load_dataset('iris')
    print(df.head())

    # iris 데이터 셋의 petal_length와 petal_width를 이용해 산점도 그리기

    # matplotlib
    # plt.scatter(df['petal_length'],df['petal_width'])

    # seaborn
    # sns.scatterplot(data=df,x='petal_length',y='petal_width')
    # plt.title('iris')


    # 영화별 관람자 수를 막대그래프로 표현
    movie_title = ['c', 'b', 's']
    audience = [664308, 2099131, 20067]

    data = {'title': movie_title, 'audi': audience}
    df = pd.DataFrame(data)
    sns.set(rc={'figure.figsize':(10,5)}) # 차트 크기 변경
    chart = sns.barplot(data=df,x='title',y='audi', order=df.sort_values('audi',ascending=False).title)
    # order 에서 정렬된 df로 정렬된 막대그래프 그리기 가능

    # 관객 수 포맷 변환
    # ylabels = ['{:,.0f}'.format(i) + 'k' for i in chart.get_yticks() / 1000]
    # chart.set_yticklabels(ylabels)

    # 경고문 없애기
    import matplotlib.ticker as mticker

    ticks_labels = chart.get_yticks().tolist()
    chart.yaxis.set_major_locator(mticker.FixedLocator(ticks_labels))
    chart.set_yticklabels(['{:,.0f}'.format(i / 1000) + 'k' for i in ticks_labels])

    chart = sns.barplot(data=df,x='audi',y='title',order=df.sort_values('audi',ascending=False).title)
    xlabels = ['{:,.0f}'.format(i)+'k' for i in chart.get_xticks()/1000]
    chart.set_xticklabels(xlabels)

    plt.show()


if __name__ == "__main__":
    # one_data_one_graph()
    # multi_data_one_graph()
    # multi_data_multi_graph()
    dataset_loading()

