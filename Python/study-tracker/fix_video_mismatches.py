#!/usr/bin/env python3
"""
Fix video-topic mismatches in coding curriculum.
Maps correct videos based on TOPIC, not day number.
"""

import yaml
from pathlib import Path

# Topic-based video mappings (not day-based!)
TOPIC_VIDEOS = {
    'linked_list_reversal': [
        {
            "title": "NeetCode: Reverse Linked List",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "8 min",
            "description": "Classic linked list reversal technique",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Advanced Linked List Reversal",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "15 min",
            "description": "Reverse in groups, advanced patterns",
            "priority": "medium"
        }
    ],
    'binary_tree_traversal': [
        {
            "title": "NeetCode: Binary Tree Level Order Traversal",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "BFS traversal of trees",
            "priority": "high"
        },
        {
            "title": "William Fiset: Tree Traversal Algorithms",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "18 min",
            "description": "Inorder, preorder, postorder, level-order",
            "priority": "medium"
        }
    ],
    'dynamic_programming': [
        {
            "title": "NeetCode: 1D DP Explained",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "18 min",
            "description": "House Robber, climbing stairs patterns",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: DP Fundamentals",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "25 min",
            "description": "Memoization, tabulation, state transitions",
            "priority": "high"
        }
    ],
    'backtracking': [
        {
            "title": "NeetCode: Backtracking Pattern",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "Subsets, permutations, combinations",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Backtracking Deep Dive",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "30 min",
            "description": "N-Queens, Sudoku solver",
            "priority": "medium"
        }
    ],
    'bit_manipulation': [
        {
            "title": "NeetCode: Bit Manipulation Tricks",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "XOR, AND, OR patterns for interviews",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Bit Manipulation Mastery",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "20 min",
            "description": "Counting bits, power of two, bit tricks",
            "priority": "medium"
        }
    ],
    'heaps': [
        {
            "title": "NeetCode: Median from Data Stream",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "14 min",
            "description": "Using two heaps for running median",
            "priority": "high"
        },
        {
            "title": "William Fiset: Priority Queue / Heap",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "16 min",
            "description": "Heap operations, heapify, top-k problems",
            "priority": "medium"
        }
    ],
    'monotonic_stack': [
        {
            "title": "NeetCode: Monotonic Stack Pattern",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "13 min",
            "description": "Next greater element, daily temperatures",
            "priority": "high"
        },
        {
            "title": "NeetCode: Stack Problems Explained",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "10 min",
            "description": "Valid parentheses, min stack",
            "priority": "medium"
        }
    ],
    'intervals': [
        {
            "title": "NeetCode: Interval Problems",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "Merge intervals, meeting rooms",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Overlapping Intervals",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "18 min",
            "description": "Insert interval, non-overlapping intervals",
            "priority": "medium"
        }
    ],
    'trie': [
        {
            "title": "NeetCode: Implement Trie (Prefix Tree)",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "11 min",
            "description": "Trie insertion, search, prefix matching",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Trie Data Structure",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "16 min",
            "description": "Word search, autocomplete with tries",
            "priority": "medium"
        }
    ],
    'greedy': [
        {
            "title": "NeetCode: Greedy vs DP",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "14 min",
            "description": "When to use greedy algorithms",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Greedy Algorithms",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "22 min",
            "description": "Jump game, gas station, interval scheduling",
            "priority": "medium"
        }
    ],
    'graph_algorithms': [
        {
            "title": "NeetCode: Network Delay Time (Dijkstra)",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "13 min",
            "description": "Dijkstra's algorithm with Python implementation",
            "priority": "high"
        },
        {
            "title": "NeetCode: Cheapest Flights (Bellman-Ford)",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "14 min",
            "description": "Shortest path with constraints in Python",
            "priority": "high"
        },
        {
            "title": "William Fiset: Dijkstra's Algorithm",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "16 min",
            "description": "Algorithmic foundation and pseudocode",
            "priority": "medium"
        },
        {
            "title": "William Fiset: Floyd-Warshall Algorithm",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "10 min",
            "description": "All-pairs shortest path algorithm",
            "priority": "medium"
        }
    ],
    'topological_sort': [
        {
            "title": "NeetCode: Course Schedule",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "Topological sort in Python with interview examples",
            "priority": "high"
        },
        {
            "title": "NeetCode: Course Schedule II",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "11 min",
            "description": "Return the actual ordering in Python",
            "priority": "high"
        },
        {
            "title": "William Fiset: Topological Sort Algorithm",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "14 min",
            "description": "Kahn's algorithm and DFS-based approaches",
            "priority": "medium"
        }
    ],
    'bfs_graph': [
        {
            "title": "NeetCode: Number of Islands",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "10 min",
            "description": "BFS on 2D grids in Python",
            "priority": "high"
        },
        {
            "title": "NeetCode: Rotting Oranges",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "Multi-source BFS with Python",
            "priority": "high"
        },
        {
            "title": "William Fiset: BFS Graph Traversal",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "14 min",
            "description": "BFS algorithm foundations",
            "priority": "medium"
        }
    ],
    'dfs_graph': [
        {
            "title": "NeetCode: Clone Graph",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "9 min",
            "description": "DFS on graphs with Python",
            "priority": "high"
        },
        {
            "title": "NeetCode: Pacific Atlantic Water Flow",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "DFS on 2D grids in Python",
            "priority": "high"
        },
        {
            "title": "William Fiset: DFS Graph Traversal",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "12 min",
            "description": "DFS algorithm foundations",
            "priority": "medium"
        }
    ],
    'union_find': [
        {
            "title": "NeetCode: Redundant Connection",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "10 min",
            "description": "Union Find implementation in Python",
            "priority": "high"
        },
        {
            "title": "NeetCode: Number of Connected Components",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "11 min",
            "description": "Union Find for connected components in Python",
            "priority": "high"
        },
        {
            "title": "William Fiset: Union Find Data Structure",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "18 min",
            "description": "Disjoint set with path compression theory",
            "priority": "medium"
        }
    ]
}

