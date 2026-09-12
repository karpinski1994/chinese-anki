# Chinese Anki

Source files for a mnemonic-first Mandarin Anki deck built around the Hanzi Movie Method.

## Deck

`00000::chinese`

## Card 00001 — 我 / wǒ

- Meaning: me; I
- Pinyin: `wǒ` (3rd tone)
- Initial: `W` → Winnie the Pooh
- Final: `o` → Słowackiego apartment
- Tone: 3rd → Mexico
- Position: 1 → before/in front of entrance
- Radical: `戈` (gē) → halberd

### Hanzi Movie

The pronunciation/meaning movie is the primary retrieval path:

Winnie the Pooh stands in front of the entrance of the Słowackiego apartment in Mexico. He points dramatically at himself and shouts **我!** (“me / I”).

The Hanzi itself gets a separate visual cue:

- **Left side:** an orc shaman's crooked wand, like the Ulu-Mulu wand from *Gothic 1*.
- **Right side:** a Viking drakkar (boat/ship).
- **Top of the mast:** a black crow perched on the mast.

The repository includes a visual mnemonic poster at [`hanzi_movie_wo.svg`](hanzi_movie_wo.svg). It is intentionally drawn with generic fantasy/cartoon imagery rather than reproducing a specific copyrighted character design.

The visual objects are mnemonic components, **not claims about the character's etymology**. The radical is recorded separately as `戈`.

### Complete memory chain

```text
Winnie → W- → Słowackiego apartment → -o → Mexico → 3rd tone
    ↓
Winnie points at himself → “I / me”
    ↓
我
    ↓
left: orc wand + right: Viking drakkar + crow on mast
    ↓
radical: 戈
```

### Example

我喜欢中文。  
Wǒ xǐhuān Zhōngwén.  
I like Chinese.

### Anki source

The deck is generated from `deck.py` using `genanki`. The model uses separate fields for the mnemonic anchors, Hanzi, pinyin, meaning, radical, visual components, movie, and example sentence. The `我` card also embeds `hanzi_movie_wo.svg` into the generated Anki package.

## Method rules

1. **Pronunciation and meaning:** use the canonical Hanzi Movie Method: initial → person/character → final → location → tone → position → movie → Hanzi/meaning.
2. **Hanzi structure:** record the actual radical separately from visual mnemonic imagery.
3. **Visual mnemonics:** may describe what a character resembles, but must not be presented as linguistic etymology.
4. **Tone accuracy:** always preserve the actual Mandarin tone.
5. **Retrieval:** recognition is not mastery; cards should support active recall of meaning, pinyin, tone, Hanzi, and character structure.
