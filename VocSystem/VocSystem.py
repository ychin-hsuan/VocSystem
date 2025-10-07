import random

# 在這裡直接修改你的單字
VOCAB = {
    "紅色": "あか",
    "烏賊／魷魚": "いか",
    "馬": "うま",
    "家": "いえ",
    "狼": "おおかみ",
    "螃蟹": "かに",
    "樹": "き",
    "熊": "くま",
    "時鐘": "とけい",
    "苔蘚": "こけ",
    "魚": "さかな",
    "鹿": "しか",
    "壽司": "すし",
    "蟬": "せみ",
    "天空": "そら",
    "章魚": "たこ",
    "地圖": "ちず",
    "梅雨／露水": "つゆ",
    "手": "て",
    "老虎": "とら",
    "茄子": "なす",
    "肉": "にく",
    "狗": "いぬ",
    "貓": "ねこ",
    "海苔": "のり",
    "花": "はな",
    "公主": "ひめ",
    "河豚": "ふぐ",
    "蛇": "へび",
    "星星": "ほし",
    "豆子": "まめ",
    "橘子": "みかん",
    "昆蟲": "むし",
    "飯／餐": "めし",
    "桃子": "もも",
    "山": "やま",
    "雪": "ゆき",
    "夜晚": "よる",
    "鮭魚卵": "いくら",
    "蘋果": "りんご",
    "淚／眼淚": "るい",
    "蓮花": "れん",
    "蘿蔔泥": "ろし",
    "海帶芽": "わかめ",
    "吃飯": "ごはんをたべます",
    "新幹線": "しんかんせん",
    "淺草（地名）": "あさくさ",
    "櫻花": "さくら",
    "北海道": "ほっかいどう",
    "沖繩": "おきなわ"
}


def quiz(vocab):
    """開始測驗"""
    if not vocab:
        print("沒有單字可以測驗！")
        return
    
    print("========== 單字測驗開始 ==========")
    print("提示：輸入 0 結束測驗，輸入 1 顯示答案\n")
    
    correct_count = 0
    total_count = 0
    
    while True:
        # 隨機選一個單字
        chinese = random.choice(list(vocab.keys()))
        correct_answer = vocab[chinese]
        
        print(f"\n請寫出「{chinese}」的外語：")
        
        # 讓使用者一直答到對為止
        while True:
            user_answer = input("你的答案: ").strip()
            
            # 檢查是否要結束
            # 使用全形數字輸入'０'＆ '１'（不用切換輸入法:)）
            if user_answer == '０':
                print(f"\n========== 測驗結束 ==========")
                print(f"總共答對：{correct_count}/{total_count} 題")
                if total_count > 0:
                    accuracy = (correct_count / total_count) * 100
                    print(f"正確率：{accuracy:.1f}%")
                return
            
            # 檢查是否要提示
            if user_answer == '１':
                print(f"💡 提示：答案是 {correct_answer}")
                continue
            
            # 檢查答案（不區分大小寫）
            if user_answer.lower() == correct_answer.lower():
                print("✓ 答對了！\n")
                correct_count += 1
                total_count += 1
                break
            else:
                print(f"✗ 答錯了，請再試一次！")

if __name__ == "__main__":
    quiz(VOCAB)

# def quiz(vocab):
#     """開始測驗"""
#     if not vocab:
#         print("沒有單字可以測驗！")
#         return
    
#     print("\n========== 單字測驗開始 ==========")
#     print("提示：輸入 0 可以結束測驗\n")
    
#     correct_count = 0
#     total_count = 0
    
#     while True:
#         # 隨機選一個單字
#         chinese = random.choice(list(vocab.keys()))
#         correct_answer = vocab[chinese]
        
#         print(f"\n請寫出「{chinese}」的日語：")
        
#         # 讓使用者一直答到對為止
#         while True:
#             user_answer = input("你的答案: ").strip()
            
#             # 檢查是否要結束
#             if user_answer == '0':
#                 print(f"\n========== 測驗結束 ==========")
#                 print(f"總共答對：{correct_count}/{total_count} 題")
#                 if total_count > 0:
#                     accuracy = (correct_count / total_count) * 100
#                     print(f"正確率：{accuracy:.1f}%")
#                 return
            
#             # 檢查答案（不區分大小寫）
#             if user_answer.lower() == correct_answer.lower():
#                 print("✓ 答對了！\n")
#                 correct_count += 1
#                 total_count += 1
#                 break
#             else:
#                 print(f"✗ 答錯了，請再試一次！")

# if __name__ == "__main__":
#     quiz(VOCAB)