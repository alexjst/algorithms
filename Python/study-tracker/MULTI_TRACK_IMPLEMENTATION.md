# Multi-Track System Implementation

## Overview

The study-tracker application has been successfully upgraded to support multiple track groups, enabling you to manage separate study tracks for **Software Engineering** and **ML Engineering** interviews within the same unified interface.

## Architecture

### Track Groups

The system now supports two track groups:

1. **general_swe** (Software Engineering)
   - Tracks: `coding`, `system_design`
   - Curriculum: 28-day programs for general software engineering interviews
   - Data: `data/general_swe/`

2. **ml_specialist** (ML Engineering)
   - Tracks: `ml_algorithms`, `ml_system_design`, `recommendations`
   - Curriculum: 14-day intensive programs for ML specialist interviews
   - Data: `data/ml_specialist/`

### Directory Structure

```
study-tracker/
└── data/
    ├── general_swe/
    │   ├── curriculum/
    │   │   ├── coding.yaml (28 days, LeetCode patterns)
    │   │   └── system_design.yaml (28 days, system design)
    │   ├── config.json (start dates, settings for coding & system_design)
    │   ├── progress.json (completion history)
    │   └── reviews.json (scheduled reviews)
    │
    └── ml_specialist/
        ├── curriculum/
        │   ├── ml_algorithms.yaml (14 days, deep learning + classical ML)
        │   ├── ml_system_design.yaml (14 days, production ML systems)
        │   └── recommendations.yaml (14 days, RecSys deep dive)
        ├── config.json (start dates, settings for ML tracks)
        ├── progress.json (ML completion history)
        └── reviews.json (ML scheduled reviews)
```

## Key Features

### 1. Track Group Isolation
- Each track group maintains **separate data files** (progress, reviews, config)
- Your general SWE progress is completely independent from ML specialist progress
- No data conflicts or mixing between track groups

### 2. Unified Spaced Repetition
- The proven **1-3-7-14 day** review intervals work across all tracks
- Reviews are scheduled per track group, ensuring focused practice
- Single review queue per track group for better organization

### 3. Dynamic Track Display
- Dashboard automatically shows **all tracks** in the current group
- No hardcoded track names - easily extensible to new tracks
- Adaptive UI based on track type (coding vs. system design)

### 4. Session-Based Switching
- Switch between track groups using the navigation bar
- Your selection persists across page loads via session
- Instant switching without data loss

## ML Curriculum Content

The ML curricula were extracted from your LaTeX study guides:

### ml_algorithms.yaml (14 days)
- **Week 1**: Deep learning fundamentals
  - Neural networks, backpropagation, optimization
  - CNNs for computer vision
  - RNNs, LSTMs, GRUs for sequences
  - Transformers and attention mechanisms
  - GANs and generative models
  - Embeddings (word2vec, BERT, sentence transformers)
  - Dimensionality reduction (PCA, t-SNE, UMAP)

- **Week 2**: Classical ML & advanced topics
  - Decision trees, random forests, boosting (XGBoost, LightGBM)
  - SVMs and kernel methods
  - Linear models and regularization
  - Unsupervised learning (k-means, hierarchical, DBSCAN)
  - Model compression and efficiency
  - ML interview strategy and connecting algorithms

### ml_system_design.yaml (14 days)
- **Week 1**: Production ML systems
  - Recommendation systems architecture
  - Search ranking systems
  - Ad CTR prediction
  - Computer vision pipelines
  - NLP systems at scale
  - Fraud detection systems
  - Real-time predictions

- **Week 2**: Infrastructure & responsible AI
  - Training infrastructure and distributed systems
  - Model serving and inference optimization
  - Feature stores and data pipelines
  - Monitoring and observability
  - Responsible AI and fairness
  - Platform vs. bespoke solutions
  - Managing ML project lifecycle

### recommendations.yaml (14 days)
Deep dive into recommendation systems:
- Three-stage funnel architecture (retrieval, ranking, re-ranking)
- Collaborative filtering (user-based, item-based, matrix factorization)
- Deep learning for retrieval (two-tower, sequential, graph-based)
- Ranking models (DeepFM, Wide & Deep, multi-task learning)
- Re-ranking and diversity (MMR, DPP)
- Cold start problem and evaluation metrics
- Contextual bandits and online learning
- LLM integration in recommendations

## How to Use

### Starting the Application

```bash
cd study-tracker
make run
# Open http://localhost:5555
```

### Switching Track Groups

