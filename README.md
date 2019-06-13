# SampleGenerater
This project it for user to collect the image data via camera and transfer the annotation file form `.xml` format which generate by [LabelImg](https://github.com/tzutalin/labelImg) into `.json` format.

### How to use
In this repository, provide two application `capture.py` and `xml2json.py` for users. 

##### `capture.py`
The `capture.py` can let user to using the webcam or ip-cam to collect to image data into ./data/img file. 

###### Usage:
```sh
-m      -> the mode of data collection, default is press C or c
-d      -> assign the device for capture image, default is ipcam
```

###### Run:
```sh
python capture.py -m $MODE -d $DEVICE
```

##### `xml2json.py`
The `xml2json.py` is for convert the 
