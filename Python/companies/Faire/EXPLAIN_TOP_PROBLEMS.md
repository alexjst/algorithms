# Understanding the Top 3 Faire Problems

## 🎯 Problem 1: Haiku Finder (MOST IMPORTANT)

### What is it?
Find the FIRST sequence of consecutive words that form a 5-7-5 syllable pattern.

### The Problem in Plain English:
```
You get:
- A long sentence: "Internationalization a Simple flower Petals shine Vibrant don't Pure Stares into Void. Return home"
- A dictionary telling you syllable counts: {"internationalization": 8, "a": 1, "simple": 2, ...}

You need to find:
- 3 consecutive groups of words that have 5, 7, and 5 syllables

Answer:
- Line 1: "a Simple flower" = 1 + 2 + 2 = 5 ✓
- Line 2: "Petals shine Vibrant don't Pure" = 2 + 1 + 2 + 1 + 1 = 7 ✓
- Line 3: "Stares into Void." = 2 + 2 + 1 = 5 ✓
```

### Why is this tricky?
1. **Punctuation:** "Void." has a period, but you look up "void" (lowercase, no punctuation)
2. **Case:** "Simple" is capitalized, but you look up "simple" (lowercase)
3. **Preserve original:** Output must have "Simple" and "Void." with original formatting
4. **Efficiency:** Can't check all combinations - need O(n) solution

### The O(n) Solution Pattern:
```python
# Step 1: Parse words and get syllables
words = sentence.split()
syllables = []
for word in words:
    clean = word.strip(punctuation).lower()  # "Void." → "void"
    count = syllable_dict.get(clean, 0)      # look up
    syllables.append(count)

# Step 2: Build prefix sum
# prefix[i] = total syllables from word 0 to i-1
prefix = [0]
for syl in syllables:
    prefix.append(prefix[-1] + syl)

# Now: prefix = [0, 8, 9, 11, 13, 15, 16, 18, 19, 20, 22, 24, 25, 27, 28]
#      words  = ["Internationalization", "a", "Simple", "flower", "Petals", ...]

# Step 3: Use hash map for O(1) lookup
sum_to_index = {prefix[i]: i for i in range(len(prefix))}

# Step 4: For each starting position, check if we can form 5-7-5
for i in range(len(prefix)):
    start_sum = prefix[i]

    # Can we find positions where we have +5, +12, +17 syllables?
    end_line1 = sum_to_index.get(start_sum + 5)   # Find where sum = start + 5
    end_line2 = sum_to_index.get(start_sum + 12)  # Find where sum = start + 12
    end_line3 = sum_to_index.get(start_sum + 17)  # Find where sum = start + 17

    if all three exist and are in order:
        # Found it! Build the answer
        line1 = " ".join(words[i:end_line1])
        line2 = " ".join(words[end_line1:end_line2])
        line3 = " ".join(words[end_line2:end_line3])
        return [line1, line2, line3]
```

### Example walkthrough:
```
Sentence: "Internationalization a Simple flower Petals shine Vibrant don't Pure Stares into Void."
Syllables: [8, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1]
Prefix:    [0, 8, 9, 11, 13, 15, 16, 18, 19, 20, 22, 24, 25]

Start at position 1 (word "a"):
- prefix[1] = 8
- Need prefix[j] = 8 + 5 = 13  → j=4 → words[1:4] = ["a", "Simple", "flower"] ✓
- Need prefix[k] = 8 + 12 = 20 → k=9 → words[4:9] = ["Petals", "shine", "Vibrant", "don't", "Pure"] ✓
- Need prefix[m] = 8 + 17 = 25 → m=12 → words[9:12] = ["Stares", "into", "Void."] ✓

Found haiku!
```

---

## 🎯 Problem 2: HTML/Tag Validator

### What is it?
Check if custom tags are properly nested (like HTML, but with {{ }} syntax).

