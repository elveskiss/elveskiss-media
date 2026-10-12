import sys; sys.path.insert(0,'/workspace/elveskiss')
from PIL import Image,ImageOps,ImageDraw,ImageFilter,ImageEnhance
import ek_style as E
S='/workspace/elveskiss/v2/src/'; S2='/workspace/elveskiss/v2/src2/'
F=lambda n,s,w=500:E.font(n,s,w)
SERIF='CormorantGaramond[wght].ttf'; SANS='Montserrat[wght].ttf'; HAND='Caveat.ttf'
CREAM=(246,241,234); INK=(52,40,58); PLUM=(108,78,150)
def load(f): return ImageOps.exif_transpose(Image.open(f)).convert('RGB')
def fit(im,W,H,cx=.5,cy=.5,zoom=1.0):
    w,h=im.size; s=max(W/w,H/h)*zoom; im=im.resize((int(w*s)+1,int(h*s)+1),Image.LANCZOS)
    x=int((im.width-W)*cx); y=int((im.height-H)*cy); return im.crop((x,y,x+W,y+H))
def wrap(d,t,f,mw):
    out=[];l=''
    for w in t.split():
        c=(l+' '+w).strip()
        if d.textlength(c,font=f)>mw and l: out.append(l); l=w
        else: l=c
    out.append(l); return '\n'.join(out)
def grad(img,y0,y1,a0,a1,col=(20,14,28)):
    W,H=img.size; m=Image.new('L',(W,H),0); d=ImageDraw.Draw(m)
    for y in range(max(0,y0),min(H,y1)): d.line([(0,y),(W,y)],fill=int(a0+(a1-a0)*(y-y0)/max(1,y1-y0)))
    ov=Image.new('RGBA',(W,H),col+(0,)); ov.putalpha(m); return Image.alpha_composite(img.convert('RGBA'),ov)
def soft(im): # consistent soft grade
    im=ImageEnhance.Contrast(im).enhance(0.94); im=ImageEnhance.Color(im).enhance(0.95)
    return Image.blend(im,Image.new('RGB',im.size,(250,240,236)),0.06)
