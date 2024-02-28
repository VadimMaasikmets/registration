import sys
import random
def lopp():
    """Заканчиваем работу приложения
    """
    sys.exit()
    return
def create_login_parool(login, parool):
        a=input("Введите логин: ")
        if a in login:
            print("Такой логин уже существует. Заново.")
        else:
            login.append(a)
            print("Логин создан.", a)           
            str0=".,:;!_*-+()/#¤%&"
            str1 = '0123456789'
            str2 = 'qwertyuiopasdfghjklzxcvbnm'
            str3 = str2.upper()
            #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
            str4 = str0+str1+str2+str3
            #print(str4)
            ls = list(str4)
            #print(ls)
            random.shuffle(ls)
            #print(ls)
            # Извлекаем из списка 12 произвольных значений
            psword = ''.join([random.choice(ls) for x in range(12)])
            # Пароль готов
            print("Ваш пароль. ", psword)
            parool.append(psword)
