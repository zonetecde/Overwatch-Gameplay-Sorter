import cv2
import os

# Charger l'image à comparer
image = cv2.imread("temp\\reinhardt\\reinhardt03.png")

# Initialiser une liste pour stocker les pourcentages de ressemblance
similarities = []

# Parcourir les dossiers de modèles
for folder in os.listdir("models_cropped"):
    folder_path = os.path.join("models_cropped", folder)
    # Parcourir les images dans chaque dossier
    for img_file in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, img_file))
        # Utiliser la fonction cv2.matchTemplate() pour calculer le pourcentage de ressemblance
        
        # entre l'image de référence et l'image actuelle
        res = cv2.matchTemplate(image, img, cv2.TM_CCOEFF_NORMED)
        
        # Utiliser cv2.minMaxLoc() pour extraire la valeur minimale du tableau d'arrays
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # Ajouter le pourcentage de ressemblance à la liste
        similarities.append((folder, min_val))


# Trouver le dossier avec la moyenne de ressemblance la plus élevée
best_folder = sorted(similarities, key=lambda x: x[1], reverse=True)[0]

# Afficher le nom du dossier
print("Le dossier avec les images les plus similaires est: {}".format(best_folder))