import genanki

DECK_ID = 2050000000
MODEL_ID = 2050000001

DECK_NAME = "00000::chinese"

CSS = r'''
.card {
  font-family: Arial, "Noto Sans CJK SC", "PingFang SC", sans-serif;
  font-size: 22px;
  text-align: center;
  color: #1f2937;
  background-color: #f7f7f2;
  line-height: 1.45;
  padding: 24px;
}

.hanzi {
  font-family: "Noto Sans CJK SC", "PingFang SC", "Microsoft YaHei", sans-serif;
  font-size: 86px;
  line-height: 1.1;
  margin: 12px 0;
}

.pinyin {
  font-size: 30px;
  font-weight: 700;
  margin: 8px 0 18px;
}

.meaning {
  font-size: 27px;
  margin-bottom: 18px;
}

.mnemonic {
  text-align: left;
  max-width: 760px;
  margin: 20px auto 0;
  padding: 18px 20px;
  border-radius: 14px;
  background: #ffffff;
  border: 1px solid #deded5;
}

.movie {
  margin-top: 10px;
}

.hanzi-cue {
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid #deded5;
}

.example {
  margin-top: 22px;
  font-size: 23px;
}

.example .zh {
  font-family: "Noto Sans CJK SC", "PingFang SC", "Microsoft YaHei", sans-serif;
  font-size: 30px;
}

.answer-separator {
  margin: 24px 0;
}

.card.nightMode {
  color: #eeeeee;
  background-color: #202124;
}

.nightMode .mnemonic {
  background: #2b2c30;
  border-color: #4a4b50;
}
'''

MODEL = genanki.Model(
    MODEL_ID,
    "Chinese Mnemonic",
    fields=[
        {"name": "Hanzi"},
        {"name": "Pinyin"},
        {"name": "Meaning"},
        {"name": "Initial"},
        {"name": "Final"},
        {"name": "Tone"},
        {"name": "Position"},
        {"name": "Radical"},
        {"name": "VisualComponents"},
        {"name": "Movie"},
        {"name": "Example"},
    ],
    templates=[
        {
            "name": "Mnemonic Card",
            "qfmt": '''
<div class="hanzi">{{Hanzi}}</div>
<div class="pinyin">{{Pinyin}}</div>
<div>What does this mean?</div>
''',
            "afmt": '''
{{FrontSide}}
<hr id="answer" class="answer-separator">
<div class="meaning">{{Meaning}}</div>
<div class="mnemonic">
  <strong>Hanzi Movie</strong>
  <div>{{Initial}} → {{Final}} → {{Tone}} → {{Position}}</div>
  <div class="movie">{{Movie}}</div>
  <div class="hanzi-cue"><strong>Hanzi cue</strong><br>{{VisualComponents}}<br>Radical: {{Radical}}</div>
</div>
<div class="example">
  <div class="zh">{{Example}}</div>
</div>
''',
        }
    ],
    css=CSS,
)

DECK = genanki.Deck(DECK_ID, DECK_NAME)

NOTE = genanki.Note(
    model=MODEL,
    fields=[
        "我",
        "wǒ",
        "me; I",
        "W → Winnie the Pooh",
        "o → Słowackiego apartment",
        "3rd tone → Mexico",
        "1 → before/in front of entrance",
        "戈 (gē) → halberd; traditional radical classification",
        "Left: orc shaman's crooked wand (Ulu-Mulu-like). Right: Viking drakkar with a crow perched on top of the mast.",
        (
            "Winnie the Pooh stands in front of the entrance of the "
            "Słowackiego apartment in Mexico. He points dramatically at "
            "himself and shouts 我! (“me / I”). At the same time, the shape "
            "of 我 becomes a bizarre scene: an orc shaman's crooked wand on "
            "the left and a Viking drakkar on the right, with a black crow "
            "perched on top of its mast."
        ),
        "我喜欢中文。<br>Wǒ xǐhuān Zhōngwén.<br>I like Chinese.",
    ],
    guid=1000000001,
)

DECK.add_note(NOTE)

if __name__ == "__main__":
    genanki.Package(DECK).write_to_file("00000_chinese.apkg")
