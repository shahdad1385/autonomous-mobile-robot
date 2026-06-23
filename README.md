# Autonomous Mobile Robot Platform

A modular, learning-enabled autonomous mobile robot platform with computer vision capabilities. Designed for flexibility — mount any head module (sensors, manipulators, displays) and let the robot perceive, learn, and navigate.

## Features

- **Modular Head System**: Hot-swappable head modules — camera arrays, LiDAR, robotic arms, displays, or custom sensors
- **Computer Vision Pipeline**: Real-time object detection, visual SLAM, depth estimation, and scene understanding
- **Online Learning**: Continuously adapts to its environment through reinforcement learning and transfer learning
- **Autonomous Navigation**: Path planning, obstacle avoidance, and dynamic route optimization
- **Plugin Architecture**: Extend functionality through standardized module interfaces

## Architecture

```
autonomous-mobile-robot/
├── src/
│   ├── core/           # Robot core: control loop, state machine, event bus
│   ├── cv/             # Computer vision: detection, tracking, SLAM
│   ├── learning/       # ML models: RL agent, transfer learning, memory
│   ├── modules/        # Head module abstractions and drivers
│   └── utils/          # Shared utilities (transforms, logging, config)
├── config/             # Runtime and model configuration files
├── docs/               # Instruction manuals and architecture docs
├── scripts/            # Setup, calibration, and deployment scripts
└── tests/              # Unit and integration tests
```

## Head Modules

The robot supports hot-swappable head modules via a standardized interface:

| Module | Description | Status |
|--------|-------------|--------|
| `vision-head` | Stereo camera + IMU for visual navigation | Stable |
| `lidar-head` | 360° LiDAR for precise mapping | In Development |
| `arm-head` | 5-DOF manipulator with gripper | Planned |
| `display-head` | LED matrix for expressions/status | Planned |
| `sensor-head` | Environmental sensors (temp, gas, UV) | Planned |

## Quick Start

```bash
# Clone and setup
git clone https://github.com/shahdad1385/autonomous-mobile-robot
cd autonomous-mobile-robot
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Run simulation
python -m src.core.robot --config config/default.yaml

# Run with specific head module
python -m src.core.robot --head vision-head --config config/vision.yaml
```

## Documentation

- [Getting Started](docs/getting-started.md)
- [Head Module Interface](docs/head-module-interface.md)
- [Computer Vision Pipeline](docs/computer-vision.md)
- [Learning System](docs/learning-system.md)
- [Configuration Guide](docs/configuration.md)
- [Hardware Integration](docs/hardware-integration.md)
- [Development Guide](docs/development.md)

## License

MIT
