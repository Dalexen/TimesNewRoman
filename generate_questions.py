import json
import random

random.seed(42)

# ---------------------------------------------------------------------------
# CURATED FACT TABLES (hand-verified, real typographic history/knowledge)
# ---------------------------------------------------------------------------

fonts = [
    # name, designer(s), year, foundry, classification
    ("Times New Roman", "Stanley Morison & Victor Lardent", "1932", "Monotype", "serif"),
    ("Helvetica", "Max Miedinger", "1957", "Haas Type Foundry", "sans-serif"),
    ("Garamond", "Claude Garamond", "1530s", "N/A (Renaissance punchcutter)", "serif"),
    ("Futura", "Paul Renner", "1927", "Bauer Type Foundry", "sans-serif"),
    ("Gill Sans", "Eric Gill", "1928", "Monotype", "sans-serif"),
    ("Baskerville", "John Baskerville", "1757", "N/A (Baskerville's own foundry)", "serif"),
    ("Bodoni", "Giambattista Bodoni", "1798", "N/A (Bodoni's own press)", "serif"),
    ("Caslon", "William Caslon", "1722", "Caslon Foundry", "serif"),
    ("Comic Sans", "Vincent Connare", "1994", "Microsoft", "novelty/script"),
    ("Arial", "Robin Nicholas & Patricia Saunders", "1982", "Monotype", "sans-serif"),
    ("Georgia", "Matthew Carter", "1993", "Microsoft", "serif"),
    ("Verdana", "Matthew Carter", "1996", "Microsoft", "sans-serif"),
    ("Palatino", "Hermann Zapf", "1948", "Stempel", "serif"),
    ("Optima", "Hermann Zapf", "1958", "Stempel", "sans-serif"),
    ("Frutiger", "Adrian Frutiger", "1976", "Stempel", "sans-serif"),
    ("Univers", "Adrian Frutiger", "1957", "Deberny et Peignot", "sans-serif"),
    ("Rockwell", "Monotype Design Studio", "1934", "Monotype", "slab serif"),
    ("Franklin Gothic", "Morris Fuller Benton", "1902", "American Type Founders", "sans-serif"),
    ("Century Gothic", "Monotype Design Studio", "1991", "Monotype", "sans-serif"),
    ("Didot", "Firmin Didot", "1799", "N/A (Didot family press)", "serif"),
    ("Avant Garde", "Herb Lubalin & Tom Carnase", "1970", "International Typeface Corporation", "sans-serif"),
    ("Myriad", "Robert Slimbach & Carol Twombly", "1992", "Adobe", "sans-serif"),
    ("Trajan", "Carol Twombly", "1989", "Adobe", "serif"),
    ("Goudy Old Style", "Frederic Goudy", "1915", "American Type Founders", "serif"),
    ("Segoe UI", "Steve Matteson", "2004", "Monotype/Microsoft", "sans-serif"),
    ("San Francisco", "Apple Type Team", "2015", "Apple", "sans-serif"),
    ("Roboto", "Christian Robertson", "2011", "Google", "sans-serif"),
    ("Open Sans", "Steve Matteson", "2011", "Google", "sans-serif"),
    ("Lato", "Lukasz Dziedzic", "2010", "N/A (independent release)", "sans-serif"),
    ("Montserrat", "Julieta Ulanovsky", "2011", "N/A (independent release)", "sans-serif"),
    ("Calibri", "Lucas de Groot", "2007", "Microsoft", "sans-serif"),
    ("Cambria", "Jelle Bosma, Steve Matteson & Robin Nicholas", "2004", "Microsoft", "serif"),
]
font_by_name = {f[0]: f for f in fonts}

