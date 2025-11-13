# Bet 777 — console slot machine!

**Bet 777** is a simple Python console game that simulates a classic slot machine.  
Place your bet, spin the reels, and see if luck is on your side!

---

## 📦 Installation

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/vasiliykireev/777.git
cd 777
```

## ▶️ Run the game

Run the script:

```bash
python play.py
```

You can specify your **bet amount**:

```bash
python play.py --bet 100
python play.py -b 100
```

You can control the **spin animation and speed** using the `--speed` (`-s`) argument:

- `0` — no animation (only the final result is shown)  
- `1–9` — spinning animation, where `1` is slow and `9` is fast  
- Default: `5`

```bash
python play.py --speed 5 # Default speed
python play.py --speed 1 # Slowest
python play.py --speed 9 # Fastest
python play.py --speed 0 # No animation

# Custom bet with fast spinning
python play.py -b 50 -s 7
```

Use ```python3``` instead of ```python``` on macOS and Linux.

---

## 💰 Winning Rules

| Combination (pattern) | Reward × bet | Description |
|------------------------|-------------|-------------|
| `777` | 200 | 777 — Jackpot 🎉 |
| `999` | 100 | 999 — Huge win |
| `555` | 50  | 555 — Big win |
| `333` | 15  | 333 — Medium win |
| `111` | 10  | 111 — Small win |
| `..7` | 3   | Any combination ending with 7 |
| `.00` | 2   | Any combination ending with 00 |
| `..0` | 1   | Any combination ending with 0 |

---

## 🧠 Technical Details

- Written in pure **Python**, no external dependencies.  
- Uses `random` for digit generation.  
- Uses `re.fullmatch()` for pattern matching.  
- Animated spinning effect with gradual slowdown (printed to console).  
- Command-line interface implemented with `argparse`.

---

## 🕹 Example Output

```text
765
776
777
Winning: 200!
```

---

## ⚙️ Requirements

- **Python 3.8+**  
- No third-party libraries required

---

## 📜 License

**Beerware License** 🍺

> “As long as you retain this notice, you can do whatever you want with this code.  
> If we meet some day, and you think this code is worth it, you can buy me a beer.”
