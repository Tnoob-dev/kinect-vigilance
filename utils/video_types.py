import freenect
import numpy as np
import cv2

def get_video():
    """
    normal
    """
    array, _ = freenect.sync_get_video()
    
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    
    return array

def get_depth():
    """
    profundidad
    """
    array, _ = freenect.sync_get_depth()
    
    array = array.astype(np.uint8)
    
    return array

def get_ir():
    """
    infrarrojo
    """
    # freenect.VIDEO_IR_10BIT hace que grabe en modo infrarrojo en vez del rgb
    array, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    
    # Normalizar visualización
    array = array.astype(np.float32)
    array = (array / 1024.0) * 255  # 10-bit a 8-bit
    
    return array.astype(np.uint8)