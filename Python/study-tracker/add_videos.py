#!/usr/bin/env python3
"""
Script to add video resources to all curriculum YAML files.
Uses the mappings from CURRICULUM_VIDEO_TEMPLATE.md
"""

import yaml
import re
from pathlib import Path

# Video resources mappings for coding curriculum (Days 2-28)
CODING_VIDEOS = {
    2: [
        {
            "title": "NeetCode: Sliding Window Technique",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "18 min",
            "description": "Fixed vs variable window patterns explained",
            "priority": "high"
        },
        {
            "title": "NeetCode: Longest Substring Without Repeating Characters",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "Classic sliding window problem walkthrough",
            "priority": "high"
        }
    ],
    3: [
        {
            "title": "NeetCode: Binary Search Explained",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "Binary search template and common patterns",
            "priority": "high"
        },
        {
            "title": "NeetCode: Search in Rotated Sorted Array",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "10 min",
            "description": "Advanced binary search technique",
            "priority": "high"
        }
    ],
    4: [
        {
            "title": "NeetCode: Floyd's Cycle Detection",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "Tortoise and hare algorithm explained",
            "priority": "high"
        }
    ],
    5: [
        {
            "title": "NeetCode: Cyclic Sort Pattern",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "10 min",
            "description": "In-place sorting for arrays with numbers 1 to n",
            "priority": "medium"
        }
    ],
    6: [
        {
            "title": "NeetCode: Reverse Linked List",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "8 min",
            "description": "Iterative and recursive approaches",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Advanced Linked List Reversal",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "15 min",
            "description": "Reverse in groups and complex patterns",
            "priority": "medium"
        }
    ],
    7: [
        {
            "title": "NeetCode: Top Patterns for Coding Interviews",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "20 min",
            "description": "Review of all Week 1 patterns",
            "priority": "high"
        }
    ],
    8: [
        {
            "title": "NeetCode: Binary Tree Level Order Traversal",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "10 min",
            "description": "BFS pattern for trees with queue",
            "priority": "high"
        }
    ],
    9: [
        {
            "title": "NeetCode: Binary Tree DFS Patterns",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "Preorder, inorder, postorder traversals",
            "priority": "high"
        }
    ],
    10: [
        {
            "title": "NeetCode: Median from Data Stream",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "Using two heaps for streaming median",
            "priority": "high"
        }
    ],
    11: [
        {
            "title": "NeetCode: Stack Problems Explained",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "18 min",
            "description": "Valid parentheses, next greater element, etc.",
            "priority": "high"
        }
    ],
    12: [
        {
            "title": "NeetCode: Monotonic Stack Pattern",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "Stack for finding next greater/smaller element",
            "priority": "medium"
        }
    ],
    13: [
        {
            "title": "NeetCode: Hash Table Techniques",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "Using hash maps for O(1) lookups",
            "priority": "high"
        }
    ],
    14: [
        {
            "title": "NeetCode: Tree and Stack Patterns Review",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "20 min",
            "description": "Consolidate Week 2 learnings",
            "priority": "high"
        }
    ],
    15: [
        {
            "title": "William Fiset: BFS Graph Traversal",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "15 min",
            "description": "BFS visualization and applications",
            "priority": "high"
        },
        {
            "title": "NeetCode: Number of Islands",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "10 min",
            "description": "Classic BFS graph problem",
            "priority": "high"
        }
    ],
    16: [
        {
            "title": "William Fiset: DFS Graph Traversal",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "18 min",
            "description": "DFS with animations and topological sort",
            "priority": "high"
        }
    ],
    17: [
        {
            "title": "William Fiset: Union Find Data Structure",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "20 min",
            "description": "Disjoint set with path compression",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Union Find Explained",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "15 min",
            "description": "Applications in graph problems",
            "priority": "medium"
        }
    ],
    18: [
        {
            "title": "William Fiset: Topological Sort Algorithm",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "12 min",
            "description": "Kahn's algorithm and DFS approach",
            "priority": "high"
        }
    ],
    19: [
        {
            "title": "NeetCode: Implement Trie (Prefix Tree)",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "Trie implementation and word search",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Trie Data Structure",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "18 min",
            "description": "Advanced trie applications",
            "priority": "medium"
        }
    ],
    20: [
        {
            "title": "NeetCode: Backtracking Pattern",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "20 min",
            "description": "Permutations, combinations, subsets",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: Backtracking Deep Dive",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "25 min",
            "description": "Complex backtracking problems",
            "priority": "medium"
        }
    ],
    21: [
        {
            "title": "William Fiset: Graph Algorithms Playlist",
            "url": "https://www.youtube.com/@WilliamFiset-videos",
            "duration": "30 min",
            "description": "Comprehensive review of graph patterns",
            "priority": "high"
        }
    ],
    22: [
        {
            "title": "NeetCode: 1D DP Explained",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "18 min",
            "description": "House robber, climbing stairs patterns",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: DP Fundamentals",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "20 min",
            "description": "Building intuition for DP",
            "priority": "high"
        }
    ],
    23: [
        {
            "title": "NeetCode: 2D DP Patterns",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "22 min",
            "description": "Grid problems, LCS, edit distance",
            "priority": "high"
        },
        {
            "title": "Back To Back SWE: 2D DP Mastery",
            "url": "https://www.youtube.com/@BackToBackSWE",
            "duration": "30 min",
            "description": "Advanced 2D DP techniques",
            "priority": "medium"
        }
    ],
    24: [
        {
            "title": "NeetCode: Greedy vs DP",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "When to use greedy approach",
            "priority": "high"
        }
    ],
    25: [
        {
            "title": "NeetCode: Interval Problems",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "18 min",
            "description": "Merge intervals, meeting rooms",
            "priority": "high"
        }
    ],
    26: [
        {
            "title": "NeetCode: Bit Manipulation Tricks",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "12 min",
            "description": "XOR, counting bits, common patterns",
            "priority": "medium"
        }
    ],
    27: [
        {
            "title": "NeetCode: Math Problems for Interviews",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "15 min",
            "description": "Prime numbers, GCD, geometry basics",
            "priority": "medium"
        }
    ],
    28: [
        {
            "title": "Cracking FAANG: Mock Coding Interview",
            "url": "https://www.youtube.com/@CrackingFAANG",
            "duration": "45 min",
            "description": "Full mock interview with feedback",
            "priority": "high"
        },
        {
            "title": "NeetCode: Interview Tips and Strategies",
            "url": "https://www.youtube.com/@NeetCode",
            "duration": "20 min",
            "description": "How to communicate during interviews",
            "priority": "high"
        }
    ]
}

