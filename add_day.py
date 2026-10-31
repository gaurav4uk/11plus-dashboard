"""Add a day to the dashboard.  Example:
python add_day.py --week 3 --day mon --subject "Maths" --score 12 --max 14 --minutes 9 --photo scan.jpg \
  --wrong "5 | 10 - 6.25 | 4.75 | 3.75 | Fractions & decimals"
Days: mon tue wed thu fri wkd.  Then: git add . && git commit -m "Week 3 Mon" && git push"""
import argparse, json, os
from PIL import Image, ImageOps
a=argparse.ArgumentParser()
for n in ["week","day","subject","score","max"]: a.add_argument("--"+n,required=True)
a.add_argument("--minutes"); a.add_argument("--photo"); a.add_argument("--wrong",action="append",default=[])
x=a.parse_args(); id=f"w{x.week}-{x.day}"; p=f"assets/scans/week{x.week}/{x.day}.jpg"
if x.photo:
    os.makedirs(os.path.dirname(p),exist_ok=True); im=ImageOps.exif_transpose(Image.open(x.photo)).convert("RGB"); im.thumbnail((1000,1400)); im.save(p,quality=72)
rows=[r for r in json.load(open("data/records.json")) if r["id"]!=id]
wr=[[int(q) if q.strip().isdigit() else q.strip() for q in [s.split("|")[0]]]+[t.strip() for t in s.split("|")[1:]] for s in x.wrong]
rows.append(dict(id=id,w=int(x.week),k=x.day,s=x.subject,sc=int(x.score),mx=int(x.max),t=int(x.minutes) if x.minutes else None,wr=[[w[0][0]]+w[1:] for w in wr],img=p))
json.dump(rows,open("data/records.json","w"),indent=1,ensure_ascii=False); print("Added",id)
