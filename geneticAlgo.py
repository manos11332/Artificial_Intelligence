import random
#Αρχικοποίηση μεταβλητών και λιστών
member1=[0,1,2,3,4,5,6,7]
member2=[0,0,0,0,0,0,0,0]
member3=[0,0,0,0,0,0,0,0]
member4=[0,0,0,0,0,0,0,0]
res=0
res1=0
res2=0
res3=0
choisemembercounter1=0
choisemembercounter2=0
choisemembercounter3=0
choisemembercounter4=0
population=[[0,0,0,1,0],[0,0,0,0,1],[0,0,0,1,1],[0,0,1,1,1],[0,1,1,1,1],[1,1,1,1,1],[0,1,0,0,0],[0,1,1,0,0],[0,1,1,1,0],[0,1,0,1,0,0]] #λίστα με τον συνολικο πλυθισμο
print(population)
#Συνάρτηση για επιλογή
def choisedMember(var):
    global choisemembercounter1
    global choisemembercounter2
    global choisemembercounter3
    global choisemembercounter4

    if (var<= (res*res)):
        choisemembercounter1 = choisemembercounter1 + 1
        return  1
    elif ((var > (res*res)) and (var < ((res*res)+(res1*res1)))):
        choisemembercounter2= choisemembercounter2 +1
        return 2
    elif ((var > ((res*res)+(res1*res1))) and (var < ((res*res)+(res1*res1)+(res2*res2)))):
        choisemembercounter3 = choisemembercounter3 + 1
        return  3
    elif  ((var> ((res*res)+(res1*res1)+(res2*res2))) and (var < ((res*res)+(res1*res1)+(res2*res2)+(res3*res3)) )):
        choisemembercounter4 = choisemembercounter4 + 1
        return  4
    else:
        return 0
for x in range(5):
    randch=random.sample(population,k=4)                                                          #επιλογη τεσαρων μελών
    print("random 4 items from list population are: ",str(randch)," atempt: ",x+1 )
    # metatropi diaikou se dekadikou
    res = int("".join(str(y) for y in randch[0]), 2)
    res1 = int("".join(str(y) for y in randch[1]), 2)
    res2 = int("".join(str(y) for y in randch[2]), 2)
    res3 = int("".join(str(y) for y in randch[3]), 2)
    #print diadiko
    print("demical of ", randch[0]," is  : ",str(res))
    print("demical of ", randch[1]," is  : ",str(res1))
    print("demical of ", randch[2]," is  : ",str(res2))
    print("demical of ", randch[3]," is  : ",str(res3))
    #Δημιουργία τυχαίων αριθμών
    m1=random.randrange(((res*res)+(res1*res1)+(res2*res2)+(res3*res3)))
    m2=random.randrange(((res*res)+(res1*res1)+(res2*res2)+(res3*res3)))
    m3=random.randrange(((res*res)+(res1*res1)+(res2*res2)+(res3*res3)))
    m4=random.randrange(((res*res)+(res1*res1)+(res2*res2)+(res3*res3)))
    #Δημιοργία αναμενόμενου αριθμού απογόνων
    anm1=(199*m1)/169
    anm2=(199*m2)/169
    anm3=(199*m3)/169
    anm4=(199*m4)/169

    # Δημιουργία των 4 πινάκων για καθε μέλος
    member0=["member in demical"," οι τιμές προσαρμογής/απόδοσης","το προοδευτικό άθροισμα των αποδόσεων","η πιθανότητα επιλογής ","ο ποσοστό (%) του συνόλου ", "οι 4 τυχαίοι αριθμοί n", "η επιλεγμένη δομή (το επιλεγμένος μέλος)" ," ο πραγματικός αριθμός των απογόνων."]
    member1=[res  ,res*res ,res*res,round((res*res)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3)), 2),round((((res*res)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m1 , choisedMember(m1), 0]
    member2=[res1 ,res1*res1,(res*res)+(res1*res1),round(((res1*res1)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),round((((res1*res1)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m2,choisedMember(m2),0]
    member3=[res2 ,res2*res2,(res*res)+(res1*res1)+(res2*res2),round(((res2*res2)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),round((((res2*res2)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m3,choisedMember(m3),0]
    member4=[res3 ,res3*res3 ,(res*res)+(res1*res1)+(res2*res2)+(res3*res3),round(((res3*res3)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),round((((res3*res3)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m4,choisedMember(m4),0]
    print("choisemembercounter1",choisemembercounter1)
    print("choisemembercounter2", choisemembercounter2)
    print("choisemembercounter3", choisemembercounter3)
    print("choisemembercounter4", choisemembercounter4)
    member0=["member in demical"," οι τιμές προσαρμογής/απόδοσης","το προοδευτικό άθροισμα των αποδόσεων","η πιθανότητα επιλογής ","ο ποσοστό (%) του συνόλου ", "οι 4 τυχαίοι αριθμοί n", "η επιλεγμένη δομή (το επιλεγμένος μέλος)" ," ο πραγματικός αριθμός των απογόνων."]
    member1=[res  ,res*res ,res*res,round((res*res)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3)), 2),round((((res*res)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m1 , member1[6], choisemembercounter1]
    member2=[res1 ,res1*res1,(res*res)+(res1*res1),round(((res1*res1)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),round((((res1*res1)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m2,member2[6],choisemembercounter2]
    member3=[res2 ,res2*res2,(res*res)+(res1*res1)+(res2*res2),round(((res2*res2)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),round((((res2*res2)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m3,member3[6],choisemembercounter3]
    member4=[res3 ,res3*res3 ,(res*res)+(res1*res1)+(res2*res2)+(res3*res3),round(((res3*res3)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),round((((res3*res3)*100)/((res*res)+(res1*res1)+(res2*res2)+(res3*res3))), 2),m4,member4[6],choisemembercounter4]
    choisemembercounter1 = 0
    choisemembercounter2 = 0
    choisemembercounter3 = 0
    choisemembercounter4 = 0
    #prostheto oles tis times prosrmogon
    #f(x)/sum
    print(*member0, sep =' | ')
    print(*member1, sep ='                                ')
    print(*member2, sep ='                                ')
    print(*member3, sep ='                                ')
    print(*member4, sep ='                                ')


    #member1[5]= random number
    #member1[2]= times prosarmogis
    #member1[6]= epilegmeni domi










