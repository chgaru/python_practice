import keyboard
import os
import sys
import time

money = 0
weapon = 0
shiled = 0
horse = 0

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def TC_1() :
    time.sleep(0.7)
    clear()

print("GAME START? \n 1. 네  2. 아니오")
main_menu = input()
while True :
    clear()
    if main_menu == "1" : 
        while True:
            print("할 일을 선택하세요. \n 1. 돈 벌기  2. 상점  3. 나가기")
            print("잔액 =",money)
            print("무기 =",weapon)
            print("방패 =",shiled)
            print("말 =",horse)      
            
            menu2_todo = input()
            if menu2_todo == "1" :
                clear()
                print("j를 눌러서 돈을 버세요")
                while True :
                    if keyboard.is_pressed("j"):
                        money += 100
                        clear()
                        print(f"현재 money: {money} \n 나가기 : q")
                        while keyboard.is_pressed("j"):
                            pass
                    elif keyboard.is_pressed("q"):
                        print("돈 벌기를 중단합니다.")
                        TC_1()
                        break
                    else :
                        pass
            
            elif menu2_todo == "2" :
                clear()
                while True :
                    print("1.무기  2. 방패  3. 말  e. 나가기\n")
                    print("잔액 =",money)
                    print("\n무기 =",weapon)
                    print("방패 =",shiled)
                    print("말 =",horse)
                    purchase = input()
                    if purchase == "1" or purchase == "2" or purchase == "3" :
                        while True :
                            if purchase == "1" :
                                clear()
                                if money >= 100 :
                                    money -= 100
                                    weapon += 1
                                    print("무기를 구입했습니다.")
                                    TC_1()
                                    break
                                else :
                                    print("잔액이 부족합니다.")
                                    TC_1()
                                    break
                            elif purchase == "2" :
                                clear()
                                if money >= 50 :
                                    money -= 50
                                    shiled += 1
                                    print("방패를 구입했습니다.")
                                    TC_1()
                                    break
                                else :
                                    print("잔액이 부족합니다.")
                                    TC_1()
                                    break
                            elif purchase == "3" :
                                clear()
                                if money >= 500 :
                                    money -= 500
                                    horse += 1
                                    print("말을 구입했습니다.")
                                    TC_1()
                                    break
                                else :
                                    print("잔액이 부족합니다.")
                                    TC_1()
                                    break
                            elif purchase == "e" :
                                clear()
                                print("상점에서 나갑니다.")
                                TC_1()
                                break
                            else : 
                                print("키가 올바르지 않습니다. 다시 입력하십시오.")
                                TC_1()
                                break
                    elif purchase == "e" :
                        clear()
                        print("상점에서 나갑니다.")
                        TC_1()
                        break

            elif menu2_todo == "3" :
                clear()
                print("게임을 종료하시겠습니까? \n 1. 네  2. 아니오")
                menu2_exit_check = input()
                if menu2_exit_check == "1" :
                    clear()
                    print("1초 후에 게임을 종료합니다.")
                    time.sleep(1)
                    sys.exit()
                elif menu2_exit_check == "2" :
                    clear()
                    main_menu = "1"
                else :
                    clear()
                    print("키가 올바르지 않습니다. 다시 입력하십시오.")
                    TC_1()
                    menu2_todo = 3

    elif main_menu == "2" :
        while True : 
            clear()
            print("게임을 종료하시겠습니까? \n 1. 네  2. 아니오")
            main_exit_check = int(input())
            
            if main_exit_check == 1 :
                clear()
                ("게임이 종료되었습니다.")
                TC_1()
                sys.exit()
            elif main_exit_check == "2" :
                main_menu = "1"
                clear()
                break
            else :
                print("키가 올바르지 않습니다. 다시 입력해주십시오.")
                TC_1()
                main_menu = "2"