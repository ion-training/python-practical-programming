# Order of subexpressions?

# A. min(max(3,4),abs(-5))
# A. max(3,4) -> abs(-5) -> min(3,5) -> 3

# B. abs(min(4,6,max(2,8)))
# B. max(2,8) -> min(4,6,8) -> abs(4) -> 4

# C. round(max(5.572, 3.258), abs(-2))
# C. max(5.572, 3.258) -> abs(-2) -> round(5.572, 2) -> 5.57
