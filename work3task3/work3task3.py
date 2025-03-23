sentence = input("Введіть речення: ")
words = sentence.split()
count = sum(1 for word in words if word.endswith('р') or word.endswith('Р'))

print("Кількість слів, які закінчуються на 'р':", count)