import cv2
import numpy as np

# Carregar o classificador de face pré-treinado
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Carregar a imagem da máscara de carnaval (com canal alfa)
try:
    mask = cv2.imread('image.png', -1)
    if mask is None:
        raise FileNotFoundError("Arquivo 'image.png' não encontrado ou não pôde ser lido.")
except Exception as e:
    print(f"Erro ao carregar a imagem da máscara: {e}")
    exit()


cap = cv2.VideoCapture(0)

def overlay_image_alpha(img, img_overlay, x, y, w, h):

    img_overlay_resized = cv2.resize(img_overlay, (w, h))

    b, g, r, a = cv2.split(img_overlay_resized)
    overlay_color = cv2.merge((b, g, r))

    mask = cv2.medianBlur(a, 5)

    y1, y2 = y, y + h
    x1, x2 = x, x + w

    if y1 >= img.shape[0] or x1 >= img.shape[1]:
        return
    if y2 <= 0 or x2 <= 0:
        return

    y1_roi, y2_roi = max(0, y1), min(img.shape[0], y2)
    x1_roi, x2_roi = max(0, x1), min(img.shape[1], x2)

    y1_mask = max(0, -y1)
    y2_mask = h - max(0, y2 - img.shape[0])
    x1_mask = max(0, -x1)
    x2_mask = w - max(0, x2 - img.shape[1])

    roi = img[y1_roi:y2_roi, x1_roi:x2_roi]
    mask_roi = mask[y1_mask:y2_mask, x1_mask:x2_mask]
    overlay_color_roi = overlay_color[y1_mask:y2_mask, x1_mask:x2_mask]

    if roi.shape[:2] != mask_roi.shape[:2]:
        return

    mask_inv = cv2.bitwise_not(mask_roi)

    img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    img_fg = cv2.bitwise_and(overlay_color_roi, overlay_color_roi, mask=mask_roi)

    dst = cv2.add(img_bg, img_fg)

    img[y1_roi:y2_roi, x1_roi:x2_roi] = dst

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            offset_y = int(-0.25 * h)
            overlay_image_alpha(frame, mask, x, y + offset_y, w, h)

        cv2.putText(frame, "Rosto Detectado", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Filtro de Carnaval', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
