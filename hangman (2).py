import random
import time
from time import sleep

jeux="PENDU"
de="##Luis SANCHEZ##"
date="15.04.2020"
simge="-"*50
bos=""*5
bilgi="""            You will earn 50 points if you know a character
            and you will lose 25 points if your answer is wrong.
            If you give 5 wrong answers you will lose."""
print("{:^80}\n{:^80}\n{:^80}\n{:^80}\n{}".format(jeux,de,date,simge,bos))
print(bilgi)
print("{:^80}\n{:^80}\n{:^80}".format(bos,simge,bos))

kelimeler = ["POLDER,","POLENTA","POLENTE,","POLERGAL","POLI","POLIANITE",
             "POLIARQUE","POLICE","POLICEMAN","POLICEMENT","POLICER","POLICER",
             "POLICHINELLE","POLICIEN,","POLICIER","POLICLINIQUE","PNEUM","RTHROSE",
             "PNEUMATE","PNEUMATIQUE","PNEUMATISTE","PNEUMATOCHIMIE","PNEUMATOCHIMIQUE",
             "PNEUMATOLOGIE","PNEUMATOLOGIQUE","PNEUMATOLOGISTE",",PNEUMATOLOGUE","PNEUMATOMPHALE",
             "MANABLE","MANAKIN","MANANT","MANCANDO","MANCENILLE",
             "MANCENILLIER","MANCHE","MANCHERON","MANCHETTE","MANCHON",
             "MANCHONNIER","MANCHOT","MANCIPATION","MALCHANCEUX","MALCHUS",
             "MALCOMPLAISANT","MALCONTENT","MALDER","MALDISANT","MALDONNE","MALDOUX","MALEBOUCHE","MALEBRANCHISME","MALEBRANCHISTE"]
secim = random.choice(kelimeler)
tablov=[]
tablov.append("-"*len(secim))
tablo=[]
for i in tablov:
    for h in i:
        tablo.append(h)
print("Our word has {} letters.".format(len(secim)),' '.join(tablo))
print(""*7)
c="""  _________
  |
  |"""
c1="\n  O"
c2="\n \|/"
c3="\n  |"      
c4="\n / \ "
cson=""
depo=""
depo1=""
a=len(depo)
can=5
puan=0
olmazlar="+/ 1234567890*-_?.,"
while True:
    if len(depo)==len(secim): 
        print("Vous avez gagné! Mot: {} Your score: {}".format(secim,puan))
        print("Please press 'Enter' for quit..")
        break
    if can==0:
        print("\nYou lose...")
        sleep(0.9)
        print ("Your score: {}".format(puan))
        sleep(0.9)
        print ("The word that you couldnt answer: {}".format(secim))
        sleep(0.9)
        print("Please press 'Enter' for quit..")
        break

    x=input("\nPlease enter a letter: ")
    if 1<len(x):
        print ("\nYou can enter only 1 letter..")
        continue
    if x in olmazlar:
        print("\nIt's not even a letter!")
        continue
    if x in depo:
        print("You used this letter before!")
        continue
    if x in depo1:
        print("You used this letter before!")
        continue
    if x in secim and not x in depo:
        puan+=50*secim.count(x)
        print("Letter {} is counted {} times.".format(x,secim.count(x)))
        sleep(0.7)
        for sayi, oge in enumerate(secim):
            if 2 <=secim.count(oge) and x==oge:
                depo+=x
                a+=secim.count(oge)
                if tablo[sayi]=="-": 
                    tablo[sayi]=x
                print("In line {} .".format(sayi+1))
                sleep(0.7)
            if secim.count(oge)==1 and x==oge:
                depo+=x
                a+=secim.count(oge)
                if tablo[sayi]=="-":
                    tablo[sayi]=x
                print("In line {} .".format(sayi+1))
                sleep(0.7)
        print("\nWord:",' '.join(tablo))
        sleep(0.7)

    else:
        depo1+=x
        can-=1
        puan-=25
        print("\nThis letter {} not in our word! {} healt left.".format(x,can))
        sleep(0.7)
        print("\nWord:",' '.join(tablo))
        sleep(0.7)
        if can==4:
            cson+=str(c)
            print(cson)
        if can==3:
            cson+=str(c1)       
            print(cson)      
        if can==2:          
            cson+=str(c2)
            print(cson)
        if can==1:
            cson+=str(c3)
            print(cson)
        if can==0:
            cson+=str(c4)
            print(cson)


try:
    input()
except SyntaxError:
    pass
