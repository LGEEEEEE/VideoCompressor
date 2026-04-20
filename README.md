🎬 VideoCompressor
O VideoCompressor é uma ferramenta simples e eficiente desenvolvida em Python para reduzir o tamanho de arquivos de vídeo. Ele calcula automaticamente o bitrate ideal para comprimir o vídeo e atingir um tamanho alvo específico (em MB) definido por você, buscando manter a melhor qualidade visual e de áudio possível.

🚀 Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina (recomenda-se a versão 3.12 ou superior).

O processamento e a conversão do vídeo são feitos através da biblioteca moviepy.

🛠️ Instalação
Para baixar as dependências necessárias, abra o seu terminal na pasta do projeto e execute o comando abaixo:

Bash
pip install moviepy
⚙️ Como Configurar
Antes de rodar a ferramenta, você precisa informar qual vídeo deseja comprimir e qual será o tamanho final.

Abra o arquivo videocompressor.py e altere as variáveis no final do código, na seção de parâmetros:

Python
# ==========================================
# PARÂMETROS DE EXECUÇÃO
# ==========================================
ARQUIVO_ORIGINAL = "meu_video.mp4"       # Insira o nome do seu vídeo original
ARQUIVO_NOVO = "meu_video_leve.mp4"      # Defina o nome do novo vídeo comprimido
TAMANHO_DESEJADO = 15                    # Defina o tamanho máximo desejado em MB
Aviso: O arquivo de vídeo original deve estar na mesma pasta que o script Python para ser lido corretamente.

▶️ Como Usar
Com as dependências instaladas e o arquivo configurado, basta executar o script no terminal:

Bash
python videocompressor.py
O terminal exibirá uma barra de progresso durante a compressão e, ao final, mostrará o tamanho exato do novo arquivo gerado.