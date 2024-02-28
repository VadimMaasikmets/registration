from module1 import*
login=[]
parool=[]
while True:
    print("0-Registreerimine\n1-Autoriseerimine\n2-nime või parooli muutmine\n3-unustanud parooli taastamine\n4-lõpetamine\n")
    vastus=int(input())
    if vastus==0:
        new_login_parool=create_login_parool(login, parool)
    #elif vastus==1:
    #elif vastus==2:
    #elif vastus==3:
    elif vastus==4:
        print("lõpetamine...")
        lopp()
