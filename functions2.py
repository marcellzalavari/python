from data import Épület

epuletek:list[Épület] = []

def beolvas(faljnev):
    f = open(faljnev,'r',encoding='utf-8')
    f.readline()
    for sor in f:
        epuletek.append(Épület(sor.strip()))
    f.close

def epuletek_szama()->int:
    return len(epuletek)