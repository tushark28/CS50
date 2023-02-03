import math
def main():
    self=0
    num=5
    self = judgeSquareSum(self,num)

def primeFactors(n,root):
        c = 2
        flag = 0
        while(n > 1):
            if(n % c == 0):
                if flag==0:
                    root[n] = 1
                    flag=1
                else:
                    root[n] +=1
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







main()