# Video resources mappings for system design curriculum (Days 2-28)
SYSTEM_DESIGN_VIDEOS = {
    2: [
        {
            "title": "ByteByteGo: What is a CDN?",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "8 min",
            "description": "How content delivery networks work",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: How DNS Works",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "10 min",
            "description": "Domain name system explained",
            "priority": "high"
        }
    ],
    3: [
        {
            "title": "ByteByteGo: Database Replication Explained",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Master-slave and master-master replication",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: SQL vs NoSQL",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "10 min",
            "description": "When to use each database type",
            "priority": "high"
        }
    ],
    4: [
        {
            "title": "ByteByteGo: How Caching Works",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Cache strategies and invalidation",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Redis Explained",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "8 min",
            "description": "In-memory data store use cases",
            "priority": "high"
        }
    ],
    5: [
        {
            "title": "ByteByteGo: Message Queue Explained",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Async communication patterns",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Queue vs Topic",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "10 min",
            "description": "Different messaging patterns",
            "priority": "medium"
        }
    ],
    6: [
        {
            "title": "ByteByteGo: API Gateway Pattern",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "10 min",
            "description": "Single entry point for microservices",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: REST vs GraphQL vs gRPC",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "API communication protocols compared",
            "priority": "high"
        }
    ],
    7: [
        {
            "title": "ByteByteGo: System Design Fundamentals",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "20 min",
            "description": "Review of Week 1 concepts",
            "priority": "high"
        }
    ],
    8: [
        {
            "title": "Hello Interview: Design TinyURL",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "25 min",
            "description": "URL shortener system design walkthrough",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: URL Shortening System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Complete URL shortener design",
            "priority": "high"
        }
    ],
    9: [
        {
            "title": "Hello Interview: Design Instagram",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "30 min",
            "description": "Photo sharing platform design",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Design Instagram Feed",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "News feed generation strategies",
            "priority": "medium"
        }
    ],
    10: [
        {
            "title": "Hello Interview: Design Twitter",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "35 min",
            "description": "Social media system design",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Design Twitter Timeline",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Fan-out strategies for timeline",
            "priority": "high"
        }
    ],
    11: [
        {
            "title": "Hello Interview: Design YouTube",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "30 min",
            "description": "Video streaming platform design",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Video Streaming Architecture",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Adaptive bitrate streaming",
            "priority": "high"
        }
    ],
    12: [
        {
            "title": "ByteByteGo: Design Web Crawler",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "18 min",
            "description": "Scalable web crawling system",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design Google Search",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "25 min",
            "description": "Search engine architecture",
            "priority": "medium"
        }
    ],
    13: [
        {
            "title": "ByteByteGo: Design Notification System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Push, SMS, email notifications at scale",
            "priority": "high"
        }
    ],
    14: [
        {
            "title": "ByteByteGo: System Design Interview Tips",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "20 min",
            "description": "Review Week 2 patterns and strategies",
            "priority": "high"
        }
    ],
    15: [
        {
            "title": "ByteByteGo: Design Rate Limiter",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Token bucket and leaky bucket algorithms",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Rate Limiting Strategies",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "15 min",
            "description": "Different rate limiting approaches",
            "priority": "medium"
        }
    ],
    16: [
        {
            "title": "ByteByteGo: Design Autocomplete",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "10 min",
            "description": "Typeahead search suggestions",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design Google Autocomplete",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "20 min",
            "description": "Trie-based autocomplete system",
            "priority": "high"
        }
    ],
    17: [
        {
            "title": "Hello Interview: Design Uber",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "35 min",
            "description": "Ride-sharing platform design",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Geospatial Indexing",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Location-based services architecture",
            "priority": "high"
        }
    ],
    18: [
        {
            "title": "ByteByteGo: Design Chat System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "18 min",
            "description": "Real-time messaging system",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design WhatsApp",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "30 min",
            "description": "Messaging app architecture",
            "priority": "high"
        }
    ],
    19: [
        {
            "title": "ByteByteGo: Design Distributed Cache",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Consistent hashing for distributed systems",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Consistent Hashing",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "12 min",
            "description": "Virtual nodes and ring structure",
            "priority": "medium"
        }
    ],
    20: [
        {
            "title": "ByteByteGo: Design Stock Exchange",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "20 min",
            "description": "High-throughput trading system",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design Payment System",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "25 min",
            "description": "Financial transactions at scale",
            "priority": "high"
        }
    ],
    21: [
        {
            "title": "ByteByteGo: Advanced System Design Patterns",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "25 min",
            "description": "Review Week 3 concepts",
            "priority": "high"
        }
    ],
    22: [
        {
            "title": "ByteByteGo: Design Netflix",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "20 min",
            "description": "Video streaming at massive scale",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Content Delivery at Scale",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "18 min",
            "description": "CDN and caching strategies",
            "priority": "medium"
        }
    ],
    23: [
        {
            "title": "Hello Interview: Design Amazon",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "40 min",
            "description": "E-commerce platform architecture",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Design Shopping Cart",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Cart management and checkout",
            "priority": "medium"
        }
    ],
    24: [
        {
            "title": "ByteByteGo: Design Dropbox",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "18 min",
            "description": "File storage and sync system",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design Google Drive",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "30 min",
            "description": "Cloud storage architecture",
            "priority": "high"
        }
    ],
    25: [
        {
            "title": "ByteByteGo: Design Metrics System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Time-series data and monitoring",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design Analytics Platform",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "25 min",
            "description": "Real-time analytics at scale",
            "priority": "medium"
        }
    ],
    26: [
        {
            "title": "ByteByteGo: Design Ad Click Aggregator",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "18 min",
            "description": "Real-time data processing",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design Ad Serving System",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "22 min",
            "description": "Ad targeting and delivery",
            "priority": "medium"
        }
    ],
    27: [
        {
            "title": "ByteByteGo: Design Hotel Reservation System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Booking system with concurrency",
            "priority": "high"
        },
        {
            "title": "Hello Interview: Design Ticketmaster",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "28 min",
            "description": "High-concurrency ticket booking",
            "priority": "high"
        }
    ],
    28: [
        {
            "title": "Hello Interview: Mock System Design Interview",
            "url": "https://www.youtube.com/@HelloInterview",
            "duration": "45 min",
            "description": "Full mock interview with feedback",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: System Design Interview Framework",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "20 min",
            "description": "How to approach any system design problem",
            "priority": "high"
        }
    ]
}

