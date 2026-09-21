from fractions import Fraction as F
from math import log2

# LLRs use base-2 logarithms. Only integer-valued initial channel LLRs are used here.
L_ch = {"a": 1, "b": -1, "c": 1, "d": -2}
q = {}
for v, L in L_ch.items():
    r = F(2) ** L
    q[v] = (r / (1 + r), 1 / (1 + r))

def xor_weights(p, q):
    """Return the weights for XOR outcomes 0 and 1 for two independent inputs."""
    p0, p1 = p
    q0, q1 = q
    return (p0 * q0 + p1 * q1, p0 * q1 + p1 * q0)

# First-round check-to-variable messages exclude the destination variable's own input.
incoming = {
    "a": [xor_weights(q["b"], q["c"])],          # C → a
    "b": [xor_weights(q["a"], q["c"])],          # C → b
    "c": [xor_weights(q["a"], q["b"]), q["d"]],  # C → c, D → c
    "d": [q["c"]],                              # D → d
}

# Compute each bit's belief and hard decision using its channel weights
# and all incoming check-to-variable messages.
belief = {}
hat = {}
for v in L_ch:
    w0, w1 = q[v]
    for m0, m1 in incoming[v]:
        w0, w1 = w0 * m0, w1 * m1
    total = w0 + w1
    if total == 0:
        raise ValueError("Cannot normalize because both weights are zero.")
    belief[v] = (w0 / total, w1 / total)
    L = log2(w0 / w1)  # Both weights are positive for the fixed inputs used here.
    hat[v] = int(w1 > w0)  # Ties are resolved in favor of bit 0.
    print(f"{v}: weights=({belief[v][0]}, {belief[v][1]}), "
          f"LLR={L:.6f}, bit={hat[v]}")

s = (hat["a"] ^ hat["b"] ^ hat["c"], hat["c"] ^ hat["d"])
print("x_hat =", tuple(hat[v] for v in "abcd"))
print("syndrome =", s)
