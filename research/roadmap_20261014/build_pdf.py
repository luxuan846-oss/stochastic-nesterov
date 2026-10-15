from pathlib import Path
import subprocess
import sys
P=Path(__file__).resolve().parent
name='261014-领域roadmap-随机快速不动点'
# Extracted locally from the installed PingFang collection: regular face 3,
# semibold face 11. Separate faces keep SC selection explicit.
font=P/'tmp/fonts/PingFangSC-Regular.otf'
if not font.exists() or not (font.parent/'PingFangSC-Semibold.otf').exists():
    sys.path.insert(0,str(P/'tmp/fonttools'))
    from fontTools.ttLib import TTFont
    source=next(Path('/System/Library/AssetsV2/com_apple_MobileAsset_Font8').glob('*/AssetData/PingFang.ttc'))
    font.parent.mkdir(parents=True,exist_ok=True)
    for index,weight in [(3,'Regular'),(11,'Semibold')]:
        face=TTFont(source,fontNumber=index)
        psname='PingFangSC-'+weight
        if face['name'].getDebugName(6)!=psname:
            raise ValueError('The installed collection uses different face indices.')
        # Regional faces share CFF data named HK in the system TTC. Preserve
        # the selected SC cmap/glyphs and make standalone CFF names agree.
        face['CFF '].cff.fontNames=[psname]
        face['CFF '].cff.topDictIndex[0].FullName=psname
        face.save(font.parent/(psname+'.otf'))
cmd=['pandoc',name+'.md','-o',name+'.pdf','--pdf-engine=xelatex','-V','mainfont=Times New Roman','-V','CJKmainfont='+font.name,'-V','CJKoptions=Path={'+str(font.parent)+'/'+'},Scale=1,BoldFont={PingFangSC-Semibold.otf}','-V','geometry:margin=2cm','-V','colorlinks=true','--toc','--toc-depth=2','--lua-filter=pdf-tables.lua','-H','pdf-header.tex']
r=subprocess.run(cmd,cwd=P,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(P/'pdf-build.log').write_text(r.stdout)
print(r.stdout)
raise SystemExit(r.returncode)
