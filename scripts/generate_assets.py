"""Original profile artwork. Rebuild with Python's standard library."""
from html import escape
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'
OUT.mkdir(exist_ok=True)
THEMES={
    'light':{'bg':'#edf3ff','surface':'#ffffff','ink':'#182346','muted':'#52627e','line':'#c5d3ee','blue':'#3557cc','soft':'#dde7ff','violet':'#7056b8','teal':'#157b83','gold':'#8d672c'},
    'dark':{'bg':'#111b35','surface':'#172441','ink':'#eef3ff','muted':'#b0bed8','line':'#334569','blue':'#9ab4ff','soft':'#243760','violet':'#c4adff','teal':'#79d6d1','gold':'#e6c58e'},
}


class Art:
    def __init__(self,title,theme,width=1600,height=620):
        self.t=THEMES[theme];self.width=width;self.height=height
        self.parts=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<defs><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{self.t['bg']}"/><stop offset="1" stop-color="{self.t['surface']}"/></linearGradient>
<pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{self.t['line']}" opacity="0.55"/></pattern></defs>
<rect width="{width}" height="{height}" rx="28" fill="url(#wash)"/>
<style>text{{font-family:'Segoe UI','Microsoft YaHei','Noto Sans CJK SC',sans-serif}}.display{{font-family:Bahnschrift,'Segoe UI',sans-serif}}.mono{{font-family:'Cascadia Code',Consolas,monospace}}</style>''']

    def text(self,x,y,s,size=28,fill=None,weight=400,cls='',anchor='start',spacing=None):
        extra=f' letter-spacing="{spacing}"' if spacing else ''
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill or self.t["ink"]}" font-weight="{weight}" class="{cls}" text-anchor="{anchor}"{extra}>{escape(s)}</text>')

    def rect(self,x,y,w,h,fill=None,stroke=None,r=16):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill or self.t["surface"]}" stroke="{stroke or self.t["line"]}"/>')

    def circle(self,x,y,r,fill='none',stroke=None,sw=2):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke or self.t["line"]}" stroke-width="{sw}"/>')

    def path(self,d,color=None,sw=2,dash=None):
        extra=f' stroke-dasharray="{dash}"' if dash else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color or self.t["line"]}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{extra}/>')

    def tag(self,x,y,label,color=None,width=180):
        self.rect(x,y,width,43,self.t['surface'],self.t['line'],21)
        self.circle(x+22,y+21,4,color or self.t['blue'],color or self.t['blue'],0)
        self.text(x+39,y+29,label,19,self.t['muted'],500)

    def save(self,name,theme):
        (OUT/f'{name}-{theme}.svg').write_text('\n'.join(self.parts)+'\n</svg>\n',encoding='utf-8')


def hero(theme):
    a=Art('YuanYCoding — Agent Application Developer',theme)
    t=a.t
    a.parts.append('<rect x="920" y="40" width="640" height="480" fill="url(#dots)"/>')
    a.rect(72,62,48,48,t['blue'],t['blue'],14)
    a.text(96,98,'Y',31,t['surface'],700,'display','middle')
    a.text(140,94,'AGENT APPLICATION DEVELOPMENT',20,t['blue'],650,spacing='1.5')
    a.text(69,243,'YuanYCoding',112,t['ink'],650,'display')
    a.text(76,316,'Agent 应用开发',44,t['blue'],650)
    a.text(77,375,'把想法变成可使用、可验证、可复用的应用。',29,t['muted'])
    a.tag(77,427,'Agent Skills',width=198)
    a.tag(291,427,'Workflows',t['violet'],190)
    a.tag(497,427,'AI Apps',t['teal'],168)
    a.path('M77 534 H1523',t['line'],1.5)
    a.text(77,578,'BUILD WITH INTENT. VERIFY THE OUTCOME.',17,t['muted'],600,'mono')
    a.text(1523,578,'登高必自卑，行远必自迩。',23,t['muted'],400,anchor='end')
    cx,cy=1230,290
    a.circle(cx,cy,171,stroke=t['line'],sw=1.5)
    a.circle(cx,cy,142,stroke=t['line'],sw=1)
    a.path('M1015 176 Q1050 265 1145 287',t['blue'],3)
    a.path('M1297 237 Q1355 201 1400 146',t['violet'],3)
    a.path('M1304 337 Q1372 380 1410 401',t['teal'],3)
    a.path('M1144 310 Q1088 343 1050 422',t['gold'],3)
    a.circle(cx,cy,84,t['soft'],t['blue'],2)
    a.circle(cx,cy,67,t['surface'],t['line'],1)
    a.text(cx,cy+12,'AGENT',32,t['blue'],650,'display','middle',2)
    for x,y,label,col in [(1009,155,'INTENT',t['blue']),(1421,123,'TOOLS',t['violet']),(1436,421,'VERIFY',t['teal']),(1045,442,'CONTEXT',t['gold'])]:
        a.rect(x-77,y-25,154,50,t['surface'],t['line'],13)
        a.circle(x-54,y,4,col,col,0)
        a.text(x+9,y+7,label,18,col,600,'mono','middle')
    a.circle(1230,119,6,t['blue'],t['blue'],0)
    a.circle(1230,461,6,t['teal'],t['teal'],0)
    a.save('hero',theme)


PROJECTS=[
    ('scaffold','vibe-scaffold-kit','PLUGIN / ENGINEERING','从需求澄清，到可运行工程。','Clarify → Select → Scaffold','blue'),
    ('agentsmd','use-agentsmd','SKILL / PROJECT CONTEXT','让项目规则，跟上代码变化。','Create → Calibrate → Maintain','teal'),
    ('regex','RegexForge','APPLICATION / LLM WORKFLOW','从自然语言，到可测试的正则。','Generate → Test → Refine','gold'),
    ('decision','decision_expert','SKILL / EVIDENCE & REASONING','让重要判断，经得起推敲。','Challenge → Support → Decide','violet'),
]


def project(theme,item):
    key,name,category,subtitle,flow,accent=item
    a=Art(name+' — '+subtitle,theme,height=244);t=a.t;col=t[accent]
    a.rect(1,1,1598,242,t['surface'],t['line'],24)
    a.rect(26,27,190,190,t['bg'],t['line'],20)
    if key=='scaffold':
        for x,y in [(65,69),(128,69),(65,132),(128,132)]:a.rect(x,y,49,49,t['soft'],col,7)
        a.path('M88 94 H154 M88 94 V157 M88 157 H154',col,2)
    elif key=='agentsmd':
        a.rect(72,62,99,124,t['surface'],col,10)
        for y,w in [(91,55),(117,61),(141,47),(163,57)]:a.path(f'M91 {y} H{91+w}',col,4)
    elif key=='regex':
        a.text(121,146,'.*',78,col,600,'mono','middle')
        a.path('M70 78 H57 V170 H70 M172 78 H185 V170 H172',col,3)
    else:
        a.path('M121 65 V180 M72 100 H170 M88 101 L62 145 H115 Z M154 101 L128 145 H181 Z',col,3)
        a.circle(121,72,8,t['surface'],col,3)
    a.text(255,69,category,18,col,650,'mono',spacing='1')
    a.text(253,131,name,54,t['ink'],600,'display')
    a.text(255,186,subtitle,29,t['muted'])
    a.path('M1002 48 V196',t['line'],1.5)
    a.text(1050,108,'WORKFLOW',17,t['muted'],600,'mono',spacing='1.5')
    a.text(1050,148,flow,24,col,550,'display')
    a.circle(1503,123,33,t['bg'],t['line'],1)
    a.path('M1491 134 L1515 110 M1494 110 H1515 V131',col,2.5)
    a.save(key,theme)


def process(theme):
    a=Art('澄清需求 → 构建能力 → 验证结果 → 沉淀复用',theme,height=176);t=a.t
    for i,(label,en,col) in enumerate([('澄清需求','CLARIFY',t['blue']),('构建能力','BUILD',t['violet']),('验证结果','VERIFY',t['teal']),('沉淀复用','REUSE',t['gold'])]):
        x=64+i*395
        a.circle(x+28,87,26,t['surface'],col,2)
        a.text(x+28,95,str(i+1),23,col,600,'mono','middle')
        a.text(x+76,82,label,31,t['ink'],600)
        a.text(x+78,116,en,17,col,600,'mono',spacing='1.5')
        if i<3:a.path(f'M{x+287} 87 H{x+339} M{x+331} 79 L{x+339} 87 L{x+331} 95',t['line'],2)
    a.save('process',theme)


if __name__=='__main__':
    for theme in THEMES:
        hero(theme)
        for item in PROJECTS:project(theme,item)
        process(theme)
    print('Generated 12 theme-aware SVG assets.')