# Video resources mappings for ML algorithms curriculum (Days 1-14)
ML_ALGORITHMS_VIDEOS = {
    1: [
        {
            "title": "3Blue1Brown: But what is a neural network?",
            "url": "https://www.youtube.com/@3blue1brown",
            "duration": "19 min",
            "description": "Visual explanation of neural networks and backpropagation",
            "priority": "high"
        },
        {
            "title": "StatQuest: Neural Networks Clearly Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "15 min",
            "description": "Intuitive explanation of forward and backward propagation",
            "priority": "high"
        }
    ],
    2: [
        {
            "title": "3Blue1Brown: Convolution",
            "url": "https://www.youtube.com/@3blue1brown",
            "duration": "21 min",
            "description": "Beautiful visual explanation of convolutions",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: CNNs from Scratch",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "25 min",
            "description": "Building CNNs step by step",
            "priority": "high"
        }
    ],
    3: [
        {
            "title": "StatQuest: RNNs and LSTMs Clearly Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "18 min",
            "description": "How RNNs and LSTMs handle sequences",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: The Unreasonable Effectiveness of RNNs",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "20 min",
            "description": "Deep dive into RNN applications",
            "priority": "medium"
        }
    ],
    4: [
        {
            "title": "3Blue1Brown: Attention in Transformers",
            "url": "https://www.youtube.com/@3blue1brown",
            "duration": "25 min",
            "description": "Visual explanation of attention mechanisms",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: Let's build GPT from scratch",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "120 min",
            "description": "Complete transformer implementation",
            "priority": "high"
        }
    ],
    5: [
        {
            "title": "StatQuest: VAEs Clearly Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "22 min",
            "description": "Variational autoencoders intuition",
            "priority": "high"
        },
        {
            "title": "StatQuest: GANs Clearly Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "18 min",
            "description": "Generative adversarial networks fundamentals",
            "priority": "high"
        }
    ],
    6: [
        {
            "title": "StatQuest: Regularization (L1, L2, Dropout)",
            "url": "https://www.youtube.com/@statquest",
            "duration": "16 min",
            "description": "Preventing overfitting techniques",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: Training Neural Nets",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "30 min",
            "description": "Practical optimization tips",
            "priority": "high"
        }
    ],
    7: [
        {
            "title": "StatQuest: Transfer Learning Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "12 min",
            "description": "Using pre-trained models effectively",
            "priority": "high"
        },
        {
            "title": "Two Minute Papers: Transfer Learning Applications",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "5 min",
            "description": "Real-world transfer learning examples",
            "priority": "medium"
        }
    ],
    8: [
        {
            "title": "StatQuest: Decision Trees Clearly Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "17 min",
            "description": "How decision trees work",
            "priority": "high"
        },
        {
            "title": "StatQuest: Random Forests and Gradient Boosting",
            "url": "https://www.youtube.com/@statquest",
            "duration": "20 min",
            "description": "Ensemble methods explained",
            "priority": "high"
        }
    ],
    9: [
        {
            "title": "StatQuest: Linear Regression and Logistic Regression",
            "url": "https://www.youtube.com/@statquest",
            "duration": "22 min",
            "description": "Classical ML foundations",
            "priority": "high"
        },
        {
            "title": "StatQuest: Support Vector Machines (SVMs)",
            "url": "https://www.youtube.com/@statquest",
            "duration": "20 min",
            "description": "SVM intuition and kernels",
            "priority": "high"
        }
    ],
    10: [
        {
            "title": "StatQuest: ROC and AUC Clearly Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "16 min",
            "description": "Evaluation metrics for classification",
            "priority": "high"
        },
        {
            "title": "StatQuest: Precision, Recall, and F1 Score",
            "url": "https://www.youtube.com/@statquest",
            "duration": "12 min",
            "description": "Understanding classification metrics",
            "priority": "high"
        }
    ],
    11: [
        {
            "title": "StatQuest: Word2Vec and Embeddings",
            "url": "https://www.youtube.com/@statquest",
            "duration": "18 min",
            "description": "How embeddings capture meaning",
            "priority": "high"
        },
        {
            "title": "3Blue1Brown: Visualizing High-Dimensional Data",
            "url": "https://www.youtube.com/@3blue1brown",
            "duration": "15 min",
            "description": "t-SNE and embedding visualization",
            "priority": "medium"
        }
    ],
    12: [
        {
            "title": "Andrej Karpathy: Training Deep Networks",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "35 min",
            "description": "Batch norm, layer norm, weight init",
            "priority": "high"
        },
        {
            "title": "Two Minute Papers: ResNet and Skip Connections",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "6 min",
            "description": "Why residual connections work",
            "priority": "high"
        }
    ],
    13: [
        {
            "title": "StatQuest: Self-Supervised Learning Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "15 min",
            "description": "Learning without labels",
            "priority": "high"
        },
        {
            "title": "Two Minute Papers: Contrastive Learning",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "7 min",
            "description": "SimCLR and other approaches",
            "priority": "medium"
        }
    ],
    14: [
        {
            "title": "Two Minute Papers: Model Compression Techniques",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "8 min",
            "description": "Quantization and pruning overview",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: Making Neural Networks Efficient",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "25 min",
            "description": "Knowledge distillation and production optimization",
            "priority": "high"
        }
    ]
}

