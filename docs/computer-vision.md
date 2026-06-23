# Computer Vision Pipeline

## Overview

The CV system processes raw camera feeds from the head module into actionable perception data: detected objects, tracked features, depth maps, and semantic understanding.

## Pipeline Stages

```
Raw Camera Feed
      │
      ▼
┌─────────────┐
│ Preprocess   │  → Resize, normalize, color space conversion
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Detection    │  → YOLOv8 / custom model inference
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Tracking     │  → ByteTrack multi-object tracking
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Depth/3D     │  → Stereo matching or monocular depth
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Scene Graph  │  → Spatial relationships between objects
└──────┬──────┘
       │
       ▼
  PerceptOutput (fed to Learning System)
```

## Models

| Model | Purpose | Framework |
|-------|---------|-----------|
| YOLOv8-nano | Real-time object detection | ONNX Runtime |
| MonoDepth2 | Monocular depth estimation | PyTorch |
| SuperPoint | Feature extraction for SLAM | PyTorch |
| NetVLAD | Place recognition | PyTorch |

## Usage

```python
from src.cv.pipeline import CVPipeline

pipeline = CVPipeline(config_path="config/cv.yaml")
pipeline.initialize()

while True:
    frame = head_module.read_sensors()['rgb']
    output = pipeline.process(frame)
    # output.detections — list of DetectedObject
    # output.depth_map — numpy array
    # output.feature_points — list of (x, y, descriptor)
    # output.scene_graph — SceneGraph
```

## Training Custom Detectors

Place your dataset in `data/custom/` with YOLO format:

```
data/custom/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── data.yaml
```

Train:
```bash
python -m src.cv.train --dataset data/custom/data.yaml --epochs 100 --model yolov8n
```
