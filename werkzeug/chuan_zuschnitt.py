from PIL import Image, ImageFilter
im=Image.open("C:/AI-Assistent/thai-massage/eigene-fotos/chuan-original.jpg").convert("RGB")
# Retusche: Blattspitze (Deko) ueber Dachholz kopieren aus darunterliegendem Holz
dst=(398,50,540,92); src=(398,96,540,138)
patch=im.crop(src)
mask=Image.new("L",patch.size,255).filter(ImageFilter.GaussianBlur(0))
m=Image.new("L",patch.size,0)
from PIL import ImageDraw
d=ImageDraw.Draw(m); d.rectangle((6,6,patch.size[0]-6,patch.size[1]-6),fill=255); m=m.filter(ImageFilter.GaussianBlur(5))
im.paste(patch,dst[:2],m)
p2=im.crop((398,106,452,156)); m2=Image.new("L",p2.size,255).filter(ImageFilter.GaussianBlur(0)); mm=Image.new("L",p2.size,0); ImageDraw.Draw(mm).rectangle((0,0,p2.size[0]-8,p2.size[1]-8),fill=255); im.paste(p2,(398,48),mm.filter(ImageFilter.GaussianBlur(4)))
c=im.crop((400,50,995,50+744))

import numpy as np
# --- Schritt 2 (27.11.): Stirnfleck entfernen, Farben kraeftiger ---
# Fleck im Zuschnitt bei ca. (264,237). Ersatz: Haut knapp darueber, auf Ringfarbe angeglichen, weiche Maske.
def stirn_retusche(c, cx=264, cy=237, r=11, dy=-30, dx=-6):
    a=np.asarray(c).astype(np.float32)
    H,W=a.shape[:2]
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
    d=np.hypot(xx-cx,yy-cy)
    ring=(d>r+3)&(d<r+9)
    src=np.roll(a,(-dy,-dx),axis=(0,1))              # Pixel von (y+dy, x+dx) nach (y,x)
    off=a[ring].mean(0)-src[ring].mean(0)
    fill=src+off
    m=np.clip(1-(d-r)/5.0,0,1)                       # voll bis r, weich bis r+5
    m=(m*m*(3-2*m))[...,None]
    return Image.fromarray(np.clip(a*(1-m)+fill*m,0,255).astype(np.uint8))

def farben(c, sat_blau=1.55, sat_gruen=1.70, hell_gruen=1.07, kontrast=1.06):
    # Fassung 2 (27.11.): Gruen/Blau deutlich kraeftiger, Gruen heller, Haut und Lichter geschuetzt
    hsv=np.asarray(c.convert('HSV')).astype(np.float32)   # H 0..255 = 0..360 Grad
    h=hsv[...,0]*360/255
    def band(lo,hi,f=15):                              # weicher Hue-Bereich
        return np.clip(np.minimum(h-lo,hi-h)/f+0.5,0,1)
    bg=band(65,170); bb=band(175,265)
    gain=1+(sat_gruen-1)*bg+(sat_blau-1)*bb
    hsv[...,1]=np.clip(hsv[...,1]*gain,0,255)
    hsv[...,2]=np.clip(hsv[...,2]*(1+(hell_gruen-1)*bg*np.clip(hsv[...,1]/90,0,1)),0,255)   # nur satte Gruentoene heller
    out=np.asarray(Image.fromarray(hsv.astype(np.uint8),'HSV').convert('RGB')).astype(np.float32)
    lum=out.mean(2,keepdims=True)
    skin=np.clip((50-np.where(h>300,360-h,h))/15+0.5,0,1)[...,None]*np.clip(hsv[...,1:2]/40,0,1)
    k=1+(kontrast-1)*(1-skin)*np.clip((250-lum)/50,0,1)   # keine Wirkung auf Haut und fast weisse Lichter
    out=128+(out-128)*k
    return Image.fromarray(np.clip(out,0,255).astype(np.uint8))

c=farben(stirn_retusche(c))


for w in (640,1200):
    c.resize((w,round(w*5/4)),Image.LANCZOS).save(f"C:/AI-Assistent/thai-massage/bilder/chuan-{w}.webp","WEBP",quality=82,method=6)
