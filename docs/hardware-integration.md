# Hardware Integration

## Supported Hardware

### Microcontrollers

| Board | Status | Use Case |
|-------|--------|----------|
| ESP32 | Supported | Motor control, sensor reading |
| STM32 | Supported | High-speed motor control |
| Arduino Mega | Experimental | Simple sensor integration |

### Motor Drivers

| Driver | Protocol | Status |
|--------|----------|--------|
| L298N | PWM | Supported |
| TB6612FNG | PWM | Supported |
| RoboHAT | I2C | Supported |
| Custom CAN | CAN | In Development |

### Sensors

| Sensor | Interface | Status |
|--------|-----------|--------|
| IMU (MPU6050) | I2C | Supported |
| IMU (BNO055) | I2C | Supported |
| Ultrasonic (HC-SR04) | GPIO | Supported |
| ToF (VL53L0X) | I2C | Supported |
| LiDAR (RPLidar) | Serial/USB | Supported |
| Camera (USB) | USB | Supported |
| Camera (CSI) | CSI | Supported |

## Wiring Diagram

```
┌──────────────────────────────────────────┐
│             Main Controller              │
│           (Jetson Orin / RPi)            │
├──────────────────────────────────────────┤
│  USB ──── Camera (vision-head)           │
│  USB ──── LiDAR (lidar-head)             │
│  I2C ──── IMU                            │
│  GPIO ─── Motor Driver                   │
│  SPI ──── Display (display-head)         │
└──────────────────────────────────────────┘
         │              │
         ▼              ▼
   ┌──────────┐   ┌──────────┐
   │ Left     │   │ Right    │
   │ Motors   │   │ Motors   │
   └──────────┘   └──────────┘
```

## Communication Protocols

### I2C

```yaml
i2c:
  bus: 1
  address_imu: 0x68
  address_tof: 0x29
  frequency: 400000  # 400kHz
```

### Serial

```yaml
serial:
  lidar:
    port: /dev/ttyUSB0
    baudrate: 115200
  esp32:
    port: /dev/ttyACM0
    baudrate: 921600
```

### CAN Bus

```yaml
can:
  interface: can0
  bitrate: 500000
  nodes:
    - id: 0x10  # motor controller
    - id: 0x20  # sensor hub
```

## Calibration

Run calibration procedures:

```bash
# Calibrate IMU
python -m scripts.calibrate --sensor imu

# Calibrate camera
python -m scripts.calibrate --sensor camera

# Calibrate motors
python -m scripts.calibrate --sensor motors
```
