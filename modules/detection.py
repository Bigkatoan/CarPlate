from ultralytics import YOLO
import cv2
import numpy

model = YOLO('models/plate_detection.pt')

def get_bbox(img, conf=0.7, verbose=True):
    """
    lấy ra các bounding box của biển xe.
    conf là độ tự tin khi có biển báo.
    """
    result = model(img, conf=conf, verbose=verbose)[0]
    outboxes = []
    for r in result:
        boxes = r.boxes
        for box in boxes:
            outboxes.append(box.xyxy[0].detach().cpu().numpy())
    return numpy.array(outboxes).astype(int)

def get_img(img, bbox):
    """
    crop ảnh dựa vào bounding box.
    """
    x1, y1, x2, y2 = bbox
    new_img = img[int(y1): int(y2), int(x1):int(x2)]
    return new_img

def draw_bbox(img, bbox):
    """
    vẽ bounding box lên ảnh.
    """
    x1, y1, x2, y2 = bbox
    new_img = cv2.rectangle(
        img, 
        (int(x1), int(y1)),
        (int(x2), int(y2)),
        thickness=2,
        color=(255, 0, 0)
    )
    return new_img