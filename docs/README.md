# YOLO Human-in-the-Loop Video Annotation

## Motivation
Annotating video datasets is expensive and slow. This project studies YOLO-assisted labeling where humans only correct keyframes.

## Research Question
How much annotation time can be saved by labeling every Nth frame while maintaining dataset quality?

## Pipeline Overview
Video → YOLO → Keyframe Review → Tracking → Export → Retraining

## Repo Structure

yolo-human-in-the-loop-video-annotation/
│
├── README.md
├── requirements.txt
├── environment.yml
│
├── data/
│   ├── raw_videos/
│   ├── extracted_frames/
│   ├── prelabels_yolo/
│   ├── annotations_manual/
│   ├── annotations_hybrid/
│   ├── ground_truth/
│   └── datasets_ready/
│
├── experiments/
│   ├── frame_skip_5/
│   ├── frame_skip_10/
│   ├── frame_skip_20/
│   └── tracking_vs_no_tracking/
│
├── src/
│   ├── video_processing/
│   │   ├── extract_frames.py
│   │   └── sample_frames.py
│   │
│   ├── yolo/
│   │   ├── run_detection.py
│   │   ├── train_yolo.py
│   │   └── export_predictions.py
│   │
│   ├── annotation_tools/
│   │   ├── cvat_integration.py
│   │   └── labelstudio_integration.py
│   │
│   ├── tracking/
│   │   ├── propagate_boxes.py
│   │   └── evaluate_tracking.py
│   │
│   ├── evaluation/
│   │   ├── compute_map.py
│   │   ├── compute_iou.py
│   │   └── time_analysis.py
│   │
│   └── utils/
│       ├── config.py
│       └── logging.py
│
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── results_visualization.ipynb
│   └── error_analysis.ipynb
│
├── reports/
│   ├── figures/
│   ├── tables/
│   └── final_report.md
│
├── scripts/
│   ├── run_full_pipeline.sh
│   ├── run_experiment_skip10.sh
│   └── retrain_cycle.sh
│
└── docs/
    ├── project_proposal.md
    ├── methodology.md
    ├── experiment_log.md
    └── future_work.md 

## Week Plan
Week 01: Baseline + setup
Week 02: YOLO prelabels + integration
Week 03: Hybrid annotation experiments
Week 04: Retraining + analysis
Week 05: Writeup