def logo(img,y=46,w=220):
    lg=E.logo(w); img.alpha_composite(lg,((img.width-lg.width)//2,y)); return img
def cover(src,title,sub,out,cx=.5,cy=.5,zoom=1.0):
    W,H=1080,1350; img=soft(fit(load(src),W,H,cx,cy,zoom)).convert('RGBA')
    img=grad(img,0,560,190,0); img=grad(img,H-330,H,0,170); img=logo(img)
    d=ImageDraw.Draw(img); f=F(SERIF,112,600); t=wrap(d,title,f,W-140)
    d.multiline_text((W/2,150),t,font=f,fill='white',anchor='ma',align='center',spacing=6)
    d.text((W/2,H-120),sub,font=F(HAND,56),fill=(255,255,255,235),anchor='mm')
    d.text((W-60,H-50),'1/6  swipe →',font=F(SANS,28,500),fill=(255,255,255,200),anchor='rm')
    img.convert('RGB').save(out,quality=93)
def edu(src,n,head,body,out,cx=.5,cy=.5,zoom=1.0,page='',tag=''):
    W,H=1080,1350; img=Image.new('RGBA',(W,H),CREAM+(255,))
    ph=soft(fit(load(src),W-120,760,cx,cy,zoom)); m=Image.new('L',ph.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0)+ph.size,radius=36,fill=255)
    img.paste(ph,(60,60),m); d=ImageDraw.Draw(img)
    if n: 
        d.ellipse((60,870,150,960),fill=PLUM); d.text((105,915),str(n),font=F(SANS,48,700),fill='white',anchor='mm')
    f=F(SERIF,70,700); d.multiline_text((170 if n else 60,872),wrap(d,head,f,W-(230 if n else 120)),font=f,fill=INK,spacing=2)
    fb=F(SANS,36,400); d.multiline_text((60,1060),wrap(d,body,fb,W-120),font=fb,fill=(80,70,86),spacing=14)
    if tag: d.text((60,H-60),tag,font=F(HAND,44),fill=PLUM,anchor='lm')
    d.text((W-60,H-60),page,font=F(SANS,28,500),fill=(140,130,146),anchor='rm')
    img.convert('RGB').save(out,quality=93)
def cta(src,lines,out):
    W,H=1080,1350; bg=soft(fit(load(src),W,H)).filter(ImageFilter.GaussianBlur(28)).convert('RGBA')
    bg=Image.alpha_composite(bg,Image.new('RGBA',(W,H),(40,28,56,150))); bg=logo(bg,120,420); d=ImageDraw.Draw(bg)
    d.text((W/2,420),'Save this',font=F(SERIF,140,600),fill='white',anchor='mm')
    d.text((W/2,540),'for your next crystal hunt',font=F(HAND,70),fill=(255,255,255,235),anchor='mm')
    y=700
    for l in lines: d.text((W/2,y),l,font=F(SANS,40,500),fill=(255,255,255,230),anchor='mm'); y+=80
    d.rounded_rectangle((240,1060,840,1160),radius=50,outline='white',width=3)
    d.text((W/2,1110),'DM us for sizes',font=F(SANS,38,600),fill='white',anchor='mm')
    d.text((W/2,1260),'6/6',font=F(SANS,28,500),fill=(255,255,255,180),anchor='mm')
    bg.convert('RGB').save(out,quality=93)
def pin(src,title,kw,out,cx=.5,cy=.5,zoom=1.0):
    W,H=1000,1500; img=soft(fit(load(src),W,H,cx,cy,zoom)).convert('RGBA'); img=grad(img,0,640,215,0); img=grad(img,H-200,H,0,150)
    d=ImageDraw.Draw(img); name,idea=[t.strip() for t in title.split('|')]
    f=F(SERIF,92,600); t=wrap(d,name,f,W-120)
    d.multiline_text((W/2,90),t,font=f,fill='white',anchor='ma',align='center',spacing=2)
    y=90+d.multiline_textbbox((0,0),t,font=f,spacing=2)[3]+30
    d.text((W/2,y),idea,font=F(HAND,64),fill=(255,255,255,240),anchor='ma')
    d.text((W/2,y+95),kw,font=F(SANS,30,500),fill=(255,255,255,215),anchor='ma')
    lg=E.logo(200); img.alpha_composite(lg,((W-lg.width)//2,H-80)); img.convert('RGB').save(out,quality=93)
def plain(src,out,cx=.5,cy=.5,zoom=1.0,size=(1080,1350),grade=True):
    im=fit(load(src),*size,cx,cy,zoom); im=soft(im) if grade else im
    im=im.convert('RGBA'); lg=E.logo(170); im.alpha_composite(lg,(im.width-lg.width-40,im.height-lg.height-40)); im.convert('RGB').save(out,quality=93)
O='/workspace/elveskiss/v3/'
import sys
ONLY=sys.argv[1:]
if not ONLY or 'q09' in ONLY:
 q=O+'q09/'
 cover(S+'Z03004_IMGP4900.jpg','How to spot real amethyst','3 checks · save for later',q+'ig_carousel_1.jpg',cx=.42,zoom=1.0)
 edu(S+'Z03004_z003.jpg',1,'Look for natural banding','Dream amethyst shows purple and white bands that formed in the stone. Ours are hand-polished to bring them out, never painted on.',q+'ig_carousel_2.jpg',page='2/6')
 edu(S+'Z03004_IMGP4900.jpg',2,'Look closely for inclusions','Real stone carries tiny natural mineral inclusions you only see up close. No two spheres share the same pattern.',q+'ig_carousel_3.jpg',cx=.45,zoom=1.6,page='3/6')
 edu(S+'Z03004_tm.png',3,'Ask where it comes from','A seller who knows their stone can tell you its origin. Ours is dream amethyst from Brazil, hand-polished.',q+'ig_carousel_4.jpg',cy=.35,page='4/6')
 edu(S+'Z03004_z005.jpg',0,'The details','Natural Brazilian dream amethyst · hand-polished · sizes 6–30 cm · stand included. In crystal tradition, amethyst is associated with calm.',q+'ig_carousel_5.jpg',cx=.6,page='5/6',tag='dream amethyst sphere · Brazil')
 cta(S+'Z03004_IMGP4900.jpg',['banding · inclusions · origin','Brazilian dream amethyst, 6–30 cm'],q+'ig_carousel_6.jpg')
 pin(S+'Z03004_IMGP1307.jpg','Dream Amethyst Sphere | Crystal Decor Idea','natural Brazilian amethyst · 6–30 cm',q+'pinterest.jpg',cx=.3,cy=.5)
 plain(S+'Z03004_z003.jpg',q+'x.jpg',cx=.5,zoom=1.15)
 plain(S+'Z03004_IMGP1307.jpg',q+'threads.jpg',cx=.3)
if not ONLY or 'q05' in ONLY:
 q=O+'q05/'
 cover(S2+'Z01008___IMG7617.jpg','Raw garnet: what to look for','3 checks · save for later',q+'ig_carousel_1.jpg',cx=.5)
 edu(S2+'Z01008___IMG7610.jpg',1,'Natural fracture faces','Raw chips keep the faces they broke along. Ours are left untouched, about 0.8 × 1.5 cm each.',q+'ig_carousel_2.jpg',cx=.45,zoom=1.3,page='2/6')
 edu(S2+'Z01008___IMG7617.jpg',2,'Color that shifts','Wine-red that changes from chip to chip. Each one catches the light differently, because none of them were cut to match.',q+'ig_carousel_3.jpg',cx=.6,zoom=1.5,page='3/6')
 edu('/tmp/gar_pour.jpg',3,'No dye, no resin','Nothing filled in or coated. We rinse every strand in the spring water at our courtyard before it ships.',q+'ig_carousel_4.jpg',cy=.45,page='4/6')
 edu(S2+'Z01008___IMG7609.jpg',0,'The details','Raw Brazilian garnet chips · natural fracture faces · no dye, no resin. In crystal tradition, garnet is associated with energy and devotion.',q+'ig_carousel_5.jpg',page='5/6',tag='raw garnet bracelet · Brazil')
 cta(S2+'Z01008___IMG7617.jpg',['fracture faces · shifting color · no dye','raw Brazilian garnet'],q+'ig_carousel_6.jpg')
 pin(S2+'Z01008__IMGP4330.jpg','Raw Garnet Bracelet | Boho Crystal Jewelry Idea','natural Brazilian garnet · no dye, no resin',q+'pinterest.jpg',cy=.4)
 plain(S2+'Z01008___IMG7617.jpg',q+'x.jpg',cx=.55,zoom=1.1)
 plain(S2+'Z01008__unnamed.jpg',q+'threads.jpg',cy=.55)

Q8=S2+'Z02001__'; R=S2+'Z01007___'
if not ONLY or 'q08' in ONLY:
 q=O+'q08/'
 cover(Q8+'IMGP0645.jpg','Vogel-style quartz: what to look for','3 checks · save for later',q+'ig_carousel_1.jpg',cx=.5)
 edu(Q8+'IMGP0645.jpg',1,'Count the facets','A Vogel-style point is cut with 12 facets. Turn it slowly and each face catches the light on its own.',q+'ig_carousel_2.jpg',cx=.4,zoom=1.3,page='2/6')
 edu(Q8+'IMGP0634.jpg',2,'Clear quartz body','The point is natural clear quartz, about 1.5 × 6 cm, so light passes straight through it.',q+'ig_carousel_3.jpg',page='3/6')
 edu(Q8+'IMGP0647.jpg',3,'Brass fittings','Brass cap and tip frame the point, so it hangs straight as a pendant or a pendulum.',q+'ig_carousel_4.jpg',page='4/6')
 edu(Q8+'IMGP0630.jpg',0,'The details','12-facet clear quartz · brass fittings · about 1.5 × 6 cm. In crystal tradition, clear quartz is associated with clarity and focus.',q+'ig_carousel_5.jpg',page='5/6',tag='Vogel-style quartz pendant')
 cta(Q8+'IMGP0634.jpg',['12 facets · clear quartz · brass','about 1.5 × 6 cm'],q+'ig_carousel_6.jpg')
 pin(Q8+'IMGP0607.jpg','Clear Quartz Pendulum | Window Light Decor Idea','12-facet clear quartz · brass fittings',q+'pinterest.jpg',cy=.6)
 plain(Q8+'IMGP0645.jpg',q+'x.jpg',zoom=1.1)
 plain(Q8+'IMGP0630.jpg',q+'threads.jpg')
if not ONLY or 'q02' in ONLY:
 q=O+'q02/'
 cover(R+'IMG7709.jpg','Raw crystal: what to look for','3 checks · save for later',q+'ig_carousel_1.jpg')
 edu(R+'IMG7709.jpg',1,'Rough natural texture','Unpolished nuggets keep the surface they came with. Run a finger over it and you feel the stone.',q+'ig_carousel_2.jpg',zoom=1.2,page='2/6')
 edu(R+'IMG8622.jpg',2,'Soft, natural pink','No dye, no enhancement. The color is the stone itself, a pale pink that changes nugget to nugget.',q+'ig_carousel_3.jpg',zoom=1.4,page='3/6')
 edu(R+'IMG9815.jpg',3,'No two strands alike','Each nugget is about 1–2 cm and shaped by nature, so every strand comes out a little different.',q+'ig_carousel_4.jpg',page='4/6')
 edu(R+'IMG8624.jpg',0,'The details','Rock candy raw crystal · nuggets 1–2 cm · no dye, no enhancement, unpolished.',q+'ig_carousel_5.jpg',page='5/6',tag='rock candy raw crystal bracelet')
 cta(R+'IMG7706.jpg',['rough texture · natural pink · one of a kind','rock candy raw crystal, 1–2 cm'],q+'ig_carousel_6.jpg')
 pin(R+'IMG8624.jpg','Rock Candy Raw Crystal Bracelet | Soft Pink Jewelry Idea','natural crystal · 1–2 cm · no dye',q+'pinterest.jpg')
 plain(R+'IMG7709.jpg',q+'x.jpg',cx=.55,cy=.6,zoom=1.25)
 plain(R+'IMG8624.jpg',q+'threads.jpg')
F11=S2+'Z03015__'; F6=S2+'Z01016__'; V6=S2+'Z01016_f'
if not ONLY or 'q11' in ONLY:
 q=O+'q11/'
 cover(F11+'IMGP4147.jpg','Real fluorite or glass?','3 checks · save for later',q+'ig_carousel_1.jpg',cx=.5)
 edu(S2+'Z03015___IMG1773.jpg',1,'Layered color','Real fluorite grows in layers, so the green deepens and fades as you turn it. It is rarely one flat shade.',q+'ig_carousel_2.jpg',cy=.62,zoom=1.7,page='2/6')
 edu(F11+'z001.jpg',2,'Natural inner patterns','Look closely: veils, lines and feathers inside the stone. No two spheres share the same pattern.',q+'ig_carousel_3.jpg',cy=.7,zoom=1.8,page='3/6')
 edu(F11+'002.jpg',3,'Glass looks too even','Glass copies tend to look perfectly even in color. Fluorite never quite does.',q+'ig_carousel_4.jpg',zoom=1.5,page='4/6')
 edu(F11+'IMGP4513.jpg',0,'The details','Green fluorite sphere · layered greens · natural inner patterns · every sphere one of a kind.',q+'ig_carousel_5.jpg',cy=.75,zoom=1.3,page='5/6',tag='green fluorite sphere')
 cta(F11+'IMGP4147.jpg',['layers · inner patterns · uneven color','green fluorite sphere'],q+'ig_carousel_6.jpg')
 pin(F11+'IMGP4512.jpg','Green Fluorite Sphere | Window Crystal Decor Idea','natural green fluorite · crystal decor',q+'pinterest.jpg')
 plain(F11+'z001.jpg',q+'x.jpg',cy=.72,zoom=1.5)
 plain(F11+'IMGP4513.jpg',q+'threads.jpg',cy=.6)
if not ONLY or 'q06' in ONLY:
 q=O+'q06/'
 cover(F6+'DSC09995.jpg','Clear quartz or glass?','3 checks · save for later',q+'ig_carousel_1.jpg')
 edu(F6+'DSC09997.jpg',1,'Tiny natural inclusions','Real clear quartz usually carries small wisps and lines inside. Hold a bead to the light and look.',q+'ig_carousel_2.jpg',zoom=1.3,page='2/6')
 edu(F6+'DSC09998.jpg',2,'Round bubbles mean glass','Perfectly round air bubbles are a sign of glass. Quartz inclusions look irregular.',q+'ig_carousel_3.jpg',zoom=1.2,page='3/6')
 edu(V6+'28.jpg',3,'Ask what it is called','A seller who knows the stone can name it. Ours is Himalayan clear quartz, rinsed in spring water at our courtyard.',q+'ig_carousel_4.jpg',cy=.55,page='4/6')
 edu(F6+'DSC09996.jpg',0,'The details','Himalayan clear quartz bracelet · round clear beads · easy to stack with colored crystals.',q+'ig_carousel_5.jpg',page='5/6',tag='Himalayan clear quartz')
 cta(F6+'DSC09995.jpg',['inclusions · no round bubbles · a real name','Himalayan clear quartz bracelet'],q+'ig_carousel_6.jpg')
 pin(F6+'DSC09994.jpg','Himalayan Clear Quartz Bracelet | Minimal Crystal Jewelry Idea','natural clear quartz · minimal jewelry',q+'pinterest.jpg',cy=.6)
 plain(F6+'DSC09997.jpg',q+'x.jpg',zoom=1.1)
 plain(V6+'2.jpg',q+'threads.jpg',cy=.6)
print('ok')