def match_topic_to_videos(topic):
    """Match curriculum topic to video resources."""
    topic_lower = topic.lower()

    # Direct keyword matching
    if 'linked list' in topic_lower and 'reversal' in topic_lower:
        return TOPIC_VIDEOS['linked_list_reversal']
    elif 'binary tree' in topic_lower and 'traversal' in topic_lower:
        return TOPIC_VIDEOS['binary_tree_traversal']
    elif 'dynamic programming' in topic_lower and 'advanced' not in topic_lower:
        return TOPIC_VIDEOS['dynamic_programming']
    elif 'backtracking' in topic_lower:
        return TOPIC_VIDEOS['backtracking']
    elif 'bit manipulation' in topic_lower:
        return TOPIC_VIDEOS['bit_manipulation']
    elif 'heap' in topic_lower or 'top k' in topic_lower:
        return TOPIC_VIDEOS['heaps']
    elif 'monotonic stack' in topic_lower:
        return TOPIC_VIDEOS['monotonic_stack']
    elif 'interval' in topic_lower:
        return TOPIC_VIDEOS['intervals']
    elif 'trie' in topic_lower:
        return TOPIC_VIDEOS['trie']
    elif 'greedy' in topic_lower:
        return TOPIC_VIDEOS['greedy']
    elif 'graph' in topic_lower and 'advanced' in topic_lower:
        return TOPIC_VIDEOS['graph_algorithms']
    elif 'topological' in topic_lower:
        return TOPIC_VIDEOS['topological_sort']
    elif 'bfs' in topic_lower or ('graph' in topic_lower and 'matrix' in topic_lower):
        return TOPIC_VIDEOS['bfs_graph']
    elif 'dfs' in topic_lower and 'fundamental' in topic_lower:
        return TOPIC_VIDEOS['dfs_graph']
    elif 'union' in topic_lower and 'find' in topic_lower:
        return TOPIC_VIDEOS['union_find']

    return None

def fix_mismatches(yaml_file, dry_run=False):
    """Fix video mismatches in curriculum."""
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    fixes_applied = 0
    days_fixed = []

    print(f"\n{'='*80}")
    print(f"FIXING VIDEO MISMATCHES: {yaml_file}")
    print(f"{'='*80}\n")

    for week_key, week_data in sorted(data['weeks'].items()):
        for day_data in sorted(week_data, key=lambda x: x['day']):
            day_num = day_data['day']
            topic = day_data.get('topic', 'Unknown')

            # Get correct videos for this topic
            correct_videos = match_topic_to_videos(topic)

            if correct_videos:
                current_videos = day_data.get('video_resources', [])
                current_titles = [v.get('title', '') for v in current_videos]
                new_titles = [v.get('title', '') for v in correct_videos]

                # Check if they're different
                if current_titles != new_titles:
                    print(f"Day {day_num}: {topic}")
                    print(f"  BEFORE: {', '.join(current_titles)}")
                    print(f"  AFTER:  {', '.join(new_titles)}")
                    print()

                    if not dry_run:
                        day_data['video_resources'] = correct_videos
                        fixes_applied += 1
                        days_fixed.append(day_num)

    if not dry_run and fixes_applied > 0:
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}\n")
    print(f"Fixes applied: {fixes_applied}")
    print(f"Days fixed: {days_fixed}")

    if dry_run:
        print("\nDRY RUN: No changes written to file")
    else:
        print(f"\nChanges written to {yaml_file}")

    return fixes_applied, days_fixed

if __name__ == '__main__':
    import sys

    yaml_file = Path('data/general_swe/curriculum/coding.yaml')

    if not yaml_file.exists():
        print(f"ERROR: {yaml_file} not found")
        exit(1)

    # Check if --dry-run flag is passed
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("Running in DRY RUN mode - no changes will be written\n")

    fixes_applied, days_fixed = fix_mismatches(yaml_file, dry_run=dry_run)

    if not dry_run:
        print(f"\n✅ Fixed {fixes_applied} days: {days_fixed}")
        print("Please refresh your browser at localhost:5555 to see corrected videos")
