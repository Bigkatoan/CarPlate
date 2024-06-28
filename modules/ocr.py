from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def get_result(img, return_conf=True):
    """
    đầu vào là 1 ảnh và đầu ra trả về là text và độ tự tin.
    tương ứng là otext, oconf.
    otext trả về chữ xuất hiện trong ảnh.
    oconf trả về mức độ tự tin, hoặc độ chính xác mà chữ có xuất hiện.
    """
    result = ocr.ocr(img, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        otext = ''
        oconf = 0
        if res is None:
            return '', 0
        for line in res:
            text, conf = line[1]
            if conf > 0.9:
                otext += text
            oconf += conf
        oconf /= len(res)
        return otext, oconf
    
def draw_text(img, bbox, text, conf):
    """
    vẽ text lên trên ảnh.
    """
    x1, y1, x2, y2 = bbox
    ftext = text + f" {conf:.2f}"
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (x1, y1) 
    fontScale = 1
    color = (255, 0, 0) 
    thickness = 2
    img = cv2.putText(img, ftext, org, font,  
                       fontScale, color, thickness, cv2.LINE_AA)
    return img
    