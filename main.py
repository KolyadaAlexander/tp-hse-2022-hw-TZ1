while True:
    try:
        file = input("Введите имя файла: ")
        f=open(file, encoding="utf-8")
        break
    except: print("Файл с введённым именем не найден")
deystv=5
m=f.readlines()
x=len(m)
info=[]
for i in range(x-1):
    y=m[i].split(",")
    y[1]=y[1][1:]
    y[2] = y[2][1:-1]
    info.append(y)
y=m[-1].split(",")
y[1]=y[1][1:]
y[2] = y[2][1:]
info.append(y)
while deystv!="0":
    print("Что вы хотите выполнить?")
    print("1-выполнить поиск по ФИО")
    print("2-выполнить поиск по номеру телефона")
    print("3-выполнить поиск по email")
    print("4-редактировать документ")
    print("0-завершить программу")
    deystv=input("Выберите номер действия: ")
    if deystv=="0":
        break
    if deystv=="1":
        p_name=input("Введите ФИО кантакта: ")
        p_name = p_name.split()
        flag_name=False
        for i in range(len(info)):
            n=0
            for j in range(len(p_name)):
                if p_name[j] not in info[i][0]:
                    continue
                else:
                    n=n+1
            if n==len(p_name):
                flag_name=True
                print("-" * 50)
                print("ID: " + str(i + 1))
                print("\033[31m{}\033[0m".format("ФИО: ") + info[i][0])
                print("Номер телефона: " + info[i][1])
                print("Почта: " + info[i][2])
        if flag_name==False:
            print("\033[31m{}\033[0m".format("Контакта с данным ФИО нет в списке"))
        print("-" * 50)
    if deystv=="2":
        p_num=input("Введите номер телефона: ")
        flag_num=False
        for i in range(len(info)):
            if p_num in info[i][1]:
                flag_num=True
                print("-"*50)
                print("ID: "+str(i+1))
                print("ФИО: "+info[i][0])
                print("\033[31m{}\033[0m".format("Номер телефона: ")+info[i][1])
                print("Почта: " + info[i][2])
        if flag_num==False:
            print("\033[31m{}\033[0m".format("Контакта с данным номером телефона нет в списке"))
        print("-" * 50)
    if deystv == "3":
        p_email=input("Введите почту: ")
        flag_email=False
        for i in range(len(info)):
            if p_email in info[i][2]:
                flag_email=True
                print("-" * 50)
                print("ID: " + str(i + 1))
                print("ФИО: " + info[i][0])
                print("Номер телефона: " + info[i][1])
                print("\033[31m{}\033[0m".format("Почта: ") + info[i][2])
        if flag_email==False:
            print("\033[31m{}\033[0m".format("Контакта с данной почтой нет в списке"))
        print("-"*50)
    if deystv == "4":
        p_redact=input("Введите ID контакта, которого желатете отредактировать: ")
        redact=input("Введите новые данные пользователя(ФИО, номер телефона, email): ")
        g = redact.split(",")
        g[1] =g[1][1:]
        g[2] = g[2][1:-1]
        info[int(p_redact) - 1]=g













