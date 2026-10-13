#!/usr/bin/env python3
"""Check exact general Theorem 3.7 residuals on the formerly 'surviving' XL curve.
Source: Srivastava--Surya arXiv:2603.25503v1, Eqs.(114),(119),(120),(141),(142),(159).
Not a preregistered discovery, independent human review, or universal QSG theorem.
No imports from historical author or referee scripts.
"""
import json
import sympy as s
I=s.eye(2)
t,beta,delta=s.symbols('t beta delta',real=True,nonzero=True)
a=(t*t+1)/(4*t);b=-t/(t*t+1);u=(t*t-1)/(2*(t*t+1))
Q1=s.diag(a,-a);Q2=s.Matrix([[b,u],[u,-b]]);Q3=beta*Q2; Q4=delta*Q2
P=(I-Q1)*Q2*Q1.inv();T2=I-2*P-Q2
Gv=T2*Q3*T2.inv();Gc=(I-Q1)*Q2*(I-Q1).inv()
mat=lambda x:x.applyfunc(s.factor)
V=mat(Gv*Q1.inv()*Q2-Q2*Q1.inv()*Gv)
C=mat(Gc*Q1.inv()*Q3-Q3*Q1.inv()*Gc)
Ev=s.factor(beta*(4*a*a-1)/(10*a**4));Ec=s.factor(-4*beta*u*u/(a*a-1))
assert mat(V-Ev*I)==s.zeros(2)
assert mat(C-Ec*I)==s.zeros(2)
assert mat(Q3*Q1.inv()*Q2-Q2*Q1.inv()*Q3)==s.zeros(2)
assert mat(P*T2*Q3*T2.inv()*Q2.inv()*T2 - T2*P*Q3*P.inv()*Q2.inv()*P)==s.zeros(2)
T3=I-3*P-3*T2-Q2
Gt=T3*Q4*T3.inv(); partner=mat(Gt*Q1.inv()*Q2-Q2*Q1.inv()*Gt)
Ep=s.factor(16*delta*t**2*(t*t-1)**2/(3*(t*t+1)**4))
assert mat(partner-Ep*I)==s.zeros(2)
assert s.factor(T3.det() + 9*(t**4-46*t**2+1)/(4*(t**2+1)**2)) == 0
for x,y in [(Ev,s.Rational(1152,3125)),(Ec,s.Rational(576,275)),(Ep,s.Rational(192,625))]:
 assert s.factor(x.subs({t:3,beta:1,delta:1})-y)==0
out={'gate':'R12BB-ER','kind':'symbolic_exact_with_sympy','status':'PASS',
 'scope':'Strong operator CPOBC, historical XL hermitian traceless 2x2 curve only',
 'eq120_restricted':'ZERO','eq145_restricted':'ZERO',
 'eq119_general_RV':str(Ev),'eq119_general_Rchain':str(Ec),
 'eq119_extra_partner':str(Ep),
 'det_timid_a3':str(s.factor(T3.det())),
 'rational_t3':{'RV':'1152/3125','Rchain':'576/275','Rpartner':'192/625'},
 'interpretation':'Old XL full-CPOBC-survival claim withdrawn; local restricted identities preserved',
 'historical_full_v095_replay':'NOT_PERFORMED'}
print(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+'\n',end='')
