Google Image Downloader

This Python script allows you to easily download multiple images from Google Images using their URLs.

Usage

    Open Google Images in Chrome and search for the images you want to download.
    Right-click on the webpage and select "Inspect" to open the Chrome DevTools.
    In the DevTools console, paste the code from code.txt and hit Enter. This will generate a urls.txt file with all the image URLs.
    Download the dwnld_imgs1.py script and place it in a folder with the urls.txt file.
    Open a terminal or command prompt and navigate to the folder where the dwnld_imgs1.py script and urls.txt file are located.
    Run the following command to start downloading the images:
    
```
python dwnld_imgs1.py -u urls.txt -o output_dir
```

  Replace output_dir with the name of the folder where you want to save the downloaded images.
  Note: You may need to install the requests and tqdm Python packages before running the script. You can install them by running the following commands:
 
 ```
  pip install requests
  pip install tqdm
  ```
  
  Disclaimer
  Please note that downloading images from Google Images may violate their terms of service and/or copyright laws. Use this script at your own risk.
