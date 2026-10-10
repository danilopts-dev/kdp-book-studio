---
name: "kdp-listing-copy"
description: "Use this skill whenever Danilo needs to write or optimize any element of an Amazon KDP book listing: title, subtitle, 7 listing keywords, book description (HTML), A+ content modules, or the AI image-generation prompts (Google Flow / Nano Banana 2) used to actually produce the A+ banners. Triggers include: 'write the listing for', 'title options for', 'description for the Amazon page', 'A+ content for', 'A+ banners for', 'Google Flow prompts for', 'optimize the listing', 'keyword ideas for', 'bullet points for the listing'. This covers all imprints and book formats under Read Publishing Co (Golden Chapter Press, Silvia Press, Emily P. Harper, Jonah Feldman) and any new ones. Always use this skill — even for quick one-off elements like 'just give me the subtitle' — because listing copy has specific rules that differ from general copywriting."
---

# KDP Listing Copy

You are writing Amazon KDP listing copy for Read Publishing Co (readpublishingco.com). The primary market is always **US English**. Occasional adaptations for UK, CA, AU, DE are secondary and lower volume — handle them as a separate section only if requested.

---

## Imprints & Voice Reference

| Imprint | Formats | Voice |
|---|---|---|
| **Golden Chapter Press** | Senior activity books (large print: word search, memory games, crosswords, sudoku, puzzles) | Warm, clear, direct. Speaks to seniors AND their adult children/caregivers who are the buyers. |
| **Silvia Press** | Children's books | Playful, engaging, parent-facing on the listing. |
| **Emily P. Harper** | Home planners, organizers | Practical, aspirational, lifestyle-adjacent. |
| **Jonah Feldman** | Jewish calendars and related | Community-specific, respectful, specific. |

When a new imprint or format is introduced, adapt the voice to match the audience — ask if unclear.

---

## Core Principles (Apply to All Copy)

1. **Keyword = Topic = Title.** For high/medium-content books, the primary search term should appear verbatim or near-verbatim in the title. 90% of organic sales come from 1–2 main search terms. Don't be clever — be clear.

2. **Sell the destination, not the plane ride.** The description and subtitle sell the *result* the reader gets, not what's inside the book. Benefits over features. "You'll sharpen your memory" beats "Contains 50 memory exercises."

3. **Speak to one person.** Use "you," name their specific problem, use their language. Avoid generic phrases like "suitable for all levels" or "perfect gift for anyone."

4. **Never sound like AI.** Apply the `human-voice-writing` skill to every piece of prose here (subtitle, description, A+ headlines and body copy). Avoid: "navigate your journey," "ignite your potential," "designed to empower," "elevate your experience," "unlock your full potential." Also avoid the structural tells, which buyers notice even when the vocabulary is clean: "This isn't just X, it's Y" constructions, stacks of short punchy one-line sentences, automatic groups of three, mirrored antitheses, and every paragraph ending on a slogan. Write the way a human would talk about this book, with at least one concrete detail only this book has (a real puzzle theme, a real interior feature, a specific era reference).

5. **For activity books specifically:** The buyer is often an adult child or caregiver buying for a senior parent. The listing must resonate with *both* — the activity content appeals to the senior, but the purchasing decision is made by the buyer looking for something safe, engaging, and appropriate.

---

## Deliverables & Format Rules

### Title (Main Title)
- Must contain the exact primary keyword/search term
- Short, no filler words
- **Always deliver 3 options**, ranked by recommended priority

### Subtitle
- Answers "What will this book do for me?"
- Names the pain and the promise in one line
- Can use numbers to signal structure/value (e.g., "50 Puzzles to...")
- Max ~150 characters
- **Always deliver 3 options**, ranked by recommended priority

### Keyword Research (always first: title and subtitle depend on it)
- Start from 3 to 6 seed phrases taken from the TOC (topic + format, topic + audience, topic + gift, topic + occasion).
- Expand them with Amazon's Books autocomplete (`./st keywords <slug> "seed" ...` in the studio): every suggestion is a phrase real buyers typed. Count how often each one shows up across expansions as a rough strength signal (it is not search volume).
- If autocomplete is unavailable, read the titles and subtitles of the 5 to 10 best-selling competitors in the niche; the phrases they repeat are buyer language. Label these "idea (competitors)", never "real search".
- Never invent search volume. Publisher Rocket / BookBeam validation is optional and Danilo's call; list the top 10 candidates in a small table with empty columns (searches/month, competition) in case he wants to check.

