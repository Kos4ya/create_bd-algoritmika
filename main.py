from random import*
f = open("BD/bd1.txt", "w")
f.write("паггозвопщупкпщзткщпркпрурпгщкрпщгтпцпгцрпцрщпрыащцрпшгпрщрщПЩЫШЦКПЩоащгрпкпшгрпгрпщрпщпгщрпщыпигкиц")
f.close()
for i in range(20):
    f = open("BD/"f"{i}.txt", "w")
    f.write(str(randint(1, 1000)))
    f.close()