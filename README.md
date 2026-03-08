# Aplicação Didática: Threshold (Limiar) com OpenCV

Este projeto é uma ferramenta educacional simples para demonstrar o conceito de **Thresholding (Limiarização)** em Processamento de Imagens para alunos iniciantes em programação Python e Visão Computacional.

A aplicação captura vídeo da webcam em tempo real e permite que o aluno ajuste dinamicamente o valor de corte (threshold) para ver como o computador decide transformar uma imagem em preto e branco.

## 📋 Pré-requisitos

*   Python (3.x) instalado.
*   Uma webcam conectada ao computador.

## 📦 Instalação

Você precisará instalar a biblioteca `opencv-python`. Abra o terminal ou prompt de comando e digite:

```bash
pip install opencv-python
```

## 🚀 Como Executar

1.  Abra o terminal na pasta onde o arquivo `aula_threshold.py` está salvo.
2.  Execute o comando:

```bash
python aula_threshold.py
```

3.  Use as janelas que abrirão para interagir com o programa.
4.  Pressione a tecla **`q`** para encerrar o programa.

## 🎓 Guia Didático para o Aluno

### Conceitos Chave

1.  **Pixel**: É o menor ponto de uma imagem digital. Imagine a tela como uma grade gigante de pequenos quadradinhos coloridos. Cada quadradinho é um pixel.
2.  **Intensidade (Escala de Cinza)**: Em uma imagem preto e branco, a "cor" é apenas a intensidade da luz.
    *   **0** = Preto absoluto (sem luz)
    *   **255** = Branco absoluto (luz máxima)
3.  **Threshold (Limiar)**: É um valor de corte que escolhemos para simplificar a imagem. O computador faz uma pergunta para cada pixel:
    *   *"Sua intensidade é maior que o Limiar?"*
    *   **SIM**: O pixel vira BRANCO (255).
    *   **NÃO**: O pixel vira PRETO (0).

### 🧪 Experimentação (O que observar)

Peça aos alunos para testarem os seguintes valores na barra deslizante (Trackbar):

#### Valor Baixo (~50)
*   **O que acontece?** A imagem fica quase toda branca.
*   **Por quê?** O limiar é muito baixo. Quase todos os pixels (mesmo os cinzas escuros) são maiores que 50, então eles "passam no teste" e viram brancos. Apenas as sombras muito escuras ficam pretas.

#### Valor Médio (~127)
*   **O que acontece?** Um equilíbrio entre preto e branco.
*   **Por quê?** 127 é a metade do caminho entre e 0 e 255. Pixels mais claros que cinza médio viram branco, e mais escuros viram preto. É bom para separar objetos do fundo em iluminação normal.

#### Valor Alto (~200)
*   **O que acontece?** A imagem fica quase toda preta.
*   **Por quê?** O limiar é muito alto/rigoroso. Apenas os pixels muito brilhantes (luzes fortes, reflexos) conseguem ser maiores que 200. O resto "reprova" e vira preto.

## 🛠️ Controles

*   **Trackbar "Limiar"**: Ajusta o valor de corte de 0 a 255.
*   **Trackbar "Inverter"**: Inverte a lógica (O que era branco vira preto e vice-versa). Útil para entender como podemos focar no objeto ou no fundo.
*   **Tecla 'q'**: Sai do programa.
