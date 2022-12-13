using OpenCvSharp;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Overwatch_Gameplay_Sorter
{
    internal class HeroDetector
    {
        /// <summary>
        /// D'une vidéo donné, récupère le nom du héro joué à l'aide d'une comparaison d'un assemble de modèles.
        /// </summary>
        /// <param name="videoPath">Lien de la vidéo</param>
        /// <returns>Nom du héro joué</returns>
        internal static string PlayedHeroFromVideoClip(string videoPath)
        {
            // open the video file
            VideoCapture capture = new VideoCapture(videoPath);

            // set the capture position to the 20th frame
            // 0 = Position in frames 
            capture.Set(0, 20);

            // create a Mat object to store the image
            Mat image = new Mat();

            // read the image at the specified position
            capture.Read(image);

            // resize the image to 1080p resolution
            Cv2.Resize(image, image, new Size(1920, 1080));

            Size size = image.Size();
            int height = size.Height;
            int width = size.Width;
            OutputArray output = OutputArray.Create(image);

            // define region of interest (ROI) and crop it
            Cv2.GetRectSubPix(image, new Size(650, 140), new Point2f(width - 650 + 325, height - 200 + 70), output);


            // Initialiser une liste pour stocker les pourcentages de ressemblance
            var similarities = new List<Tuple<string, float>>();

            // Parcourir les dossiers de modèles
            foreach (string folder in Directory.GetDirectories("models_cropped"))
            {
                // Parcourir les images dans chaque dossier
                foreach (string imgFile in Directory.GetFiles(folder))
                {
                    Mat img = Cv2.ImRead(imgFile);
                    // Utiliser la fonction Cv2.MatchTemplate() pour calculer le pourcentage de ressemblance
                    // entre l'image de référence et l'image actuelle
                    Mat res = new Mat();
                    Cv2.MatchTemplate(image, img, res, TemplateMatchModes.CCoeffNormed);
                    // Utiliser Cv2.MinMaxLoc() pour extraire la valeur minimale du tableau d'arrays
                    // create variables to store the min and max values and their locations
                    double minVal, maxVal;
                    Point minLoc, maxLoc;

                    // find the min and max values and their locations in the image
                    Cv2.MinMaxLoc(res, out minVal, out maxVal, out minLoc, out maxLoc);
                    // Ajouter le pourcentage de ressemblance à la liste
                    similarities.Add(Tuple.Create(folder, (float)minVal));
                }
            }

            // Trouver le dossier avec la moyenne de ressemblance la plus élevée
            var bestFolder = similarities.OrderByDescending(x => x.Item2).First();

            // Afficher le nom du dossier
            return bestFolder.Item1;
        }
    }
}
