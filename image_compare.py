import argparse
from PIL import Image
import numpy as np 
import os
from os import listdir
import errno
import sys
from stable_diffusion import sd_main

SUCCESS = 0
ERROR = 1
UNKNOWN_FAILURE = 2


def compare(platform, thresholds, corelation_factor, verbosity):
    
    num_threshold = len (thresholds)
    if num_threshold == 0:
        return UNKNOWN_FAILURE
        
    goldenImageDir = "./goldenImages/"
    generatedImageDir = "./generatedImages"
    
    if(platform == "MTL"):
        goldenImageDir = goldenImageDir + "MTL"
    else:
        goldenImageDir = goldenImageDir + "DG2"
    
    for imageName in os.listdir(goldenImageDir):
          if (imageName.endswith(".png")):
            
            goldenImgPath = goldenImageDir + "/" + imageName;
            generatedImgPath = generatedImageDir + "/" + imageName;
            if not os.path.isfile(generatedImgPath):
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), generatedImgPath)
                sys.exit(1)
                
            img_a_pixels = Image.open(goldenImgPath).getdata()
            img_b_pixels = Image.open(generatedImgPath).getdata()
            if(len(img_a_pixels) != len(img_b_pixels)):
                if verbosity:
                    print("FAIL : Image shapes do not match between ", goldenImgPath, " and ", generatedImgPath)
                return UNKNOWN_FAILURE
                
            img_a_array = np.array(img_a_pixels)
            img_b_array = np.array(img_b_pixels)
            #difference = (img_a_array != img_b_array).sum()
            threshold = thresholds[0]
            size = img_a_array.size
            difference_with_threshold  = 0
            difference_with_threshold = (np.abs(img_a_array - img_b_array) >= threshold).sum()
            if( float(difference_with_threshold/size) <= float(corelation_factor/threshold)):
                if verbosity:
                    print("Threshold = ", threshold, "Pass!")
                    print("Pixel mismatch percentage : ", float(difference_with_threshold/size)*100, " %")
                if num_threshold == 1:
                    return SUCCESS
            else:
                if verbosity:
                    print("Threshold = ", threshold, "Fail!")
                    print("Pixel mismatch percentage : ", float(difference_with_threshold/size)*100, " %")
                return ERROR
                  
            threshold = thresholds[1]
            difference_with_threshold = (np.abs(img_a_array - img_b_array) >= threshold).sum()
            if( float(difference_with_threshold/size) <= float(corelation_factor/threshold)):
                if verbosity:
                    print("Threshold = ", threshold, "Pass!")
                    print("Pixel mismatch percentage : ", float(difference_with_threshold/size)*100, " %")
                if num_threshold == 2:
                    return SUCCESS   
            else:
                if verbosity:
                    print("Threshold = ", threshold, "Fail!")
                    print("Pixel mismatch percentage : ", float(difference_with_threshold/size)*100, " %")
                return ERROR
                 
            threshold = thresholds[2]
            difference_with_threshold = (np.abs(img_a_array - img_b_array) >= threshold).sum()
            if( float(difference_with_threshold/size) <= float(corelation_factor/threshold)):
                if verbosity:
                    print("Threshold = ", threshold, "Pass!")
                    print("Pixel mismatch percentage : ", float(difference_with_threshold/size)*100, " %")
                return SUCCESS
            else:
                if verbosity:
                    print("Threshold = ", threshold, "Fail!")
                    print("Pixel mismatch percentage : ", float(difference_with_threshold/size)*100, " %")
                return ERROR
        
    
    return UNKNOWN_FAILURE
            
          
     

def run_comparator(platform, thresholds, corr_const, verbosity):
    #create image using stable diffusion 
    sd_main();
    
    #compare generated image with golden image
    print("Comparing generated image with golden image...")
    ret_code = compare(platform, thresholds, corr_const, verbosity)
    if ret_code == SUCCESS:
       print("PASS!")
    elif ret_code == ERROR:
       print("ERROR!")
    else:
       print("Unknown Failure!")   

    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--thresholds", default=[5.0, 10.0, 15.0], nargs="*", type=float, help="Maximum difference between two pixel. ")
    parser.add_argument("--correlation_const", default=2.0, type=float, help="When a threshold value is small, corelation constant should be higher")
    parser.add_argument("--platform", default="DG2", type=str, help="Platform: DG2 or MTL")
    parser.add_argument("--verbosity", action="store_true", help="Print error details")
    args = parser.parse_args()
    run_comparator(args.platform, args.thresholds, args.correlation_const, args.verbosity)
 
    