# Video resources mappings for ML system design curriculum (Days 1-14)
ML_SYSTEM_DESIGN_VIDEOS = {
    1: [
        {
            "title": "ByteByteGo: How Netflix Recommends",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Recommendation system architecture overview",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: RecSys at Scale",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "Candidate generation strategies",
            "priority": "high"
        }
    ],
    2: [
        {
            "title": "ByteByteGo: Design YouTube Recommendations",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Ranking and re-ranking pipelines",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Multi-Stage Recommendation",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "18 min",
            "description": "From millions to dozens of recommendations",
            "priority": "medium"
        }
    ],
    3: [
        {
            "title": "ByteByteGo: Design Google Search",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "18 min",
            "description": "Search and ranking system architecture",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Learning to Rank",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "15 min",
            "description": "Ranking algorithms for search",
            "priority": "medium"
        }
    ],
    4: [
        {
            "title": "ByteByteGo: Ad Serving System Design",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "16 min",
            "description": "CTR prediction and ad auction mechanics",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Real-Time ML at Scale",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "22 min",
            "description": "Low-latency prediction systems",
            "priority": "high"
        }
    ],
    5: [
        {
            "title": "Two Minute Papers: Object Detection Overview",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "8 min",
            "description": "YOLO, Faster R-CNN architectures",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: Computer Vision in Production",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "30 min",
            "description": "Building CV systems at scale",
            "priority": "high"
        }
    ],
    6: [
        {
            "title": "Andrej Karpathy: NLP Systems Overview",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "25 min",
            "description": "Text classification and QA architectures",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Large Language Models in Production",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "Deploying and serving LLMs",
            "priority": "medium"
        }
    ],
    7: [
        {
            "title": "Chip Huyen: Anomaly Detection Systems",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "18 min",
            "description": "Fraud detection architecture",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Real-Time Fraud Detection",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Low-latency anomaly detection",
            "priority": "medium"
        }
    ],
    8: [
        {
            "title": "ByteByteGo: Design Instagram Feed",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Multi-objective feed ranking",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Personalized Feeds at Scale",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "22 min",
            "description": "Balancing engagement and diversity",
            "priority": "high"
        }
    ],
    9: [
        {
            "title": "Chip Huyen: Distributed Training",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "25 min",
            "description": "Data and model parallelism",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: Training at Scale",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "30 min",
            "description": "Infrastructure for large models",
            "priority": "high"
        }
    ],
    10: [
        {
            "title": "Chip Huyen: ML Model Serving",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "Batching, caching, and deployment",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Design ML Inference System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Low-latency prediction serving",
            "priority": "high"
        }
    ],
    11: [
        {
            "title": "Chip Huyen: Feature Stores Explained",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "18 min",
            "description": "Feature engineering at scale",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Data Pipeline Architecture",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "ETL for ML systems",
            "priority": "medium"
        }
    ],
    12: [
        {
            "title": "Chip Huyen: ML Monitoring and Observability",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "22 min",
            "description": "Detecting drift and model degradation",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: ML Ops Best Practices",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "14 min",
            "description": "Model retraining pipelines",
            "priority": "high"
        }
    ],
    13: [
        {
            "title": "Chip Huyen: ML Fairness and Bias",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "Responsible AI practices",
            "priority": "high"
        },
        {
            "title": "Two Minute Papers: Explainable AI",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "8 min",
            "description": "SHAP and interpretability",
            "priority": "medium"
        }
    ],
    14: [
        {
            "title": "Chip Huyen: ML System Design Interview",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "30 min",
            "description": "End-to-end case study walkthrough",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Design ML-Powered System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "20 min",
            "description": "Comprehensive system design approach",
            "priority": "high"
        }
    ]
}

