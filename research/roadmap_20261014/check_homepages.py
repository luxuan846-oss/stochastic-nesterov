import urllib.request,json,concurrent.futures
from pathlib import Path
from fetch_sources import clean
P=Path(__file__).parent
urls={
'bot':'https://www.mat.univie.ac.at/~rabot/',
'csetnek':'https://www.mat.univie.ac.at/~csercser/index.htm',
'nguyen':'https://www.mat.univie.ac.at/~rabot/group.html',
'chenchene':'https://www.mat.univie.ac.at/~rabot/group.html',
'fadili':'https://fadili.users.greyc.fr/',
'trandinh':'https://quoctd.web.unc.edu/',
'nguyentrung':'https://nghiant01.github.io/',
'ryu':'https://ernestryu.com/',
'yoon':'https://tetrzim.github.io/CV/',
'loizou':'https://nicolasloizou.github.io/index.html',
'bravo':'https://sites.google.com/site/mbravogon/',
'cominetti':'https://www.uai.cl/profesores/ingenieria-y-ciencias/roberto-cominetti',
'contreras':'https://citylog.udp.cl/persona/juan-pablo-contreras/',
'combettes':'https://pcombet.math.ncsu.edu/',
'pesquet':'https://jc.pesquet.eu/',
'diakonikolas':'https://www.jelena-diakonikolas.com/',
'salzo':'https://www.open.diag.uniroma1.it/users/saverio_salzo',
'alacaoglu':'https://ahmetalacaoglu.github.io/',
'hermant':'https://j-hermant.github.io/'
}
def get(item):
 name,url=item
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35)
  s=clean(r.read().decode('utf8','replace'))
  (P/'sources'/('homepage_'+name+'.txt')).write_text(s)
  return {'name':name,'url':url,'final_url':r.url,'status':r.status,'checked':'2026-10-14','text_length':len(s)}
 except Exception as e:return {'name':name,'url':url,'checked':'2026-10-14','status':'待核实','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:results=list(ex.map(get,urls.items()))
(P/'homepage_checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
for x in results:print(x['name'],x['status'],x.get('error',''))
