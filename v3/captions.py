import json
WA='https://wa.me/8619901529320'
C={'q09':{
 'tiktok':"Real or fake? 💜 Natural Brazilian dream amethyst, hand-polished, bands and inclusions all natural. 6–30 cm, stand included. What was your first guess? #amethyst #crystaltok #crystals #realorfake #elveskiss",
 'tiktok_title':"Is this real amethyst?",
 'ig_reel':"Is this real amethyst? 💜\n\nNatural Brazilian dream amethyst, hand-polished so the purple and white bands come through. Every inclusion is natural, so no two spheres look the same. Sizes 6–30 cm, stand included.\n\nIn crystal tradition, amethyst is associated with calm.\n\nDM us for sizes ✨\n\n#amethyst #dreamamethyst #crystalsphere #crystaldecor #crystals #elveskiss",
 'ig_carousel':"How to spot real amethyst: 3 checks 💜 Save this for your next crystal hunt.\n\n1. Natural banding\n2. Tiny inclusions up close\n3. Ask where it comes from\n\nOur Brazilian dream amethyst spheres are hand-polished, 6–30 cm, stand included.\n\nWhich check do you already use?\nDM us for sizes ✨\n\n#amethyst #realcrystals #crystaltips #crystalsphere #crystalcollector #elveskiss",
 'youtube_title':"How to Tell Real Amethyst: 3 Quick Checks #Shorts",
 'youtube_description':"3 quick checks for real amethyst: natural banding, tiny inclusions up close, and knowing where it comes from. Shown on our natural Brazilian dream amethyst spheres, hand-polished, 6–30 cm, stand included.\nIn crystal tradition, amethyst is associated with calm.\nSee it here: https://elveskiss.github.io/#{ID}\nQuestions? DM us on Instagram ✨\n#amethyst #realamethyst #crystals #crystalsphere #shorts #elveskiss",
 'pinterest_title':"Dream Amethyst Sphere | Crystal Decor Idea",
 'pinterest_description':"Natural Brazilian dream amethyst sphere on its stand, an easy crystal decor idea for a shelf or tea table. 💜 Hand-polished, 6–30 cm, stand included. Traditionally associated with calm. Tap the pin for sizes and details, or chat with us on WhatsApp.\n#amethyst #crystaldecor #crystalsphere #homedecorideas #naturalcrystals",
 'x':"Factory diary, Donghai: a Brazilian dream amethyst sphere, hand-polished so the natural purple-white bands run like a chevron. 💜 Wholesale & custom DMs open",
 'threads':"Picture it on a tea table 💜 A Brazilian dream amethyst sphere, hand-polished, every band and inclusion natural. We make them from 6 to 30 cm with a stand. Where would you put one: desk, shelf or bedside?"},
'q05':{
 'tiktok':"Raw garnet, rinsed in spring water 🍷 Natural fracture faces, no dye, no resin. Everyday piece or special occasion? #garnet #rawcrystals #crystaltok #crystalbracelet #elveskiss",
 'tiktok_title':"Would you wear raw garnet?",
 'ig_reel':"Wine-red, rough and real 🍷\n\nRaw Brazilian garnet chips, about 0.8 × 1.5 cm, with their natural fracture faces left untouched. No dye, no resin. Every strand is rinsed in the spring water at our courtyard before it ships.\n\nIn crystal tradition, garnet is associated with energy and devotion.\n\nDM us for sizes ✨\n\n#garnet #rawgarnet #crystalbracelet #rawcrystals #crystals #elveskiss",
 'ig_carousel':"Raw garnet: what to look for 🍷 Save this before you buy.\n\n1. Natural fracture faces\n2. Color that shifts chip to chip\n3. No dye, no resin\n\nOur raw Brazilian garnet chips are about 0.8 × 1.5 cm and rinsed in spring water before they ship.\n\nRaw or polished, which do you prefer?\nDM us for sizes ✨\n\n#garnet #rawcrystals #crystaltips #crystalbracelet #crystaljewelry #elveskiss",
 'youtube_title':"Raw Garnet Bracelet: What to Look For #Shorts",
 'youtube_description':"What to look for in raw garnet: natural fracture faces, wine-red color that shifts from chip to chip, and no dye or resin. Our raw Brazilian garnet chips are about 0.8 × 1.5 cm, rinsed in spring water before shipping.\nIn crystal tradition, garnet is associated with energy and devotion.\nSee it here: https://elveskiss.github.io/#{ID}\nQuestions? DM us on Instagram ✨\n#garnet #rawgarnet #crystalbracelet #crystals #shorts #elveskiss",
 'pinterest_title':"Raw Garnet Bracelet | Boho Crystal Jewelry Idea",
 'pinterest_description':"Raw Brazilian garnet bracelet with natural fracture faces, a wine-red boho jewelry idea. 🍷 No dye, no resin, rinsed in spring water before it ships. Traditionally associated with energy and devotion. Tap the pin for sizes and details, or chat with us on WhatsApp.\n#garnet #bohojewelry #crystalbracelet #rawcrystals #naturalcrystals",
 'x':"Factory diary, Donghai: a raw garnet strand fresh from its spring-water rinse. Wine-red, rough, no dye, no resin. 🍷 Wholesale & custom DMs open",
 'threads':"Wine-red and rough, worn every day 🍷 Brazilian garnet chips with their natural fracture faces, no dye, no resin, rinsed in spring water before shipping. Would you wear it every day or save it for special days?"}}
