# 🚨 FAIRE INTERVIEW TOMORROW - QUICK REFERENCE

**Based on 15+ actual candidate reports (2021-2025) from 1point3acres.com**

---

## 🔥 TOP 3 MOST ASKED (Practice These First!)

### 1. ⭐⭐⭐⭐⭐ HAIKU FINDER (Asked 5+ times)

**What they give you:**
- A sentence: `"Internationalization a Simple flower Petals shine Vibrant don't Pure Stares into Void. Return home"`
- A dictionary: `{"internationalization": 8, "a": 1, "simple": 2, "flower": 2, ...}`

**What to return:**
```python
["a Simple flower",              # 5 syllables
 "Petals shine Vibrant don't Pure",  # 7 syllables
 "Stares into Void."]            # 5 syllables
```

**⚡ Quick Solution:**
1. Split sentence → words
2. For each word: `clean_word = word.strip(punctuation).lower()` → lookup in dict
3. Build prefix sum array
4. Use hash map: `sum_to_index = {sum: index}`
5. For each position i, find where sum = start + 5, start + 12, start + 17
6. **PRESERVE ORIGINAL CASE/PUNCTUATION IN OUTPUT!**

**🎯 Key Points:**
- **O(n) solution expected** (prefix sum + hash map)
- Strip punctuation BEFORE lookup, preserve AFTER
- Convert to lowercase for lookup
- Edge cases: empty string, no valid haiku, missing words in dict

**File:** `03_haiku_finder.py` ✅ UPDATED

---

### 2. ⭐⭐⭐⭐⭐ TAG VALIDATOR (Asked 5+ times)

**NOT standard HTML! Uses {{ }} syntax**

**Valid:**
```
"{{ #abc }} {{ #cba }} hello world {{ /cba }} {{ /abc }}" → True
"{{ #abc }} hello { world {{ /abc }}" → True (single { is OK!)
```

**Invalid:**
```
"{{ #abc }} {{ /abc" → False (incomplete tag)
"{{ #abc }} {{ #cba }} {{ /cba }}" → False (missing /abc)
"{{ #abc }} {{ #cba }} {{ /abc }} {{ /cba }}" → False (wrong order)
```

**⚡ Quick Solution:**
1. Parse string, look for `{{`
2. Find matching `}}`
3. Extract tag: if starts with `#` → opening tag (push to stack)
4. If starts with `/` → closing tag (must match top of stack, pop)
5. Single `{` or `}` is normal text (ignore)
6. Stack must be empty at end

**🎯 Key Points:**
- **Use STACK**
- Edge case: `{{` without space (double brace)
- Interviewer WILL ask: "What other edge cases?"
- Similar to LC 591 but **DIFFERENT syntax**!

**File:** `02_html_format_validation.py` ✅ UPDATED

---

### 3. ⭐⭐⭐⭐ ANAGRAM GROUPING (Asked 3+ times)

Standard LC 49 - Group words that are anagrams.

**⚡ Quick Solution:**
```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))  # or use char count as key
        groups[key].append(s)
    return list(groups.values())
```

**🎯 Key Points:**
- **MUST be optimal** (not brute force)
- Time: O(n * k log k) where k = max word length
- Alternative: Use character count as key for O(n * k)

**File:** `01_group_anagrams.py` ✅ EXISTS

---

## 📊 OTHER FREQUENTLY ASKED

### 4. ⭐⭐⭐ Funnel Problem (Asked 4+ times)

Track user events through multi-step funnels:
- Input: Event log `(user_id, step_id, timestamp)`
- Input: Funnel definitions
- Output: Count users at each step
- **Key:** Users must follow steps IN ORDER

**File:** `04_funnel_problem.py`

---

### 5. ⭐⭐⭐ Ads Assortment (Asked 3+ times)

**Rules:**
- Each recipient: max 1 ad/week from same brand
- Each recipient: max 3 total ads/week

**Input:** Past ads + future ads
**Output:** Which users to block for each new ad

**File:** `13_ads_assortment_problem.py`

---

### 6. ⭐⭐⭐ Number to Word (Asked 3+ times)

Convert numbers to words, sum lengths:
```python
Input: 1 to 1000
1 → "one" (3), 2 → "two" (3), ...
Output: Sum of all word lengths
```