### Primary Keyword
- Recommend one primary keyword plus 2 alternates, each labeled "real search" or "idea", with one line on why (fit with what the book actually is beats raw popularity).
- If `primary_keyword` is already validated in book.yaml, use it and skip the recommendation.

### 7 Listing Keywords (KDP backend keyword fields)
- These are the 7 keyword fields in KDP (not bullet points)
- Each field: up to 50 characters, customer search-style; a field may hold a longer phrase or two related phrases
- Cover: primary use case, gift angle, audience descriptor, format/style, related activity types
- Do not repeat words already in the title or subtitle (Amazon already indexes them); do not repeat words across fields
- Deliver as a numbered list of exactly 7, one per line, with the character count, each labeled "real search" or "idea"
- **Deliver one set only**

### Amazon Ads Launch Terms
- 15 to 25 search terms for the launch Sponsored Products campaign (manual, exact and phrase match), taken from the research. Real searches first.
- Include the primary keyword and its close variants, the gift and audience angles, and 3 to 5 long-tail terms that describe this book specifically. No competitor brand names or author names.

### Categories (guidance only, for the KDP category picker)

Deliver this block after the 7 keywords. It is **orientative**: the exact category names change over time and by marketplace, so the Danilo must confirm each one in the KDP category picker for the format and marketplace (Amazon.com for the US). Never present a path as certain; write "closest match to look for".

- **How many:** KDP lets the author pick 3 categories per format when creating the book. Do not promise extra categories: asking KDP Support for more is no longer reliable and Support does not advise on category choice. Amazon may also shelve the book in other browse nodes from the title, subtitle, description and keywords, which cannot be controlled.
- **Give 3 primary picks + 2 or 3 alternates, in this order of the 3 slots:**
  1. **The niche or theme node** (e.g. the holiday or topic). Small and specific: it is the easiest place to reach a Best Seller badge, and the badge lifts conversion.
  2. **The activity-type node** (e.g. activity books, puzzles, games, word search). Bigger and more competitive, but it is where buyers browse by format.
  3. **The audience or subject node** (e.g. religion/culture, age, grade, or the adult gift angle for senior books).
- **For each pick:** the likely path in Amazon's taxonomy (Books > ...), one line on why, and one line on the competition ("small shelf" or "crowded shelf").
- **Method to confirm (include as a short checklist for the Danilo):** open 3 to 5 close competitors on Amazon.com, read the "Best Sellers Rank" lines under Product details to see which categories they sit in, and prefer shelves where the 20th book has a modest rank, so the new book can climb. Choose categories that match what the book actually is; never a category chosen only for volume.
- **Rules:** a children's activity book is nonfiction, not "juvenile fiction"; match the category to the format the book is (activity/puzzle) and to the theme it teaches; keep the age range (reading age) consistent with the listing; do not mix an adult category into a children's book, or the reverse.

### Description (Amazon Product Page)
- This is a sales page, not a summary
- Structure: Hook → Problem/Context → What makes this different → What's inside (brief) → Who it's for → CTA
- Use HTML formatting: `<b>`, `<br>`, `<p>` — KDP accepts basic HTML in descriptions
- Reading level: simple, conversational
- Length: 300–600 words
- **Deliver one optimized version only**
- Do not list every feature — pick the 2–3 most compelling and go deep on them

### A+ Content (Module Plan)
- Deliver a **module-by-module plan** with: module number, visual suggestion, headline copy, body copy
- Standard structure: 4 modules using 970×600px format
  - **Module 1 — Hook:** Book cover + bold headline. Captures attention, restates the core promise
  - **Module 2 — Problem/Context:** Speaks to the reader's situation and why this book exists
  - **Module 3 — Inside the Book:** Interior page spread + feature bullets. Let the buyer see what they're getting
  - **Module 4 — Close:** Reinforce trust, call to action, optionally add imprint credibility
