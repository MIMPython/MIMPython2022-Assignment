if __name__ == '__main__':
    input_choice = input("Cả hai người chơi cùng nhập: ")
    #Example input: bua bua
    possible_actions = ["bua", "bao", "keo"]
    user_action = input_choice.split(" ")
    user_action_1 = user_action[0]
    user_action_2 = user_action[1]
    print(f"\nuser_1 chọn {user_action_1}, user_2 chọn {user_action_2}.\n")

    if user_action_1 == user_action_2:
        print(f"Cả hai cùng chọn  {user_action_1}. Hòa rồi nhé!")
    elif user_action_1 == "bua":
        if user_action_2 == "keo":
            print("Búa đập kéo, user_1 thắng!")
        else:
            print("Bao đùm búa! user_1 thua.")
    elif user_action_1 == "bao":
        if user_action_2 == "bua":
            print("Bao đùm búa! user_1 thắng!")
        else:
            print("Kéo cắt bao! user_1 thua.")
    elif user_action_1 == "keo":
        if user_action_2 == "bao":
            print("Kéo cắt bao! user_1 thắng!")
        else:
            print("Đấm đập kéo, user_1 lose.")

#c) Mình đã thiết kế game theo luật công bằng như sau là user_1 và user_2 đồng thời cùng nhập trong 1 lần nhập duy nhất và cả hai sẽ
#không biết nhau nhập gì từ đó trò chơi sẽ trở lên công bằng hơn là nhập 2 lần.