terms = [
    # term, definition
    ("Serif", "a small line or stroke attached to the end of a larger stroke in a letter"),
    ("Sans-serif", "a typeface whose letters have no small projecting strokes at their ends"),
    ("Kerning", "the adjustment of space between two specific letters to improve visual spacing"),
    ("Tracking", "a uniform adjustment of spacing applied across a range of characters"),
    ("Leading", "the vertical space between the baselines of consecutive lines of type"),
    ("X-height", "the height of a typeface's lowercase letters, excluding ascenders and descenders"),
    ("Ascender", "the part of a lowercase letter, like 'b' or 'd', that extends above the x-height"),
    ("Descender", "the part of a lowercase letter, like 'g' or 'p', that extends below the baseline"),
    ("Baseline", "the invisible line on which most letters visually rest"),
    ("Cap height", "the height of a capital letter measured from the baseline"),
    ("Ligature", "a single glyph formed by combining two or more letters, such as 'fi'"),
    ("Counter", "the enclosed or partially enclosed space within a letter such as 'o' or 'e'"),
    ("Bowl", "the curved stroke that encloses a counter, as in the letters 'b' or 'p'"),
    ("Stem", "the main, usually vertical, stroke of a letterform"),
    ("Terminal", "the end of a stroke that does not carry a serif"),
    ("Ear", "a small stroke projecting from the top of letters like lowercase 'g' or 'r'"),
    ("Spine", "the main curving stroke that forms the body of the letter 'S'"),
    ("Apex", "the point at the top of a letter where two diagonal strokes meet, as in 'A'"),
    ("Crossbar", "the horizontal stroke connecting two strokes, as in 'A' or 'H'"),
    ("Bracket", "the curved part that connects a serif to the main stroke of a letter"),
    ("Hairline", "the thinnest stroke weight found within a typeface"),
    ("Swash", "a decorative flourish that extends or replaces a normal terminal or serif"),
    ("Small caps", "capital letterforms drawn at roughly the height of lowercase letters"),
    ("Old-style figures", "numerals of varying heights, some with ascenders or descenders, that blend into text"),
    ("Lining figures", "numerals that are all a uniform height, aligned with capital letters"),
    ("Oblique", "a slanted version of an upright typeface created by skewing the original letterforms"),
    ("Weight", "the relative thickness of the strokes making up a typeface, such as light or bold"),
    ("Em", "a unit of typographic measurement equal to the point size of the type"),
    ("En", "a unit of typographic measurement equal to half an em"),
    ("Widow", "a short final line of a paragraph left stranded at the top of the next page or column"),
    ("Orphan", "a short first line of a paragraph left stranded at the bottom of a page or column"),
    ("Glyph", "a specific visual shape used to represent a character or part of one"),
    ("Drop cap", "an enlarged capital letter at the start of a paragraph that spans several lines of text"),
    ("Pica", "a traditional unit of typographic measurement equal to 12 points"),
    ("Monospace", "a typeface in which every character occupies exactly the same horizontal width"),
    ("Condensed", "a narrower variant of a typeface, with letters set closer together"),
    ("Hinting", "instructions embedded in a digital font to improve how it renders at small sizes"),
    ("Foundry", "a company or individual that designs, produces, or distributes typefaces"),
    ("Letterpress", "a relief printing technique that applies ink using raised, inked surfaces"),
    ("Movable type", "individual, reusable pieces of type that can be arranged to form text for printing"),
    ("OpenType", "a font format jointly developed by Microsoft and Adobe"),
    ("TrueType", "a font format originally developed by Apple in the late 1980s"),
    ("Variable font", "a single font file that can render a continuous range of weights, widths, or styles"),
    ("Typeface", "the overall design of a set of letterforms, as distinct from a specific file or size of it"),
    ("Point size", "the unit, based on points, used to measure the size of type"),
    ("Italic", "a style of type with letterforms redrawn at a slant, distinct from simple slanting"),
]
term_by_name = {t[0]: t for t in terms}