# Video resources mappings for recommendations curriculum (Days 1-14)
RECOMMENDATIONS_VIDEOS = {
    1: [
        {
            "title": "ByteByteGo: Netflix Recommendation System",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Three-stage funnel architecture",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: RecSys Architecture Overview",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "18 min",
            "description": "Retrieval, ranking, and re-ranking",
            "priority": "high"
        }
    ],
    2: [
        {
            "title": "StatQuest: Collaborative Filtering Clearly Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "15 min",
            "description": "User-based and item-based approaches",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Matrix Factorization Techniques",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "SVD and ALS for recommendations",
            "priority": "high"
        }
    ],
    3: [
        {
            "title": "Two Minute Papers: Two-Tower Neural Networks",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "7 min",
            "description": "Dual encoder architectures",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Embedding-Based Retrieval",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "22 min",
            "description": "ANN search and vector databases",
            "priority": "high"
        }
    ],
    4: [
        {
            "title": "Two Minute Papers: Sequential Recommendations",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "8 min",
            "description": "Capturing user behavior over time",
            "priority": "high"
        },
        {
            "title": "Andrej Karpathy: Transformers for Sequences",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "25 min",
            "description": "BERT4Rec and attention-based models",
            "priority": "high"
        }
    ],
    5: [
        {
            "title": "Two Minute Papers: Graph Neural Networks",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "9 min",
            "description": "GNNs for recommendations",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Graph-Based Retrieval",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "Random walks and node embeddings",
            "priority": "high"
        }
    ],
    6: [
        {
            "title": "StatQuest: Deep Learning for CTR",
            "url": "https://www.youtube.com/@statquest",
            "duration": "18 min",
            "description": "DeepFM and Wide & Deep models",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Ranking Models in Production",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "22 min",
            "description": "Feature crosses and deep networks",
            "priority": "high"
        }
    ],
    7: [
        {
            "title": "Chip Huyen: Multi-Task Learning",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "Optimizing multiple objectives",
            "priority": "high"
        },
        {
            "title": "Two Minute Papers: Pareto Optimization",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "7 min",
            "description": "Balancing conflicting goals",
            "priority": "medium"
        }
    ],
    8: [
        {
            "title": "Chip Huyen: Re-ranking Strategies",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "18 min",
            "description": "MMR and diversity algorithms",
            "priority": "high"
        },
        {
            "title": "Two Minute Papers: Submodular Optimization",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "8 min",
            "description": "DPP for diverse recommendations",
            "priority": "medium"
        }
    ],
    9: [
        {
            "title": "StatQuest: Feature Importance",
            "url": "https://www.youtube.com/@statquest",
            "duration": "15 min",
            "description": "Understanding feature contribution",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Feature Engineering for RecSys",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "User, item, and context features",
            "priority": "high"
        }
    ],
    10: [
        {
            "title": "Chip Huyen: Cold Start Solutions",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "18 min",
            "description": "Handling new users and items",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: Content-Based Recommendations",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "12 min",
            "description": "Bootstrapping recommendations",
            "priority": "medium"
        }
    ],
    11: [
        {
            "title": "StatQuest: NDCG Explained",
            "url": "https://www.youtube.com/@statquest",
            "duration": "14 min",
            "description": "Ranking evaluation metrics",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: RecSys Evaluation Metrics",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "20 min",
            "description": "Diversity, coverage, and serendipity",
            "priority": "high"
        }
    ],
    12: [
        {
            "title": "StatQuest: Reinforcement Learning Basics",
            "url": "https://www.youtube.com/@statquest",
            "duration": "18 min",
            "description": "Q-learning and policy gradients",
            "priority": "high"
        },
        {
            "title": "Chip Huyen: Contextual Bandits for RecSys",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "22 min",
            "description": "Exploration vs exploitation",
            "priority": "high"
        }
    ],
    13: [
        {
            "title": "Chip Huyen: ML in Production",
            "url": "https://www.youtube.com/@chiphuyen",
            "duration": "25 min",
            "description": "Serving, monitoring, and A/B testing",
            "priority": "high"
        },
        {
            "title": "ByteByteGo: ML Ops for RecSys",
            "url": "https://www.youtube.com/@ByteByteGo",
            "duration": "15 min",
            "description": "Production ML infrastructure",
            "priority": "high"
        }
    ],
    14: [
        {
            "title": "Andrej Karpathy: LLMs and Recommendations",
            "url": "https://www.youtube.com/@AndrejKarpathy",
            "duration": "30 min",
            "description": "Integrating large language models",
            "priority": "high"
        },
        {
            "title": "Two Minute Papers: Next-Gen RecSys",
            "url": "https://www.youtube.com/@TwoMinutePapers",
            "duration": "8 min",
            "description": "Future of recommendation systems",
            "priority": "medium"
        }
    ]
}

