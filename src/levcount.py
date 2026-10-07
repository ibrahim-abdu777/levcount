"""Count lines by leading level token."""


def count(lines):
    counts = {}
    for line in lines:
        token = line.split(None, 1)[0].strip(":").upper() if line.strip() else ""
        if token.isalpha() and len(token) <= 10:
            counts[token] = counts.get(token, 0) + 1
    return counts


def count_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return count(handle)
