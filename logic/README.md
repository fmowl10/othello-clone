Logic packages
===
# 목차
1. [board](#board)
2. [cell](#cell)
3. [enums](#enums)
4. [game](#game)

## board
---
1. [Board](#Board)
### Board
___
## attribute
* [size](#size)
* [board](#board)
* [black_point](#black_point)
* [white_point](#white_point)
* [placed_able](#placed_able)
* [is_over](#is_over)
* [is_pass](#is_pass)
* [who_win](#who_win)
* [turn](#turn)
---

#### size
게임판의 크기
___
#### board
게임판
____
#### black_point
검정말들의 위치 정보들
___
#### white_point
흰말의 위치 정보들
___
#### placed_able
현재 턴에서 말을 둘 수 있는 위치 정보들
___
#### is_over
게임이 끝났는가를 저장
___
#### is_pass
현재 턴에서 말을 둘 수 없는 경우
___
#### who_win
게임이 끝나고 누가 이겼는지를 저장
___
#### turn
누구의 턴인지 저장
___
methods
* [생성자](#Board-생성자)
* [get_who_win](#get_who_win)
* [get_turn](#get_turn)
* [get_is_over](#get_is_over)
* [get_is_pass](#get_is_pass)
* [get_placed_able_next](#get_placed_able_next)
* [start_game](#start_game)
* [place_cell](#place_cell)
* [reverse](#reverse)
* [go](#go)
* [__clean_placed_able](#__clean_placed_able)
* [next_turn](#next_turn)
* [search](#search)
* [__place_cell](#__place_cell)
* [__str__](#__str__board) 
---
#### Board-생성자  
Board(size)
보드의 크기를 받고 인스턴스를 반환합니다.
___
#### get_who_win
[who_win](#who_win)을 가져오는 메소드
___
#### get_turn
[turn](#turn)을 가져오는 메소드
___
#### get_is_over
[is_over](#is_over)을 가져오는 메소드
___
#### get_is_pass
[is_pass](#is_pass)을 가져오는 메소드
___
#### get_placed_able_next
[placed_able](#placed_able)을 갸져오는 제너레이
___
#### start_game  
게임을 시작하기 위해보드를 생성하고 초기값들을 설정합니다. 아무런 값을 반환하지 않습니다.
___
#### place_cell  
    * parameter  
        y : y 좌표  
        x : x 좌표
    * returns  
        * 정상 'right'를 반한합나다.  
        * 게임이 끝나면 'over'  
        * 패스면 'pass'
보드 판 위에 돌을 올려 놓습니다. 현재 판에 맞는 돌을 올립니다.
뒤집을 돌을 뒤집습니다.
___
#### reverse  
    * parameters
        y : y좌표  
        x : x좌표  
        delete : 사라질 곳(원래 말의 색의 리스트)  
        add : 더해질 곳 (뒤집여야할 색의 리스트)  

해당 좌표의 말을 뒤집습니다.  
그리고 좌표를 delete에서 삭제하고 add에서 추가함으로써 색이 바뀐 곳의 리스트에 위치 정보를 저장합니다.
___
#### is_in  
    * parameters  
        * position : (y, x) 꼴의 자표값을 가진 튜플  
    * return  
        * 안에 있으면 True 아니면 False  

position을 값을 보고 보드 안에 있는 지 확인합니다.  
___
#### go
    * parameters
        * y : y 좌표
        * x : x 좌표
        * delta : 방향  
    * returns
        * y : y 좌표
        * x : x 좌표
    
y, x로 부터 한칸 [delta](#Direction) 방향으로 움직여 좌표를 반환합니다.
___
#### __clean_placed_able  


놓을 수 있다고 판정된 장소의 리스트(placed_albe)을 정리합니다.
___
#### next_turn  
    * returns  
        * 게임이 끝나면 True를 반환하고 아니면 False  

게임이 끝났는가 누가 이겼는가를 알아내고 게임이 아직도 진행중이면 턴을 전환하고 이번턴에서 놓을 수 있는 곳의 좌표를 계산하여 place_ale 리스트에 저장합니다. 
___
#### search
    * parameter
        * y : y 좌표
        * x : x 좌표
        * delta : 탐색 방향
    * returns
        * y : y 좌표
        * x : x 좌표
        * delta : 탐색 방향한 방향의 반전 값

한돌에서 특정한 방향으로 어떤 위치에 돌을 두면 다른 색 돌을 뒤집을 수 있는 지 계산하는 메소드이다.
진행 방향에 같은 돌이 있거나 보드판 밖이거나 진행 방향에 돌이 하나도 없는 경우는 (-1, -1, [Direction.NONE](#NONE-Direction))을 반환한다.
see also [Direction](#Direction)
#### __place_cell
    * paramter
        * cell : 말 색
        * point : 좌표
        * point_list : 말들 색 위치 정보 저장 리스트
강제로 말을 두는 메소드
#### __str__board
    * return
        문자열로 보드를 시각화합니다.
보드를 시각화 합니다.
___
## cell
___
1. [cell](#cell)
___
### cell
attribute
* [status](#status)
* [direction](#direction)
___
#### status
위치에 말이 있거나 놓을 수 있거나 등의 정보를 담고있다.  
see also [Status](#Status)  
___
#### direction
현재 위치로 어떤 방향으로 가야지 돌을 뒤집을 수 있는 지 알려주는 ***리스트***  
see also [Direction](#Direction)  
___
method
* [생성자](#생성자-cell)
* [__str__](#__str__cell)
* [__eq__](#___eq___cell)
___
#### 생성자-cell
    * parameter : 말색
    * direction : 뒤집을 수 있는 방향
___
#### __str__cell
이것 또한 시각화를 위한 반환
___
#### __eq__cell
== 오버 라이딩
___
## enums
1. [Status](#Status)
2. [Direction](#Direction)
---
### Status
말의 색이나 상황을 나타냄 

    NONE = 0
    WHITE = 1
    BLACK = 2
    PLACED_ABLE = 3
___
#### NONE-Status
말이 없다.
___
#### WHITE
흰말
___
#### BLACK
검은 말
___
#### PLACED_ABLE
말을 둘 수 있는 장소
___
### Direction
___
이 장소에 말을 두면 뒤집을 수 있는 말이 있는 방향을 나타냄

    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8
    NONE = -1
___
#### N
북
___
#### NE
북동
___
#### E
동
___
#### SE
남동
___
#### S
남
___
#### SW
남서
___
#### W
서
___
#### NW
남서
___
#### NONE-Direction
뒤집을 돌이 없은 경우
___
## game
---
이 게임을 만들때 테스트 용도로 만든 것으로 간단히
1. Board 생성
2. place_cell
3. next_turn
4. 2와 3을 반복하며 게임 진행을 하나 game 끝나면 누가 이겼는지 알려주고 끝남