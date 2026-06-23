# Configuration Guide

## Overview

All robot behavior is configured through YAML files in `config/`. The system merges multiple config layers: defaults → head-specific → user overrides.

## Config Hierarchy

```
config/
├── default.yaml          # Base configuration
├── cv.yaml               # CV pipeline settings
├── learning/             # Learning system configs
│   ├── rl.yaml
│   ├── memory.yaml
│   └── rewards.yaml
├── heads/                # Per-head-module configs
│   ├── vision-head.yaml
│   ├── lidar-head.yaml
│   └── arm-head.yaml
└── environments/         # Environment-specific overrides
    ├── indoor.yaml
    └── outdoor.yaml
```

## Main Config (default.yaml)

```yaml
robot:
  name: "mrr-001"
  max_velocity: 1.5  # m/s
  max_angular_velocity: 3.14  # rad/s

head:
  module: "vision-head"
  auto_detect: true

navigation:
  planner: "astar"
  obstacle_threshold: 0.3  # meters
  safety_margin: 0.5

cv:
  enabled: true
  detection_confidence: 0.7
  tracking_buffer: 30  # frames

learning:
  enabled: true
  mode: "online"  # online | offline | hybrid
  experience_buffer_size: 50000
```

## Environment Variables

Override any config key via environment variables:

```bash
export MRR_ROBOT_MAX_VELOCITY=2.0
export MRR_HEAD_MODULE=vision-head
export MRR_CV_DETECTION_CONFIDENCE=0.8
```

## Runtime Configuration

Change config at runtime via the event bus:

```python
from src.core.events import EventBus

bus = EventBus()
bus.emit('config.update', {'robot.max_velocity': 2.0})
```
