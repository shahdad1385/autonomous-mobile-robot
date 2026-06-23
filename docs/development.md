# Development Guide

## Project Structure

```
src/
├── core/
│   ├── robot.py           # Main robot control loop
│   ├── state_machine.py   # Robot state machine
│   ├── events.py          # Event bus for decoupled communication
│   └── config.py          # Configuration loader
├── cv/
│   ├── pipeline.py        # CV processing pipeline
│   ├── detector.py        # Object detection
│   ├── tracker.py         # Multi-object tracking
│   ├── depth.py           # Depth estimation
│   └── train.py           # Model training scripts
├── learning/
│   ├── agent.py           # RL agent (PPO)
│   ├── memory.py          # Episodic memory
│   ├── transfer.py        # Transfer learning
│   └── train.py           # Training scripts
├── modules/
│   ├── base.py            # HeadModule abstract base class
│   ├── registry.py        # Module registry
│   └── heads/             # Implementations
│       ├── vision/
│       ├── lidar/
│       ├── arm/
│       └── display/
└── utils/
    ├── transforms.py      # Coordinate transforms
    ├── logging.py         # Structured logging
    └── timing.py          # Profiling utilities
```

## Code Style

- Python 3.10+ (use `match` statements, type hints everywhere)
- Black formatter, isort for imports
- Ruff for linting
- Type annotations on all public functions

```bash
# Format
black src/ tests/
isort src/ tests/

# Lint
ruff check src/ tests/

# Type check
mypy src/
```

## Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Run specific module tests
pytest tests/test_cv.py
```

## Commit Convention

Follow Conventional Commits:

```
feat: add new head module interface
fix: resolve depth estimation memory leak
docs: update hardware integration guide
refactor: simplify state machine transitions
```

## Adding Features

1. Create feature branch: `git checkout -b feat/my-feature`
2. Implement with tests
3. Run linting and type checks
4. Submit PR with description

## Debugging

Enable debug logging:

```bash
export MRR_LOG_LEVEL=DEBUG
python -m src.core.robot --verbose
```

Use the built-in profiler:

```python
from src.utils.timing import Profiler

profiler = Profiler()
profiler.start('cv_process')
output = pipeline.process(frame)
profiler.stop('cv_process')
print(profiler.summary())
```
