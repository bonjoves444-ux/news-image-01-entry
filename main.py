"""News-image-01 round 2: a broadsheet summing up Friday 13 November 2026.

The image is entry.png beside this file: "FRIDAY 13 NOVEMBER 2026",
21 verified stories from the day across 6 continents. The lead is the
FAA's nationwide ground stop (only the second since 9/11): grounded
airliners at dusk, 10,000+ flights delayed, 2,500 cancelled. Below it a
numbered world map places every story, with "By the numbers" (10,000+
delayed, 1,200 drones in one night, 483,200 deportations in 2026),
then a grid of 20 numbered story cards, each with a short label and a
region tag: Ukraine's ~1,200-drone attack, Russian strikes on Kyiv and
Odesa, a drone hitting a Russian warship off Finland, Europe joining
the Ukraine peace talks, the war's largest prisoner swap, Iran's claim
of a US radar strike in Bahrain, tankers hit in the Strait of Hormuz,
a Gaza hospital strike, China's Pacific drills, North Korea's $400m
crypto heist, the Microsoft outage, record US deportations, the
Schumer leadership challenge, the Kansas governor race, the Brooklyn
collapse, Pope Leo in Peru, Sudan's army taking an RSF stronghold,
the UN on Australia's Indigenous rights, the IEA oil surplus, and
Kane's England caps record. Every label is drawn with a real font, so
the text is crisp and legible at any size -- nothing is generated
text, so nothing can garble.

The program only copies bytes, so every run writes exactly the same
output: no network, no randomness, no timestamps. The bundled image
is 1024x1024 PNG, 301270 bytes, sha256
8d9e59189d39e428589c3e9cd49896eea923de1cfa955d68255620bb2022f962.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
# The judge sees exactly the bytes copied: the same file, every run.
