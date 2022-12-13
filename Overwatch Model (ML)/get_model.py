import os
import cv2
import numpy as np
import youtube_dl

def setOutside(cap, start, end):
    imgs = [];
    cap.set(cv2.CAP_PROP_POS_FRAMES, start);
    for a in range(start, end):
        _, frame = cap.read();
        imgs.append(frame);
        
def download_videos_frame(url, folder, skip = False):
    video_url = url

    ydl_opts = {}

    # create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)

    # get video formats available
    formats = info_dict.get('formats',None)

    for f in formats:

        # I want the lowest resolution, so I set resolution as 144p
        if f.get('format_note',None) == '1080p60' or f.get('format_note',None) == '1080p':

            #get the video url
            url = f.get('url',None)

            # open url with opencv
            cap = cv2.VideoCapture(url)

            # check if url was opened
            if not cap.isOpened():
                print('video not opened ' + folder )
                

            # create directory if it does not exist
            if not os.path.exists(folder):
                os.makedirs(folder)


            i = 0
            while True:
                try:
                    # read frame
                    ret, frame = cap.read()
                    
                    if i == 0:
                        cap.set(1, cap.get(1) + 750)
                        ret, frame = cap.read()

                    # check if frame is empty
                    if not ret:
                        break
                    
                    # check if we have enough models 
                    if i >= 50:
                        break
                    
                    # get image dimensions
                    height, width = frame.shape[:2]

                    # define region of interest (ROI)
                    # x, y, w, h = width - 650, height - 200, 650, 200
                    # roi = cv2.getRectSubPix(frame, (w, h), (x + w // 2, y + h // 2))
                    # define region of interest (ROI) and crop it
                    roi = cv2.getRectSubPix(frame, (650, 140), (width - 650 + 325, height - 200 + 70), (650, 140))
                    
                    # sauvegarde la frame entiere
                    # cv2.imwrite(folder + "/" + folder + str(i).zfill(2) + ".png", frame)

                    
                    #gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

                    # save cropped image to PNG file
                    cv2.imwrite(folder + "/" + folder + str(i).zfill(2) + ".png", roi)

                    # skip 500 frames (8s)
                    cap.set(1, cap.get(1) + 500)
                    #                cap.set(cv2.CAP_PROP_POS_MSEC, cap.get(cv2.CAP_PROP_POS_MSEC) + 5000)

                    #for z in range(1):
                    #    cap.grab()
                    
                    i += 1
                except:
                    print("erreur " + folder + " " + str(i))
                    pass

                print(folder + " " + str(i) + "/50")
            # release VideoCapture
            cap.release()
            
            break

