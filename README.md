

# Hill Climbing Algorithms in Python

A Python implementation of Hill Climbing search algorithms applied to a simple mathematical function. Built as part of an AI/search algorithms assignment.

---

## Problem

Maximize the function:

```
f(x) = -(x - 3)² + 9
```

The true maximum is at **x = 3**, where **f(x) = 9**.

---

## Algorithms Implemented

### (a) Simple Hill Climbing
- Starts from `x₀ = 0.0` with step size `0.1`
- Moves to the **first neighbor** that improves the value
- Stops when neither neighbor is better
- Prints the full path taken

### (b) Steepest-Ascent Hill Climbing
- At each step, evaluates **both** neighbors (`x + step` and `x - step`)
- Moves to the **better** of the two, only if it improves current value
- More careful than simple hill climbing

### (c) Random-Restart Hill Climbing
- Runs Steepest-Ascent from **10 random starting points** in `[-10, 10]`
- Reports the best solution found and which start produced it

### (d) Visualization
- Plots the full curve of `f(x)`
- Overlays the trajectory of each random restart
- Saved as `hill_climbing_plot.png`

---
## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/hill-climbing.git
cd hill-climbing
```

**2. Install dependencies**
```bash
pip install matplotlib numpy
```

**3. Run the script**
```bash
python hill_climbing.py
```

---

## Requirements

- Python 3.x
- `matplotlib`
- `numpy`

---

## Sample Output

```
=== Simple Hill Climbing ===
Start: x = 0.0000, f(x) = 0.0000
  Moved to x = 0.1000, f(x) = 0.5900
  ...
  Moved to x = 3.0000, f(x) = 9.0000
No improvement found. Stopping.

=== Random-Restart Hill Climbing ===
  Restart 1: start = 2.79 -> result x = 3.00, f(x) = 9.0000
  ...
Best solution found: x = 3.0000, f(x) = 9.0000
```

---

## Discussion

**Does random restart always help?**
Not really — for a unimodal function like this one, every restart converges to the same peak. Random restart shines when the search space has multiple local maxima.

**When is random restart wasteful?**
When the function is smooth and has only one peak, running multiple restarts just wastes computation without adding any benefit.

---

## File Structure

```
hill-climbing/
│
├── hill_climbing.py       # Main implementation
├── hill_climbing_plot.png # Output plot
└── README.md              # This file
```

---

## Author

Made with ☕ and a few bugs along the way.
