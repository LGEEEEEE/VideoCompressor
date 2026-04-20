import os
from moviepy import VideoFileClip

def comprimir_video(arquivo_entrada, arquivo_saida, tamanho_alvo_mb):
    """
    Processa um arquivo de vídeo com o objetivo de reduzir seu tamanho 
    para um valor aproximado especificado em megabytes.
    """
    # Validação inicial do caminho do arquivo
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: O arquivo de origem '{arquivo_entrada}' não foi localizado.")
        return

    print(f"Iniciando leitura do arquivo: {arquivo_entrada}...")
    
    try:
        clip = VideoFileClip(arquivo_entrada)
        duracao_segundos = clip.duration
        
        # --- CÁLCULO DE BITRATE ---
        # 1. Conversão do tamanho alvo (MB) para bits
        tamanho_alvo_bits = tamanho_alvo_mb * 8 * 1024 * 1024
        
        # 2. Definição do bitrate total (bits por segundo)
        bitrate_total = tamanho_alvo_bits / duracao_segundos
        
        # 3. Subtração da taxa reservada para o áudio (padrão de 128 kbps)
        bitrate_audio = 128 * 1024
        bitrate_video = bitrate_total - bitrate_audio
        
        # Limite de segurança: Evita que o bitrate seja reduzido a um nível 
        # que cause degradação inaceitável na qualidade visual.
        if bitrate_video < 200000:
            print("Aviso: O tamanho alvo é insuficiente para a duração do vídeo. Aplicando limite mínimo de qualidade (200 kbps).")
            bitrate_video = 200000
            
        print(f"Preparando compressão (Alvo: ~{tamanho_alvo_mb} MB)...")
        print(f"Duração total: {duracao_segundos:.1f}s | Bitrate de vídeo estimado: {int(bitrate_video/1000)} kbps")

        # --- PROCESSAMENTO E EXPORTAÇÃO ---
        clip.write_videofile(
            arquivo_saida,
            codec='libx264',                 # Padrão de codificação de vídeo
            audio_codec='aac',               # Padrão de codificação de áudio
            bitrate=str(int(bitrate_video)), # Taxa de bits calculada dinamicamente
            audio_bitrate='128k',            # Taxa de bits fixa para a faixa de áudio
            preset='medium',                 # Balanceamento entre velocidade de processamento e eficiência
            threads=4,                       # Número de threads alocadas para a execução
            logger='bar'                     # Feedback visual de progresso no terminal
        )
        
        clip.close()
        
        # Validação do resultado
        tamanho_final = os.path.getsize(arquivo_saida) / (1024 * 1024)
        print(f"\nProcesso concluído com êxito. Arquivo gerado: {arquivo_saida}")
        print(f"Tamanho final em disco: {tamanho_final:.2f} MB")

    except Exception as e:
        print(f"Falha na execução: {e}")

# ==========================================
# PARÂMETROS DE EXECUÇÃO
# ==========================================
if __name__ == "__main__":
    
    # Caminho do arquivo original
    ARQUIVO_ORIGINAL = "meu_video.mp4"
    
    # Caminho de saída para o novo arquivo comprimido
    ARQUIVO_NOVO = "meu_video_leve.mp4"
    
    # Tamanho final desejado em megabytes (MB)
    TAMANHO_DESEJADO = 15 

    # Inicialização do processo
    comprimir_video(ARQUIVO_ORIGINAL, ARQUIVO_NOVO, TAMANHO_DESEJADO)