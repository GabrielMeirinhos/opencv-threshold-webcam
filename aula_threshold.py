import cv2

# Função callback necessária para as trackbars (barras de deslizamento)
# Ela é chamada toda vez que o valor muda, mas não precisamos fazer nada aqui
# pois leremos o valor diretamente no loop principal.
def nada(x):
    pass

def main():
    # --- Configuração Inicial ---
    
    # 1. Inicializa a captura da webcam (o número 0 geralmente é a webcam padrão)
    cap = cv2.VideoCapture(0)
    
    # Verifica se a webcam abriu corretamente
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return

    # 2. Cria uma janela nomeada onde adicionaremos os controles (trackbars)
    cv2.namedWindow('Ajustes')

    # 3. Criação das Trackbars (Barras de deslizamento)
    # Sintaxe: cv2.createTrackbar('Nome', 'Janela', Valor Inicial, Valor Máximo, Função Callback)
    
    # Trackbar para o valor do Threshold (Limiar)
    # Varia de 0 (preto absoluto) a 255 (branco absoluto)
    cv2.createTrackbar('Limiar', 'Ajustes', 127, 255, nada)
    
    # Trackbar para inverter as cores (0 = Normal, 1 = Invertido)
    cv2.createTrackbar('Inverter', 'Ajustes', 0, 1, nada)

    print("Pressione 'q' para sair do programa.")

    # --- Loop Principal (Processamento em Tempo Real) ---
    while True:
        # Lê um frame (imagem) da webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Erro ao capturar imagem.")
            break

        # --- Conceito: Imagem em Escala de Cinza ---
        # Convertemos a imagem colorida (BGR) para tons de cinza.
        # Numa imagem em cinza, cada pixel tem apenas uma intensidade de luz,
        # variando de 0 (preto) a 255 (branco). Isso simplifica o processamento.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # --- Leitura dos Valores das Trackbars ---
        # Pegamos o valor atual que o usuário escolheu na barra deslizante
        valor_limiar = cv2.getTrackbarPos('Limiar', 'Ajustes')
        inverter = cv2.getTrackbarPos('Inverter', 'Ajustes')

        # --- Conceito: Threshold Binário (Limiarização) ---
        # O Threshold é uma decisão simples para cada pixel:
        # "Se a intensidade do pixel for MAIOR que o limiar, ele vira BRANCO (255).
        #  Caso contrário, ele vira PRETO (0)."
        
        # Define o tipo de threshold baseado na escolha do usuário (Normal ou Invertido)
        tipo_threshold = cv2.THRESH_BINARY
        if inverter == 1:
            tipo_threshold = cv2.THRESH_BINARY_INV # Inverte: Maior que limiar vira PRETO

        # Aplica o threshold
        # Retorna dois valores: o valor usado (ret_val) e a imagem processada (thresh_img)
        ret_val, thresh_img = cv2.threshold(gray, valor_limiar, 255, tipo_threshold)

        # --- Exibição de Informações na Tela ---
        # Escreve o valor do limiar na imagem processada para facilitar a visualização
        texto = f"Limiar: {valor_limiar}"
        # Sintaxe: imagem, texto, posição (x,y), fonte, escala, cor (B,G,R), espessura
        cv2.putText(thresh_img, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # --- Exibição das Janelas ---
        # Mostra as 3 etapas do processo em janelas separadas
        cv2.imshow('1. Imagem Original (Colorida)', frame)
        cv2.imshow('2. Escala de Cinza (Intensidade)', gray)
        cv2.imshow('3. Resultado Threshold (Preto e Branco)', thresh_img)

        # O comando cv2.waitKey(1) espera 1 milissegundo por uma tecla.
        # Se a tecla 'q' for pressionada, saímos do loop.
        # A função ord('q') retorna o código ASCII da letra 'q'.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # --- Encerramento ---
    # Libera a câmera e fecha todas as janelas abertas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
