# 참참참 게임 프로그램
# 게임 순서
# 1. 컴퓨터/나 둘 중 누가 먼저 공격 할지 정한 후
# 2. 왼쪽/가운데/오른쪽 정해서 게임을 진행한다.
# 3. 한 게임이 종료 되면 이긴 사람이 득점 후, 공격 하는 것으로 게임이 진행됨
# 4. 5판 3선승제

import random  # 컴퓨터의 방향을 랜덤으로 정해주기 위한 random 모듈 import

direction = ["왼쪽", "가운데", "오른쪽"]  # 방향 pool


def chamchamcham():  # 참참참 게임이 실행되는 함수
    global pc_win, player_win, turn  # 메인 함수에서 선언해 둔 컴퓨터 승리 횟수/플레이어 승리 횟수/공격 차례를 함수 내에서 쓰기 위한 global 선언
    if turn == 1:  # 컴퓨터 공격 차례인 경우
        pc_direction = random.choice(
            direction)  # 컴퓨터의 공격 방향을 뽑는다 - 미리 선언해둔 direction 배열에서 random 모듈의 choice함수를 사용해 무작위 방향을 뽑는다
        print("\n고개를 돌릴 방향을 정해주세요!")
        player_direction = int(input("1.왼쪽  2.가운데  3.오른쪽 (번호로 선택해 주세요):"))  # 사용자가 고개를 돌려 수비할 방향을 정수값으로 받는다
        print("참 참 참!")
        print("컴퓨터: ", pc_direction, " | 나: ", direction[
            player_direction - 1])  # 컴퓨터의 공격 방향과 사용자의 수비 방향을 보여준다 ** 사용자의 입력값은 정수값으로 1~3까지의 값이지만 direction 배열의 인덱스는 0~2까지 이므로 -1 해준 인덱스로 접근 해 준다.
        if pc_direction == direction[player_direction - 1]:  # 컴퓨터의 공격 방향과 플레이어의 수비 방향이 같은 경우
            pc_win += 1  # 컴퓨터의 승점 1 증가
            print("컴퓨터가 공격에 성공했습니다.", pc_win, ":", player_win)  # 게임 결과 출력
        else:  # 컴퓨터의 공격 방향과 플에이어의 수비 방향이 다른 경우
            player_win += 1  # 플레이어의 승점 1 증가
            print("플레이어가 수비에 성공했습니다.", pc_win, ":", player_win)  # 게임 결과 출력
            turn = 2  # 플레이어가 수비에 성공, 플레이어가 공격하는 것으로 변경
    else:  # 플레이어가 공격 차례인 경우
        print("\n공격할 방향을 정해주세요!")
        player_direction = int(input("1.왼쪽  2.가운데  3.오른쪽 (번호로 선택해 주세요):"))  # 플레이어의 공격 방향을 정한다(정수 형으로 입력받는다).
        pc_direction = random.choice(direction)  # 컴퓨터의 수비 방향을 뽑는다(랜덤으로)
        print("참 참 참!")
        print("컴퓨터: ", pc_direction, " | 나: ", direction[player_direction - 1])  # 컴퓨터의 수비 방향과 플레이어의 공격 방향을 보여준다
        if pc_direction == direction[player_direction - 1]:  # 컴퓨터의 수비 방향과 플레이어의 공격 방향이 같은 경우
            player_win += 1  # 플레이어의 승점 1 증가
            print("플레이어가 공격에 성공했습니다.", pc_win, ":", player_win)  # 게임 결과 출력
        else:
            pc_win += 1  # 컴퓨터의 승점 1 증가
            print("컴퓨터가 수비에 성공했습니다.", pc_win, ":", player_win)  # 게임 결과 출력
            turn = 1  # 컴퓨터가 수비에 성공, 컴퓨터가 공격하는 것으로 변경


pc_win = 0  # 컴퓨터의 승리 횟수
player_win = 0  # 플레이어의 승리 횟수

print("누가 먼저 공격 할까요?")
turn = int(input("1.컴퓨터 2.나 : "))  # 누가 먼저 공격할 지 turn 변수에 정수형으로 입력받는다

while pc_win < 3 and player_win < 3:  # 3선승제로 진행하기 위해 컴퓨터, 플레이어 둘 중 한명이라도 3번 이기면 반복문을 탈출한다
    chamchamcham()  # 참참참 게임 실행

# 게임 총 결과 출력 - 각각 점수 보여주며 플레이어 승패 여부 출력
if pc_win == 3: # 컴퓨터가 세 번 이긴 경우
    print(pc_win, ":", player_win, "으로 패배하였습니다!")
else: # 플레이어가 세 번 이긴 경우
    print(pc_win, ":", player_win, "으로 승리하였습니다!")
