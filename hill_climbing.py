import random
import numpy as np
import matplotlib.pyplot as plt

# objective function to maximize
def objective(val):
    return -(val - 3)**2 + 9


# ==========================================
# PART A - Simple Hill Climbing
# ==========================================
def run_simple_hc(x0=0.0, delta=0.1):
    current = x0
    visited = [current]

    print("-------------------------------")
    print("  Simple Hill Climbing")
    print("-------------------------------")
    print(f"  Initial point -> x={current:.3f}  f={objective(current):.3f}")

    step_count = 0
    while True:
        next_right = current + delta
        next_left  = current - delta

        # try right first, then left - take first that's better
        improved = False
        for candidate in [next_right, next_left]:
            if objective(candidate) > objective(current):
                current = candidate
                visited.append(current)
                step_count += 1
                print(f"  step {step_count} -> x={current:.3f}  f={objective(current):.3f}")
                improved = True
                break

        if not improved:
            print(f"  Stuck at local max. Exiting loop.")
            break

    print(f"  Final answer: x={current:.3f}, f(x)={objective(current):.3f}\n")
    return current, visited


# ==========================================
# PART B - Steepest Ascent Hill Climbing
# ==========================================
def run_steepest_hc(x0=0.0, delta=0.1):
    current = x0
    visited = [current]

    while True:
        r = current + delta
        l = current - delta

        # compare both neighbors and take the best one
        best = r if objective(r) >= objective(l) else l

        if objective(best) > objective(current):
            current = best
            visited.append(current)
        else:
            break   # no better neighbor exists

    return current, visited


# ==========================================
# PART C - Random Restart
# ==========================================
def run_random_restart(n=10, delta=0.1, lower=-10, upper=10):
    print("-------------------------------")
    print("  Random Restart Hill Climbing")
    print("-------------------------------")

    champion_x     = None
    champion_val   = float('-inf')
    champion_start = None

    trajectories = []
    starting_pts = []

    for run in range(n):
        s = random.uniform(lower, upper)
        starting_pts.append(s)

        peak_x, traj = run_steepest_hc(x0=s, delta=delta)
        trajectories.append(traj)

        score = objective(peak_x)
        print(f"  Run {run+1:02d} | start={s:7.3f} | peak x={peak_x:.3f} | f={score:.4f}")

        if score > champion_val:
            champion_val   = score
            champion_x     = peak_x
            champion_start = s

    print(f"\n  >> Overall best: x={champion_x:.3f}, f(x)={champion_val:.4f}")
    print(f"  >> Came from start: {champion_start:.3f}\n")

    return champion_x, champion_val, champion_start, trajectories, starting_pts


# ==========================================
# PART D - Plot
# ==========================================
def draw_plot(trajectories, starting_pts):
    xs = np.linspace(-10, 10, 500)
    ys = [objective(x) for x in xs]

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(xs, ys, color='black', linewidth=2.5, label='f(x) = -(x-3)² + 9', zorder=2)

    cmap = plt.cm.Set1.colors
    for i, traj in enumerate(trajectories):
        ty = [objective(x) for x in traj]
        col = cmap[i % len(cmap)]

        ax.plot(traj, ty, linestyle='dashed', linewidth=1.2,
                color=col, alpha=0.8,
                label=f'Run {i+1} (s={starting_pts[i]:.1f})')

        # triangle marker at start
        ax.plot(traj[0], objective(traj[0]), '^', color=col, markersize=7)
        # circle marker at end
        ax.plot(traj[-1], objective(traj[-1]), 'o', color=col, markersize=9)

    ax.set_title('Hill Climbing — Random Restart Trajectories', fontsize=13, pad=12)
    ax.set_xlabel('x value', fontsize=11)
    ax.set_ylabel('f(x) value', fontsize=11)
    ax.legend(fontsize=7, loc='lower right', ncol=2)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_ylim(-170, 20)

    plt.tight_layout()
    plt.savefig('hill_climbing_plot.png', dpi=150)
    plt.show()
    print("Plot saved -> hill_climbing_plot.png")


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    random.seed(7)

    # part a
    run_simple_hc(x0=0.0, delta=0.1)

    # part b - single demo run
    print("-------------------------------")
    print("  Steepest Ascent (single run)")
    print("-------------------------------")
    px, pt = run_steepest_hc(x0=0.0, delta=0.1)
    print(f"  Result: x={px:.3f}, f(x)={objective(px):.3f}\n")

    # part c
    bx, bv, bs, all_trajs, all_starts = run_random_restart(n=10)

    # part d
    draw_plot(all_trajs, all_starts)