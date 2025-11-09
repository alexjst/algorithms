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

## All 14 Problems

1. 01_group_anagrams - Hash map grouping
2. 02_html_format_validation - Stack-based tag matching
3. 03_haiku_finder - Syllable counting (5-7-5)
4. 04_funnel_problem - Conversion funnel analysis
5. 05_number_to_word_conversion - Number to English words
6. 06_course_schedule_min_time - Topological sort
7. 07_max_consecutive_ones - Simple iteration
8. 08_date_format_function - Date parsing/validation
9. 09_maze_with_portals - BFS with teleportation
10. 10_string_parsing_problem - Log parsing with regex
11. 11_array_divisibility_check - Modular arithmetic
12. 12_digit_frequency_counter - Frequency counting
13. 13_ads_assortment_problem - 0/1 Knapsack DP
14. 14_object_manipulation - ProductCatalog class

Happy practicing! 🚀
