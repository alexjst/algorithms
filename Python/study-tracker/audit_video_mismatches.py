#!/usr/bin/env python3
"""
Audit script to identify video-topic mismatches in coding curriculum.
Checks if video titles/descriptions semantically match the day's topic.
"""

import yaml
from pathlib import Path

def load_curriculum(yaml_file):
    """Load curriculum YAML file."""
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)

def extract_keywords(text):
    """Extract meaningful keywords from topic/video text."""
    # Lowercase for comparison
    text = text.lower()

    # Common algorithm/data structure keywords
    keywords = set()

    # Data structures
    if any(term in text for term in ['array', 'hashing', 'hash', 'hashmap', 'hash map']):
        keywords.add('arrays_hashing')
    if 'two pointer' in text or 'two-pointer' in text:
        keywords.add('two_pointers')
    if 'sliding window' in text:
        keywords.add('sliding_window')
    if 'stack' in text:
        keywords.add('stack')
    if 'binary search' in text:
        keywords.add('binary_search')
    if 'linked list' in text:
        keywords.add('linked_list')
    if any(term in text for term in ['tree', 'bst', 'binary tree']):
        keywords.add('trees')
    if 'trie' in text:
        keywords.add('trie')
    if 'heap' in text or 'priority queue' in text:
        keywords.add('heap')
    if 'backtrack' in text:
        keywords.add('backtracking')
    if any(term in text for term in ['graph', 'bfs', 'dfs', 'dijkstra', 'floyd', 'warshall', 'topological', 'mst', 'spanning tree', 'kruskal', 'prim']):
        keywords.add('graphs')
    if any(term in text for term in ['dynamic programming', 'dp', '1d dp', '2d dp', 'knapsack', 'lcs', 'edit distance']):
        keywords.add('dp')
    if 'greedy' in text:
        keywords.add('greedy')
    if 'interval' in text:
        keywords.add('intervals')
    if 'bit' in text and 'manipulation' in text:
        keywords.add('bit_manipulation')
    if any(term in text for term in ['math', 'geometry', 'matrix']):
        keywords.add('math')

    return keywords

def check_video_match(topic, video_resources):
    """Check if videos match the topic."""
    topic_keywords = extract_keywords(topic)

    if not video_resources:
        return True, "No videos"

    # Check each video
    video_keywords = set()
    video_titles = []
    for video in video_resources:
        title = video.get('title', '')
        description = video.get('description', '')
        video_titles.append(title)
        video_keywords.update(extract_keywords(title + ' ' + description))

    # Check for overlap
    if topic_keywords and video_keywords:
        overlap = topic_keywords & video_keywords
        if overlap:
            return True, f"Match via: {', '.join(overlap)}"
        else:
            return False, f"Topic: {', '.join(topic_keywords)} vs Videos: {', '.join(video_keywords)}"

    return None, f"Unable to determine (topic: {', '.join(topic_keywords)}, videos: {', '.join(video_keywords)})"

def audit_curriculum(yaml_file):
    """Audit all days in curriculum for video-topic mismatches."""
    data = load_curriculum(yaml_file)

    results = []
    mismatches = []

    print(f"\n{'='*80}")
    print(f"AUDITING: {yaml_file}")
    print(f"{'='*80}\n")

    for week_key, week_data in sorted(data['weeks'].items()):
        for day_data in sorted(week_data, key=lambda x: x['day']):
            day_num = day_data['day']
            topic = day_data.get('topic', 'Unknown')
            video_resources = day_data.get('video_resources', [])

            matches, reason = check_video_match(topic, video_resources)

            video_titles = [v.get('title', 'Untitled') for v in video_resources] if video_resources else ['No videos']

            status = '✓' if matches else '✗' if matches is False else '?'

            result = {
                'day': day_num,
                'topic': topic,
                'video_count': len(video_resources),
                'video_titles': video_titles,
                'matches': matches,
                'reason': reason,
                'status': status
            }
            results.append(result)

            if matches is False:
                mismatches.append(result)

            # Print summary line
            print(f"Day {day_num:2d} [{status}] {topic}")
            print(f"         Videos: {', '.join(video_titles[:2])}")
            if len(video_titles) > 2:
                print(f"                 {', '.join(video_titles[2:])}")
            print(f"         {reason}")
            print()

    # Summary
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}\n")
    print(f"Total days: {len(results)}")
    print(f"Days with videos: {sum(1 for r in results if r['video_count'] > 0)}")
    print(f"Days without videos: {sum(1 for r in results if r['video_count'] == 0)}")
    print(f"Confirmed matches: {sum(1 for r in results if r['matches'] is True)}")
    print(f"MISMATCHES: {len(mismatches)}")
    print(f"Uncertain: {sum(1 for r in results if r['matches'] is None)}")

    if mismatches:
        print(f"\n{'='*80}")
        print(f"MISMATCHED DAYS (NEED FIXING)")
        print(f"{'='*80}\n")
        for m in mismatches:
            print(f"Day {m['day']:2d}: {m['topic']}")
            print(f"  Current videos:")
            for title in m['video_titles']:
                print(f"    - {title}")
            print(f"  Reason: {m['reason']}")
            print()

    return results, mismatches

if __name__ == '__main__':
    yaml_file = Path('data/general_swe/curriculum/coding.yaml')

    if not yaml_file.exists():
        print(f"ERROR: {yaml_file} not found")
        exit(1)

    results, mismatches = audit_curriculum(yaml_file)

    print(f"\n{'='*80}")
    print(f"Audit complete. Found {len(mismatches)} mismatches that need fixing.")
    print(f"{'='*80}\n")
