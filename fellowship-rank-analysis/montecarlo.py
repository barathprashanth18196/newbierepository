"""Monte Carlo robustness check (SMAA-style) for the rebuilt rank list.

Each simulation draws (1) weights from a Dirichlet centred on the AHP weights,
(2) a random outcome for every still-unknown input (interview read, 24-hour call,
moonlighting), and optionally (3) +/-1 tier of noise on the subjective clinical and research
scores (clinical tier = 3.33, research tier = 2.5).
It then ranks programs with the same formula and tiebreak chain.
"""
import random
from collections import Counter, defaultdict

import rebuild as r

N = 20000
CONCENTRATION = 40  # higher = weights stay closer to the AHP values
random.seed(2026)


def dirichlet(alphas):
    draws = [random.gammavariate(a, 1) for a in alphas]
    s = sum(draws)
    return [d / s for d in draws]


def simulate(teaching_noise):
    counts = defaultdict(Counter)
    for _ in range(N):
        w = dirichlet([x * CONCENTRATION for x in r.WEIGHTS])
        m = {}
        for n, (c, f, g, read, call, vac, moon) in r.PROGRAMS.items():
            res = r.RESEARCH[n]
            if teaching_noise:
                c = min(10, max(0, c + random.choice((-1, 0, 1)) * 10 / 3))
                res = min(10, max(0, res + random.choice((-1, 0, 1)) * 2.5))
            t = r.teaching(n, c, res)
            read = random.choice((0, 2.5, 5, 7.5, 10)) if read is None else read
            call = random.choice((0, 1)) if call is None else call
            moon = random.choice(("Yes", "No")) if moon == "TBD" else moon
            m[n] = (t, f, g, r.culture(read, call, vac, moon, emr_good=n not in r.BAD_EMR))
        score = {n: sum(a * b for a, b in zip(w, v)) for n, v in m.items()}
        for i, n in enumerate(r.final_order(score, m), 1):
            counts[n][i] += 1
    return counts


def report(title, counts):
    print(f"\n{title}")
    print(f"{'Program':<22} {'P(#1)':>6} {'P(top3)':>8} {'P(top5)':>8} {'median':>7} {'90% range':>10}")
    rows = []
    for n, c in counts.items():
        ranks = sorted(k for k, v in c.items() for _ in range(v))
        rows.append((ranks[N // 2], n, c, ranks))
    for med, n, c, ranks in sorted(rows):
        p = lambda k: sum(v for rk, v in c.items() if rk <= k) / N
        print(f"{n:<22} {p(1):>6.1%} {p(3):>8.1%} {p(5):>8.1%} {med:>7} {ranks[int(N*.05)]:>4}-{ranks[int(N*.95)-1]:<4}")


if __name__ == "__main__":
    report("A. Weight uncertainty + unknown interview/call/moonlighting inputs", simulate(False))
    report("B. Same, plus +/-1 tier uncertainty on every clinical and research score", simulate(True))
