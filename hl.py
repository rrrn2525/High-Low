import random

# A〜K を数値に変換する辞書 A<K
card_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

cards = list(card_values.keys())

print("--- High & Low ---")
input("ゲーム開始 - Enterでスタート")

while True:
    # CPUカード生成
    cpu_card = random.choice(cards)
    print(f"\n相手のカード：{cpu_card}")

    # プレイヤーカード生成
    player_card = random.choice(cards)

    # High / Low 選択
    choice = input("あなたのカードがHigh(h) か Low(l) を選んでください：")

    cpu_value = card_values[cpu_card]
    player_value = card_values[player_card]

    print(f"あなたのカード：{player_card}")
    # 勝敗判定
    if player_value == cpu_value:
        print("引き分け")
        continue  # 3 に戻る（やり直し）

    if choice == "h":
        if player_value > cpu_value:
            print("あなたの勝ち！")
        else:
            print("あなたの負け…")
    elif choice == "l":
        if player_value < cpu_value:
            print("あなたの勝ち！")
        else:
            print("あなたの負け…")
    else:
        print("正しい入力ではありません")

    break  # ゲーム終了
