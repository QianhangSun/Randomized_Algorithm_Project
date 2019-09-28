#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 15:39:10 2018

@author: sunqianhang
"""

from __future__ import print_function
import sys
import time

class RabinKarp(object):
    """ RABIN KARP STRING MATCHING """

    def __init__(self, string, substring):
        self.string = string
        self.substring = substring
        if string is None and substring is None:
            self.get_input()
        self.search()

    def hash(self, text):
        """ CREATING SIMPLE HASH FOR STRING SEGMENT """
        hashval = 0
        for i in range(0, len(text)):
            hashval += ord(text[i])**i
        return hashval

    def comparison(self):
        """ COMPARES HASHES AND IF MATCHES COMPARES STRINGS"""
        for i in range(len(self.string)-len(self.substring)+1):
            if self.hash(self.string[i:i+len(self.substring)]) == self.hash(self.substring):
                #if self.string[i:i+len(self.substring)] == self.substring:
                return i
        return -1

    def get_input(self):
        """ GETTING INPUT FROM USER """
        print(" String --> ", end='')
        self.string = str(input())
        print(" Substring --> ", end='')
        self.substring = str(input())
        return self.string, self.substring


    def search(self):
        """ SEARCHING STRING FOR SUBSTRING """
        if self.substring in [None, ""]:
            print("Invalid Value For Substring")
        elif self.string in [None, ""]:
            print("Invalid Value For String")
        elif len(self.substring) > len(self.string):
            print("Length of Substring Less Than String")
        else:
            posn = self.comparison()
            if posn == -1:
                print(" Substring Not Found :: Search Failed")
            else:
                print(" Substring Found at Position --> ", posn+1)

def main():
    """ Arguments as input to search """
    try:
        string = sys.argv[1]
        substring = sys.argv[2]

    except IndexError:
        string = None
        substring = None

    try:
        sys.argv[3]

    except IndexError:
        pass

    else:
        print(" More than expected Number of Arguments")
        string = None
        substring = None

    RabinKarp(string, substring)
if __name__ == '__main__':
    with open("test/string2.txt","r")as stringFile:
        string = stringFile.read().replace('\n',' ')
    with open("test/substring2.txt","r")as substringFile:
        substring = substringFile.read().replace('\n',' ')
    start3 = time.time()    
    for i in range(1,int(len(string)/10000)):
        j=10000*(i-1)
        stri=string[j:j+10000]
        k=10*(i-1)
        substr=substring[k:k+10]
        #print("test ",i)
        #print(substr)
        RabinKarp(stri,substr)
    end3 = time.time()
    print("###################################")
    print("Time elapsed ", end3-start3) 
    print("###################################")