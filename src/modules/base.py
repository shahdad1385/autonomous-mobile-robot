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
        """Return list of capability strings."""
        pass

    @abstractmethod
    def read_sensors(self) -> Dict[str, Any]:
        """Read current sensor data."""
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
        return [0, 0, 0.3, 0, 0, 0]
