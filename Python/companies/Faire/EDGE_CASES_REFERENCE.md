# 🚨 Faire Interview - Critical Edge Cases Reference

**IMPORTANT: Faire puts heavy emphasis on edge cases and test cases!**

According to 1point3acres reports, interviewers will ask: **"What OTHER edge cases can you think of?"** even after you've tested thoroughly.

---

## 01. HTML Format Validation (5⭐ - MOST ASKED)

### Critical Edge Cases to Mention:
1. **Empty string** → `True` (no tags to validate)
2. **Text only, no tags** → `True` (e.g., "Hello World")
3. **Single braces** → `True` (e.g., "{ text }" - NOT tags!)
4. **Incomplete tag** → `False` (e.g., "{{ #abc" - missing }})
5. **Only opening tags** → `False` (e.g., "{{ #abc }}")
6. **Only closing tags** → `False` (e.g., "{{ /abc }}")
7. **Wrong closing order** → `False` (must be LIFO - stack behavior)
8. **Nested same-name tags** → `True` if properly closed
9. **Extra closing tag** → `False` (more closes than opens)
10. **Double braces without spaces** → "{{#abc}}" (implementation-dependent)
11. **Tag names with numbers/special chars** → Should handle "{{ #tag123 }}"

### What Interviewers Look For:
- **MUST understand**: `{{` starts a tag, single `{` is text
- **MUST understand**: Need both `#` (open) and `/` (close) prefix
- **MUST understand**: LIFO order (stack-based validation)
- **MUST handle**: Incomplete tags (missing `}}`)

---

## 02. Haiku Finder (5⭐ - MOST ASKED)

