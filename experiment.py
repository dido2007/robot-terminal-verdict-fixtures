#!/usr/bin/env python3
"""Evidence fixture for temporal success labels; no video model is used."""
import json

# Frame values: T=true, F=false, ?=occluded/unobservable.
# Task is "place object in bin AND finish with drawer closed".
EPISODES = {
    'clean_success':       [('F','F'), ('T','F'), ('T','T')],
    'transient_success':   [('F','F'), ('T','T'), ('F','T')],
    'drawer_reopens':      [('F','F'), ('T','T'), ('T','F')],
    'object_removed':      [('F','F'), ('T','T'), ('F','F')],
    'final_occlusion':     [('F','F'), ('T','T'), ('?','T')],
    'never_in_bin':        [('F','F'), ('F','T'), ('F','T')],
    'late_success':        [('F','F'), ('F','T'), ('T','T')],
    'all_occluded':        [('?','?'), ('?','?'), ('?','?')],
}

def any_frame(frames):
    return 'success' if ('T','T') in frames else 'failure'

def terminal_evidence(frames):
    obj, drawer = frames[-1]
    if obj == 'F' or drawer == 'F':
        return 'failure'
    if obj == '?' or drawer == '?':
        return 'unknown'
    return 'success'

rows = [{'episode': name, 'any_frame': any_frame(frames),
         'terminal_evidence': terminal_evidence(frames),
         'final_frame': frames[-1]}
        for name, frames in EPISODES.items()]
report = {'scope': 'Hand-authored symbolic frame fixture; no Instance API, robot, or video model',
          'task': 'object in bin AND drawer closed at final observable frame',
          'episodes': rows,
          'disagreements': sum(r['any_frame'] != r['terminal_evidence'] for r in rows),
          'unknowns': sum(r['terminal_evidence'] == 'unknown' for r in rows)}
assert report['disagreements'] >= 3
print(json.dumps(report, indent=2))
