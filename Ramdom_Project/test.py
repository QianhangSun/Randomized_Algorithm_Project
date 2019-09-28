#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:33:23 2018

@author: sunqianhang
"""
import StringMatcher as RK
import KMP_string_matching as KMP
import time
def naiveMatch(T,P):
    result = []; m = len(T); n = len(P)
    for i in range(m-n+1):
        if T[i:i+n] == P:
            result.append(i)
    if result:
        print("Substring1 Found at Position -->",result)
    #else:
        #print("Substring1 Not Found :: Search Failed")


if __name__ == '__main__':
    with open("test/string3.txt","r")as stringFile:
        string = stringFile.read().replace('\n',' ')
    with open("test/substring3.txt","r")as substringFile:
        substring = substringFile.read().replace('\n',' ')
    start3 = time.time()    
    for i in range(1,int(len(string)/100000)):
        
        j=100000*(i-1)
        stri=string[j:j+100000]
        k=10*(i-1)
        substr=substring[k:k+10]
        #print("test ",i)
        #print(substr)
        naiveMatch(stri, substr)
    end3 = time.time()
    print("###################################")
    print("Time elapsed ", end3-start3) 
    print("###################################")
    start1 = time.time()    
    for i in range(1,int(len(string)/100000)):
        j=100000*(i-1)
        stri=string[j:j+100000]
        k=10*(i-1)
        substr=substring[k:k+10]
        #print("test ",i)
        #print(substr)
        kmp = RK.KarpRabin(substr, stri)
    end1 = time.time()
    print("###################################")
    print("Time elapsed ", end1-start1)
    print("###################################")
    start2 = time.time()    
    for i in range(1,int(len(string)/100000)):
        j=100000*(i-1)
        stri=string[j:j+100000]
        k=10*(i-1)
        substr=substring[k:k+10]
        #print("test ",i)
        #print(substr)
        kmp = KMP.KMP().search(stri, substr)
    end2 = time.time()
    print("###################################")
    print("Time elapsed ", end2-start2)
    print("###################################")