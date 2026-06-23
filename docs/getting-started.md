# Getting Started

## Prerequisites

- Python 3.10+
- ROS2 Humble (optional, for hardware integration)
- OpenCV 4.8+
- PyTorch 2.0+

## Installation

```bash
git clone <repo-url>
cd autonomous-mobile-robot
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## First Run

1. Connect a head module (or use simulation)
2. Launch: `python -m src.core.robot --config config/default.yaml`
3. The robot initializes, calibrates sensors, and begins autonomous behavior

## Simulation Mode

No hardware needed:

```bash
python -m src.core.robot --sim --head vision-head
```

## Next Steps

- Read [Head Module Interface](head-module-interface.md) to understand modularity
- Read [Computer Vision Pipeline](computer-vision.md) for CV setup
- Read [Learning System](learning-system.md) to enable adaptive behavior