**File:** `05_number_to_word_conversion.py`

---

## 💡 CRITICAL INTERVIEW INSIGHTS FROM 1POINT3ACRES

### 🚨 Why Candidates Failed:

1. **Not enough test cases** (mentioned by 5+ candidates)
   - Interviewers use JUnit
   - They WILL ask: "What other edge cases?"
   - Write tests BEFORE coding

2. **Punctuation handling** (Haiku, HTML validator)
   - Must strip before lookup
   - Must preserve in output

3. **Wrong optimization**
   - Brute force may pass but optimal expected
   - Know your time complexity

4. **Regex edge cases** (HTML validator)
   - One candidate failed for `{{` case
   - Test double braces, single braces

### ✅ How to Succeed:

1. **Ask clarifying questions:**
   - Input format/constraints?
   - Edge cases?
   - Optimize for time or space?

2. **Think out loud:**
   - Explain your approach
   - Mention optimizations
   - Discuss trade-offs

3. **Write comprehensive tests:**
   - Empty input
   - Single element
   - Duplicates
   - Edge cases
   - Large input

4. **Run your code:**
   - They want to see it execute
   - Use pytest or similar

5. **Optimize iteratively:**
   - Start with working solution
   - Then optimize if time

---

## 🎯 TOMORROW'S STRATEGY

### Before Interview:
- [ ] Review Haiku Finder (highest priority!)
- [ ] Review HTML/Tag Validator (highest priority!)
- [ ] Quick review Anagrams
- [ ] Skim Funnel, Ads, Number to Word

### During Interview:

**First 2 minutes:**
1. Clarify the problem
2. Ask about input format
3. Ask about edge cases
4. Confirm expected output format

**Next 5 minutes:**
1. Explain your approach
2. Discuss time/space complexity
3. Get confirmation before coding

**Coding (40 minutes):**
1. Write clean, readable code
2. Add comments for complex parts
3. Handle edge cases explicitly
4. Use meaningful variable names

**Last 10 minutes:**
1. Write test cases
2. Run your code
3. When asked "other edge cases?":
   - Empty input
   - Single element
   - Duplicates
   - Boundary values
   - Invalid input

---

## 📋 QUICK SYNTAX REFERENCE

### Stack (for HTML validator):
```python
stack = []
stack.append(item)  # push
stack.pop()         # pop
stack[-1]           # peek top
len(stack) == 0     # is empty
```

### Prefix Sum (for Haiku):
```python
prefix = [0]
for val in values:
    prefix.append(prefix[-1] + val)

# Sum from i to j (exclusive)
range_sum = prefix[j] - prefix[i]
```

### Hash Map (for Anagrams):
```python
from collections import defaultdict
groups = defaultdict(list)
groups[key].append(value)
```

### String Processing (for Haiku):
```python
import string
word.strip(string.punctuation)  # remove punctuation
word.lower()                    # to lowercase
s.split()                       # split by spaces
" ".join(words)                 # join with spaces
```

---

## 🔑 MOST IMPORTANT TIPS

1. **Haiku & HTML Validator are GOLD** - likely to get one of these
2. **Test cases matter MORE than you think**
3. **They WILL ask "what other edge cases?"** - have answers ready
4. **Preserve formatting** (case, punctuation) when required
5. **Use STACK for nesting problems**
6. **Use PREFIX SUM for range queries**

---

## ⏰ TIME MANAGEMENT

- **1-2 min:** Understand problem
- **3-5 min:** Explain approach
- **30-40 min:** Code + handle edge cases
- **10-15 min:** Write & run tests

**Don't:**
- Rush into coding without planning
- Skip edge case handling
- Forget to run your code
- Give up if stuck (ask for hints!)

**Do:**
- Think out loud
- Write clean code
- Test thoroughly
- Ask questions

---

## 🎬 FINAL CHECKLIST FOR TOMORROW

Morning of interview:
- [ ] Quick review Haiku solution (10 min)
- [ ] Quick review HTML validator (10 min)
- [ ] Review edge cases for both (5 min)
- [ ] Practice explaining your approach out loud (5 min)

**You've got this! The problems are well-defined, you have the patterns, just execute! 💪**

---

**Good luck! 🍀**
