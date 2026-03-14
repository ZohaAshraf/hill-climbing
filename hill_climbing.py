import random
import matplotlib.pyplot as plt
import numpy as np

# The function we want to maximize
def f(x):
    return -(x - 3)**2 + 9


# -------------------------------------------------------
# (a) Simple Hill Climbing
# -------------------------------------------------------
def simple_hill_climbing(start=0.0, step=0.1):
    x = start
    path = [x]

    print("=== Simple Hill Climbing ===")
    print(f"Start: x = {x:.4f}, f(x) = {f(x):.4f}")

    while True:
        # Check right neighbor first, then left
        moved = False
        for neighbor in [x + step, x - step]:
            if f(neighbor) > f(x):
                x = neighbor
                path.append(x)
                print(f"  Moved to x = {x:.4f}, f(x) = {f(x):.4f}")
                moved = True
                break  # simple hill climbing: take the FIRST improvement

        if not moved:
            print(f"No improvement found. Stopping.")
            break

    print(f"Result: x = {x:.4f}, f(x) = {f(x):.4f}\n")
    return x, path


# -------------------------------------------------------
# (b) Steepest-Ascent Hill Climbing
# -------------------------------------------------------
def steepest_ascent_hill_climbing(start=0.0, step=0.1):
    x = start
    path = [x]

    while True:
        left  = x - step
        right = x + step

        # Pick the better of the two neighbors
        if f(right) >= f(left):
            best_neighbor = right
        else:
            best_neighbor = left

        # Only move if the best neighbor is actually better
        if f(best_neighbor) > f(x):
            x = best_neighbor
            path.append(x)
        else:
            break  # neither neighbor is better, we're at a peak

    return x, path


# -------------------------------------------------------
# (c) Random-Restart Hill Climbing
# -------------------------------------------------------
def random_restart_hill_climbing(num_restarts=10, step=0.1, low=-10, high=10):
    print("=== Random-Restart Hill Climbing ===")

    best_x = None
    best_val = float('-inf')
    best_start = None
    all_paths = []
    all_starts = []

    for i in range(num_restarts):
        start = random.uniform(low, high)
        all_starts.append(start)

        result_x, path = steepest_ascent_hill_climbing(start=start, step=step)
        all_paths.append(path)

        val = f(result_x)
        print(f"  Restart {i+1}: start = {start:.4f} -> result x = {result_x:.4f}, f(x) = {val:.4f}")

        if val > best_val:
            best_val = val
            best_x = result_x
            best_start = start

    print(f"\nBest solution found: x = {best_x:.4f}, f(x) = {best_val:.4f}")
    print(f"Best starting point: {best_start:.4f}\n")

    return best_x, best_val, best_start, all_paths, all_starts


# -------------------------------------------------------
# (d) Plotting
# -------------------------------------------------------
def plot_results(all_paths, all_starts):
    # Draw the actual curve of f(x)
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x) = -(x-3)² + 9')

    # Plot the trajectory for each restart
    colors = plt.cm.tab10.colors  # 10 distinct colors
    for i, path in enumerate(all_paths):
        path_y = [f(x) for x in path]
        color = colors[i % len(colors)]
        plt.plot(path, path_y, 'o--', color=color,
                 markersize=5, linewidth=1,
                 label=f'Restart {i+1} (start={all_starts[i]:.2f})')
        # Mark starting point
        plt.plot(path[0], f(path[0]), 's', color=color, markersize=8)
        # Mark ending point
        plt.plot(path[-1], f(path[-1]), '*', color=color, markersize=12)

    plt.title('Random-Restart Hill Climbing on f(x) = -(x-3)² + 9')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc='upper left', fontsize=7)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('hill_climbing_plot.png', dpi=150)
    plt.show()
    print("Plot saved as hill_climbing_plot.png")


# -------------------------------------------------------
# (e) Short Discussion
# -------------------------------------------------------
def print_discussion():
    print("=== Discussion ===")
    print("""
Does random restart always help?
  Not necessarily. For a simple unimodal function like f(x) = -(x-3)^2 + 9,
  there is only one peak, so every restart will end up at the same maximum.
  Random restart is most useful when the search space has many local maxima,
  where a single run might get stuck in a suboptimal peak.

When might random restart be wasteful?
  - On smooth unimodal functions (like this one), every restart gives the
    same answer, so extra restarts just waste computation.
  - If the function evaluations are expensive (e.g., running a simulation),
    many restarts can be very costly.
  - When the search space is huge, random starts may still land in bad
    regions and never find the true global optimum within a limited budget.
""")


# -------------------------------------------------------
# Main
# -------------------------------------------------------
if __name__ == "__main__":
    random.seed(42)  # for reproducibility

    # (a) Simple Hill Climbing
    simple_hill_climbing(start=0.0, step=0.1)

    # (b) Steepest-Ascent (single run for demo)
    print("=== Steepest-Ascent Hill Climbing (single run from x=0) ===")
    result, path = steepest_ascent_hill_climbing(start=0.0, step=0.1)
    print(f"Result: x = {result:.4f}, f(x) = {f(result):.4f}\n")

    # (c) Random-Restart
    best_x, best_val, best_start, all_paths, all_starts = random_restart_hill_climbing()

    # (d) Plot
    plot_results(all_paths, all_starts)

    # (e) Discussion
    print_discussion()
