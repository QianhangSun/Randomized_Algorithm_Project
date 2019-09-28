#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:41:00 2018

@author: sunqianhang
"""
import time
class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in S
        """
    
        partial, ret, j = self.partial(P), [], 0
    
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = 0  
        if ret:
            print("Substring3 Found at Position -->",ret)
        #else:
            #print("Substring3 Not Found :: Search Failed")
        
            #return ret
    
if __name__ == '__main__':
    with open("test/string.txt","r")as stringFile:
        string = stringFile.read().replace('\n',' ')
    with open("test/substring.txt","r")as substringFile:
        substring = substringFile.read().replace('\n',' ')
    kmp = KMP()
    start = time.time()
    kmp.search(string,substring)
    end = time.time()
    print("Time elapsed ", end-start)
    