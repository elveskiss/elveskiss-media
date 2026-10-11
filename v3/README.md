# v3 platform-native recipe (Elves Kiss)

One item → 6 platform variants. Output in `/workspace/elveskiss/v3/<id>/`, pushed to `elveskiss/elveskiss-media` under `posts/v3/<id>/`.

## Sources
- Product photos: `/workspace/elveskiss/v2/src*/<SKU>_*.jpg` (model photos are real and may be used).
- Real footage from 天猫视频 when it exists (`v2/src2/*.mp4`, crop top ~8–20% to drop watermarks/Chinese text).
- Facts only from the product files / `海外发布规范.md`. Write only what the files support (no invented events like "polished one today").

## Variants and scripts
| Platform | File | Spec | Script |
|---|---|---|---|
| TikTok | `tiktok.mp4` | 9:16, ~11 s, question hook on screen at 0 s, a cut every ~1.5 s, bold Montserrat captions, ends on a question, end card = logo + product name only | `vids.py <id>_tiktok` |
| IG Reel | `ig_reel.mp4` | 9:16, ~11.6 s, 4 slow shots, 0.7 s crossfades, soft grade (`GRADE` eq/colorbalance) | `vids.py <id>_reel` |
| IG carousel | `ig_carousel_1..6.jpg` | 1080×1350, 小红书 style: cover hook → 3 numbered checks → details → "Save this" + "DM us for sizes" | `imgs.py <id>` (`cover/edu/cta`) |
| YouTube Short | `youtube.mp4` | 9:16, ~18 s, explanatory subtitles; title with search keyword + `#Shorts` | `vids.py <id>_yt` |
| Pinterest | `pinterest.jpg` | 1000×1500, "Name \| Idea" keyword overlay at top, home/decor shot | `imgs.py` (`pin`) |
| X | `x.jpg` | 1080×1350 striking close-up + one-line factory-diary text | `imgs.py` (`plain`) |
| Threads | `threads.jpg` | lifestyle shot (in hand / room / model) + conversational text ending in a question | `imgs.py` (`plain`) |

To add an item: add a block to `imgs.py` (guarded by `if not ONLY or '<id>' in ONLY`), three `elif job=='<id>_…'` blocks to `vids.py`, captions to `captions_more.py`, then:
```
python3 imgs.py <id>; for j in tiktok reel yt; do python3 vids.py <id>_$j; done
python3 captions.py; python3 sheet.py <id>     # -> sheet_<id>.jpg
```
Audio: 48 kHz AAC, music ≈ −19 LUFS (check `ffmpeg -af ebur128`). Check every output visually (contact sheet + frame strips), including the TikTok end card.

## Contact policy (2026-10-11)
- TikTok: NO contact anywhere (caption, on-screen text, subtitles, end card): no WhatsApp, wa.me, DM, message us, buy, order, PayPal, link in bio.
- Instagram / Threads: no WhatsApp; CTA "DM us for sizes ✨" / "DM us for details ✨".
- X: "DMs open".
- YouTube: description links the landing page (URL pending; until then "Questions? DM us on Instagram ✨", no wa.me).
- Pinterest: pin link → landing page (pending; currently wa.me), WhatsApp may be mentioned.
`captions.py` asserts the TikTok/X rules.

## Hosting
Copy outputs to `elveskiss-media/posts/v3/<id>/`, commit, push. Videos via jsDelivr `https://cdn.jsdelivr.net/gh/elveskiss/elveskiss-media@main/posts/v3/<id>/<file>.mp4` (must return `video/mp4` + content-length); images via `https://raw.githubusercontent.com/elveskiss/elveskiss-media/main/posts/v3/<id>/<file>.jpg`. Re-rendered videos get a new filename (jsDelivr caches).

## Scheduling (Buffer, org 6ac608956ed4410ab01b37f2)
Slots 08:15 and 21:15 (UTC+8). Per slot, same dueAt on every channel:
| Channel | channelId | Post |
|---|---|---|
| TikTok | 6ac60a9c6a5c39ccb63df0eb | `tiktok.mp4`, text=tiktok caption, `metadata.tiktok.title` |
| Instagram | 6ac6093d6a5c39ccb63ddf10 | `ig_reel.mp4`, `metadata.instagram {type:"reel", shouldShareToFeed:true}` |
| Instagram carousel | same | 6 images, `type:"post"`, dueAt = slot + 3 h (supported; tested 2026-10-11 as a draft) |
| YouTube | 6acaf2fb778b240e2fd145bb | `youtube.mp4`, `metadata.youtube {title, categoryId:"26"}` |
| Pinterest | 6ac99cae6a5c39ccb66b1b64 | `pinterest.jpg`, `metadata.pinterest {title, url, boardServiceId:"1061512643359051642"}`; max 5 pins/day |
| X | 6acaf2d6778b240e2fd144bd | `x.jpg` + X text |
| Threads | 6acaf250778b240e2fd140e6 | `threads.jpg` + Threads text |
Before creating, `list_posts` for that dueAt to avoid duplicates; prefer `edit_post` on an existing post (send the full assets + required metadata; edits are validated as whole posts). Record post ids in `queue.json` → `<item>.v3` / `buffer_post_ids`.
