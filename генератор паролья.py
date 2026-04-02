import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("длина паролья: "))
final_password = ""
for i in range(password_length):
    final_password+=random.choice(symbols)
print("Новый пароль: ", final_password)