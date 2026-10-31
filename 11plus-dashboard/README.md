# 11+ Progress Dashboard

Static site: marked scans, booklets and a progress dashboard.

## Publish on GitHub Pages
1. Create a new repository (private is fine if your plan supports Pages, otherwise public: it contains your child's work, so consider keeping it private).
2. Upload everything in this folder (index.html and the assets folder).
3. Settings > Pages > Source: Deploy from a branch > main > / (root).
4. Open the Pages URL shown.

## Daily updates (the dashboard reads data/records.json, so it updates itself)
Option 1, command line: `python add_day.py --week 3 --day mon --subject Maths --score 12 --max 14 --minutes 9 --photo scan.jpg`, then `git add . && git commit -m "Week 3 Mon" && git push`.
Option 2, browser: open the dashboard's Add day tab, fill in the marks, copy the JSON line into data/records.json on GitHub, and upload the scan to assets/scans/weekN/ (named mon.jpg, tue.jpg, wed.jpg, thu.jpg, fri.jpg, wkd.jpg).
GitHub Pages rebuilds in about a minute. Put new booklets in assets/booklets/ and list them in the BK array in index.html.
