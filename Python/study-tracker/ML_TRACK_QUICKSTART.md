# ML Track Quick Start Guide

Welcome to your new **ML Engineering** track! This guide will help you start using the ML specialist curricula.

## What's New?

You now have **3 specialized ML tracks** for Staff/Principal ML Engineer interviews:

1. **🤖 ML Algorithms** (14 days)
   - Deep learning: neural nets, CNNs, RNNs, transformers, GANs
   - Classical ML: trees, boosting, SVMs, linear models
   - Advanced: embeddings, dimensionality reduction, model compression

2. **🏗️ ML System Design** (14 days)
   - Production systems: recommendations, search, ads, CV, NLP
   - Infrastructure: training, serving, feature stores, monitoring
   - Strategy: platforms, lifecycle management, ROI

3. **🎯 Recommendations Deep Dive** (14 days)
   - Architecture: retrieval, ranking, re-ranking
   - Algorithms: collaborative filtering, matrix factorization
   - Deep learning: two-tower, sequential models, graph-based
   - Advanced: cold start, bandits, LLM integration

## Quick Start

### 1. Start the Application
```bash
cd study-tracker
make run
```

Open http://localhost:5555 in your browser.

### 2. Switch to ML Track
Click **🤖 ML** in the navigation bar (top left, next to "Track:")

You should see three sections:
- ML Algorithms - Day 1
- ML System Design - Day 1
- Recommendations - Day 1

### 3. Study Your First ML Topic

**Day 1 Topics:**
- **ML Algorithms**: Neural Network Fundamentals
  - Forward propagation, backpropagation
  - Activation functions (ReLU, sigmoid, tanh)
  - Loss functions and gradient descent
  - Practice: Explain vanishing gradients, derive backprop

- **ML System Design**: Recommendation System Architecture
  - Three-stage funnel (retrieval → ranking → re-ranking)
  - Candidate generation strategies
  - Ranking model design
  - Practice: Design a video recommendation system

- **Recommendations**: Intro to RecSys & Problem Framing
  - Explicit vs implicit feedback
  - Evaluation metrics (precision@K, NDCG, MRR)
  - Business objectives and constraints
  - Practice: Tradeoffs between accuracy and diversity

### 4. Complete Topics

1. Read through the topic content and practice questions
2. Click "Mark as Complete"
3. Rate difficulty (1-5): How challenging was this topic?
4. Add notes: Key insights, things to review
5. System automatically schedules reviews at 1, 3, 7, 14 days

### 5. Spaced Repetition Reviews

After completing a topic, you'll see reviews appear on future days:
- **Day 2**: 1-day review (quick refresh)
- **Day 4**: 3-day review (moderate depth)
- **Day 8**: 7-day review (full recall)
- **Day 15**: 14-day review (long-term retention)

Each review shows practice questions to test your understanding.

## Study Strategy

### For ML Algorithms Track

Focus on **conceptual understanding** + **mathematical derivations**:
- Can you explain the algorithm to a peer?
- Can you derive key formulas (backprop, attention, SVM dual)?
- Do you understand when to use which algorithm?
- Can you discuss tradeoffs (bias-variance, capacity, speed)?

**Practice questions format:**
- Concepts: "Explain dropout. Why does it prevent overfitting?"
- Tradeoffs: "When would you use LSTM vs. Transformer?"
- Derivations: "Derive the gradient for cross-entropy loss"

### For ML System Design Track

Focus on **production engineering** + **system architecture**:
- How would you scale to 1B users?
- What are the latency/throughput requirements?
- How do you handle training data drift?
- What monitoring metrics are critical?

**Practice questions format:**
- Estimation: "Estimate compute for training a 175B parameter model"
- Concepts: "Explain feature store architecture and benefits"
- Tradeoffs: "When to use batch vs. online serving?"
- Scenarios: "Design a real-time fraud detection system"

### For Recommendations Deep Dive

Focus on **modern techniques** + **production experience**:
- How do the retrieval, ranking, re-ranking stages differ?
- What are pros/cons of different embedding methods?
- How do you handle cold start problems?
- How do you balance exploration vs. exploitation?

**Practice questions format:**
- Concepts: "Explain negative sampling in two-tower models"
- Tradeoffs: "Matrix factorization vs. deep learning for RecSys"
- Scenarios: "Design recommendations for a new e-commerce site"

## Time Estimates

Each track estimates **60-90 minutes per day**:
- Reading and understanding: 30-40 min
- Working through practice questions: 20-30 min
- Making notes and connections: 10-20 min

