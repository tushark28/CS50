import math
def main():
    self=False
    num=20
    self = judgeSquareSum(self,num)

def primeFactors(n,root):
    c = 2
    flag = 0
    while(n > 1):
        if(n % c == 0):
            if flag==0:
                root[c] = 1
                flag=1
            else:
                root[c] +=1
            n = n / c
        else:
            c = c + 1
            flag=0
    return root

def judgeSquareSum(self, c: int) -> bool:
    if math.sqrt(c).is_integer() or math.sqrt(c/2).is_integer():
        return True
    root = {}
    root = primeFactors(c,root)
    print(root)
    print(len(root))
    flag = 0
    for i in root:
        if root[i]%2 != 0:
            if i%4 !=3:
                flag+=1
            else:
                return False
        if flag==len(root):
            return True







main()