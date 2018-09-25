

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, letter = "@"):
        self.value = 0
        self.sons = {}
        self.letter = letter
    def print(self):
        print("Eu ",self.letter)
        print("Filhos:")
        for f in self.sons:
            print(self.sons[f].letter, end=" ")
        print('')
        for f in self.sons:
            self.sons[f].print()


if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))
    
    rootNode = Node()
    for gene in genes:
        currentNode = rootNode
        for letter in gene:
            if(letter in currentNode.sons):
                currentNode = currentNode.sons[letter]
            else:
                newNode = Node(letter)
                currentNode.sons[letter] = newNode
                currentNode = newNode
    rootNode.print()


# 6
# a b c aa d b
# 1 2 3 4 5 6

    # s = int(input())
    
    # lowerSum = None
    # higherSum = 0
    
    # for s_itr in range(s):
    #     firstLastd = input().split()

    #     first = int(firstLastd[0])

    #     last = int(firstLastd[1])

    #     d = firstLastd[2]
        
    #     # print(first, last, d)
    #     dic = {}
    #     i = first 
        
    #     dic[genes[i]] = health[i]
    #     i += 1
    #     smallestGene = len(genes[i])
    #     # biggerGene = len(genes[i])
    #     geneSizes = []
    #     geneSizes.append(len(genes[i]))
    #     while i <= last:
    #         if(genes[i] in dic):
    #             dic[genes[i]] += health[i]
    #         else:
    #             dic[genes[i]] = health[i]
    #         if len(genes[i]) not in geneSizes:
    #             geneSizes.append(len(genes[i]))
    #         # if(len(genes[i]) > biggerGene):
    #         #     biggerGene = len(genes[i]) 
    #         # if(len(genes[i]) < smallestGene):
    #         #     smallestGene = len(genes[i])
    #         i += 1

    #     sum = 0
    #     # 'i' will iterate through the genes in list 'genes'
    #     i = 0
    #     limite = len(d) - smallestGene + 1
    #     while(i < limite):
    #         # j = smallestGene
    #         # print('s', smallestGene, 'b', biggerGene)
    #         for j in geneSizes:
    #             if(i+j <= len(d)):
    #                 if(d[i:i+j] in dic):
    #                     sum += dic[d[i:i+j]]
    #                 j += 1
    #         i += 1
            
    #     if(sum > higherSum):
    #         higherSum = sum
    #     if(lowerSum == None or sum < lowerSum):
    #         lowerSum = sum
        
    # print(lowerSum, higherSum)