### Critical Edge Cases to Mention:
1. **Punctuation** → Strip before lookup, preserve in output (e.g., "Void." → lookup "void")
2. **Case sensitivity** → Lowercase for lookup, preserve original in output
3. **Missing words from dictionary** → Treat as 0 syllables OR skip
4. **Empty string** → Return `None`
5. **Sentence < 3 words** → Return `None` (can't form haiku)
6. **Total syllables < 17** → Return `None` (impossible to form 5-7-5)
7. **Multiple valid haikus** → Return FIRST (leftmost) one only
8. **Contractions** → Must strip punctuation correctly (e.g., "don't" → lookup "dont")
9. **Words with multiple punctuation** → "word..." → lookup "word"
10. **No valid haiku pattern** → Return `None`

### What Interviewers Look For:
- **MUST use**: Prefix sum + hash map for O(n) solution (not brute force!)
- **MUST preserve**: Original case and punctuation in output
- **MUST find**: FIRST haiku if multiple exist
- **MUST handle**: Edge case where word not in dictionary

### Interview Insight:
> "Interviewer asked: 'What if a word has punctuation?' and 'What if the same word appears multiple times?' Be ready to explain your string cleaning logic."

---

## 03. Funnel Problem (4⭐ - HIGH PRIORITY)

### Critical Edge Cases to Mention:
1. **Empty events list** → All metrics return 0
2. **Single user, single event** → 100% drop-off after first stage
3. **Users skip stages** → e.g., Browse → Purchase (validate journey validity)
4. **User repeats same stage** → Count only ONCE per user
5. **Users go backwards** → e.g., Browse → View → Browse (invalid order?)
6. **All users complete funnel** → 100% conversion at each stage
7. **No users reach final stage** → Purchase conversion = 0%
8. **Duplicate timestamps** → Need tie-breaking logic
9. **Invalid stage names** → Filter out or raise error
10. **Division by zero** → When no users at a stage

### What Interviewers Look For:
- **MUST clarify**: Can users skip stages? (Yes for Faire's version)
- **MUST clarify**: How to handle duplicate events for same stage?
- **MUST clarify**: How to handle out-of-order events?
- **MUST discuss**: Time windows for conversion (e.g., within 24 hours?)

### Interview Insight:
> "Even after I wrote comprehensive tests, interviewer kept asking 'what other edge cases?' Be prepared to discuss invalid data, performance with large datasets, and time-window constraints."

---

## 04. Group Anagrams (3⭐)

### Critical Edge Cases to Mention:
1. **Empty string in array** → `[""]` → `[[""]]`
2. **Single character** → `["a"]` → `[["a"]]`
3. **All anagrams** → `["abc", "bca", "cab"]` → All in one group
4. **No anagrams** → `["a", "b", "c"]` → Each in separate group
5. **Duplicate strings** → `["a", "a"]` → Both in same group `[["a", "a"]]`
6. **Mixed lengths** → `["a", "ab", "ba"]` → Different groups by length
7. **Case sensitivity** → Problem specifies lowercase only

### What Interviewers Look For:
- **MUST know**: Two approaches (sorted string vs. character count)
- Time complexity: O(n * k log k) for sorted, O(n * k) for count
- This is a standard LeetCode problem - know it cold!

---

## 05. Number to Word Conversion (3⭐)

### Critical Edge Cases to Mention:
1. **Single number** → start = end = 1 → "one" (3 chars)
2. **Teens (11-19)** → Special handling ("eleven", not "ten one")
3. **Exact tens (20, 30, ...)** → "twenty", no "and"
4. **Hundreds** → 100 = "one hundred" (10 chars including space)
5. **1000** → "one thousand" (special case, 12 chars)
6. **Crossing boundaries** → [19, 21] includes "nineteen", "twenty", "twenty one"
7. **Spaces** → Clarify if spaces count toward length (usually NO)

### What Interviewers Look For:
- **MUST clarify**: Do spaces count toward character length?
- **MUST clarify**: British vs American English ("and" placement)
- **MUST handle**: All special cases (1-9, 10-19, 20-90, 100-900, 1000)

---

## 06. Ads Assortment Problem (3⭐)

### Critical Edge Cases to Mention:
1. **Empty ads array** → Return 0
2. **Single ad** → Return that ad's value
3. **All ads same brand** → Can only show max N ads per brand
4. **All ads same user** → Can only show max M ads per user
5. **Ties in value** → Which ads to prioritize?
6. **Weekly limit exactly met** → No more ads for that user/brand
7. **More ads than weekly slots** → Need to optimize selection

### What Interviewers Look For:
- **MUST understand**: Weekly constraints (brand limit, user limit)
- **MUST clarify**: What happens when multiple constraints conflict?
- This is a greedy/optimization problem - discuss approach

---

## 07. Course Schedule with Minimum Time (2⭐)

### Critical Edge Cases to Mention:
1. **No prerequisites** → All courses can be taken in parallel (max course time)
2. **Linear dependency chain** → Must complete sequentially (sum of all times)
3. **Cycle detection** → Invalid input (can't complete if cycle exists)
4. **Multiple prerequisites for one course** → Must wait for ALL to complete
5. **Zero-duration courses** → Edge case in timing calculation
6. **Disconnected components** → Multiple independent course chains

### What Interviewers Look For:
- **MUST use**: Topological sort + BFS/DFS
- **MUST track**: Earliest completion time for each course
- This is similar to "Parallel Course" on LeetCode

---

## 08. Maze with Portals (1⭐)

### Critical Edge Cases to Mention:
1. **No path exists** → Return -1
2. **Start = End** → Return 0
3. **No portals** → Standard BFS shortest path
4. **Portal to unreachable area** → May create new path
5. **Multiple portals to same location** → Choose shortest route
6. **Portal at start or end** → Can use immediately
7. **Visited state** → Must track (x, y, used_portal_flag) to avoid infinite loop

### What Interviewers Look For:
- **MUST use**: BFS with state = (x, y, portal_used_flag)
- **MUST track**: Whether portal has been used (can use at most once)
- Similar to "Shortest Path in Binary Matrix" with teleportation

---

## 🎯 General Interview Strategy for Edge Cases

### When Asked "What Other Edge Cases?"

**Always mention these categories:**

1. **Empty/Null Input** → Empty string, empty array, null values
2. **Single Element** → Minimum valid input
3. **Boundary Values** → Min/max values, exact limits
4. **Invalid Input** → Malformed data, out-of-range values
5. **Duplicate Values** → Repeated elements, same timestamps
6. **Order Issues** → Out-of-order data, backwards flow
7. **Special Characters** → Punctuation, whitespace, unicode
8. **Performance Edge Cases** → Very large inputs, many duplicates

### How to Discuss Edge Cases:

```
✅ GOOD: "Let me think about edge cases systematically:
         - Empty input: returns true/none/0
         - Single element: [explain behavior]
         - Boundary values: [explain limits]
         - Invalid data: [explain validation]"

❌ BAD:  "I think I covered everything."
```

### What NOT to Do:

- ❌ Don't say "I can't think of any more edge cases"
- ❌ Don't skip testing edge cases in your code
- ❌ Don't assume valid input without asking
- ❌ Don't implement without discussing approach first

### What TO Do:

- ✅ Test your code with edge cases OUT LOUD
- ✅ Write test cases BEFORE coding (if time allows)
- ✅ Ask clarifying questions about edge cases
- ✅ Mention how you'd handle invalid input

---

## 📊 Interview Success Formula

```
Success = Clean Code (40%) + Test Cases (30%) + Edge Cases (20%) + Clear Explanation (10%)
```

**Key Takeaway from 1point3acres:**
> "Candidates who failed often said: 'I didn't test enough edge cases' or 'I missed the punctuation/formatting edge case.' Write tests and run your code!"

**Good luck! 🍀**
