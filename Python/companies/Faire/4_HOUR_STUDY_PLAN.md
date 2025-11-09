# 🎯 4-Hour Faire Interview Prep Plan

**Interview:** Tomorrow
**Time Available:** 4 hours
**Focus:** Top 3-4 verified problems from 1point3acres (2021-2025)

---

## ⏰ Hour 1: HTML/Tag Validator (MOST IMPORTANT - Asked 5+ times)

**Goal:** Implement stack-based validation with correct `{{ }}` syntax

### Tasks:
- [ ] **0:00-0:15** Read `EXPLAIN_TOP_PROBLEMS.md` - HTML Validator section
- [ ] **0:15-0:50** Implement solution in `01_html_format_validation_solution.py`
  - Use stack to track opening tags
  - Look for `{{` and `}}` (not single `{`)
  - Check for `#` (opening) or `/` (closing) prefix
  - Single braces = normal text (ignore them!)
  - Validate LIFO order
- [ ] **0:50-1:00** Run tests and debug edge cases
  - Incomplete tags (missing `}}`)
  - Single braces as text
  - Wrong closing order
  - Only opening or only closing tags

### Key Takeaways:
```python
# The pattern you MUST know:
1. Scan for "{{" (not "<")
2. Find matching "}}"
3. Extract: s[i+2:j].strip()
4. If starts with "#": stack.append(tag_name)
5. If starts with "/": check stack[-1] == tag_name
6. Single "{" or "}" → skip (normal text!)
```

---

## ⏰ Hour 2: Haiku Finder (MOST IMPORTANT - Asked 5+ times)

**Goal:** Understand and implement the O(n) prefix sum solution

### Tasks:
- [ ] **1:00-1:15** Read `EXPLAIN_TOP_PROBLEMS.md` - Haiku section
- [ ] **1:15-1:50** Implement solution in `02_haiku_finder_solution.py`
  - Build prefix sum array
  - Create hash map for O(1) lookup
  - Handle punctuation (strip before lookup, preserve in output)
  - Handle case (lowercase for lookup, preserve original)
- [ ] **1:50-2:00** Run tests and debug edge cases
  - Empty string
  - No valid haiku found
  - Words missing from dictionary
  - Multiple valid haikus (return FIRST one)

### Key Takeaways:
```python
# The pattern you MUST know:
1. Clean words: word.strip(string.punctuation).lower()
2. Build prefix: prefix[i] = sum of syllables from 0 to i-1
3. Hash map: {prefix_sum: index}
4. Find: start + 5, start + 12, start + 17
5. Preserve: Original case and punctuation in output
```

---

## ⏰ Hour 3: Funnel + Anagrams (Round out top problems)

**Goal:** Quick review of remaining high-priority problems

### Tasks:
- [ ] **2:00-2:20** Anagram Grouping (Asked 3+ times - Verified)
  ```python
  # Super simple - make sure you know it:
  from collections import defaultdict

  def groupAnagrams(strs):
      groups = defaultdict(list)
      for s in strs:
          key = ''.join(sorted(s))  # "eat" → "aet"
          groups[key].append(s)
      return list(groups.values())
  ```
  - Time: O(n * k log k)
  - Alternative: Character count as key for O(n * k)
  - Test with: ["eat", "tea", "tan", "ate", "nat", "bat"]

- [ ] **2:20-2:50** Funnel Problem (Asked 4+ times)
  - Read the problem description
  - Understand: Users must go through steps IN ORDER
  - Practice explaining the approach
  - Don't need to code - just understand the logic

- [ ] **2:50-3:00** Break! Walk around, hydrate

---

## ⏰ Hour 4: Test Cases + Mock Practice

**Goal:** Be ready to answer "What other edge cases?"

