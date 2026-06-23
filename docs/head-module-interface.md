# Head Module Interface

The head module system is the core of the robot's modularity. Any hardware or virtual module can be mounted as the "head" by implementing the `HeadModule` interface.

## Interface Contract

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, List

class HeadModule(ABC):
    """Base class for all head modules."""

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> bool:
        """Initialize hardware connections and calibration."""
        pass

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """Return list of capability strings (e.g., 'depth', 'rgb', 'point_cloud')."""
        pass

    @abstractmethod
    def read_sensors(self) -> Dict[str, Any]:
        """Read current sensor data. Returns dict of named sensor outputs."""
        pass

    @abstractmethod
    def get_camera_intrinsics(self) -> Dict[str, float]:
        """Return camera calibration matrix if applicable."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Clean shutdown of hardware resources."""
        pass

    def get_transform_to_base(self) -> List[float]:
        """Return 6-DOF transform [x, y, z, roll, pitch, yaw] from head to robot base."""
        return [0, 0, 0.3, 0, 0, 0]  # default: mounted 30cm above base
```

## Creating a New Head Module

1. Create a new directory in `src/modules/your_head/`
2. Implement the `HeadModule` interface
3. Register it in `src/modules/registry.py`
4. Add config in `config/heads/your_head.yaml`

### Example: Custom Sensor Head

```python
from src.modules.base import HeadModule

class CustomSensorHead(HeadModule):
    def __init__(self):
        self.sensor = None

    def initialize(self, config):
        self.sensor = init_sensor(config['port'])
        return self.sensor is not None

    def get_capabilities(self):
        return ['temperature', 'humidity', 'air_quality']

    def read_sensors(self):
        return {
            'temperature': self.sensor.read_temp(),
            'humidity': self.sensor.read_humidity(),
            'air_quality': self.sensor.read_aqi()
        }

    def get_camera_intrinsics(self):
        return {}  # no camera on this head

    def shutdown(self):
        self.sensor.close()
```

## Available Head Modules

### vision-head

Stereo camera module with IMU for visual SLAM and object detection.

**Capabilities**: `rgb`, `depth`, `stereo`, `imu`, `point_cloud`

**Config** (`config/heads/vision-head.yaml`):
```yaml
camera:
  resolution: [1280, 720]
  fps: 30
  stereo_baseline: 0.06  # meters
imu:
  sample_rate: 200  # Hz
  fusion: complementary
```

### lidar-head

360° rotating LiDAR for precision mapping.

**Capabilities**: `point_cloud`, `2d_scan`

### arm-head

5-DOF robotic arm with parallel gripper.

**Capabilities**: `manipulation`, `gripper`

### display-head

LED matrix for expressions and status display.

**Capabilities**: `display`, `led`

## Module Lifecycle

```
[Power On] → initialize() → read_sensors() loop → shutdown()
                                       ↓
                              [Learning System] processes data
                                       ↓
                              [Core] makes decisions
```
