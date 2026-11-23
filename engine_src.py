import json,os,sys,urllib.request as U
D={'n':(-21,-19,-12,-8,8,12,19,21),'b':(-11,-9,9,11),'r':(-10,-1,1,10)}
D['q']=D['k']=D['b']+D['r']
V=dict(p=100,n=320,b=330,r=500,q=900,k=0)
M=dict(n=4,b=3,r=2,q=1)
T=dict(p=('@@@BELY@','@@AC'),n=('6<BFHHB<','4=BE'),b=('<@BCCB@=','<@BC'),r=('@@@@@AEB','?@AB'),q=('=?@@@@@@','>@AA'),k=('F@:40,($','BF@<'))
CR={95:'KQ',91:'Q',98:'K',25:'kq',21:'q',28:'k'}
S=[];TT={};K={};H={};N=LIM=0;BM=None
class X(Exception):pass
def load(f):
 global B,R,E
 p=f.split();B=[' ']*120
 for i,r in enumerate(p[0].split('/')):B[21+10*i:29+10*i]=''.join('.'*int(c)if c.isdigit()else c for c in r)
 R=p[2];E=0 if p[3]=='-'else 21+10*(8-int(p[3][1]))+ord(p[3][0])-97
 return 1 if p[1]=='w'else -1
def att(s,w):
 f=str.upper if w>0 else str.lower
 if f('p')in(B[s+9*w],B[s+11*w]):return 1
 for d in D['n']:
  if B[s+d]==f('n'):return 1
 for d in D['q']:
  t=s+d
  if B[t]==f('k'):return 1
  while B[t]=='.':t+=d
  if B[t]in(f('q'),f('b'if d in D['b']else'r')):return 1
 return 0
def gen(w,q=0):
 L=[]
 def add(s,t):
  if B[s]in'Pp'and(t<29 or t>90):L.extend((s,t,p)for p in'qrbn')
  else:L.append((s,t,''))
 for s in range(21,99):
  c=B[s]
  if c in' .'or c.isupper()!=(w>0):continue
  k=c.lower()
  if k=='p':
   d=-10*w
   for t in(s+d+1,s+d-1):
    if B[t]not in' .'and B[t].isupper()==(w<0)or t==E:add(s,t)
   t=s+d
   if B[t]=='.':
    add(s,t)
    if s//10==(8 if w>0 else 3)and B[t+d]=='.':add(s,t+d)
   continue
  for d in D[k]:
   t=s+d
   while B[t]!=' ':
    x=B[t]
    if x=='.':add(s,t)
    else:
     if x.isupper()==(w<0):add(s,t)
     break
    if k in'nk':break
    t+=d
  if k=='k'and s==(95 if w>0 else 25):
   for e,z,n in(1,'Kk',2),(-1,'Qq',3):
    if z[w<0]in R and all(B[s+e*i]=='.'for i in range(1,n+1))and not att(s,-w)and not att(s+e,-w):add(s,s+2*e)
 if q:L=[m for m in L if B[m[1]]!='.'or m[2]or(B[m[0]]in'Pp'and m[1]==E)]
 return L
def mk(m,w):
 global R,E
 s,t,p=m;c=B[s];x=B[t]
 S.append((B[:],R,E))
 B[t]=c;B[s]='.'
 if c in'Pp':
  if t==E and x=='.':B[t+10*w]='.'
  if p:B[t]=p.upper()if w>0 else p
 if c in'Kk'and abs(t-s)==2:
  a,b=(t+1,t-1)if t>s else(t-2,t+1)
  B[b]=B[a];B[a]='.'
 E=(s+t)//2 if c in'Pp'and abs(t-s)==20 else 0
 for q in(s,t):
  for z in CR.get(q,''):R=R.replace(z,'')
def un(w):
 global R,E
 B[:],R,E=S.pop()
def ck(w):return att(B.index('Kk'[w<0]),-w)
def ev():
 v=P=0;ks={};bp={1:0,-1:0}
 for s in range(21,99):
  c=B[s]
  if c in' .':continue
  k=c.lower();w=1 if c<'a'else -1
  i,j=divmod(s-21,10)
  if k=='k':ks[w]=s;continue
  a,b=T[k]
  x=V[k]+2*(ord(a[7-i if w>0 else i])+ord(b[min(j,7-j)])-128)
  if k!='p':
   P+=V[k];m=M[k]
   if k=='b':bp[w]+=1
   for d in D[k]:
    t=s+d
    while B[t]=='.':
     x+=m
     if k=='n':break
     t+=d
  v+=w*x
 v+=30*((bp[1]>1)-(bp[-1]>1))
 f=min(P,3600)/3600
 for w in(1,-1):
  s=ks[w];i,j=divmod(s-21,10);a,b=T['k']
  h=sum(B[s-10*w+e]=='Pp'[w<0]for e in(-1,0,1))
  g=f*(2*(ord(a[7-i if w>0 else i])+ord(b[min(j,7-j)])-128)+12*h)-(1-f)*6*(abs(2*i-7)+abs(2*j-7))
  v+=w*g
 return int(v)
