import cv2
import os
from datetime import datetime

def create_video_writer(folder="videos"):
    """
    Crea un nuevo archivo de video con timestamp
    """
    # Crear carpeta si no existe
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Generar nombre con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/video_{timestamp}.avi"
    
    # Configurar el video writer (ajusta FPS según necesites)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30
    frame_size = (640, 480)  # Ajusta según la resolución de tu Kinect
    
    writer = cv2.VideoWriter(filename, fourcc, fps, frame_size)
    
    return writer
