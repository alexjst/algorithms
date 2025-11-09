# ClickUp Backend Engineer Interview Prep

Comprehensive preparation materials for ClickUp backend engineering interviews.

## 📁 Structure

This folder contains **practice problems** and **comprehensive documentation** for ClickUp interviews.

### Practice Files (Separated for Easy Reset)

Each problem has **TWO files**:

1. **`XX_problem_name.py`** - Scaffolding file with tests (DON'T EDIT)
2. **`XX_problem_name_solution.py`** - Your implementation (EDIT THIS)

## 🎯 How to Practice

### First Time
```bash
# 1. Read the problem in the scaffolding file or PDF
# 2. Implement your solution in the _solution.py file
# 3. Run tests
python 01_two_sum.py
```

### To Practice Again
```bash
# Simply reset the solution file (keep scaffolding)
rm 01_two_sum_solution.py
# Or manually clear your code and start fresh
```

## 📝 Problems List

### Backend Problems (Based on Real ClickUp Interviews)

1. **Two Sum** - Hash maps, confirmed in interviews
2. **Combination Sum** - Backtracking, confirmed variation
3. **Task Dependency Resolution** - Graphs, topological sort (ClickUp tasks)
4. **API Rate Limiter** - System design, sliding window

## 📖 Complete Documentation

See `clickup_interview_questions.pdf` for:
- Complete problem descriptions
- Full solutions with explanations
- Time/space complexity analysis
- Test cases and edge cases
- Interview tips and strategies

## 🔧 Tech Stack Focus

ClickUp uses:
- Node.js / TypeScript / Express
- Microservices architecture
- Docker & Kubernetes (EKS)
- Focus on API design and scalability

## 💡 Interview Process

1. **Technical Recruiter** - Initial screen
2. **Take-Home Assignment** (~1hr Node.js API)
3. **Technical Interview** - LeetCode medium + technical discussion
4. **System Design** - Design part of ClickUp
5. **Cultural Fit** - Fast-paced environment assessment

## 🎓 Preparation Tips

### Master These Topics:
- Hash maps and arrays (Two Sum variations)
- Graph algorithms (task dependencies)
- Backtracking (combination problems)
- API design patterns
- Rate limiting and caching
- Microservices concepts

### Technical Discussion Topics:
- JavaScript Event Loop
- Async/await patterns
- Microservices architecture
- Database optimization
- API security

### Practice Strategy:
1. Solve all problems without looking at solutions
2. Compare your solution with provided optimal solution
3. Understand time/space complexity tradeoffs
4. Practice explaining your approach out loud

## 📚 Additional Resources

- **LeetCode**: Focus on medium difficulty, graphs, and backtracking
- **Node.js Docs**: Study async patterns and streams
- **System Design**: "Designing Data-Intensive Applications"
- **ClickUp Blog**: Read about their engineering challenges

## ✅ Testing Your Solutions

All problems include comprehensive test suites:
```bash
# Run individual problem
python 01_two_sum.py

# Check all problems
for file in 0*_*.py; do
    [ "$file" != *"_solution.py" ] && python "$file"
done
```

## 🚀 Quick Start Example

```python
# 1. Open 01_two_sum_solution.py
# 2. Implement the function:

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# 3. Run tests:
# python 01_two_sum.py
#
# Output:
# ✓ Test 1 passed: Basic case
# ✓ Test 2 passed: Numbers not in order
# ...
# All tests passed! ✓
```

## 📞 Good Luck!

Remember: ClickUp values **speed**, **quality**, and **ability to work in a fast-paced environment**. Show your problem-solving skills and enthusiasm for their product!