def O(m,p,tm=None):
 if m==tm:return 9e6
 x=B[m[1]];v=V.get(m[2],0)
 if x!='.':return 1e5+10*V[x.lower()]-V[B[m[0]].lower()]+v
 if v:return 9e4+v
 if m in K.get(p,()):return 5e4
 return H.get((B[m[0]],m[1]),0)
def qs(a,b,w,qd):
 global N
 N+=1
 c=ck(w)if qd<2 else 0
 v=ev()*w
 if c:g=-29000
 else:
  g=v
  if v>=b:return v
  a=max(a,v)
 for m in sorted(gen(w,qd>0 and not c),key=lambda m:-O(m,99)):
  q=B[m[1]]=='.'and not m[2]
  mk(m,w)
  if ck(w)or q and not c and not att(B.index('Kk'[w>0]),w):un(w);continue
  v=-qs(-b,-a,-w,qd+1);un(w)
  if v>g:
   g=v
   if v>=b:return v
   a=max(a,v)
 return g
def sr(d,a,b,w,p,nm=1):
 global N,BM
 N+=1
 if N>LIM:raise X
 c=ck(w);d+=c
 if d<1:return qs(a,b,w,0)
 j=''.join(B);k=(j,w,R,E);e=TT.get(k);tm=None;a0=a
 if e:
  tm=e[3]
  if e[0]>=d and p:
   v,f=e[2],e[1]
   if f==0 or f==1 and v>=b or f==2 and v<=a:return v
 if nm and d>=3 and not c and p and b-a==1 and any(z in j for z in('NBRQ'if w>0 else'nbrq')):
  s=E
  globals()['E']=0
  v=-sr(d-3,-b,-b+1,-w,p+1,0)
  globals()['E']=s
  if v>=b:return v if v<29000 else b
 n=0;g=-99999;bm=None;f=2
 for m in sorted(gen(w),key=lambda m:-O(m,p,tm)):
  q=B[m[1]]=='.'and not m[2]
  mk(m,w)
  if ck(w):un(w);continue
  if n==0:v=-sr(d-1,-b,-a,-w,p+1)
  else:
   r=0
   if d>=3 and n>=3 and q and not c and m not in K.get(p,()):r=1+(n>=9 and d>=5)
   v=-sr(d-1-r,-a-1,-a,-w,p+1)
   if v>a and r:v=-sr(d-1,-a-1,-a,-w,p+1)
   if a<v<b:v=-sr(d-1,-b,-a,-w,p+1)
  n+=1;un(w)
  if v>g:
   g=v;bm=m
   if v>a:
    a=v;f=0
    if a>=b:
     f=1
     if q:
      K[p]=[m]+[x for x in K.get(p,())if x!=m][:1]
      H[B[m[0]],m[1]]=H.get((B[m[0]],m[1]),0)+d*d
     break
 if n==0:return p-30000 if c else 0
 if abs(g)<29000:TT[k]=(d,f,g,bm)
 if p==0:BM=bm
 return g
def best(f,dep=5):
 global BM,N,LIM,K,H
 w=load(f);S.clear();K={};H={};N=0;r=None
 if len(TT)>300000:TT.clear()
 for d in range(1,dep+1):
  LIM=10**9 if d==1 else HARD
  try:sr(d,-99999,99999,w,0)
  except X:break
  r=BM
  if N>SOFT:break
 return r
HARD=60000;SOFT=20000
uci=lambda m:''.join(chr(96+s%10)+str(10-s//10)for s in m[:2])+m[2]
#--
u=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("MAKEFUN_ENV_URL is not set")
def post(p,b):
 try:return json.load(U.urlopen(U.Request(u+p,json.dumps(b).encode(),{"content-type":"application/json"})))
 except Exception as e:sys.exit(p+str(e))
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  m=uci(best(g["fen"]));L=g["legal_moves"]
  g=post("/move",{"game":g["game"],"move":m if m in L else L[0]})
 print(g['game'],g['outcome'],g['reason'],file=sys.stderr)
print("done",g.get('wins'),g.get('draws'),g.get('losses'),file=sys.stderr)
