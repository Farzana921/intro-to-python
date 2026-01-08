from math import isqrt
from functools import reduce

# Paste the full enc list here (must be clean, no ".....", no code glued onto it)
enc = [
    3827591716288630776540535668038365628871133898264070018792556815246012718335698404146173574751497387952867457629767297216012860845869627771721518203820241154212224,
    6960136184559430601681076640675186981775522614425463143207438380941559783783716813850739989978132330480107310443927842355512366409900326676275298793621864033812864,
    5623642457703922457490680337903628699091770794711163299663249078999644752494393952375103098657035066080687446171743217065981160810211492725692886373681255787004288
]


def ecv(v, n):
    return reduce(lambda v, s: (v << s) ^ s, n, v)

def inv_ecv(y, n):
    # exact inverse of (v<<s)^s applied in reverse order
    v = y
    for s in reversed(n):
        v = (v ^ s) >> s
    return v

known = "BYPASS_CTF{"
known_sq = [ord(c) ** 2 for c in known]

# brute n = [16, a, b, c]
# Use bit-length to constrain total shifts: sum(n) ≈ bitlen(enc[i]) - bitlen(ord^2)
# We'll search a,b in 1..200 and compute c from a reasonable total window.
c0_bit = enc[0].bit_length()
v0_bit = (ord('B') ** 2).bit_length()

# likely total shift sum is around this:
approx_total = c0_bit - v0_bit

candidates = []
for a in range(1, 201):
    for b in range(1, 201):
        for total in range(approx_total - 20, approx_total + 21):
            c = total - 16 - a - b
            if 1 <= c <= 1200:
                n = [16, a, b, c]
                ok = True
                for i, v_sq in enumerate(known_sq):
                    if inv_ecv(enc[i], n) != v_sq:
                        ok = False
                        break
                if ok:
                    candidates.append(n)

print("Candidates:", candidates)
if not candidates:
    raise SystemExit("No n found. Your enc list is probably incomplete/corrupted.")

n = candidates[0]
print("Using n =", n)

# decode full flag
flag_chars = []
for y in enc:
    v_sq = inv_ecv(y, n)
    r = isqrt(v_sq)
    if r*r != v_sq:
        raise ValueError("Not a perfect square—enc list still wrong at some position.")
    flag_chars.append(chr(r))

flag = "".join(flag_chars)
print(flag)
