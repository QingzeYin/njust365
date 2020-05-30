# njust365
## Prerequisition
cuda >=10.0
python = 3.7
## split bike and person images
1. ```extractgallname.py``` extract the path and name of images from train, gallery and query dataset and saved in ```train.txt```. Commond is ```python extractgallname.py --root /path/to/dataset/```
2. copy ```train.txt``` to ```/darknet/data/```
3. under the root of **YOLOV4**, ```./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights -ext_output -dont_show -out result.json < data/train.txt``` generates a ```result.json``` file in ```/darknet```.
4. under ```/darknet```path, run ```json2bike.py``` to load a json file and generate a ```bikename.txt``` in target file. Also can move bike images from root file to target file. Commond is ```python json2bike.py --data ./result.json --target /target/path/to/save/bike-images/ --root /root/path/```
