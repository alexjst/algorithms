# Faire Interview Practice - File Structure

## How It Works

Each problem has TWO files:

### 1. Scaffolding File (XX_problem_name.py) - READ ONLY
- Contains problem description
- Contains all test cases  
- Imports your solution
- Run this file to test: `python 01_group_anagrams.py`

### 2. Solution File (XX_problem_name_solution.py) - YOU EDIT THIS
- Contains only function signatures
- This is where you implement your solution
- Reset anytime to practice again

## Example Workflow

```bash
# Work on problem 1
python 01_group_anagrams.py
# ❌ Tests fail (solution not implemented)

# Edit the solution file
vim 01_group_anagrams_solution.py
# Implement your solution...

# Test again
python 01_group_anagrams.py
# ✓ All tests passed!

# Practice again later - just reset the solution file
cp 01_group_anagrams_solution.py 01_group_anagrams_solution.py.backup
# Edit fresh...
```

## All Problems (Verified from 1point3acres)

### Top Priority (Asked 3+ times):
1. **01_group_anagrams** - Hash map grouping (LC 49)
2. **02_html_format_validation** - Stack-based tag matching with `{{ #tag }}` format
3. **03_haiku_finder** - Find 5-7-5 syllable pattern in sentence (O(n) prefix sum)
4. **04_funnel_problem** - User conversion funnel analysis
5. **05_number_to_word_conversion** - Convert numbers 1-1000 to English words
6. **13_ads_assortment_problem** - Weekly ad limits per user/brand

### Medium Priority (Asked 1-2 times):
7. **06_course_schedule_min_time** - Topological sort + time calculation
8. **09_maze_with_portals** - BFS with teleportation

**Total: 8 verified problems**

Happy practicing! 🚀
