import cv2
import numpy as np

def canny_edge_detection(image_path):
    """
    Mendeteksi tepi menggunakan metode Canny Edge Detection.
    
    Args:
        image_path (str): Path ke file gambar.
    
    Returns:
        str: Path ke file hasil gambar dengan deteksi tepi.
    """
    # Membaca gambar dalam mode grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Mengaburkan gambar menggunakan Gaussian Blur
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)
    
    # Mendeteksi tepi menggunakan Canny Edge Detection
    edges = cv2.Canny(img_blur, 50, 150)
    
    # Menampilkan hasil deteksi tepi
    cv2.imshow("Canny Edge Detection", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Menyimpan hasil deteksi tepi ke file
    result_path = "canny_result.png"
    cv2.imwrite(result_path, edges)
    
    return result_path

# Contoh penggunaan
if __name__ == "__main__":
    canny_edge_detection("Fotorel.jpg")