# Hand-written, unique Times New Roman-specific facts (question, options, correct)
tnr_facts = [
    ("Times New Roman was originally commissioned for which newspaper?",
     ["The Times of London", "The New York Times", "The Washington Post", "The Guardian"], 0),
    ("In what year did Times New Roman first appear in print?",
     ["1932", "1928", "1945", "1901"], 0),
    ("Who was the typographic advisor at The Times who directed the creation of the typeface?",
     ["Stanley Morison", "Eric Gill", "Jan Tschichold", "Frederic Goudy"], 0),
    ("Who was the Monotype draftsman who physically drew the letterforms under Morison's direction?",
     ["Victor Lardent", "Matthew Carter", "Adrian Frutiger", "Hermann Zapf"], 0),
    ("Times New Roman replaced an older typeface previously used by The Times called what?",
     ["Times Old Roman", "Plantin", "Century", "Baskerville"], 1),
    ("Which company originally produced and licensed Times New Roman?",
     ["Monotype", "Linotype", "Adobe", "American Type Founders"], 0),
    ("What broad classification of serif typeface is Times New Roman usually placed in?",
     ["Transitional serif", "Slab serif", "Humanist sans-serif", "Blackletter"], 0),
    ("For rival hot-metal typesetting machines, a very similar cut of the design was sold under a different name. What was it commonly called?",
     ["Times Roman", "Times Classic", "Times Modern", "Times Standard"], 0),
    ("For many years, Times New Roman was the default body font in which widely used word processor?",
     ["Microsoft Word", "Google Docs", "WordPerfect", "Apple Pages"], 0),
    ("Microsoft Word switched its default font away from Times New Roman/Arial in 2007 to which typeface?",
     ["Calibri", "Cambria", "Georgia", "Segoe UI"], 0),
    ("Times New Roman is designed to be relatively space-efficient, which was part of its original goal for a newspaper. What was that goal generally about?",
     ["Fitting more text into limited column width", "Making headlines louder", "Reducing ink usage in color printing", "Simplifying handwriting instruction"], 0),
    ("A metrically-compatible, open-source alternative to Times New Roman, used by Google Fonts and LibreOffice, is called what?",
     ["Tinos", "Liberation Serif", "PT Serif", "Noto Serif"], 0),
    ("Does Times New Roman belong to the serif or sans-serif family of typefaces?",
     ["Serif", "Sans-serif", "Monospace", "Script"], 0),
    ("Times New Roman has noticeably short, blunt serifs compared to older typefaces like Garamond. What typeface era does this transitional style bridge?",
     ["Old-style and modern (didone) serif design", "Blackletter and roman type", "Wood type and metal type", "Handwriting and calligraphy"], 0),
    ("Roughly how many years after its 1932 debut did Times New Roman remain Microsoft Word's default font before being replaced?",
     ["About 75 years", "About 10 years", "About 40 years", "About 150 years"], 0),
    ("Times New Roman is named after which publication rather than after its designer, unlike many classic typefaces (e.g. Baskerville, Garamond).",
     ["The Times", "Life Magazine", "National Geographic", "The New Yorker"], 0),
    ("What was one of the stated design goals for the original Times New Roman commission, alongside legibility?",
     ["Economical use of newsprint space", "Maximum decorative flourish", "Compatibility with typewriters only", "Exclusive use for headlines"], 0),
    ("Times New Roman's design was partly a reaction against an older Times typeface that Morison considered what?",
     ["Too worn and old-fashioned for clear printing", "Too modern and geometric", "Too expensive to license", "Too similar to handwriting"], 0),
    ("On a typical printed page set in Times New Roman, is the typeface generally considered fairly narrow/condensed or wide, compared to many contemporaries?",
     ["Fairly narrow/condensed", "Extremely wide", "Monospaced", "Extra bold by default"], 0),
    ("Since Times New Roman is a licensed Monotype design, which company's very similar competing cut was called 'Times Roman'?",
     ["Linotype", "Adobe", "Bitstream", "URW"], 0),
]

