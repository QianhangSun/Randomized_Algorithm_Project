import RollingHash
import time
RollingHash = RollingHash.RollingHash

def KarpRabin(s,t):

	#hashing s
    rs = RollingHash(256,2147483647)
    for c in s: rs.append(c)
    rt = RollingHash(256,2147483647)
	#hashing the string consisting of the first |s| chars
    for c in t[:len(s)]: rt.append(c)
    if(rs.hash() == rt.hash()): 
        return 0

	#sliding
    result=[]
    for i in range(len(s),len(t)):
        rt.skip()
        rt.append(t[i])
        if(rs.hash() == rt.hash()): 
            result.append(i-len(s)+1)
    if result:
        print("Substring2 Found at Position -->",result)
    #else:
	#if we're here, s is not in t
        #print("Substring2 Not Found :: Search Failed")

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
        naiveMatch(stri, substr)
    end3 = time.time()
    print("###################################")
    print("Time elapsed ", end3-start3) 
    print("###################################")
#assert(KarpRabin("the","the thing we're looking for is here") == 0)
#assert(KarpRabin("567","01234567") == 5)
#assert(KarpRabin("bcd","abcde") == 1)

#error case
#KarpRabin("not found","")