'''
Given a number N. Count the number of digits in N which evenly divide N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 

Example 1:

Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly
'''
class Aravind:
    def divideEvenli(self,n):
        num=[int(m) for m in str(n) if m != '0']
        i=0
        for x in num:
            if n%x==0:
                i+=1
        print(i)


obj = Aravind()
n = int(input())
obj.divideEvenli(n)
