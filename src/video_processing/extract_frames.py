import cv2
import argparse
from pathlib import Path

def extract_frames(video_path, output_dir, every_n=1):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    frame_id = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % every_n == 0:
            out_file = output_dir / f"{saved:06d}.jpg"
            cv2.imwrite(str(out_file), frame)
            saved += 1

        frame_id += 1

    cap.release()
    print(f"Saved {saved} frames to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--every", type=int, default=1)

    args = parser.parse_args()
    extract_frames(args.video, args.out, args.every)