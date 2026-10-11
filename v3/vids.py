import sys
src=open('/workspace/elveskiss/v2/video.py').read().split('job=sys.argv[1]')[0]
src=src.replace("def render(out,segs,texts,end_sub,dur_end=2.2,xf=0.5):","def render(out,segs,texts,end_sub,dur_end=2.2,xf=0.5,vf='null'):")
src=src.replace("'-map','0:v','-map','[a]',","'-map','0:v','-map','[a]','-vf',vf,'-ar','48000',")
exec(src)
FB=font('Montserrat[wght].ttf',78,800); FBs=font('Montserrat[wght].ttf',58,700)
S2='/workspace/elveskiss/v2/src2/'; O='/workspace/elveskiss/v3/'
A=S+'Z03004_'; G=S2+'Z01008_'
GRADE='eq=contrast=0.95:saturation=0.9:gamma=1.03,colorbalance=rs=0.03:gs=0.0:bs=0.02:rh=0.02'
job=sys.argv[1]
def tt(segs,texts,out,sub): render(out,segs,texts,sub,dur_end=1.3,xf=0.12)
if job=='q09_tiktok':
    segs=[(prep(A+'IMGP4900.jpg',0.42,0.5),1.7,1.25,1.45,0,0),(prep(A+'z003.jpg',0.5,0.5),1.5,1.1,1.3,0,0),(prep(A+'IMGP4900.jpg',0.3,0.4),1.5,1.9,2.2,0,0),
          (prep(A+'z005.jpg',0.45,0.4),1.5,1.3,1.1,0,0),(prep(A+'z005.jpg',0.6,0.5),1.5,1.2,1.0,0,0),(prep(A+'IMGP1307.jpg',0.3,0.5),1.5,1.0,1.2,0,0),(prep(A+'z003.jpg',0.5,0.5),1.6,1.6,1.9,0,0)]
    tt(segs,[(0,1.6,'Is this REAL\namethyst?',300,FB),(1.6,3.1,'Look at the bands',1450,FBs),(3.1,4.6,'Natural inclusions up close',1450,FBs),
       (4.6,6.1,'Hand-polished Brazilian dream amethyst',1450,FBs),(6.1,7.6,'6 to 30 cm, stand included',1450,FBs),(7.6,9.7,'Real or fake?\nComment below',1380,FB)],O+'q09/tiktok.mp4','dream amethyst sphere')
elif job=='q05_tiktok':
    segs=[(prep_vid(S2+'gar.mp4',1.2,1.8,top=0.08),1.7,1.0,1.08,0,0),(prep(G+'__IMG7617.jpg',0.55,0.5),1.5,1.3,1.5,0,0),(prep_vid(S2+'gar.mp4',4.0,1.6,top=0.08),1.5,1.0,1.08,0,0),
          (prep(G+'__IMG7610.jpg',0.45,0.5),1.5,1.2,1.4,0,0),(prep_vid(S2+'gar.mp4',13.0,1.6,top=0.08),1.5,1.0,1.08,0,0),(prep(G+'_unnamed.jpg',0.5,0.6),1.5,1.0,1.15,0,0),(prep(G+'__IMG7609.jpg',0.5,0.5),1.6,1.2,1.4,0,0)]
    tt(segs,[(0,1.6,'Would you wear\nRAW garnet?',300,FB),(1.6,3.1,'Natural fracture faces',1450,FBs),(3.1,4.6,'Rinsed in spring water',1450,FBs),
       (4.6,6.1,'No dye. No resin.',1450,FBs),(6.1,7.6,'Raw Brazilian garnet',1450,FBs),(7.6,9.7,'Everyday or special?\nTell us below',1380,FB)],O+'q05/tiktok.mp4','raw garnet bracelet')
elif job=='q09_reel':
    segs=[(prep(A+'IMGP1307.jpg',0.3,0.5),3.4,1.0,1.12,0,0),(prep(A+'z003.jpg',0.5,0.5),3.0,1.12,1.0,0,0),(prep(A+'IMGP4900.jpg',0.42,0.5),3.0,1.2,1.4,0,0),(prep(A+'z005.jpg',0.6,0.5),2.8,1.05,1.2,0,0)]
    render(O+'q09/ig_reel.mp4',segs,[(0.2,3.0,'Is this real\namethyst?',300,FT),(3.4,6.0,'Natural bands, hand-polished',1500,FC),(6.4,9.2,'Every sphere is one of a kind',1500,FC)],'dream amethyst sphere · Brazil',dur_end=2.2,xf=0.7,vf=GRADE)
elif job=='q05_reel':
    segs=[(prep_vid(S2+'gar.mp4',13.0,3.5,top=0.08),3.4,1.0,1.06,0,0),(prep(G+'__IMG7617.jpg',0.55,0.5),3.0,1.1,1.25,0,0),(prep_vid(S2+'gar.mp4',1.0,3.1,top=0.08),3.0,1.0,1.06,0,0),(prep(G+'__IMG7609.jpg',0.5,0.5),2.8,1.15,1.0,0,0)]
    render(O+'q05/ig_reel.mp4',segs,[(0.2,3.0,'Wine-red,\nrough and real',300,FT),(3.4,6.0,'Raw Brazilian garnet, natural fracture faces',1500,FC),(6.4,9.2,'Rinsed in spring water. No dye, no resin.',1500,FC)],'raw garnet bracelet · Brazil',dur_end=2.2,xf=0.7,vf=GRADE)