if __name__ == '__main__':
    # download_videos_frame("https://www.youtube.com/watch?v=2TgDapll6SA", "hammond")
    # download_videos_frame("https://www.youtube.com/watch?v=c0A91_BkXLs", "ana")
    # download_videos_frame("https://www.youtube.com/watch?v=QylCKJ24lZg", "mercy")
    # download_videos_frame("https://www.youtube.com/watch?v=AlX-hP9OEVk", "ashe")
    # download_videos_frame("https://www.youtube.com/watch?v=YLuK3ihMWaY", "baptiste", True)
    # download_videos_frame("https://www.youtube.com/watch?v=DIk_Ly3zAKw", "bastion", True)
    # download_videos_frame("https://www.youtube.com/watch?v=ncomzYJHqsM", "brigitte")
    # download_videos_frame("https://www.youtube.com/watch?v=sITagisQYk8", "cassidy")
    # download_videos_frame("https://www.youtube.com/watch?v=--Wwth_B570", "junkrat")
    # download_videos_frame("https://www.youtube.com/watch?v=KntTJrodZWA", "roadhog")
    # download_videos_frame("https://www.youtube.com/watch?v=mnUl5xTNrKw", "sombra")
    # download_videos_frame("https://www.youtube.com/watch?v=ited0afoWH0", "d.va")
    # download_videos_frame("https://www.youtube.com/watch?v=ngMpuiNeMJs", "doomfist")
    # download_videos_frame("https://www.youtube.com/watch?v=OkZgokTCO5A", "echo")
    # download_videos_frame("https://www.youtube.com/watch?v=GA7RapEbWQg", "widow", True)
    # download_videos_frame("https://www.youtube.com/watch?v=Df0ousvkbno", "reaper", True)
    # download_videos_frame("https://www.youtube.com/watch?v=p5dHptpbdAw", "genji")
    # download_videos_frame("https://www.youtube.com/watch?v=68F-2pkD3xI", "hanzo")
    # download_videos_frame("https://www.youtube.com/watch?v=ppNAzNA0U8k", "kiriko")
    # download_videos_frame("https://www.youtube.com/watch?v=sFSQl9akIEc", "lucio", True)
    # download_videos_frame("https://www.youtube.com/watch?v=lD1q_oJtLVM", "mei")
    # download_videos_frame("https://www.youtube.com/watch?v=TftfvUrCMP0", "moira")
    # download_videos_frame("https://www.youtube.com/watch?v=OGdmyEuUwjY", "orisa", True)
    # download_videos_frame("https://www.youtube.com/watch?v=OAB2Oi7xt6Q", "pharah")
    # download_videos_frame("https://www.youtube.com/watch?v=GpNIfkc6oOI", "ramattra", True)
    # download_videos_frame("https://www.youtube.com/watch?v=7IfLP7xPi_A", "junker queen")
    # download_videos_frame("https://www.youtube.com/watch?v=_TLy8kA6Bw8", "reinhardt")
    # download_videos_frame("https://www.youtube.com/watch?v=0krOwgXJYw0", "sigma")
    # download_videos_frame("https://www.youtube.com/watch?v=H1UsI_4Aq2M", "sojourn")
    # download_videos_frame("https://www.youtube.com/watch?v=d_e7xHHKxus", "soldier 76")
    # download_videos_frame("https://www.youtube.com/watch?v=SgNDE75Rpy8", "symettra")
    # download_videos_frame("https://www.youtube.com/watch?v=e_DNPVCMkgg", "torbjorn")
    # download_videos_frame("https://www.youtube.com/watch?v=X1eTlY1MU8A", "tracer", True)
    # download_videos_frame("https://www.youtube.com/watch?v=0MIoE4-jqjI", "winston")
    # download_videos_frame("https://www.youtube.com/watch?v=UA6KLxmRAxY", "zarya")
    # download_videos_frame("https://www.youtube.com/watch?v=7tR4JH35MYI", "zenyatta", True)
    
    pass

    # POUR AJOUTER UN NOUVEAU HERO
    # 1. Execute download_videos_frame("lien d'une vidéo 1080p60 d'une personne jouant le héro", "nom du hero")
    # 2. Vérifie les images généré dans "/nom du hero"
    # 3. Ajoute le dossier "/nom du hero" au modèle de Overwatch Gameplay Sorter

    #os.system("shutdown /s /t 1")
    
    # Crop les images
    
    # pas besoin d'utiliser ce code normalement car déjà crop 
    # folder = "models_cropped"
   
    # # Pour chaque élément dans le dossier...
    # for item_name in os.listdir(folder):
    #     # Si l'élément est un dossier...
    #     if os.path.isdir(os.path.join(folder, item_name)):
                   
    #         # Pour chaque image dans le dossier...
    #         for image_name in os.listdir(os.path.join(folder, item_name)):
    #             # Lire l'image
    #             image = cv2.imread(os.path.join(os.path.join(folder, item_name), image_name))

    #             # Rogner l'image pour ne conserver que la partie en bas à droite (50x50)
    #             x, y, w, h = 0, 12, 650, 140
    #             roi = cv2.getRectSubPix(image, (w, h), (x + w // 2, y + h // 2))

    #             # Écrire l'image rogner sur le disque
    #             cv2.imwrite(os.path.join(os.path.join(folder, item_name), image_name), roi)
                
    #             print(folder + " " + image_name)
            