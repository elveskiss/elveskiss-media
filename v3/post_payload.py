"""Build a Buffer create_post payload for one item/platform and run the WRITING_SPEC CHECK.
Usage: python3 post_payload.py <qid> <platform> <dueAt ISO> <media_url> [--carousel url1,url2,...]
Platforms: tiktok instagram threads twitter pinterest youtube
If ANY check fails the payload gets saveToDraft=true (Buffer draft, NOT the queue)
and the failures are printed. Never hand-edit a failing post into the queue."""
import sys,json,re
from spec import check,FACTS,L
from copy_spec import C,build
CH={'instagram':'6ac6093d6a5c39ccb63ddf10','tiktok':'6ac60a9c6a5c39ccb63df0eb','pinterest':'6ac99cae6a5c39ccb66b1b64',
    'twitter':'6acaf2d6778b240e2fd144bd','threads':'6acaf250778b240e2fd140e6','youtube':'6acaf2fb778b240e2fd145bb'}
BOARD='1061512643359051642'
def payload(k,plat,due,media,carousel=None):
    is_video=media.endswith('.mp4')
    fails=[]
    if k not in FACTS or k not in C: fails.append('MISSING INFO: '+k)
    if plat=='youtube' and not is_video: return None,['YOUTUBE: SKIP (photo)']
    text=(C[k].get('x') if plat=='twitter' else build(k,plat,bool(carousel))) if k in C else ''
    if plat=='twitter' and not text: fails.append('no X text in copy_spec')
    title=C.get(k,{}).get('pin_title') if plat=='pinterest' else C.get(k,{}).get('yt_title') if plat=='youtube' else None
    fails+=check(plat,text or '',k,title=title,is_video=is_video,url=L+'#'+k if plat=='pinterest' else None)
    urls=carousel or [media]
    assets=[{'video':{'url':u}} if u.endswith('.mp4') else {'image':{'url':u}} for u in urls]
    p={'channelId':CH[plat],'schedulingType':'automatic','mode':'customScheduled','dueAt':due,'text':text,'assets':assets}
    if plat=='pinterest': p['metadata']={'pinterest':{'title':title,'url':L+'#'+k,'boardServiceId':BOARD}}
    if plat=='youtube': p['metadata']={'youtube':{'title':title,'categoryId':'26','privacy':'public','license':'youtube','notifySubscribers':True,'madeForKids':False,'embeddable':True}}
    if plat=='tiktok': p['metadata']={'tiktok':{'title':C[k].get('tt_title') or re.split(r"[^\w\s'?,-]",C[k]['tt'])[0].strip()}}
    if plat=='instagram': p['metadata']={'instagram':{'type':'post' if carousel else 'reel','shouldShareToFeed':True}}
    if fails: p['saveToDraft']=True; p.pop('mode'); p.pop('dueAt')
    return p,fails
def check_block(k,plat,fails,is_video):
    code,name,form,size,origin=FACTS.get(k,(None,)*5)
    f=lambda pre:[x for x in fails if x.startswith(pre)]
    return '\n'.join(['CHECK',f'- Stone name matches input: {"no" if f("name") or f("MISSING") else "yes"}',
      f'- Size matches input: {"no" if f("size") else "yes"}',f'- Banned words found: {",".join(f("banned")) or "none"}',
      f'- TikTok contains contact info: {"yes" if f("tiktok contact") else "no"}',f'- YouTube file is video: {"yes" if is_video else "skip"}',
      f'- Other: {", ".join(x for x in fails if not x.startswith(("name","size","banned","tiktok contact"))) or "none"}'])
if __name__=='__main__':
    a=sys.argv[1:]; car=None
    if '--carousel' in a: i=a.index('--carousel'); car=a[i+1].split(','); a=a[:i]
    k,plat,due,media=a
    p,f=payload(k,plat,due,media,car)
    print(check_block(k,plat,f,media.endswith('.mp4')))
    print('RESULT:', 'DRAFT (saveToDraft)' if f else 'QUEUE')
    print(json.dumps(p,ensure_ascii=False,indent=1))
    sys.exit(1 if f else 0)
