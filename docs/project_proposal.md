## Title 

YOLO-Assisted Human-in-the-Loop Video Annotation for Traffic Scenes

## Motivation

Manual labeling of traffic footage is expensive and slow. This project
studies how key-frame correction combined with YOLO predictions and
tracking can reduce human effort.

## Research Question

How much annotation time can be saved by labeling every Nth frame while
maintaining bounding-box quality?

## Domain

Traffic surveillance footage from road intersections and highways.

## Target Classes

car, bus, truck, motorcycle, person

## Planned Experiments

• Frame skip rates: 5 / 10 / 20
• Manual vs YOLO-only vs Hybrid
• Retraining loop
• Tracking on/offs