# General historical / printing facts, hand-written and fact-checked
history_facts = [
    ("Johannes Gutenberg's movable-type printing press is generally dated to around which century?",
     ["The 15th century", "The 10th century", "The 18th century", "The 12th century"], 0),
    ("Which German city is most associated with Gutenberg's early printing press?",
     ["Mainz", "Berlin", "Munich", "Hamburg"], 0),
    ("The Linotype machine, which cast an entire line of type at once from molten metal, was invented by whom?",
     ["Ottmar Mergenthaler", "Johannes Gutenberg", "Tolbert Lanston", "Frederic Goudy"], 0),
    ("The Monotype Corporation's casting system, a rival to Linotype, cast type in what unit?",
     ["Individual characters", "Whole lines", "Whole pages", "Whole paragraphs"], 0),
    ("What is the general term for casting metal type from molten lead alloy for printing, as done by Linotype and Monotype machines?",
     ["Hot metal typesetting", "Cold type typesetting", "Phototypesetting", "Digital typesetting"], 0),
    ("What printing method uses raised, inked surfaces pressed directly onto paper?",
     ["Letterpress", "Offset lithography", "Screen printing", "Digital inkjet"], 0),
    ("TrueType, a widely used digital font format, was originally developed by which company?",
     ["Apple", "Microsoft", "Adobe", "IBM"], 0),
    ("OpenType, a font format that unified earlier rival formats, was jointly developed by Microsoft and which other company?",
     ["Adobe", "Apple", "Google", "IBM"], 0),
    ("What term describes reusable, individually cast pieces of type that can be rearranged for different pages?",
     ["Movable type", "Fixed type", "Composite type", "Static type"], 0),
    ("Which type designer created both Verdana and Georgia for Microsoft, aimed at improving on-screen readability?",
     ["Matthew Carter", "Hermann Zapf", "Adrian Frutiger", "Eric Gill"], 0),
]

categories_map = {}

def make_qid_counter():
    n = [0]
    def nxt():
        n[0] += 1
        return n[0]
    return nxt

next_id = make_qid_counter()
questions = []
seen_prompts = set()

def add_question(category, prompt, options, correct_index):
    if prompt in seen_prompts:
        return False
    if len(options) != 4:
        return False
    if len(set(options)) != 4:
        return False
    seen_prompts.add(prompt)
    questions.append({
        "id": next_id(),
        "category": category,
        "prompt": prompt,
        "options": options,
        "correctIndex": correct_index,
    })
    return True

def shuffled_options(correct_value, distractor_pool, correct_index_label=None):
    """Return (options, correct_index) with 3 random distractors + the correct value, shuffled."""
    pool = [v for v in distractor_pool if v != correct_value]
    random.shuffle(pool)
    distractors = pool[:3]
    options = distractors + [correct_value]
    random.shuffle(options)
    return options, options.index(correct_value)

# --- 1) Hand-written Times New Roman facts ---
for prompt, options, correct in tnr_facts:
    add_question("Times New Roman", prompt, options, correct)

# --- 2) Hand-written history/printing facts ---
for prompt, options, correct in history_facts:
    add_question("Printing History", prompt, options, correct)

# --- 3) Templated font-fact questions (designer / year / foundry / classification) ---
all_designers = [f[1] for f in fonts]
all_years = [f[2] for f in fonts]
all_foundries = [f[3] for f in fonts]
all_classes = sorted(set(f[4] for f in fonts))

designer_templates = [
    "Who designed the typeface {name}?",
    "{name} is a typeface created by which designer?",
    "Which designer is credited with creating {name}?",
]
year_templates = [
    "In what year was the typeface {name} first released?",
    "{name} was released in which year?",
    "Which year marks the debut of the typeface {name}?",
]
foundry_templates = [
    "Which type foundry or company released the typeface {name}?",
    "{name} was released by which foundry or company?",
]
class_templates = [
    "How is the typeface {name} generally classified?",
    "{name} belongs to which broad category of typeface?",
]