def add_video_resources_to_yaml(yaml_file, video_mappings, track_name="coding"):
    """Add video resources to a YAML curriculum file."""

    with open(yaml_file, 'r') as f:
        content = f.read()

    # Parse YAML
    data = yaml.safe_load(content)

    # Track changes
    changes_made = 0

    # Iterate through weeks and days
    for week_key, week_data in data['weeks'].items():
        for day_data in week_data:
            day_num = day_data['day']

            # Skip if already has video_resources
            if 'video_resources' in day_data:
                print(f"  Day {day_num}: Already has videos, skipping")
                continue

            # Add videos if we have them for this day
            if day_num in video_mappings:
                day_data['video_resources'] = video_mappings[day_num]
                changes_made += 1
                print(f"  Day {day_num}: Added {len(video_mappings[day_num])} videos")

    # Write back to file
    if changes_made > 0:
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print(f"\n✅ Updated {yaml_file}: Added videos to {changes_made} days")
    else:
        print(f"\n✓ {yaml_file}: No changes needed")

    return changes_made

def main():
    print("Adding video resources to curricula...\n")

    # Add to coding curriculum
    print("📝 Processing coding curriculum...")
    coding_file = Path("data/general_swe/curriculum/coding.yaml")
    add_video_resources_to_yaml(coding_file, CODING_VIDEOS, "coding")

    # Add to system design curriculum
    print("\n📝 Processing system design curriculum...")
    system_design_file = Path("data/general_swe/curriculum/system_design.yaml")
    add_video_resources_to_yaml(system_design_file, SYSTEM_DESIGN_VIDEOS, "system_design")

    # Add to ML algorithms curriculum
    print("\n📝 Processing ML algorithms curriculum...")
    ml_algorithms_file = Path("data/ml_specialist/curriculum/ml_algorithms.yaml")
    add_video_resources_to_yaml(ml_algorithms_file, ML_ALGORITHMS_VIDEOS, "ml_algorithms")

    # Add to ML system design curriculum
    print("\n📝 Processing ML system design curriculum...")
    ml_system_design_file = Path("data/ml_specialist/curriculum/ml_system_design.yaml")
    add_video_resources_to_yaml(ml_system_design_file, ML_SYSTEM_DESIGN_VIDEOS, "ml_system_design")

    # Add to recommendations curriculum
    print("\n📝 Processing recommendations curriculum...")
    recommendations_file = Path("data/ml_specialist/curriculum/recommendations.yaml")
    add_video_resources_to_yaml(recommendations_file, RECOMMENDATIONS_VIDEOS, "recommendations")

    print("\n✅ All done!")

if __name__ == "__main__":
    main()
