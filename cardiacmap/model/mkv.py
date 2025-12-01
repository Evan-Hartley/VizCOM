import os
import cv2
import numpy as np

from cardiacmap.model.data import CardiacSignal
from cardiacmap.viewer.dataShape import dataShape, dimImg

def read_mkv_data(filepath: str):
    capture = cv2.VideoCapture(filepath)
    if not capture.isOpened():
        print("Error opening video file")

    frame_rate = int(capture.get(cv2.CAP_PROP_FPS))
    data = []
    i = 0
    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            data.append(cv2.resize(frame, (dimImg.width,dimImg.height)))
        else:
            break
        i+=1
    capture.release()

    filename = os.path.basename(filepath)
    metadata = {"filename": filename, "span_T": len(data), "span_X": dimImg.width, "span_Y": dimImg.height, "framerate": frame_rate}
    return metadata, np.array(data)

def load_mkv_file(filepath):
    """Wrapper to load a raw .MKV file.

    Args:
        filepath (str): Path ot file

    Returns:
        signals: Dictionary of CascadeSignal
    """
    signals = {}

    file_metadata, sigarray = read_mkv_data(filepath)
    if sigarray is not None:
        signals[0] = CardiacSignal(
            signal=sigarray, metadata=file_metadata, channel="Single"
        )
    return signals