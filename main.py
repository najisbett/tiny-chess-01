import json,os,sys,urllib.request as U
D={'n':(-21,-19,-12,-8,8,12,19,21),'b':(-11,-9,9,11),'r':(-10,-1,1,10)}
D['q']=D['k']=D['b']+D['r']
V=dict(p=100,n=320,b=330,r=500,q=900,k=0)
T=dict(p=('@@@BELY@','@@AC'),n=('6<BFHHB<','4=BE'),b=('<@BCCB@=','<@BC'),r=('@@@@@AEB','?@AB'),q=('=?@@@@@@','>@AA'),k=('F@:40,($','BF@<'))
CR={95:'KQ',91:'Q',98:'K',25:'kq',21:'q',28:'k'}
S=[]
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
 v=0
 for s in range(21,99):
  c=B[s]
  if c in' .':continue
  k=c.lower();w=1 if c<'a'else -1
  i,j=divmod(s-21,10);a,b=T[k]
  v+=w*(V[k]+2*(ord(a[7-i if w>0 else i])+ord(b[min(j,7-j)])-128))
 return v
def O(m,p):
 if p<1 and RS:return RS.get(m,-9e5)+1e6*(m==BM)
 v=10*V.get(B[m[1]].lower(),0)+V.get(m[2],0)
 if v:v+=2e4-V[B[m[0]].lower()]
 elif m in K.get(p,()):v=9e3
 return v
def qs(a,b,w):
 v=ev()*w
 if v>=b:return v
 a=max(a,v)
 for m in sorted(gen(w,1),key=lambda m:-O(m,99)):
  mk(m,w)
  if not ck(w):
   v=-qs(-b,-a,-w)
   if v>=b:un(w);return v
   a=max(a,v)
  un(w)
 return a
def sr(d,a,b,w,p):
 global BM
 c=ck(w)
 d+=c*(p<9)
 if d<1:return qs(a,b,w)
 n=0;g=-99999
 for m in sorted(gen(w),key=lambda m:-O(m,p)):
  mk(m,w)
  if ck(w):un(w);continue
  n+=1;v=-sr(d-1,-b,-a,-w,p+1);un(w)
  if p<1:RS[m]=v
  if v>g:
   g=v
   if p<1:BM=m
   if v>a:
    a=v
    if a>=b:
     if B[m[1]]=='.':K[p]=[m]+[x for x in K.get(p,())if x!=m][:1]
     break
 if n==0:return p-30000 if c else 0
 return g
def best(f,dep=4):
 global BM,RS,K
 w=load(f);BM=None;RS={};K={}
 for d in range(1,dep+1):sr(d,-99999,99999,w,0)
 return BM
uci=lambda m:''.join(chr(96+s%10)+str(10-s//10)for s in m[:2])+m[2]
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
