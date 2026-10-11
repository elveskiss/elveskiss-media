"""Writing spec v1 (WRITING_SPEC.md): per-item facts, per-platform copy, and the CHECK step.
Facts come ONLY from the product detail pages (上架产品/<Z code>/长详情.jpg)."""
import re
L='https://elveskiss.github.io/'
# id: (product code, exact stone name, form, size or None, origin or None)
FACTS={
 'q01':('Z01004','raw aquamarine','bracelet',None,None),
 'q02':('Z01007','rock candy raw crystal','bracelet','1–2 cm',None),
 'q03':('Z01005','aquamarine & morganite','bracelet',None,None),
 'q04':('Z01006','raw peridot','bracelet','0.8 × 1.5 cm','Egypt'),
 'q05':('Z01008','raw garnet','bracelet','0.8 × 1.5 cm','Brazil'),
 'q07':('Z02013','raw aquamarine','pendant (925 silver)',None,None),
 'q08':('Z02001','Vogel 12-facet clear quartz','pendulum pendant','1.5 × 6 cm',None),
 'q09':('Z03004','dream amethyst','sphere','6–30 cm','Brazil'),
 'q10':('Z03010','golden Iceland spar (calcite)','sphere','3–6 cm',None),
 'q14':('Z05007','raw super seven','raw stone',None,None),
}
BANNED=r"\b(heal\w*|cure[sd]?|curing|treat|treats|anxiety|depression|sleep\w*|pain\w*|medical\w*|guarantee\w*|luck\w*|wealth\w*|money|manifest money|protect you from)\b"
CONTACT=r"whatsapp|wa\.me|wechat|paypal|@\w+\.\w|https?://|www\.|\bdms?\b|message us|link in bio|\bbuy\b|\border\b|phone|email"
COUNTRIES=r"\b(Brazil\w*|Egypt\w*|Zimbabwe\w*|Madagascar\w*|Uruguay\w*|Mexic\w*|India\w*|Pakistan\w*|Afghan\w*|Russia\w*|Namibia\w*|Morocc\w*)\b"
WRONG_NAMES={'q02':['rose quartz'],'q07':['aquamarine 925'],'q08':['vogel-style']}
# product-specific claims the boss forbade (2026-10-11): never return for these items
FORBIDDEN_CLAIMS={'q03':[r'no resin',r'acid[- ]wash',r'no dye',r'\ball[- ]natural\b',r'treat\w*',r'certificat\w*',r'\blab\b']}
STATS=r"\d+\s?%"
def tags(t): return re.findall(r"(?<![/\w])#\w+",t)
def check(platform,text,item,title=None,is_video=True,url=None):
    """Return list of failures (empty = pass)."""
    f=[]; full=(title or '')+'\n'+text
    b=re.findall(BANNED,full,re.I)
    if b: f.append('banned:'+','.join(sorted(set(x.lower() for x in b))))
    if re.search(STATS,full): f.append('statistic')
    code,name,form,size,origin=FACTS[item]
    for rx in FORBIDDEN_CLAIMS.get(item,[]):
        if re.search(rx,full,re.I): f.append('forbidden claim:'+rx)
    for w in WRONG_NAMES.get(item,[]):
        if w in full.lower(): f.append('name:'+w)
    for c in re.findall(COUNTRIES,full):
        if not origin or not c.lower().startswith(origin.lower()[:5]): f.append('origin:'+c)
    for s in re.findall(r"\d+(?:\.\d+)?\s?(?:[–-]|×|x)\s?\d+(?:\.\d+)?\s?cm",full):
        if not size or s.replace(' ','').replace('x','×')!=size.replace(' ',''): f.append('size:'+s)
    if 'aqua aura' in full.lower() and 'coated' not in full.lower(): f.append('aqua aura not named coated')
    n=len(tags(text))
    if platform=='tiktok':
        if not text.rstrip().split('\n')[0].endswith('Follow for the next drop 💎'): f.append('tiktok ending')
        if not 3<=n<=5: f.append(f'tiktok hashtags {n}')
        if re.search(CONTACT,full,re.I): f.append('tiktok contact')
    elif platform=='instagram':
        if 'DM us to order 💌' not in text: f.append('ig cta')
        if not 5<=n<=8: f.append(f'ig hashtags {n}')
        if not re.search(r"(#\w+\s*)+$",text.strip()): f.append('ig hashtags not at end')
        if re.search(r"whatsapp|wa\.me",text,re.I): f.append('ig whatsapp')
    elif platform=='threads':
        if 'DM us on IG' not in text: f.append('threads cta')
        if n>1: f.append(f'threads hashtags {n}')
        if re.search(r"whatsapp|wa\.me",text,re.I): f.append('threads whatsapp')
    elif platform in('x','twitter'):
        if len(text)>=240: f.append(f'x length {len(text)}')
        if 'DMs open' not in text: f.append('x cta')
        if n>2: f.append(f'x hashtags {n}')
    elif platform=='pinterest':
        if not title or len(title)>100: f.append('pin title')
        body=re.sub(r"#\w+","",text).strip()
        if not body.endswith('Tap to see more'): f.append('pin ending')
        sents=len(re.findall(r"[.!?](\s|$)",body))+(0 if body.endswith(('.', '!', '?')) else 1)
        if not 2<=sents<=4: f.append(f'pin sentences {sents}')
        if not 3<=n<=5: f.append(f'pin hashtags {n}')
        if url is not None and url!=L+'#'+item: f.append('pin link')
    elif platform=='youtube':
        if not is_video: f.append('youtube needs video')
        if L+'#'+item not in text: f.append('yt landing')
        if 'Subscribe for daily crystals' not in text: f.append('yt subscribe')
        if n!=3: f.append(f'yt hashtags {n}')
        if not title or len(title)>100: f.append('yt title')
    return f