for name, designer, year, foundry, cls in fonts:
    for t in designer_templates:
        opts, idx = shuffled_options(designer, all_designers)
        add_question("Typeface Designers", t.format(name=name), opts, idx)
    for t in year_templates:
        opts, idx = shuffled_options(year, all_years)
        add_question("Typeface History", t.format(name=name), opts, idx)
    for t in foundry_templates:
        if foundry.startswith("N/A"):
            continue
        opts, idx = shuffled_options(foundry, [f for f in all_foundries if not f.startswith("N/A")])
        add_question("Type Foundries", t.format(name=name), opts, idx)
    for t in class_templates:
        opts, idx = shuffled_options(cls, all_classes)
        if len(set(opts)) == 4:
            add_question("Typeface Classification", t.format(name=name), opts, idx)

# Reverse designer questions: "Which typeface did X design?"
designer_to_fonts = {}
for name, designer, year, foundry, cls in fonts:
    designer_to_fonts.setdefault(designer, []).append(name)

all_font_names = [f[0] for f in fonts]
for designer, names in designer_to_fonts.items():
    if designer.startswith("N/A") or "Studio" in designer or "Team" in designer:
        continue
    for name in names:
        opts, idx = shuffled_options(name, all_font_names)
        add_question("Typeface Designers", f"Which of these typefaces was designed by {designer}?", opts, idx)

# --- 4) Templated typography-term questions ---
all_term_names = [t[0] for t in terms]
all_definitions = [t[1] for t in terms]

term_def_templates = [
    "In typography, what does the term '{term}' refer to?",
    "Which of these best defines the typographic term '{term}'?",
]
def_to_term_templates = [
    "Which typographic term describes {definition}?",
]

for term, definition in terms:
    for t in term_def_templates:
        opts, idx = shuffled_options(definition, all_definitions)
        add_question("Typography Terms", t.format(term=term), opts, idx)
    for t in def_to_term_templates:
        opts, idx = shuffled_options(term, all_term_names)
        add_question("Typography Terms", t.format(definition=definition), opts, idx)

# --- 5) Classification comparison questions: "Which of these is NOT a serif typeface?" etc ---
serif_fonts = [f[0] for f in fonts if f[4] == "serif"]
sans_fonts = [f[0] for f in fonts if f[4] == "sans-serif"]

for target_name in serif_fonts:
    others = [n for n in sans_fonts]
    if len(others) >= 3:
        distractor_sample = random.sample(others, 3)
        options = distractor_sample + [target_name]
        random.shuffle(options)
        add_question(
            "Typeface Classification",
            "Which of these typefaces is classified as a serif design (the other three are sans-serif)?",
            options, options.index(target_name)
        )

for target_name in sans_fonts:
    others = [n for n in serif_fonts]
    if len(others) >= 3:
        distractor_sample = random.sample(others, 3)
        options = distractor_sample + [target_name]
        random.shuffle(options)
        add_question(
            "Typeface Classification",
            "Which of these typefaces is classified as a sans-serif design (the other three are serif)?",
            options, options.index(target_name)
        )

print(f"Generated so far: {len(questions)}")

# --- 6) Top up to exactly 500 with additional non-duplicate templated combinations ---
extra_templates_designer = [
    "The letterforms of {name} were designed by which person or team?",
]
extra_templates_year = [
    "{name} first saw use in which year?",
]

idx_cycle = 0
while len(questions) < 500:
    name, designer, year, foundry, cls = fonts[idx_cycle % len(fonts)]
    made_any = False
    for t in extra_templates_designer:
        opts, idx = shuffled_options(designer, all_designers)
        if add_question("Typeface Designers", t.format(name=name), opts, idx):
            made_any = True
            if len(questions) >= 500:
                break
    if len(questions) >= 500:
        break
    for t in extra_templates_year:
        opts, idx = shuffled_options(year, all_years)
        if add_question("Typeface History", t.format(name=name), opts, idx):
            made_any = True
            if len(questions) >= 500:
                break
    idx_cycle += 1
    if idx_cycle > 5000:
        break

print(f"Final count: {len(questions)}")

questions = questions[:500]
for i, q in enumerate(questions, start=1):
    q["id"] = i

with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2)

# sanity checks
cats = {}
for q in questions:
    cats[q["category"]] = cats.get(q["category"], 0) + 1
print("Category breakdown:", cats)
print("Total:", len(questions))