elif job=='q09_yt':
    segs=[(prep(A+'IMGP4900.jpg',0.42,0.5),3.2,1.2,1.35,0,0),(prep(A+'z003.jpg',0.5,0.5),3.2,1.0,1.2,0,0),(prep(A+'z003.jpg',0.5,0.45),3.0,1.5,1.8,0,0),
          (prep(A+'IMGP4900.jpg',0.3,0.4),3.0,1.8,2.1,0,0),(prep(A+'z005.jpg',0.55,0.5),3.0,1.0,1.15,0,0),(prep(A+'IMGP1307.jpg',0.3,0.5),3.2,1.0,1.15,0,0)]
    render(O+'q09/youtube.mp4',segs,[(0,2.8,'How to tell\nreal amethyst',300,FT),(2.8,5.6,'Check 1: natural purple and white banding',1450,FC),(5.6,8.4,'Dream amethyst bands formed in the stone, then hand-polished',1450,FC),
       (8.4,11.1,'Check 2: tiny natural inclusions you only see up close',1450,FC),(11.1,13.8,'Check 3: ask for a certificate. Ours is available on request',1450,FC),(13.8,16.0,'Brazilian dream amethyst, 6 to 30 cm, stand included',1450,FC)],'dream amethyst sphere · Brazil',dur_end=2.4,xf=0.5)
elif job=='q05_yt':
    segs=[(prep(G+'__IMG7617.jpg',0.55,0.5),3.2,1.2,1.35,0,0),(prep(G+'__IMG7610.jpg',0.45,0.5),3.0,1.3,1.5,0,0),(prep_vid(S2+'gar.mp4',1.0,3.2,top=0.08),3.0,1.0,1.06,0,0),
          (prep_vid(S2+'gar.mp4',4.2,3.2,top=0.08),3.0,1.0,1.06,0,0),(prep_vid(S2+'gar.mp4',13.0,3.2,top=0.08),3.0,1.0,1.06,0,0),(prep(G+'_unnamed.jpg',0.5,0.6),3.2,1.0,1.15,0,0)]
    render(O+'q05/youtube.mp4',segs,[(0,2.8,'What to look for\nin raw garnet',300,FT),(2.8,5.6,'Raw chips keep their natural fracture faces',1450,FC),(5.6,8.4,'The wine-red shifts from chip to chip',1450,FC),
       (8.4,11.1,'Ours: no dye, no resin, nothing filled in',1450,FC),(11.1,13.8,'Every strand is rinsed in spring water before it ships',1450,FC),(13.8,16.0,'Raw Brazilian garnet, about 0.8 x 1.5 cm per chip',1450,FC)],'raw garnet bracelet · Brazil',dur_end=2.4,xf=0.5)

Q8=S2+'Z02001__'; R=S2+'Z01007___'
VOG=lambda st,d:prep_vid(S2+'vog.mp4',st,d,top=0.0)
if job=='q08_tiktok':
    segs=[(VOG(0.3,1.8),1.7,1.0,1.08,0,0),(prep(Q8+'IMGP0645.jpg',0.4,0.5),1.5,1.3,1.5,0,0),(prep(Q8+'IMGP0634.jpg',0.5,0.5),1.5,1.1,1.3,0,0),
          (VOG(2.3,1.6),1.5,1.0,1.06,0,0),(prep(Q8+'IMGP0647.jpg',0.5,0.5),1.5,1.2,1.0,0,0),(prep(Q8+'IMGP0630.jpg',0.5,0.5),1.5,1.0,1.2,0,0),(VOG(4.4,1.8),1.6,1.0,1.08,0,0)]
    tt(segs,[(0,1.6,'Can you count\nthe facets?',300,FB),(1.6,3.1,'12 facets',1450,FB),(3.1,4.6,'Clear quartz point',1450,FBs),
       (4.6,6.1,'Brass cap and tip',1450,FBs),(6.1,7.6,'About 1.5 x 6 cm',1450,FBs),(7.6,9.7,'Pendant or pendulum?\nTell us below',1380,FB)],O+'q08/tiktok.mp4','Vogel-style quartz pendant')
elif job=='q08_reel':
    segs=[(VOG(0.3,3.5),3.4,1.0,1.06,0,0),(prep(Q8+'IMGP0634.jpg',0.5,0.5),3.0,1.1,1.25,0,0),(prep(Q8+'IMGP0645.jpg',0.4,0.5),3.0,1.2,1.05,0,0),(prep(Q8+'IMGP0630.jpg',0.5,0.5),2.8,1.0,1.15,0,0)]
    render(O+'q08/ig_reel.mp4',segs,[(0.2,3.0,'12 facets.\nWatch it catch light',300,FT),(3.4,6.0,'Clear quartz point, brass fittings',1500,FC),(6.4,9.2,'Wear it, or hang it by a window',1500,FC)],'Vogel-style quartz pendant',dur_end=2.2,xf=0.7,vf=GRADE)
