import lzma,re,itertools
src=open('engine_src.py','rb').read()
best=None
for lc,lp,pb in itertools.product(range(5),range(3),range(3)):
 try:
  z=lzma.compress(src,lzma.FORMAT_ALONE,filters=[{'id':lzma.FILTER_LZMA1,'preset':9|lzma.PRESET_EXTREME,'lc':lc,'lp':lp,'pb':pb,'dict_size':1<<16}])
 except lzma.LZMAError:continue
 if best is None or len(z)<len(best):best=z
s=best.decode('l1')
s=re.sub(r"\\|'|\r|\x00(?=[0-7])|\x00",lambda m:{'\\':'\\\\',"'":"\\'",'\r':'\\r'}.get(m[0],'\\x00' if m[0]=='\x00' and False else '\\0'),s)
# \0 followed by octal digit would misparse; use \x00 in that case
s=re.sub(r"\\0(?=[0-7])",r"\\x00",s)
out=("# coding:l1\nimport lzma\nexec(lzma.decompress('''"+s+"'''.encode('l1')))\n").encode('l1')
open('main.py','wb').write(out)
print(len(src),len(best),len(out))
