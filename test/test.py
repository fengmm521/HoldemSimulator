#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import hashlib
import random
import RSAtool
import AEStool


def getPKStr():
    basepks = ['A','2','3','4','5','6','7','8','9','t','j','q','k']
    outs = []
    tids = []
    tid = 0
    for k in basepks:
        for i in range(1,5):
            tmp = k + str(i)
            outs.append(tmp)
            tids.append(tid)
            tid += 1
    print outs,tids

def getRandomPK():
    d = range(52)
    outs = []
    while d:
        t = random.randint(0, len(d)-1)
        outs.append(d[t])
        d.remove(d[t])
    return outs

def gethashDat():
    rpks = getRandomPK()
    print(rpks)
    outks = []
    dats = {}
    for k in rpks:
        x = hashlib.sha256(str(k)).hexdigest()
        outks.append(k)
        dats[k] = x
    # x2 = hashlib.sha512(a).digest()
    # cout = 0
    # for d in x2:
    #     print(ord(d))
    #     cout += 1
    # print('--->',cout)
    return outks,dats



def createPK(pkey = '3'):
    ks,dic = gethashDat()
    pks = []
    tmpkey = hashlib.sha512(pkey).digest()
    while len(pks) < 52:
        tmpkey = hashlib.sha512(tmpkey).digest()
        for d in tmpkey:
            tmp = ord(d)
            pk = tmp%52
            if pk not in pks:
                pks.append(pk)
    return pks,dic
    #得到52张扑克的hash

def getUserPk():
    pks,dic = createPK('test')
    aRSA = RSAtool.prpcrypt(mURL='', mkeyPth = '.', gkeyPth = '.',isCreateGkey = True)
    bRSA = RSAtool.prpcrypt(mURL='', mkeyPth = '.', gkeyPth = '.',isCreateGkey = True)
    aAES = AEStool.prpcrypt('keyAkeyAkeyAkeyA')
    bAES = AEStool.prpcrypt('keyBkeyBkeyBkeyB')
    apks = []
    rpks = []
    for p in pks:
        tmp = chr(p+1)*16
        ak = aAES.decryptWithBinascii(tmp)
        apks.append(ak)
        rk = bAES.decryptWithBinascii(ak)
        rpks.append(rk)
    # for p in pks:
    #     tmp = chr(p+1)*16
    #     ak = aRSA.decryptWithGhostPriKey(tmp)
    #     apks.append(ak)
    #     rk = bRSA.decryptWithGhostPriKey(ak)
    #     rpks.append(rk)

    outs = []
    for d in rpks:
        eend = d[-1]
        outs.append(ord(eend))
    print(pks)
    print(outs)
    print(len(outs))
    outs.sort()
    print(outs)



def main():
    getUserPk()

if __name__ == '__main__':
    main()