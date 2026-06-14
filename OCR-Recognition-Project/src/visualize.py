import cv2


def draw_boxes(image, data):

    annotated = image.copy()

    for _, row in data.iterrows():
        try:
            conf = float(row["conf"])
            if conf < 0:
                continue
            
            x = int(row["left"])
            y = int(row["top"])
            w = int(row["width"])
            h = int(row["height"])

            cv2.rectangle(
                annotated,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        except Exception:
            continue

    return annotated