from captions_more import MORE
C.update(MORE)
for k,v in C.items():
    v['youtube_description']=v['youtube_description'].replace('{ID}',k)
    assert len(v['x'])<=280 and len(v['threads'])<=500 and v['threads'].endswith('?') and len(v['youtube_title'])<=100 and len(v['tiktok'])<=300
    assert 'wa.me' not in v['tiktok']+v['x']
    json.dump(v,open(f'{k}/captions.json','w'),ensure_ascii=False,indent=1)
    open(f'{k}/captions.md','w').write('\n\n'.join(f'## {a}\n{b}' for a,b in v.items()))
print('ok')

# ---- WRITING_SPEC CHECK (mandatory) ----
from copy_spec import C as SPEC, build
from spec import check
_bad=0
for _k in SPEC:
    for _p in ('tiktok','instagram','threads','pinterest','youtube','twitter'):
        if _p=='twitter' and 'x' not in SPEC[_k]: continue
        if _p in ('tiktok','instagram','threads','youtube') and 'hook' not in SPEC[_k] and 'tt' not in SPEC[_k]: continue
        if _p in ('instagram','threads','youtube') and 'hook' not in SPEC[_k]: continue
        _t=SPEC[_k]['x'] if _p=='twitter' else build(_k,_p)
        _ti=SPEC[_k].get('pin_title') if _p=='pinterest' else SPEC[_k].get('yt_title') if _p=='youtube' else None
        _f=check(_p,_t,_k,title=_ti)
        if _f: _bad+=1; print('CHECK FAIL',_k,_p,_f)
print('CHECK:', 'all pass' if not _bad else f'{_bad} failing -> these must go to Buffer as DRAFT')

# ---- spec copy overrides the legacy text above (copy_spec.py is the source of truth) ----
import json as _j, os as _os
_MAP={'instagram':'ig_reel','instagram_carousel':'ig_carousel','youtube':'youtube_description','pinterest':'pinterest_description','twitter':'x'}
for _k in SPEC:
    _f=f'{_k}/captions.json'
    if not _os.path.exists(_f): continue
    _c=_j.load(open(_f))
    for _p in ('tiktok','instagram','threads','pinterest','youtube'):
        if _p in ('instagram','threads','youtube') and 'hook' not in SPEC[_k]: continue
        _c[_MAP.get(_p,_p)]=build(_k,_p)
    if 'car_hook' in SPEC[_k]: _c['ig_carousel']=build(_k,'instagram',True)
    if 'x' in SPEC[_k]: _c['x']=SPEC[_k]['x']
    _c['pinterest_title']=SPEC[_k]['pin_title']
    if 'yt_title' in SPEC[_k]: _c['youtube_title']=SPEC[_k]['yt_title']
    _j.dump(_c,open(_f,'w'),ensure_ascii=False,indent=1)
