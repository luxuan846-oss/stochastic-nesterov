from pathlib import Path
from html.parser import HTMLParser
import urllib.request,re,html,json,concurrent.futures
ROOT=Path(__file__).parent/'sources'
class P(HTMLParser):
 def __init__(self):super().__init__();self.a=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if t in ['p','section','div','h1','h2','h3','h4','li','tr']:self.a.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
  if t in ['p','section','h1','h2','h3','h4','li','tr']:self.a.append('\n')
 def handle_data(self,d):
  if not self.skip:self.a.append(d)
def clean(s):
 def math(m):
  a=re.search(r'alttext="([^"]*)"',m.group(0));return ' $'+html.unescape(a.group(1))+'$ ' if a else m.group(0)
 s=re.sub(r'<math\b.*?</math>',math,s,flags=re.S)
 p=P();p.feed(s);return '\n'.join(re.sub(r'\s+',' ',x).strip() for x in ''.join(p.a).splitlines() if x.strip())
def fetch(item):
 name,url=item
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40);s=r.read().decode('utf8','replace');(ROOT/(name+'.html')).write_text(s);(ROOT/(name+'.txt')).write_text(clean(s));return name,r.status,len(s)
 except Exception as e:return name,str(e)
if __name__=='__main__':
 urls={'vfog':'https://arxiv.org/html/2508.16791','vrhalpern':'https://arxiv.org/html/2203.09436','vfosa_page':'https://www.jmlr.org/papers/v26/25-0500.html','bot_group':'https://www.mat.univie.ac.at/~rabot/group.html','salzo':'https://arxiv.org/html/2511.12665v3'}
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  for x in ex.map(fetch,urls.items()):print(x)
