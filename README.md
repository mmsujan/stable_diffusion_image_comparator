## Installation

 - Clone "stable_diffusion_image_comparator"
 - cd to "stable_diffusion_image_comparator" directory
 - Open Anaconda prompt 
 
Run following command to create conda environment ( Recommended)
 
```
conda env create -f environment.yaml
conda activate sd-dml
```
For python environment, open command prompt, and cd to "stable_diffusion_image_comparator" directory. Run following command:
```
pip install -r requirements.txt
```
## Run Test
 - Unzip " models" directory and put it inside "sd_image_comparator"
 - cd path to "sd_image_comparator" directory  
 
 ```
 python image_compare.py --platform DG2 
 ```
 
 - You can set different threshold values as per requirement
 - Platform can be either "DG2 or MTL"
 - Golden images are kept inside "goldenImages" directory.  
 - After running the app, a new image will be created inside the "generatedImages" directory. Then, compare the generated image with golden image pixel by pixel. 
 