"""Monthly take-home for a single J-1 fellow (resident alien for tax after 2 calendar years -> FICA applies).
Federal: projected 2027 single (Bloomberg Tax): std ded 16,600; 10% to 12,800; 12% to 52,025; 22% to ~109,000."""
import json, sys
FED_STD=16600
FED_BR=[(12800,.10),(52025,.12),(109000,.22),(208200,.24)]
def fed(g):
    t=max(0,g-FED_STD); tax=0; lo=0
    for hi,r in FED_BR:
        if t>lo: tax+=(min(t,hi)-lo)*r
        lo=hi
    return tax
def fica(g): return g*0.062+g*0.0145
def state(st,g,city=None):
    if st=='MA': s=max(0,g-4400)*0.05 + g*0.0046   # 5% flat after $4,400 exemption; + PFML employee share ~0.46%
    elif st=='OH': s=max(0,g-26050)*0.0275 + (g*0.025 if city=='Columbus' else 0)
    elif st=='WI':
        sd=max(0,13930-0.12*max(0,g-19070)); t=max(0,g-sd-700); s=0; lo=0
        for hi,r in [(15110,.035),(51950,.044),(332720,.053),(1e12,.0765)]:
            if t>lo: s+=(min(t,hi)-lo)*r
            lo=hi
    elif st=='GA': s=max(0,g-15000)*0.0499
    elif st=='MI': s=max(0,g-5900)*0.0425 + (max(0,g-600)*0.024 if city=='Detroit' else 0)
    elif st=='LA': s=max(0,g-12500)*0.03
    elif st=='TN': s=0
    return s
def month(st,g,city=None,ins=300):
    f,fi,s=fed(g),fica(g),state(st,g,city)
    return dict(gross_m=g/12,fed_m=f/12,fica_m=fi/12,state_m=s/12,ins_m=ins,net_m=(g-f-fi-s)/12-ins)
if __name__=='__main__':
    for g in (70000,75000,80000,85000,90000):
        print(g,{k:round(v) for k,v in month('TN',g).items()})