- For activity books: Module 3 must include showing actual interior pages (puzzles, grids, activity layouts)
- **Deliver one plan only** — include all copy for each module
- If the book warrants more differentiation angles, the plan can extend up to 5 modules (Amazon's hard limit) by pulling from the extended banner-type list below. Default to 4 unless there's a clear reason for a 5th (e.g., strong competitive differentiation angle, or a lifestyle/gift angle worth its own module).

### A+ Content — Image Generation Prompts (Google Flow / Nano Banana 2)
Once the module plan (headline + body copy per module) is approved, this deliverable turns it into ready-to-paste image-generation prompts for **Google Flow** (free, Nano Banana 2 model, no credits consumed) — the actual banners get generated from these prompts, not designed by hand in Canva.

**Extended banner-type list** (pick up to 5 — Amazon's max — based on which best support this book's differentiation strategy from its positioning work):
1. **Hero** — main attention-grabbing banner: cover + headline, states the core promise
2. **Key Benefits & Features** — the most advantageous/functional parts of the book
3. **Lifestyle Scene** — the book in a real setting, reader enjoying it
4. **Inside Pages Preview** — real interior pages, builds trust
5. **Use Case & Versatility** — different ways/contexts the book gets used
6. **Comparison & Value** — this book vs. generic alternatives
7. **Curiosity / Closing** — final emotional push toward the buy button

Default recommendation when nothing else dictates otherwise: **Hero, Key Benefits & Features, Inside Pages Preview, Comparison & Value, Curiosity/Closing.** Swap in Lifestyle Scene or Use Case & Versatility instead of Comparison & Value when the book's strongest angle is emotional/gift-driven rather than competitive.

**Master prompt template** — fill every bracket, keep the structure, one prompt per banner:

```
Create a professional Amazon A+ content marketing banner for a [book type/genre] book titled "[BOOK TITLE]".

Banner purpose: [BANNER TYPE — Hero / Key Benefits & Features / Lifestyle Scene / Inside Pages Preview / Use Case & Versatility / Comparison & Value / Curiosity & Closing]

Visual style: Match the exact color palette, typography, and illustration/photography style of the attached book cover. Keep the design clean and consistent with the cover's mood — [imprint voice, e.g. "warm and encouraging" for Golden Chapter Press, "playful" for Silvia Press].

Layout: 16:9 landscape banner. [Placement instruction — see per-type notes below]. Leave clear negative space so the text stays legible.

Safe margins (mandatory): the banner will be center-cropped from 16:9 to a 970 x 600 px module, so keep every piece of text, every icon, and the book cover fully inside the central 88% of the frame width and the central 84% of the frame height. Nothing important may touch, approach, or be cut by the edges: leave at least 6% empty on the left and right, and 8% on the top and bottom. Only the background, stars, and glow may extend to the edges.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "[HEADLINE FROM MODULE PLAN]"
Supporting phrases: "[BENEFIT PHRASE 1]" | "[BENEFIT PHRASE 2]" | "[BENEFIT PHRASE 3]"

Audience: [target reader / buyer, e.g. "adult children buying a gift for their mother turning 70" or "seniors 65+"]. The imagery and mood should feel authentic to this audience — no cartoonish or generic stock-photo feel.

Do not add any logos, watermarks, or extra text beyond what is specified above.
```

**Interior fidelity (mandatory):** when a banner shows the interior (pages, puzzles, vignettes of interior art), it must look like the interior. If `paper` in `book.yaml` is `bw-white` (black-and-white interior), every interior element is drawn in black and white on white paper, no color, no gray shading; only the banner background, the cover, and the lettering carry the cover's colors. Use the book's real interior illustrations as attachments instead of asking the generator to invent them. An Inside Pages Preview or Use Case banner with a colorful interior misleads the buyer. When the plan names example activities, the banner must also say there is more (e.g. a closing phrase "And more, every night"), so the buyer does not think the examples are the whole book.

**Per-type placement instruction** (drop into the `[Placement instruction]` bracket):
- **Hero:** Book cover large and prominent on one side; themed background related to the book's topic on the other.
- **Key Benefits & Features:** 3 icon-style callouts, each paired with one supporting phrase.
- **Lifestyle Scene:** A realistic scene of the target reader/buyer in a natural setting (reading at home, gifting the book, using it with family), book visible in the scene.
- **Inside Pages Preview:** Showing the *attached* interior pages laid out attractively (fanned, on a table, or as a clean spread) — do not invent generic interior content, use only what's attached.
- **Use Case & Versatility:** 2–3 small vignettes showing different contexts the book gets used in (gift, travel, group activity, solo).
- **Comparison & Value:** Split composition — our book with checkmarked benefits on one side, a generic unbranded competitor-style book with plain/greyed-out features on the other. Never use real competitor branding or covers. The generic book gets a crude, amateur cover with its own plain title (never our title or any part of it) and its own four short greyed-out lines, written differently from ours: the image generator copies the left-side lines to the right side unless the prompt lists the right-side lines explicitly and forbids repeating or paraphrasing the left ones.
- **Curiosity/Closing:** A warm, inviting closing image that sparks emotion or curiosity about the reading experience — final push toward the buy button.

**Attachment checklist — what to upload in Google Flow for each prompt:**

| Banner type | Attach |
|---|---|
| Hero | Book cover |
| Key Benefits & Features | Book cover |
| Lifestyle Scene | Book cover |
| Inside Pages Preview | Book cover **+ 1–2 actual interior page spreads** |
| Use Case & Versatility | Book cover |
| Comparison & Value | Book cover |
| Curiosity/Closing | Book cover |

**Rule: attach the book cover on every single prompt, every single time** — this is what keeps all banners visually consistent with each other and with the cover (font, palette, style).

**Process:**
1. Confirm the module plan (copy) is finalized first — image prompts are generated *from* the approved headline/body copy, never invented independently.
2. Build one prompt per module using the template above.
3. In Google Flow: image mode, 16:9, 4 generations per prompt, model = Nano Banana 2 (free/no credits). Attach files per the checklist above before submitting each prompt.
4. Generate, keep the best of the 4, discard the rest. Repeat per module.
5. **Resize before uploading to KDP.** Google Flow outputs 16:9 — Amazon's A+ modules require 970×600px or 970×300px, neither of which is 16:9. Crop/resize each chosen image to the exact module dimension in Canva before uploading (do not upload the raw 16:9 output). The safe-margin paragraph in the template exists so this center crop never cuts text, icons, or the cover; keep it in every prompt of every book.

### Bonus Capture Texts (Brevo form + email), only when the book has a free bonus

Every book that promises a free bonus (PDF, printable kit, family pack) needs the copy for the Brevo capture flow. Write it in the same pass as the listing and save it as `listing/bonus-brevo.md`. **Always use the simple confirmation email** (no double opt-in): the form's confirmation email IS the delivery email, so there is no separate "confirm your address" email and no double opt-in success message. Models to follow: `books/hanukkah-8-nights/listing/bonus-brevo.md` (flow as built in Brevo) and `books/declutter-12-weeks/listing/bonus-brevo.md` (full text template; ignore its double opt-in blocks). Notes to the Danilo in Portuguese, all copy in US English, in the imprint's voice and signed by the imprint's name (Emily P. Harper, Jonah Feldman / Read Publishing Co, etc.).

**Rules**
- Name the bonus items exactly as the book's bonus page names them (`content/_bonus.md`, last page before the Answer Key, or the front matter). Same item names, same count. Never promise something the PDF does not contain.
- The reader is a buyer who already has the book: "You bought the workbook, so this part is on me." Never sell the book again.
- Short and concrete. One detail only this bonus has (what to print, where to tape it, which night to use it). No hype words, no "journey", no slogan endings. Run the `human-voice-writing` audit on every block.
- Print instructions: regular US letter-size paper. Always include the line "If the link stops working or the file won't open, just reply to this email and I'll send it again."
- If the PDF has sacred or sensitive content (e.g. Hebrew blessings with God's name), add the respectful-handling note in the PDF itself, not in the form.

**Deliver these blocks, in this order**
1. **Form page (landing page):** browser-tab title; headline; subheadline; supporting text (2 sentences); "what's inside" bullets (one line per item); fields (first name optional, email required, with placeholders); required consent checkbox (unchecked by default); button text (action + object, e.g. "Send Me the Kit"); privacy note under the button; **success message** shown right after the form is sent (what happens next, check spam/promotions); error message for an invalid email.
2. **Confirmation email (simple confirmation = delivery email):** recommended subject plus 2 alternatives, preview text, sender, body (greeting with `{{contact.FIRSTNAME | default: "there"}}`, one download button with the exact label, 3 short paragraphs on how to use each item, sign-off, P.S. with the "link stops working" line).
3. **Email HTML:** fill `templates/brevo/bonus-email.html` (all placeholders except the PDF link and the first-name tag) and save as `listing/bonus-email.html`. If the TOC promises an email sequence or a reminder, one HTML per email plus the automation steps.
4. **Form steps for the Danilo (Portuguese, plain words, no technical terms):** duplicate the last book's form in Brevo, paste the texts from block 1, choose "Simple confirmation email" with this book's template (Claude creates it in Brevo, active, once the PDF link exists), pick or create the list in the USA folder, publish, and send the form link back so the studio prints the real QR. Remind: sender physical address (CAN-SPAM) and the privacy-policy link on readpublishingco.com stay as in the duplicated form; test the full flow by phone (QR, email, download) before the book goes to KDP.

---

## Workflow

When asked to write listing copy:

1. **Identify what's needed** — full listing or specific element(s)?
2. **Confirm the book** — title, format, target reader, primary keyword (if already validated)
3. **Check if primary keyword is known** — if not, run the Keyword Research above and recommend one. Don't guess the search term without research.
4. **Deliver in this order:** Keywords (primary + 7 fields + Ads terms) → Title options → Subtitle options → Categories (guidance) → Description → A+ Content (module plan) → A+ Content image prompts (only if requested). Bonus Capture Texts are a separate pass (the studio's bonus stage).
   - If only one element is requested, deliver just that
5. **For title/subtitle:** Deliver 3 options each, with a one-line rationale per option
6. **For description and A+:** Deliver one version, optimized
7. **For A+ image prompts:** Require the module plan to exist first (generate it if it doesn't), then require the actual book cover file and, if the plan includes an Inside Pages Preview banner, the actual interior spreads to reference in the attachment checklist. Never fabricate interior content for that banner type.

---

## Golden Chapter Press — Additional Rules

These apply specifically to all senior activity books (the primary commercial focus):

- **Large print** must appear in the title or subtitle — it is a core search modifier and buyer filter
- **Decade/era themes** (1950s, 1960s, etc.) are high-converting angles for this audience — include in keywords and subtitle when relevant
- **Gift framing** is a major purchase driver: "retirement gift," "gift for grandma," "mom dad birthday gift" — always include at least one gift-angle keyword
- **Caregiver audience:** Some buyers are adult children or facility staff. Listing copy can speak to both ("a great activity for aging parents" / "keeps the mind active")
- **Avoid medical claims**: Do not claim the book treats, prevents, or helps with dementia, Alzheimer's, or any medical condition — use "mind-stimulating," "brain-engaging," "keeps the mind sharp" instead
- Cover/listing images shown in ads should reflect **interior pages**, not the cover — this applies to ad creative but informs A+ content Module 3 emphasis

---

## Keyword Strategy Notes

- The 7 listing keywords complement, not duplicate, the title
- Think in search-intent clusters: (1) activity type, (2) format/accessibility, (3) audience descriptor, (4) occasion/gift, (5) theme/era, (6) companion/collection angle, (7) alternate audience framing
- For multi-country adaptations (UK, CA, AU, DE): adapt spelling (colour vs color), gift occasions, and era references as needed — handle as a separate block at the end

---

## What Not to Do

- Do not write vague subtitles ("A Guide to Better Memory") — they speak to no one
- Do not list features without connecting them to benefits
- Do not use the word "comprehensive," "ultimate," "perfect," or "journey" unless the copy genuinely earns it
- Do not repeat the same phrase across title, subtitle, and description verbatim — vary the language
- Do not pad the description to hit a word count — tight and specific beats long and generic
- Do not deliver any prose (description, A+ copy) without first running the audit pass from `human-voice-writing`
- Do not invent a search term — use the validated keyword, or the Keyword Research output, and label each term "real search" or "idea"
- Do not generate A+ image prompts before the module plan copy is approved — copy drives the visuals, not the other way around
- Do not invent generic "interior pages" content for the Inside Pages Preview banner — always reference the actual attached interior spreads