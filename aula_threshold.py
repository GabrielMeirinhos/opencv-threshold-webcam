import cv2
import numpy as np

def nada(x):
    pass

def criar_histograma(imagem_gray):
    """Cria uma imagem do histograma da imagem em escala de cinza."""
    hist_h = 300
    hist_w = 512
    bin_w = int(round(hist_w / 256))
    
    hist_img = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
    
    hist = cv2.calcHist([imagem_gray], [0], None, [256], [0, 256])
    cv2.normalize(hist, hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
    
    for i in range(1, 256):
        cv2.line(hist_img,
                 (bin_w * (i - 1), hist_h - int(hist[i - 1])),
                 (bin_w * i, hist_h - int(hist[i])),
                 (255, 200, 0), 2)
    
    return hist_img

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return

    cv2.namedWindow('Ajustes')

    cv2.createTrackbar('Limiar', 'Ajustes', 127, 255, nada)
    
    cv2.createTrackbar('Inverter', 'Ajustes', 0, 1, nada)

    print("Pressione 'q' para sair do programa.")

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Erro ao capturar imagem.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        valor_limiar = cv2.getTrackbarPos('Limiar', 'Ajustes')
        inverter = cv2.getTrackbarPos('Inverter', 'Ajustes')

        tipo_threshold = cv2.THRESH_BINARY
        if inverter == 1:
            tipo_threshold = cv2.THRESH_BINARY_INV 

        ret_val, thresh_img = cv2.threshold(gray, valor_limiar, 255, tipo_threshold)


        texto = f"Limiar: {valor_limiar}"
        cv2.putText(thresh_img, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        histograma = criar_histograma(gray)

        cv2.imshow('1. Imagem Original (Colorida)', frame)
        cv2.imshow('2. Escala de Cinza (Intensidade)', gray)
        cv2.imshow('3. Resultado Threshold (Preto e Branco)', thresh_img)
        cv2.imshow('4. Histograma', histograma)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
