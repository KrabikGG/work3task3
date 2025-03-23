sentence = input("Введіть речення: ")

words = sentence.split()
count = sum(1 for word in words if word.lower().startswith('н'))

print("Кількість слів, які починаються на 'н':", count)
