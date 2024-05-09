from righttriangle import RightTriangle as rt
from rectangle import Rectangle as rc
from pyramid import Pyramid as py
from diamond import Diamond as di
from x import X
from ribbon import Ribbon as rib
from sandwatch import Sandwatch as san

while True:
    try: # 잘못 입력할 경우
        print("\n\t\t * 그리기 마당 *")
        print("1. 직각 삼각형    2. 피라미드    3. 사각형    4. 다이아몬드    5. 엑스    6. 리본    7. 모래시계    0. 종료") # 그릴 도형 메뉴
        choice = int(input("메뉴 선택 : ")) # 메뉴 선택

        if choice == 0: # 종료 선택시
            break       # 반복문 탈출

        height = int(input("도형의 높이 : ")) # 도형의 높이 입력
        ch = input("출력 문자 : ")           # 출력할 문자 입력

        fi = None
        if choice == 1:
            fi = rt(height, ch) # 직각 삼각형 출력
        elif choice == 2:
            fi = py(height, ch) # 피라미드 출력
        elif choice == 3:
            fi = rc(height, ch) # 사각형 출력
        elif choice == 4:
            fi = di(height, ch) # 다이아몬드 출력
        elif choice == 5:
            fi = X(height, ch) # X 출력
        elif choice == 6:
            fi = rib(height, ch) # 리본 출력
        elif choice == 7:
            fi = san(height, ch) # 모래 시계 출력

        fi.draw() # polymorphism 구현
    except ValueError as e:
        print('[ERROR] 잘못 입력 하셨습니다.') # 오류 출력