elif job=='q08_yt':
    segs=[(VOG(0.3,3.3),3.2,1.0,1.06,0,0),(prep(Q8+'IMGP0645.jpg',0.4,0.5),3.0,1.3,1.5,0,0),(prep(Q8+'IMGP0634.jpg',0.5,0.5),3.0,1.1,1.3,0,0),
          (prep(Q8+'IMGP0647.jpg',0.5,0.5),3.0,1.2,1.0,0,0),(VOG(3.0,3.2),3.0,1.0,1.06,0,0),(prep(Q8+'IMGP0607.jpg',0.5,0.6),3.2,1.0,1.15,0,0)]
    render(O+'q08/youtube.mp4',segs,[(0,2.8,'What is a\nVogel-style crystal?',300,FT),(2.8,5.6,'A clear quartz point cut with 12 facets',1450,FC),(5.6,8.4,'Light passes straight through the quartz body',1450,FC),
       (8.4,11.1,'Brass cap and tip let it hang straight',1450,FC),(11.1,13.8,'Wear it as a pendant, or use it as a pendulum',1450,FC),(13.8,16.0,'About 1.5 x 6 cm',1450,FC)],'Vogel-style quartz pendant',dur_end=2.4,xf=0.5)
elif job=='q02_tiktok':
    segs=[(prep(R+'IMG7709.jpg',0.55,0.6),1.7,1.3,1.5,0,0),(prep(R+'IMG8622.jpg',0.5,0.5),1.5,1.1,1.3,0,0),(prep(R+'IMG7706.jpg',0.5,0.5),1.5,1.2,1.0,0,0),
          (prep(R+'IMG9815.jpg',0.5,0.5),1.5,1.0,1.2,0,0),(prep(R+'IMG8624.jpg',0.5,0.5),1.5,1.2,1.0,0,0),(prep(R+'IMG9817.jpg',0.5,0.5),1.5,1.0,1.2,0,0),(prep(R+'IMG7709.jpg',0.5,0.5),1.6,1.0,1.2,0,0)]
    tt(segs,[(0,1.6,'Raw or polished\ncrystal?',300,FB),(1.6,3.1,'Unpolished nuggets',1450,FBs),(3.1,4.6,'No dye. No enhancement.',1450,FBs),
       (4.6,6.1,'About 1-2 cm each',1450,FBs),(6.1,7.6,'No two strands alike',1450,FBs),(7.6,9.7,'Raw or polished?\nVote below',1380,FB)],O+'q02/tiktok.mp4','rock candy raw crystal bracelet')
elif job=='q02_reel':
    segs=[(prep(R+'IMG8624.jpg',0.5,0.5),3.4,1.0,1.12,0,0),(prep(R+'IMG7709.jpg',0.55,0.6),3.0,1.12,1.0,0,0),(prep(R+'IMG8622.jpg',0.5,0.5),3.0,1.2,1.4,0,0),(prep(R+'IMG9817.jpg',0.5,0.5),2.8,1.05,1.2,0,0)]
    render(O+'q02/ig_reel.mp4',segs,[(0.2,3.0,'Raw crystal,\nexactly as found',300,FT),(3.4,6.0,'Raw nuggets, no dye',1500,FC),(6.4,9.2,'Every strand a little different',1500,FC)],'rock candy raw crystal bracelet',dur_end=2.2,xf=0.7,vf=GRADE)
elif job=='q02_yt':
    segs=[(prep(R+'IMG7709.jpg',0.55,0.6),3.2,1.2,1.35,0,0),(prep(R+'IMG7706.jpg',0.5,0.5),3.0,1.0,1.2,0,0),(prep(R+'IMG8622.jpg',0.5,0.5),3.0,1.3,1.5,0,0),
          (prep(R+'IMG9815.jpg',0.5,0.5),3.0,1.0,1.2,0,0),(prep(R+'IMG8624.jpg',0.5,0.5),3.0,1.15,1.0,0,0),(prep(R+'IMG9817.jpg',0.5,0.5),3.2,1.0,1.15,0,0)]
    render(O+'q02/youtube.mp4',segs,[(0,2.8,'Raw crystal:\nwhat to look for',300,FT),(2.8,5.6,'Unpolished nuggets keep their rough natural texture',1450,FC),(5.6,8.4,'The pink is the stone itself: no dye',1450,FC),
       (8.4,11.1,'Color shifts a little from nugget to nugget',1450,FC),(11.1,13.8,'Each nugget is about 1 to 2 cm',1450,FC),(13.8,16.0,'So no two strands come out alike',1450,FC)],'rock candy raw crystal bracelet',dur_end=2.4,xf=0.5)
