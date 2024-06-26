import cv2
import numpy as np
MODEL = "model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "model/MobileNetSSD_deploy.prototxt.txt"

def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image,(300,300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections

def annotate_image(
        image, detections, confidence_threshold = 0.5
):
    #loop over the detections
    (h, v) = image.shape[:2]
    for i in np.range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startx, starty, endx, endy) = box.astype("int")
            cv2.rectangle(image, (startx, starty), (endx, endy), 70, 2)
    return image


import numpy as np
from PIL import Image
import streamlit as st

def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg','png','jpeg'])
    if file is not None:
        st.image(file, caption = "Upload Image")

        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption = "Processed Image")

if __name__ == "__main__":
    main()