### Tasks:
- [ ] **3:00-3:20** Write comprehensive test cases for Haiku:
  ```python
  # Edge cases to mention:
  1. Empty string → no haiku found
  2. All words missing from dict → no haiku
  3. Sentence shorter than 3 words → no haiku
  4. Multiple valid haikus → return FIRST one
  5. Punctuation: "Void." vs "void" in dict
  6. Case: "Simple" vs "simple" in dict
  7. Multiple punctuation: "don't" → "dont"
  8. No spaces between punctuation: "word."
  ```

- [ ] **3:20-3:40** Write comprehensive test cases for HTML:
  ```python
  # Edge cases to mention:
  1. Empty string → True (no tags to validate)
  2. Only text, no tags → True
  3. Single { or } → True (normal text)
  4. {{ without matching }} → False
  5. Only opening tags → False
  6. Only closing tags → False
  7. Wrong order → False (must be LIFO)
  8. Nested same-name tags → True if properly closed
  9. Extra closing tag → False
  10. Tag with spaces: "{{ #abc }}" → valid
  ```

- [ ] **3:40-4:00** Mock Interview Practice:
  1. Set 10-minute timer
  2. Explain Haiku approach out loud (as if to interviewer)
  3. Explain HTML validator approach out loud
  4. Practice saying: "Let me think about edge cases..."
  5. List 3-4 edge cases for each problem OUT LOUD

---

## 📋 Interview Day Checklist (Tomorrow Morning)

### 30 Minutes Before Interview:
- [ ] Review `INTERVIEW_TOMORROW_CHEAT_SHEET.md` (10 min)
- [ ] Skim your implemented solutions (5 min)
- [ ] Review edge cases list above (5 min)
- [ ] Practice explaining approach out loud (5 min)
- [ ] Deep breath! You've got this! (5 min)

---

## 🎯 What to Say During Interview

### When Given the Problem:
1. "Let me make sure I understand the input format..."
2. "Are there any constraints on input size?"
3. "What should I return if no valid result exists?"
4. "Can I assume the input is valid, or should I handle errors?"

### Before Coding:
1. "Let me explain my approach..."
2. "I'm thinking of using [prefix sum / stack / hash map]..."
3. "The time complexity would be O(n)..."
4. "Does this approach sound good before I start coding?"

### After Coding:
1. "Let me test this with the example..."
2. "Now let me think about edge cases..."
3. [List 3-4 edge cases from your practice]
4. "Would you like me to add any additional test cases?"

### If Stuck:
1. "I'm thinking through a few approaches..."
2. "Could you give me a hint about [specific part]?"
3. DON'T: Sit in silence
4. DO: Think out loud

---

## 🔑 SUCCESS FORMULA

```
RIGHT ANSWER = Working Code + Test Cases + Edge Cases + Clear Explanation

Interviewers care about:
1. Does your code work? (40%)
2. Did you test it? (30%)
3. Did you think of edge cases? (20%)
4. Can you explain it clearly? (10%)
```

**Remember:** According to 1point3acres, candidates who failed often said:
- "I didn't write enough test cases"
- "I missed the edge case for [punctuation/incomplete tags/etc]"
- "I should have run my code"

**You will succeed if you:**
- Write clean, working code
- Test thoroughly
- Think out loud
- Ask clarifying questions

---

## ⚡ Quick Reference

### Haiku: O(n) Pattern
```python
prefix = [0] + cumulative syllable counts
sum_to_idx = {sum: idx for idx, sum in enumerate(prefix)}
find: start+5, start+12, start+17 in hash map
```

### HTML: Stack Pattern
```python
if "{{": find "}}", check if "#" or "/"
if "#": stack.append(tag_name)
if "/": check stack[-1] == tag_name, then pop
single "{": skip (normal text)
```

### Anagrams: Hash Map Pattern
```python
key = ''.join(sorted(word))
groups[key].append(word)
```

---

**YOU'VE GOT THIS! 💪**

The problems are well-defined. You have the patterns. You have the edge cases.

Just execute tomorrow!

Good luck! 🍀
