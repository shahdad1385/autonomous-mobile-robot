# Learning System

## Overview

The learning system enables the robot to adapt to its environment through online learning, combining reinforcement learning with episodic memory for continual improvement.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                 Learning Manager                │
├─────────────┬──────────────┬────────────────────┤
│ RL Agent    │ Memory Bank  │ Transfer Learning  │
│ (PPO)       │ (episodic)   │ (fine-tune)        │
├─────────────┴──────────────┴────────────────────┤
│              Experience Replay Buffer            │
├─────────────────────────────────────────────────┤
│         CV Pipeline Output (percepts)           │
└─────────────────────────────────────────────────┘
```

## Components

### RL Agent (PPO)

Proximal Policy Optimization agent that learns navigation and interaction policies.

- **State space**: CV features + proprioceptive data (odom, IMU)
- **Action space**: [velocity_x, velocity_y, angular_velocity]
- **Reward**: Based on task completion, energy efficiency, safety

### Episodic Memory

Stores and retrieves past experiences to avoid repeating mistakes:

```python
from src.learning.memory import EpisodicMemory

memory = EpisodicMemory(capacity=10000)

# Store experience
memory.store({
    'observation': obs,
    'action': action,
    'reward': reward,
    'context': {'location': 'kitchen', 'time': timestamp}
})

# Retrieve similar past experiences
similar = memory.retrieve(query=current_obs, k=5)
```

### Transfer Learning

Fine-tune pre-trained models on new environments:

```python
from src.learning.transfer import AdaptToEnvironment

adapter = AdaptToEnvironment(base_model='navigation_v1.pt')
adapter.fine_tune(new_env_data, epochs=50)
```

## Training

```bash
# Train RL agent in simulation
python -m src.learning.train --mode rl --env sim --episodes 10000

# Train with real robot (requires head module)
python -m src.learning.train --mode rl --env real --head vision-head --episodes 500

# Run evaluation
python -m src.learning.eval --checkpoint checkpoints/latest.pt
```

## Reward Shaping

Rewards are configurable in `config/learning/rewards.yaml`:

```yaml
rewards:
  goal_reached: 100.0
  collision: -50.0
  energy_penalty: -0.01
  exploration_bonus: 1.0
  safety_violation: -100.0
```

## Safety Constraints

The learning system enforces hard safety constraints:

- Maximum velocity limits
- Collision avoidance (override learned policy)
- Battery level thresholds
- Geofencing (stay within defined area)
