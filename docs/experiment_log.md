# 📅 Day-03: Frame Extraction & Keyframe Sampling

## 🎯 Objective

Convert raw traffic videos into:

- Full frame datasets (every frame)
- Keyframe datasets (every Nth frame)
- Logged statistics for research experiments

This step prepares data for manual annotation and hybrid YOLO-assisted labeling.

---

# 📁 Input Data

Location:

data/raw_videos/

Videos used:

- traffic_01.mp4
- traffic_02.mp4
- traffic_03.mp4
- (add more if applicable)

---

# 🛠️ Frame Extraction Script

Script location:

src/video_processing/extract_frames.py

### Script Purpose

- Open video file
- Read frame-by-frame
- Save frames as JPG images
- Support skipping logic using `--every N`

---

# ▶️ Commands Used

### Extract All Frames

Example:

python src/video_processing/extract_frames.py \
  --video data/raw_videos/traffic_01.mp4 \
  --out data/extracted_frames/traffic_01_all \
  --every 1

---

### Extract Skip-10 Keyframes

python src/video_processing/extract_frames.py \
  --video data/raw_videos/traffic_01.mp4 \
  --out data/extracted_frames/traffic_01_skip10 \
  --every 10

---

# 📊 Frame Counts

Fill in your actual numbers below:

---

## traffic_01.mp4

- Total frames (every=1): _______
- Skip-10 frames: _______
- Resolution: _______
- FPS: _______
- Notes:
  - Scene type:
  - Density:
  - Occlusion level:
  - Lighting:

---

## traffic_02.mp4

- Total frames (every=1): _______
- Skip-10 frames: _______
- Resolution: _______
- FPS: _______
- Notes:
  - Scene type:
  - Density:
  - Occlusion level:
  - Lighting:

---

## traffic_03.mp4

- Total frames (every=1): _______
- Skip-10 frames: _______
- Resolution: _______
- FPS: _______
- Notes:
  - Scene type:
  - Density:
  - Occlusion level:
  - Lighting:

---

# 📂 Output Folder Structure

After execution:

data/extracted_frames/
├── traffic_01_all/
├── traffic_01_skip10/
├── traffic_02_all/
├── traffic_02_skip10/
├── traffic_03_all/
├── traffic_03_skip10/

---

# 🧠 Observations

- Frame numbering is zero-padded (000000.jpg format)
- Skip-10 reduces annotation load by ~90%
- Keyframes will be used for manual annotation in Day-04
- All frames will be used later for:
  - YOLO inference
  - Tracking experiments
  - Accuracy comparison

---

# ⚠️ Potential Issues Observed

(Write if applicable)

- Motion blur:
- Fast object movement:
- Night lighting:
- Heavy occlusion:
- Camera shake:

---

# 📈 Why This Step Matters

This enables:

- Controlled frame-skip experiments (5 / 10 / 20)
- Accurate measurement of annotation effort reduction
- Fair comparison between:
  - Manual labeling
  - YOLO-only labeling
  - Hybrid labeling

---

# ✅ Day-03 Completion Checklist

- [ ] Extraction script working
- [ ] All frames generated
- [ ] Skip-10 frames generated
- [ ] Frame counts recorded
- [ ] Results committed to GitHub

---

# 🚀 Next Step (Day-04 Preview)

Manual annotation of skip-10 frames to create:

- Ground truth dataset
- Annotation time baseline
- Box count statistics