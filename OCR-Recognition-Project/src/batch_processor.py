import os
import cv2
import pandas as pd

from src.preprocess import preprocess_image
from src.ocr_engine import extract_text_from_image
from src.confindence import calculate_confidence, get_status
from src.visualize import draw_boxes


SUPPORTED_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff"
)


def process_dataset(dataset_folder="dataset"):

    os.makedirs("output/annotated", exist_ok=True)
    os.makedirs("output/extracted_text", exist_ok=True)
    os.makedirs("output/reports", exist_ok=True)

    results = []

    files = [
        f for f in os.listdir(dataset_folder)
        if f.lower().endswith(SUPPORTED_EXTENSIONS)
    ]

    for file in files:

        path = os.path.join(dataset_folder, file)

        try:

            original, gray, blur, threshold = preprocess_image(path)

            text, data = extract_text_from_image(threshold)

            confidence = calculate_confidence(data)

            status = get_status(confidence)

            annotated = draw_boxes(original, data)

            cv2.imwrite(
                f"output/annotated/{file}",
                annotated
            )

            txt_name = os.path.splitext(file)[0] + ".txt"

            with open(
                f"output/extracted_text/{txt_name}",
                "w",
                encoding="utf-8"
            ) as f:
                f.write(text)

            results.append({
                "filename": file,
                "confidence": confidence,
                "status": status
            })

            print(f"Processed: {file}")

        except Exception as e:

            print(f"Error processing {file}: {e}")

    df = pd.DataFrame(results)

    df.to_csv(
        "output/reports/summary.csv",
        index=False
    )

    if len(df):

        avg_conf = round(df["confidence"].mean(), 2)
        pass_count = len(df[df["status"] == "PASS"])

        fail_count = len(df[df["status"] == "FAIL"])

        pass_rate = round( pass_count / len(df) * 100, 2)

        with open(
            "output/reports/statistics.txt",
            "w"
        ) as f:

            f.write(f"Total Images: {len(df)}\n")
            f.write(f"Average Confidence: {avg_conf}%\n")
            f.write(f"PASS Count: {pass_count}\n")
            f.write(f"FAIL Count: {fail_count}\n")
            f.write(f"Pass Rate: {pass_rate}%\n")
    return df