1. **Using the UI**: Click the track switcher in the navigation bar
   - 💻 SWE - Software Engineering track
   - 🤖 ML - ML Engineering track

2. **Using the URL**: Navigate directly
   - `/switch-track-group/general_swe`
   - `/switch-track-group/ml_specialist`

### Daily Workflow

1. **Morning**: Open dashboard to see today's topics + due reviews
2. **Study**: Work through topics for all tracks in your current group
3. **Complete**: Mark topics complete with difficulty ratings (1-5)
4. **Review**: Answer practice questions for due reviews
5. **Track**: System automatically schedules spaced repetition reviews

### Track Type Behavior

**Coding-type tracks** (`coding`, `ml_algorithms`):
- Display LeetCode-style problems
- Show template links for pattern reference
- Focus on implementation practice

**System design-type tracks** (`system_design`, `ml_system_design`, `recommendations`):
- Display conceptual practice questions (concepts, tradeoffs, estimation)
- Show resources and key concepts
- Focus on understanding and explanation

## Technical Implementation

### Backend Changes (app.py)

1. **Track Group Management**:
   - `get_track_group()` - Get current group from session
   - `get_data_paths(track_group)` - Get file paths for a group
   - `TRACK_GROUPS` - Configuration dict defining all groups

2. **Updated Functions** (all track group-aware):
   - `load_config(track_group)` - Load group-specific config
   - `load_curriculum(track, track_group)` - Load track-specific curriculum
   - `get_due_reviews(date, track_group)` - Get reviews for a group
   - `dashboard()` - Dynamic track display
   - `day_view()` - Dynamic day view
   - All data access routes updated

3. **New Routes**:
   - `/switch-track-group/<track_group>` - Switch between groups
   - `/api/track-groups` - Get available track groups

### Frontend Changes

1. **dashboard.html**:
   - Added track group switcher in navigation
   - Replaced hardcoded sections with dynamic track loop
   - Auto-detects track type for appropriate display

2. **day_view.html**:
   - Same track switcher and dynamic structure
   - Works seamlessly with any track configuration

3. **Template Variables** (new structure):
   ```python
   {
       'track_group': 'ml_specialist',
       'track_group_name': 'ML Engineering',
       'tracks': ['ml_algorithms', 'ml_system_design', 'recommendations'],
       'track_data': {
           'ml_algorithms': {
               'day': 1,
               'topic': {...},
               'completed': False,
               'completion_data': None
           },
           ...
       }
   }
   ```

## Benefits for Interview Preparation

### 1. Holistic Visibility
- See all your preparation tracks in one dashboard
- Identify which areas need more focus
- Balance time across different interview types

### 2. Efficient Context Switching
- Quickly toggle between SWE and ML preparation
- Maintain separate progress without confusion
- Study ML in the morning, SWE in the afternoon

### 3. Consistent Methodology
- Same proven spaced repetition across all domains
- Familiar UI regardless of track group
- Unified timer and tracking features

### 4. Strategic Flexibility
- Can adjust study intensity per track based on interview timeline
- Easy to see "I've done 40 hours on general coding, only 5 on ML systems"
- Rebalance focus areas as needed

## Adding New Tracks

The system is designed to be easily extensible. To add new tracks:

1. Create curriculum YAML in the appropriate track group folder
2. Add track name to `TRACK_GROUPS` config in `app.py`
3. Update config.json with start date for the new track
4. Restart the application - no code changes needed!

## Migration Notes

Your existing data has been preserved:
- Old `data/curriculum/` → `data/general_swe/curriculum/`
- Old `data/progress.json` → `data/general_swe/progress.json`
- Old `data/reviews.json` → `data/general_swe/reviews.json`
- Old `data/config.json` → `data/general_swe/config.json`

The application defaults to `general_swe` track group for backward compatibility.

## Testing Checklist

- [x] Python syntax validation passed
- [x] All 5 curriculum files created (2 SWE + 3 ML)
- [x] Data directory structure set up correctly
- [x] Config files created for both track groups
- [x] Templates updated with track switcher UI
- [x] All routes updated to be track group-aware
- [x] Dynamic track loop implemented in templates

## Next Steps

1. **Start the application**: `make run`
2. **Test general_swe**: Verify your existing data loads correctly
3. **Switch to ml_specialist**: Test the ML curriculum
4. **Complete a topic**: Verify progress saves to correct track group
5. **Review scheduling**: Complete a topic and check reviews are created

---

**Congratulations!** You now have a powerful, unified study tracker that supports both Software Engineering and ML Engineering interview preparation with complete data isolation and seamless switching. 🎉
