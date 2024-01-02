## Installation

 - Clone "stable_diffusion_image_comparator"
 - cd to "stable_diffusion_image_comparator" directory
 - Open Anaconda prompt ( Recommended)
 
Run following command to create conda environment
 
```
conda env create -f environment.yaml
conda activate sd-dml
```
For python environment, open command prompt, and cd to "stable_diffusion_image_comparator" directory. Run following command:
```
pip install -r requirements.txt
```
## Run Test
 - Unzip " models" directory and put it inside "stable_diffusion_image_comparator"
 - From conda or command prompt, cd path to "stable_diffusion_image_comparator" directory  
 
 ```
 python image_compare.py
 ```
 
 - You can set different threshold values as per requirement. For an example:
 ```
 python image_compare.py --thresholds 5.0 10.0 15.0
 ```
 - You need adjust "--correlation_const" flag based on threshold values. When threshold values are small, corelation constant value should be higher. For an example,
 
  ```
 python image_compare.py --thresholds 5.0 10.0 15.0 --correlation_const 2.0
 ```
 
 - Platform can be either "DG2 or MTL". For MTL platform, use  "--platform MTL" flag as a command argument 
 - Golden images are kept inside "goldenImages" directory.  
 - After running the app, a new image will be created inside the "generatedImages" directory. Then, compare the generated image with golden image pixel by pixel. 
 