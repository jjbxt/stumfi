import random
from collections import defaultdict
from math import prod


def simulate_sequence(N_true):
    """
    Simulate drawing all socks for a basket with N_true pairs.
    Returns a list of 0/1.
    """
    # label socks: pair i has labels (i, 0) and (i, 1)
    socks = [(i, j) for i in range(N_true) for j in (0, 1)]
    random.shuffle(socks)

    seen_once = set()
    seq = []
    for pair_id, _ in socks:
        if pair_id in seen_once:
            seq.append(0)  # second occurrence -> match
        else:
            seq.append(1)  # first occurrence -> new
            seen_once.add(pair_id)
    return seq


def likelihood_for_N(seq, N):
    """
    Compute L(N) = P(seq | N) using the product formula.
    seq is a list of 0/1.
    """
    a = 0  # distinct pairs seen so far
    b = 0  # matches so far
    L = 1.0

    for t, x in enumerate(seq, start=1):
        # t-1 socks already drawn before this step
        remaining = 2 * N - (t - 1)
        if remaining <= 0:
            return 0.0  # impossible: we drew more socks than exist

        if N < a:
            return 0.0  # impossible: can't have seen more pairs than exist

        if x == 1:
            # new pair
            p = 2 * (N - a) / remaining
            if p < 0:
                return 0.0
            L *= p
            a += 1
        else:
            # match
            if a - b <= 0:
                return 0.0  # impossible: no unmatched singles
            p = (a - b) / remaining
            L *= p
            b += 1

    return L


def posterior_over_N(seq, N_max, prior=None):
    """
    Compute posterior P(N | seq) for N in [0, N_max].
    Returns dict {N: posterior_prob}, and MAP N.
    """
    if prior is None:
        # uniform prior
        prior = {N: 1.0 for N in range(N_max + 1)}

    # compute unnormalized posterior = prior * likelihood
    unnorm = {}
    for N in range(N_max + 1):
        L = likelihood_for_N(seq, N)
        unnorm[N] = prior.get(N, 0.0) * L

    Z = sum(unnorm.values())
    if Z == 0:
        # All probabilities zero: data incompatible with assumed range
        posterior = {N: 0.0 for N in range(N_max + 1)}
        MAP = None
    else:
        posterior = {N: v / Z for N, v in unnorm.items()}
        MAP = max(posterior, key=posterior.get)

    return posterior, MAP


def incremental_MAP_path(N_true, N_max):
    """
    Simulate one full sequence for true N_true,
    and compute the MAP estimate after each draw.
    """
    seq = simulate_sequence(N_true)
    partial_seq = []
    map_path = []

    for x in seq:
        partial_seq.append(x)
        posterior, MAP = posterior_over_N(partial_seq, N_max)
        map_path.append(MAP)

    return seq, map_path


if __name__ == "__main__":
    N_true = 384
    N_max = 1000

    seq, map_path = incremental_MAP_path(N_true, N_max)
    print("Simulated 0/1 sequence:", seq)
    print("MAP estimate after each draw:")
    print(map_path)
    print("True N:", N_true)
