# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    a = s.split('!')
    return ''.join(a)

s = "Hi! Hello!"
print('A)', remove_exclamation_marks(s))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == '!':
        a = list(s)
        del a[-1]
    return ''.join(a)

s = "Hi! Hello!"
print('B)',remove_last_em(s))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    a = s.split(' ')
    d = []
    for i in range(len(a)):
        count = 0
        for k in a[i]:
            if k == '!':
                count += 1
        if count > 1:
            d.append(a[i])
    return d

s = "Hi! !Hello!"
print('C)',*remove_word_with_one_em(s))
