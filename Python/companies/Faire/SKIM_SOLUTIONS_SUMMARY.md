# Quick Review: Skim These Solutions (5 min each)

**You have working solutions for problems you should SKIM (not fully implement)**

---

## ✅ Problem 3: Funnel Problem (Asked 4+ times)

**File:** `03_funnel_problem_solution.py`

**Key Approach:**
```python
# Track users per stage using sets (handles duplicates)
self.stage_users = defaultdict(set)  # {stage: set of user_ids}

for user_id, stage, timestamp in events:
    self.stage_users[stage].add(user_id)  # Users can skip stages!
```

**Important Points:**
- Users can **skip stages** (Browse → Purchase directly)
- Users counted **once per stage** (set handles duplicates)
- Drop-off = transition with biggest user loss
- If user goes Browse → Purchase, they "dropped off" from View, Cart, Checkout

**Complexity:** O(n) time, O(n) space

**Interview Questions They'll Ask:**
- "What if user skips stages?" → Only count stages they visited
- "What if user repeats a stage?" → Use set (count once)
- "How to handle no users at a stage?" → Division by zero check

---

## ✅ Problem 5: Number to Word (Asked 3+ times)

**File:** `05_number_to_word_conversion_solution.py`

**Key Approach:**
```python
# Three lookup tables
ones = {1: "one", 2: "two", ...}
teens = {10: "ten", 11: "eleven", 12: "twelve", ...}  # Special!
tens = {20: "twenty", 30: "thirty", 40: "forty", ...}  # Note: "forty" not "fourty"

# Build compositionally
# 23 = "twenty" + " " + "three" → "twenty three"
# Count chars WITHOUT spaces: len(word.replace(" ", ""))
```

**Special Cases:**
- 11-19 are irregular (eleven, twelve, thirteen, NOT "ten one")
- 40 = "forty" (NOT "fourty")
- 1000 = "one thousand" (edge case)

**Complexity:** O(1) per number, O(n) for range

**Interview Tip:** They often ask "sum character length for 1-1000"
- Answer: 18,451 characters (your solution calculates this)

---

## ✅ Problem 6: Ads Assortment (Asked 3+ times)

**File:** `06_ads_assortment_problem_solution.py`

**Key Approach:**
```python
# Greedy algorithm
sorted_ads = sorted(ads, key=lambda x: x[2], reverse=True)  # By value DESC

brand_count = {}
user_count = {}

for user_id, brand_id, value in sorted_ads:
    if brand_count[brand_id] < brand_limit and user_count[user_id] < user_limit:
        total_value += value
        brand_count[brand_id] += 1
        user_count[user_id] += 1
```

**Why Greedy Works:**
- Always pick highest value ad that satisfies constraints
- No benefit to saving capacity for lower-value ads

**Complexity:** O(n log n) for sorting

**Interview Questions:**
- "Why greedy?" → Maximizing value, no future benefit
- "What if we need exact N ads?" → Different problem (knapsack-like)

---

## ✅ Problem 7: Course Schedule Min Time (Asked 2+ times)

**File:** `07_course_schedule_min_time_solution.py`

**Key Approach:**
```python
# Topological sort (Kahn's algorithm) + time tracking
graph = defaultdict(list)  # prereq -> courses that depend on it
in_degree = [0] * n  # Count prerequisites for each course

# Track earliest start/end times
earliest_start = [0] * n
earliest_end = [0] * n

# BFS from courses with no prerequisites
queue = deque()
for i in range(n):
    if in_degree[i] == 0:
        queue.append(i)
        earliest_end[i] = time[i]

# Process in topological order
while queue:
    prereq = queue.popleft()
    for course in graph[prereq]:
        # Course starts when prerequisite finishes
        earliest_start[course] = max(earliest_start[course], earliest_end[prereq])
        in_degree[course] -= 1
        if in_degree[course] == 0:
            earliest_end[course] = earliest_start[course] + time[course]
            queue.append(course)

return max(earliest_end)  # When last course finishes
```

