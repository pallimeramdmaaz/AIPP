def _apply_percentage(price, percent):
    return price * (1 - percent)

def _student_discount(price):
    return _apply_percentage(price, 0.10) if price > 1000 else _apply_percentage(price, 0.05)

def _regular_discount(price):
    return _apply_percentage(price, 0.15) if price > 2000 else price

def _refactored_discount(price, category):
    return _student_discount(price) if category == "student" else _regular_discount(price)

discount = _refactored_discount

# Self-checks (should all pass)
assert discount(500, "student") == 500 * 0.95
assert discount(1200, "student") == 1200 * 0.90
assert discount(2500, "student") == 2500 * 0.90
assert discount(1000, "regular") == 1000
assert discount(2200, "regular") == 2200 * 0.85
assert discount(3000, "regular") == 3000 * 0.85

print("Refactor applied and tests passed.")
