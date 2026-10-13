#!/usr/bin/env python3
"""Independent exact rational-point matrix verification, Python Fraction only.
Computes the historical t=3 case afresh, without SymPy or importing other scripts.
It does NOT prove the t-symbolic identity by itself.
"""
from fractions import Fraction as F
import json
# 2x2 matrix encoded as tuple of rows of fractions
def M(a,b,c,d):return ((F(a),F(b)),(F(c),F(d)))
I=M(1,0,0,1)
def mm(x,y):return M(*(sum(x[i][k]*y[k][j] for k in range(2)) for i in range(2) for j in range(2)))
def add(x,y):return M(*(x[i][j]+y[i][j] for i in range(2) for j in range(2)))
def neg(x):return M(*(-x[i][j] for i in range(2) for j in range(2)))
def sub(x,y):return add(x,neg(y))
def mul(x,y):return mm(x,y)
def inv(x):
 det=x[0][0]*x[1][1]-x[0][1]*x[1][0];assert det!=0
 return M(x[1][1]/det,-x[0][1]/det,-x[1][0]/det,x[0][0]/det)
def nscale(x,k):return M(*(k*x[i][j] for i in range(2) for j in range(2)))
def ident(x,v):return x==nscale(I,v)
a=F(5,6);b=F(-3,10);u=F(2,5)
Q1=M(a,0,0,-a);Q2=M(b,u,u,-b);Q3=Q2;Q4=Q2
P=mul(mul(sub(I,Q1),Q2),inv(Q1))
T2=sub(sub(I,nscale(P,2)),Q2)
GV=mul(mul(T2,Q3),inv(T2));GC=mul(mul(sub(I,Q1),Q2),inv(sub(I,Q1)))
RV=sub(mul(mul(GV,inv(Q1)),Q2),mul(mul(Q2,inv(Q1)),GV))
RC=sub(mul(mul(GC,inv(Q1)),Q3),mul(mul(Q3,inv(Q1)),GC))
T3=sub(sub(sub(I,nscale(P,3)),nscale(T2,3)),Q2)
GT=mul(mul(T3,Q4),inv(T3))
RP=sub(mul(mul(GT,inv(Q1)),Q3),mul(mul(Q3,inv(Q1)),GT))
# Verify historical reduced equations using independently spelled-out products
R120=sub(mul(mul(Q3,inv(Q1)),Q2),mul(mul(Q2,inv(Q1)),Q3))
left=mul(mul(mul(mul(mul(P,T2),Q3),inv(T2)),inv(Q2)),T2)
right=mul(mul(mul(mul(mul(T2,P),Q3),inv(P)),inv(Q2)),P)
R145=sub(left,right)
assert ident(RV,F(1152,3125)),RV
assert ident(RC,F(576,275)),RC
assert ident(RP,F(192,625)),RP
assert R120==M(0,0,0,0) and R145==M(0,0,0,0)
assert all(x[0][0]*x[1][1]-x[0][1]*x[1][0] != 0 for x in (Q1,Q2,Q3,Q4,P,T2,T3,sub(I,Q1)))
out={'gate':'R12BB-ER','kind':'independent_fraction_exact_single_fixture','status':'PASS',
 'fixture':'t=3, beta=delta=1, a=5/6,b=-3/10,u=2/5',
 'eq120_restricted':'ZERO','eq145_restricted':'ZERO',
 'eq119_general_RV':'1152/3125', 'eq119_general_Rchain':'576/275',
 'eq119_extra_partner':'192/625',
 'interpretation':'Counterexample to global XL-survival on frozen rational fixture; symbolic proof separate',
 'independent_symbolic_global_proof':'NOT_CLAIMED'}
print(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+'\n',end='')
