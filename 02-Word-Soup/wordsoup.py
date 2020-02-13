# Jonathon Bell, 6/15/2019

def Create_List(fp):
    myList = []
    for words in fp:
        myList.append(words.strip('\n'))

    return myList

# creates a dictionary based on alphabetical order; O(nlogn) time complexity
def Create_Dict(myList):
    #myList.sort()
    myDict = {}
    
    for i in range(0, 26):
        myDict[chr(i + 97)] = []

    for strs in myList:
        if myDict[strs[0]] == []:
            myDict[strs[0]].append(strs)
        else:
            for i in range(0, len(myDict[strs[0]])):
                if strs < myDict[strs[0]][i]:
                    myDict[strs[0]].insert(i, strs)
                    break
                elif strs == myDict[strs[0]][i]:
                    break
                elif i == (len(myDict[strs[0]]) - 1):
                    myDict[strs[0]].append(strs)

    return myDict

def Fancy_Print(myDict):
    for keys in myDict:
        if myDict[keys] == []:
            continue
        else:
            print("'%c' : " % keys, end = '')
            print (myDict[keys])

# testing suite, this should not be part of any student submission code
#fp = open("TestCases/testcase7.txt", 'r')
#myFullList = Create_List(fp)
#myBigDict = Create_Dict(myFullList)
#Fancy_Print(myBigDict)
