# image_decryption_gan
Pix2Pix Gan &amp; CycleGan used to generate images from Encrypted Images for decryption , Face recognition is then used to asses the result
# Introduction
Decryption of images encrypted for facial recognition systems, AI GANS are used for this purpose to generate images in decrypted domain.

# Datasets
Three datasets are used consisting of faces of celebrity images
- Normal dataset 
#### Sample
![normalData](https://github.com/hazem-kamel/image_decryption_gan/blob/main/dataset.png)
- L Dataset (Semi encrypted)
#### Sample
![LData](https://github.com/hazem-kamel/image_decryption_gan/blob/main/dataset_r.png)
- R dataset (Highly encrypted)
#### Sample
![RData](https://github.com/hazem-kamel/image_decryption_gan/blob/main/dataset_l.png)
# Models
Two models were created , trained and tested 
##  Pix2Pix GAN Model 
- Semi Encrypted Dataset
#### Sample
![LFinal](https://github.com/hazem-kamel/image_decryption_gan/blob/main/l_f.png)
- Highly Encrypted Dataset
#### Sample
![RFinal](https://github.com/hazem-kamel/image_decryption_gan/blob/main/r_f.png)
 ## CycleGAN Model
- Semi Encrypted Dataset
#### Sample
![RResult](https://github.com/hazem-kamel/image_decryption_gan/blob/main/r_results.png)
- Highly Encrypted Dataset
#### Sample
![LResult](https://github.com/hazem-kamel/image_decryption_gan/blob/main/l_results.png)
# Face Recogonition
Face recognition system was created with the help of Deepface for evaulating the results of the model by firstly testing the face recognition system with the datasets without decryption then testing the results of the first model and finally with the second model , results of similarities are plotted and compared 

# Final Results of the four models
- Datasets before and after using the models are fed into a Face Recognition system to get results of distances and see how the GAN models improved the faceial recognition recognising persons from images which were intially decrypted 
## Normal Results
![normalResult](https://github.com/hazem-kamel/image_decryption_gan/blob/main/normal.png)
## Pix2Pix Results
![pix2pixResult](https://github.com/hazem-kamel/image_decryption_gan/blob/main/Pix.png)
## CycleGan Results
![cycleResult](https://github.com/hazem-kamel/image_decryption_gan/blob/main/cycle.png)



