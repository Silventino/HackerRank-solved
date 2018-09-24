#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())
    
    lowerSum = None
    higherSum = 0
    
    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
        
        # 'i' will iterate through the genes in list 'genes'
        i = first
        sum = 0
        
        while(i <= last):
            # get the size of current gene
            sizeGene = len(genes[i])
            
            # iterate through the 'd' string
            for j in range(len(d) - sizeGene + 1):
                found = True
                k = 0
                while found and k < sizeGene:
                    if(d[j + k] != genes[i][k]):
                        found = False
                    k += 1
                # if found, sum
                if(found):
                    sum += health[i]
            i += 1
        if(sum > higherSum):
            higherSum = sum
        if(lowerSum == None or sum < lowerSum):
            lowerSum = sum
        
    print(lowerSum, higherSum)