**Total daily commitment** (all 3 ML tracks): **3-4.5 hours**

You can choose to:
- Do all 3 tracks in parallel (intensive ML prep)
- Focus on 1-2 tracks based on interview needs
- Interleave with general SWE tracks

## Switching Between SWE and ML

Use the track switcher to toggle between your tracks:

- **💻 SWE**: General software engineering (coding + system design)
- **🤖 ML**: ML specialist (ml_algorithms + ml_system_design + recommendations)

Each track group has completely separate:
- Progress tracking
- Review schedules
- Completion history

This allows you to:
- Prepare for both SWE and ML roles simultaneously
- Switch focus based on upcoming interviews
- Maintain clear separation of different prep areas

## Example Daily Schedule

**Morning (ML Focus):**
- 08:00 - 09:00: ML Algorithms topic + practice
- 09:00 - 10:00: ML System Design topic + practice
- 10:00 - 10:30: Break
- 10:30 - 11:30: Recommendations topic + practice

**Afternoon (SWE Focus):**
Switch to 💻 SWE track
- 14:00 - 15:00: Coding pattern (LeetCode problems)
- 15:00 - 16:00: System design concepts

**Evening (Reviews):**
- 19:00 - 20:00: Complete due reviews (both SWE and ML)

## Tips for Success

### 1. Understand, Don't Memorize
ML interviews test **deep understanding**, not rote memorization:
- Can you explain the intuition behind an algorithm?
- Can you discuss real-world applications and limitations?
- Can you compare alternatives and justify choices?

### 2. Connect to Production
Always think about **real-world deployment**:
- How would this scale?
- What could go wrong in production?
- How would you monitor this in prod?
- What are the computational costs?

### 3. Practice Explaining Out Loud
ML interviews often involve whiteboarding:
- Explain algorithms as if teaching someone
- Draw diagrams for system architectures
- Verbalize your thought process

### 4. Review Consistently
The spaced repetition schedule is optimized for retention:
- Don't skip reviews (they're quick, 10-15 min each)
- Mark reviews complete after answering questions
- Add notes on topics that still feel shaky

### 5. Cross-Reference Your Materials
The curricula are extracted from your LaTeX study guides:
- **ml-algorithm-study-guide.pdf** - Deep reference for algorithms
- **ml-algorithm-templates-cheatsheet.pdf** - Quick formulas
- **ml-system-design-study-guide.pdf** - System design patterns
- **ml-system-design-templates-cheatsheet.pdf** - Architecture templates
- **recommendation-systems-deep-dive.pdf** - Comprehensive RecSys guide

Use these PDFs for deeper study when needed.

## Customization

### Adjust Start Dates
If you want to start tracks on different dates:
1. Go to "⚙️ Config" page
2. Find "ML Algorithms", "ML System Design", or "Recommendations"
3. Set your preferred start date
4. Save changes

### Accelerate Progress
If you want to skip ahead:
1. Go to "⚙️ Config"
2. Set "acceleration_days" for a track (e.g., 5 to skip to day 6)
3. This is useful if you've already studied certain topics

### Modify Review Intervals
Default is 1, 3, 7, 14 days. To change:
1. Edit `data/ml_specialist/config.json`
2. Modify `settings.review_intervals` array
3. Restart the application

## Troubleshooting

**Q: I see "No topic for day X"**
- The ML tracks are 14-day curricula (vs. 28 days for SWE)
- After day 14, focus on reviews and reinforcement

**Q: Practice questions not showing**
- ML tracks use system-design-style practice questions
- Check that you're on the correct track (not coding track)
- Questions are randomly sampled based on review type

**Q: Want to focus on only one ML track**
- You can skip topics by marking them complete without studying
- Or just ignore tracks you're not focused on
- Progress is tracked independently per track

**Q: Reviews piling up**
- Prioritize reviews over new learning (they're quick)
- Reviews are critical for retention
- Aim to complete all reviews daily

## Next Steps

1. **Complete Day 1** of all ML tracks (or choose your focus tracks)
2. **Review tomorrow** - You'll see 1-day reviews for completed topics
3. **Establish routine** - Consistency is key for spaced repetition
4. **Track progress** - Use the History page to see your completion patterns
5. **Adjust as needed** - The system is flexible to your interview timeline

---

**Good luck with your ML interview preparation! 🚀**

Remember: The goal is not to memorize everything, but to build **deep understanding** and **production intuition** for Staff/Principal-level ML roles.
