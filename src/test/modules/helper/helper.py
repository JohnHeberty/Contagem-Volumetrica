import cv2
import os

# FUNÇÃO PRA CRIAR VIDEO DE SAIDA
def create_video_from_images(image_folder, output_video_path, frame_rate):
    # Obter a lista de arquivos na pasta
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images = sorted(images, key=lambda x: int("".join([row for row in x.split('.')[0] if row.isdigit()])))  

    # Verificar se há imagens na pasta
    if not images:
        print("Nenhuma imagem encontrada na pasta especificada.")
        return

    # Obter as dimensões da primeira imagem
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Criar o objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para o formato MP4
    video = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

    # Adicionar cada imagem ao vídeo
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    # Liberar o objeto VideoWriter
    video.release()
    print(f"Vídeo criado com sucesso: {output_video_path}")

# FUNÇÃO PARA OBTER O FRAMRATE DO VÍDEO
def get_framerate(video_path):
    # Abrir o vídeo
    fps = 0
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        fps = int(round(cap.get(cv2.CAP_PROP_FPS), 0))
    # Liberar o vídeo
    cap.release()
    return fps
