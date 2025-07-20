import random
import re

# تابع بررسی حدس کاربر
def guess_the_number():
    # عدد درست (هدف) فقط یک بار تولید می‌شود
    target = random.randint(1, 100)

    for i in range(1000):
        # گرفتن ورودی از کاربر
        user_input = input("Please enter a number from 1 to 100: ")

        # بررسی اینکه ورودی فقط شامل عدد باشد
        if re.fullmatch(r"\d+", user_input):
            num = int(user_input)

            # بررسی اینکه عدد در محدوده مجاز باشد
            if num == 0 or num > 100:
                print("عدد باید بین 1 تا 100 باشد.")
                continue

            # بررسی نتیجه حدس
            if num == target:
                print("آفرین! عدد درست را حدس زدی ✅")
                break
            elif num > target:
                print("عدد واردشده بزرگ‌تر از عدد درست بود!")
            else:
                print("عدد واردشده کوچک‌تر از عدد درست بود!")
        else:
            print("لطفاً فقط عدد وارد کن ❌")
            continue

guess_the_number()

# تابع بررسی تطابق دو عدد تصادفی توسط رایانه
def random_auto_match():
    # عدد ثابت اولیه
    first_number = random.randint(1, 100)

    # تلاش تا ۵۰۰ بار برای پیدا کردن عدد مساوی
    for i in range(500):
        # تولید عدد تصادفی جدید
        last_number = random.randint(1, 100)

        # بررسی تطابق
        if first_number == last_number:
            print(f"i: {i} | first: {first_number} | last: {last_number} | Status: ✅ OK")
            break
        else:
            print(f"i: {i} | first: {first_number} | last: {last_number} | Status: ❌ NO")

random_auto_match()