**Important Points:**
- Courses can run in **parallel** if no dependency
- Course can start when **ALL** prerequisites are done
- Start time = max(end time of all prerequisites)
- Total time = max(end time of all courses)

**Complexity:** O(V + E) where V = courses, E = prerequisites

**Interview Questions They'll Ask:**
- "How do you handle parallel execution?" → Track earliest start time
- "What if there's a cycle?" → Topological sort will detect it (some in_degree never reaches 0)
- "How is this different from sequential?" → Use max() not sum

---

## ✅ Problem 8: Maze with Portals (Asked 2+ times)

**File:** `08_maze_with_portals_solution.py`

**Key Approach:**
```python
# BFS with state = (row, col, used_portals_set)
portal_map = {}  # {position: [(destination, portal_id), ...]}

# Build bidirectional portal map
for portal_id, (pos1, pos2) in enumerate(portals):
    portal_map[pos1].append((pos2, portal_id))
    portal_map[pos2].append((pos1, portal_id))

# BFS with frozenset to track used portals
queue = deque([(start_r, start_c, frozenset(), 0)])
visited = set()

while queue:
    r, c, used_portals, dist = queue.popleft()

    # Normal moves (4 directions)
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if valid and (nr, nc, used_portals) not in visited:
            queue.append((nr, nc, used_portals, dist + 1))

    # Portal moves
    if (r, c) in portal_map:
        for dest, portal_id in portal_map[(r, c)]:
            if portal_id not in used_portals:
                new_used = used_portals | {portal_id}
                queue.append((dest[0], dest[1], new_used, dist + 1))
```

**Important Points:**
- State = **(position, portal_usage)** not just position!
- Portals are **bidirectional** (A→B or B→A)
- Each portal can be used **once per path**
- Use **frozenset** for hashable portal tracking
- Portal teleport counts as **1 move**

**Complexity:** O(R×C×2^P) worst case, much better in practice

**Interview Questions:**
- "Why frozenset?" → Need hashable type for visited set
- "Can portals be reused?" → Depends on problem (usually once per path)
- "Portal vs normal move?" → Both cost 1, BFS finds optimal

---

## 🎯 Quick Interview Prep Checklist

For each problem, you should be able to:

**In 30 seconds, say:**
1. ✅ "This is a [algorithm type] problem"
2. ✅ "The key data structure is [X]"
3. ✅ "Time complexity is O(X), space is O(Y)"

**Funnel:**
- "User funnel tracking with hash maps and sets"
- "O(n) time, O(n) space"

**Number to Word:**
- "Lookup tables with compositional building"
- "O(1) per conversion, O(n) for range"

**Ads:**
- "Greedy optimization with constraint tracking"
- "O(n log n) for sorting"

**Course Schedule:**
- "Topological sort with parallel execution tracking"
- "O(V + E) time, O(V + E) space"

**Maze with Portals:**
- "BFS with state tracking for portal usage"
- "O(R×C×2^P) worst case, better in practice"

---

## 💡 If Asked in Interview

**Don't say:** "I haven't implemented this before"

**DO say:** "I've reviewed this problem type. The approach is [X], using [data structure]. Let me implement it..."

Then code it based on the pattern you reviewed!

---

## 🚀 Final Prep Tonight

1. **Spend ~1 hour** skimming these 5 solutions
2. **Run each solution** to see output examples
3. **Understand the approach** (don't memorize code)
4. **Then move to system design prep** (2 hours for search systems)

**You're ready!** You have:
- ✅ 3 fully implemented & tested (Tag Validator, Haiku Finder, Group Anagrams)
- ✅ 5 working reference solutions to skim:
  - Problem 3: Funnel (hash maps + sets)
  - Problem 5: Number to Word (lookup tables)
  - Problem 6: Ads Assortment (greedy)
  - Problem 7: Course Schedule (topological sort)
  - Problem 8: Maze with Portals (BFS + state)

**Total: 8/8 problems covered!** 🎉

Good luck tomorrow! 🎯
