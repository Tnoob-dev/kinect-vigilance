import cv2
import time
from datetime import datetime
from utils.video_types import get_video, get_ir, get_depth
from utils.functions import create_video_writer
import freenect

def main():
    duration = 86400
    
    last_time_saved = time.time()
    video_writer = None
    frame_count = 0
    
    body = freenect.init()
    
    
    while True:
        video_rgb = get_video()
        frame_count += 1
        
        # crear el video_writer si no existe
        if video_writer is None:
            video_writer = create_video_writer()
            print("Iniciando grabaciones")
            
        if video_writer is not None:
            video_writer.write(video_rgb)
        
        # tiempo actual
        current_time = time.time()
        
        # si tiempo actual - el primer tiempo cogido >= 5
        if current_time - last_time_saved >= duration:
            # otra vez chequear que video_writer no sea None
            if video_writer is not None:
                
                video_writer.release()
                
                date = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                print(f"Video guardado. Fecha: {date}")
                frame_count = 0
                
            video_writer = create_video_writer()
            last_time_saved = current_time
            print("Iniciando nuevo segmento de grabacion")
            
        cv2.imshow("Vigilancia", video_rgb)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
        # if cv2.waitKey(1) & 0xFF == ord("w"):
        #     freenect.set_tilt_d
    
    if video_writer is not None:
        video_writer.release()
    cv2.destroyAllWindows()
    print("Sistema de vigilancia detenido.")

    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()