### The WRONG version (what you might have seen):
```
Standard HTML: <div><p>text</p></div>
```

### The CORRECT Faire version:
```
Opening tag: {{ #tagname }}
Closing tag: {{ /tagname }}

Valid: "{{ #abc }} {{ #def }} hello {{ /def }} {{ /abc }}"
       Open abc → Open def → Close def → Close abc (LIFO order)

Invalid: "{{ #abc }} {{ #def }} {{ /abc }} {{ /def }}"
         Open abc → Open def → Close abc (WRONG! Should close def first)
```

### Key Differences from Standard HTML:
1. **Syntax:** `{{ #tag }}` not `<tag>`
2. **Single braces OK:** `"{ text }"` is valid (treated as normal text)
3. **Must have spaces:** `{{ #abc }}` (with spaces)

### The Solution Pattern:
```python
def is_valid_tags(s):
    stack = []
    i = 0

    while i < len(s):
        # Look for opening {{
        if i < len(s) - 1 and s[i:i+2] == '{{':
            # Find closing }}
            j = i + 2
            while j < len(s) - 1:
                if s[j:j+2] == '}}':
                    # Found complete tag {{ ... }}
                    tag_content = s[i+2:j].strip()

                    if tag_content.startswith('#'):
                        # Opening tag
                        tag_name = tag_content[1:].strip()
                        stack.append(tag_name)
                    elif tag_content.startswith('/'):
                        # Closing tag
                        tag_name = tag_content[1:].strip()
                        if not stack or stack[-1] != tag_name:
                            return False  # Mismatch!
                        stack.pop()

                    i = j + 2
                    break
                j += 1
            else:
                # No closing }} found
                return False
        else:
            # Regular character (including single {)
            i += 1

    return len(stack) == 0  # All tags must be closed
```

### Example walkthrough:
```
Input: "{{ #abc }} {{ #def }} hello {{ /def }} {{ /abc }}"

Step 1: i=0, find "{{" → find "}}" at position 10
        Extract: " #abc " → tag_name = "abc"
        Action: stack.append("abc") → stack = ["abc"]

Step 2: i=11, find "{{" → find "}}" at position 21
        Extract: " #def " → tag_name = "def"
        Action: stack.append("def") → stack = ["abc", "def"]

Step 3: i=22, normal text "hello "

Step 4: i=34, find "{{" → find "}}" at position 44
        Extract: " /def " → tag_name = "def"
        Action: stack[-1] == "def" ✓ → stack.pop() → stack = ["abc"]

Step 5: i=45, find "{{" → find "}}" at position 55
        Extract: " /abc " → tag_name = "abc"
        Action: stack[-1] == "abc" ✓ → stack.pop() → stack = []

Result: stack is empty → return True
```

---

## 🎯 Problem 3: Group Anagrams

### What is it?
Group words that are anagrams of each other.

### Example:
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

### The Pattern:
```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        # Key idea: sorted("eat") = "aet", sorted("tea") = "aet"
        # Same sorted string → same group
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
```

**That's it!** This one is straightforward.

---

## 🎯 Problem 4: Funnel Problem

### What is it?
Track how many users complete each step in a multi-step process.

### Example:
```
Events:
- user1: Browse → View → Cart → Purchase
- user2: Browse → View
- user3: Browse

Funnel:
- Browse: 3 users (100%)
- View: 2 users (67% of Browse)
- Cart: 1 user (50% of View)
- Purchase: 1 user (100% of Cart)
```

### Key Rules:
1. Users must go through steps **in order** (can't skip)
2. Each user counted once per step
3. Track conversion rates between steps

This one is more about careful bookkeeping than algorithms.

---

## 📊 SUMMARY

**Haiku:** Prefix sum + hash map, preserve formatting
**HTML Validator:** Stack, `{{ #tag }}` syntax
**Anagrams:** Hash map with sorted string key
**Funnel:** Track user progression through ordered steps

Which ones do you want me to explain more?
