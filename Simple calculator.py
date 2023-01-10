import math
import numpy as np
from sympy import symbols,Eq,solve
import cmath
def _sum(a):
            sum=0
            for i in a:
                        sum=sum+i
        
            return(sum)
def _difference(a):
                    diff=0
                    for i in a:
                                diff=diff-i
                    return(diff)
def _product(a):
                prod=1
                for i in a:
                            prod=prod*i
                return(prod) 
def _divi(a):
            div=1
            for i in a:
                        div=div/i
            return(div)
def _equations(a):
                    while True:
                                print("1. px+by=c")
                                print("2. px+by+cz=d")
                                print("3. p(x*x)+bx+c=0")
                                print("4. p(x*x*x)+b(x*x)+cx+d=0")
                                print("5. Exit")
                                chi=(int(input("Enter your choice =")))
                                if chi==1:
                                            p1=(float(input("Enter the value of p1=")))
                                            b1=(float(input("Enter the value of b1=")))
                                            c1=(float(input("Enter the value of c1=")))
                                            p2=(float(input("Enter the value of p2=")))
                                            b2=(float(input("Enter the value of b2=")))
                                            c2=(float(input("Enter the value of c2=")))
                                            #print("The Equation 1 is ",p1,"X+",b1,"Y=",c1)
                                            #print("The equation 2 is",p2,"X+",b2,"Y=",c2)
                                            x,y=symbols("x,y")
                                            eq1= Eq(((p1)*x)+(b1)*y,c1)
                                            print(eq1)
                                            eq2= Eq(((p2)*x)+(b2)*y,c2)
                                            print(eq2)
                                            print("Values of 2 unknown variable are as follows:")
                                            print(solve((eq1,eq2),(x,y)))
                                elif chi==2:
                                            pa1=(float(input("Enter the value of p1=")))
                                            pb1=(float(input("Enter the value of b1=")))
                                            pc1=(float(input("Enter the value of c1=")))
                                            pd1=(float(input("Enter the value of d1=")))
                                            pa2=(float(input("Enter the value of p2=")))
                                            pb2=(float(input("Enter the value of b2=")))
                                            pc2=(float(input("Enter the value of c2=")))
                                            pd2=(float(input("Enter the value of d2=")))
                                            pa3=(float(input("Enter the value of p3=")))
                                            pb3=(float(input("Enter the value of b3=")))
                                            pc3=(float(input("Enter the value of c3=")))
                                            pd3=(float(input("Enter the value of d3=")))
                                            x,y,z=symbols("x,y,z")
                                            equ1=Eq(((pa1)*x)+(pb1)*y+(pc1)*z,pd1)
                                            print("Equation 1=",equ1)
                                            equ2=Eq(((pa2)*x)+(pb2)*y+(pc2)*z,pd2)
                                            print("Equation 2 =",equ2)
                                            equ3=Eq(((pa3)*x)+(pb3)*y+(pc3)*z,pd3)
                                            print("Equation 3 =",equ3)
                                            print("Values of 3 unknown variable are as follows:")
                                            print(solve((equ1, equ2, equ3), (x, y, z)))
                                elif chi==3:
                                            pb1=(float(input("Enter the value of p =")))
                                            bb1=(float(input("Enter the value of b=")))
                                            bc1=(float(input("Enter the value of c=")))
                                            dis=(bb1**2)-(4*pb1*bc1)
                                            ans1=(-bb1-cmath.sqrt(dis))/(2*pb1)
                                            ans2=(-bb1+cmath.sqrt(dis))/(2*pb1)
                                            print('The roots are')
                                            print(ans1)
                                            print(ans2)
                                elif chi==4:
                                            pce=(float(input("Enter the value of p =")))
                                            bce=(float(input("Enter the value of b =")))
                                            cce=(float(input("Enter the value of c =")))
                                            dce=(float(input("Enter the value of d =")))
                                            x=symbols("x")
                                            equa1=Eq((pce)*pow(x,3)+(bce)*pow(x,2)+(cce)*x+(dce),0)
                                            print("The equation =",equa1)
                                            s1=solve(equa1)
                                            print("The roots =",s1)
                                elif chi==5:
                                            break
                                else:
                                        print("Oops incorrect choice") 

print("\n Simple Calculator")
n=int(input("Enter the number of elements="))
a=[]
for i in range(0,n):
    e=int(input("Enter the number="))
    a.append(e)
print(a)
while True:           
            print("\n Main Menu")
            print("1.Addition of numbers")
            print("2. Subtraction of numbers")
            print("3. Product of numbers")
            print("4. Division of numbers")
            print("5. sin of angle")
            print("6. Cosine of angle")
            print("7. Tangent of an angle")
            print("8. cotangent of an angle")
            print("9. sec of angle")
            print("10. cosec of angle")
            print("11.1og of number")
            print("12. x to power ")
            print("13. square root of")
            print("14. sin inverse ")
            print("15. cos inverse")
            print("16. tan inverse")
            print("17. cot inverse")
            print("18. Solve Equations")
            print("19. Delete")
            print("20. AC")
            print("21. Exit")
            ch=int(input("Enter your choice="))
            if ch==1:
                        pr=_sum(a)
                        print("The sum of the elements =",pr)  
            elif ch==2:
                        qy=_difference(a)
                        print("The difference of the numbers =",qy)
            elif ch==3:
                        rz=_product(a)
                        print("The product of the numbers =",rz)
            elif ch==4:
                        di=_divi(a)
                        print("The division of the numbers =",di)
            elif ch==5:
                        six=(int(input("Enter the angle in degrees =")))
                        print(math.sin(math.radians(six)))
            elif ch==6:
                        cy=(int(input("Enter the angle in degrees =")))
                        print(math.cos(math.radians(cy)))
            elif ch==7:
                        tz=(int(input("Enter the angle in degrees =")))
                        print(math.tan(math.radians(tz)))
            elif ch==8:
                        cz=(int(input("Enter the angle in degrees =")))
                        cz1=1/(math.tan(math.radians(cz)))
                        print(cz1)
            elif ch==9:
                        sy=(int(input("Enter the angle in degrees =")))
                        sy1=1/(math.cos(math.radians(sy)))
                        print(sy1)
            elif ch==10:
                        csx=(int(input("Enter the angle in degrees =")))
                        csx1=1/(math.sin(math.radians(csx)))
                        print(csx1)
            elif ch==11:
                        lx=(float(input("Enter the number =")))
                        ba=(int(input("Enter the base of a number =")))
                        print(math.log(lx,ba))
            elif ch==12:
                        x5=(float(input("Enter the value of x=")))
                        po=(float(input("Enter the value of power to raise =")))
                        an=pow(x5,po)
                        print(an)
            elif ch==13:
                        ax=(float(input("Enter the number =")))
                        print(pow(ax,2))
            elif ch==14:
                        isix=(float(input("Enter the value =")))
                        print("The value of angle in radians =",np.arcsin(isix))
            elif ch==15:
                        icox=(float(input("Enter the value =")))
                        print("The value of angle in radians =",np.arccos(icox))
            elif ch==16:
                        itax=(float(input("Enter the value =")))
                        print("The value of angle in radians =",np.arctan(itax))
            elif ch==17:
                        icot=(float(input("Enter the value =")))
                        icot1=(1.571-(np.arctan(icot)))
                        print("The value of angle in radians =",icot1)
            elif ch==18:
                        se=_equations(a)
            elif ch==19:
                        a=a[:-1]
                        print("New list is ",a)
            elif ch==20:
                        a.clear()
                        print(a)
            elif ch==21:
                        break
            else:
                    print("Oops incorrect choice")         