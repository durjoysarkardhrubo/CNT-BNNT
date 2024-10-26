#Area for computing TC of BNNT+CNT 
import math
r_hi=float(input("Radius of Outer Lyer in A unit :"))
r_lo=float(input("Radius of Inner Lyer in A unit :"))
space=float(input("Spacing between the layer in A unit:"))

def cal_Area(a,b,c):
  A=math.pi*(3.4+space)*(r_hi+r_lo)
  return A

print(f"Effective area for TC cal;culation is {cal_Area(r_hi,r_lo,space)} A^2")
