# Используя один из алгоритмов симметричного шифрования, зашифровать свои данные: фамилию, имя, отчество.
# Выполнить проверку, расшифровав полученное сообщение.
# Написать программу
# Алгоритм шифровани: простая перестановка

text = list(str(input()))

def Crypto(text):
    new_text = ''
    i = 0 
    while (len(text) > len(new_text)):
        if text[i] != ' ' and text[i + 1] != ' ':
            new_text += text[i + 1]
            new_text += text[i]
            i += 2 
        else:
            new_text += text[i]
            i += 1

        if (i == len(text) - 1):
            new_text+= text[i] 
            break
    return  (new_text)
print(Crypto(text))
print(Crypto(list(Crypto(text))))