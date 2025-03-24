from ultralytics import YOLO
import cv2

# Load model YOLOv8 Instance Segmentation
model = YOLO("yolov8n-seg.pt")

def detect_rail_lane(image_path):
    """
    Mendeteksi jalur rel menggunakan YOLOv8 Instance Segmentation.
    
    Args:
        image_path (str): Path ke file gambar.
    
    Returns:
        None: Hasil deteksi disimpan sebagai file gambar.
    """
    # Melakukan deteksi menggunakan model YOLO
    results = model(image_path, show=True)
    
    # Menyimpan hasil deteksi ke file
    results[0].save("lane_detection_result.jpg")

# Contoh penggunaan
if __name__ == "__main__":
    detect_rail_lane("Fotorel.jpg")