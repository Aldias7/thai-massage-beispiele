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


for w in (640,1200):
    c.resize((w,round(w*5/4)),Image.LANCZOS).save(f"C:/AI-Assistent/thai-massage/bilder/chuan-{w}.webp","WEBP",quality=82,method=6)
