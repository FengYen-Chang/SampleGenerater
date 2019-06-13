# SampleGenerater
This project it for user to collect the image data via camera and transfer the annotation file form `.xml` format which generate by [LabelImg](https://github.com/tzutalin/labelImg) into `.json` format.

### How to use
In this repository, provide two application `capture.py` and `xml2json.py` for users. 

##### - `capture.py`
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

##### - `xml2json.py`
The `xml2json.py` is for convert the annotation file form `.xml` into `.json` format to fit the require when user want using [openvino_training_extensions](https://github.com/opencv/openvino_training_extensions) to train a SSD detector.

###### The data struct of `.json` file
The annotation file following below pattern sample:
```json
{
    "annotations": [
        {
            "area": 9196.0,
            "attributes": {},
            "bbox": [
                132.0,
                1.0,
                121.0,
                76.0
            ],
            "category_id": 1,
            "id": 0,
            "image_id": 0,
            "is_occluded": false,
            "iscrowd": 0,
            "segmentation": null
        },
        ...
    ],
    "categories": [
        {
            "id": 0,
            "name": "bg",
            "supercategory": ""
        },
        {
            "id": 1,
            "name": "remote_car",
            "supercategory": ""
        },
        ...
    ],
    "images": [
        {
            "coco_url": null,
            "dataset": "globalme",
            "date_captured": null,
            "file_name": "0019.jpg",
            "flickr_url": null,
            "height": 360,
            "id": 0,
            "image": "./img/0019.jpg",
            "license": null,
            "width": 640
        },
        ...
    ]
{  
```
The tag of `annotations` will describe the information of each object you select in LableImg, The mean of each information will show on below.
```
"area": 9196.0,             -> The area of this selected object, means width * height.
"attributes": {},         
"bbox": [                   -> The position in the image of this selected object.
    132.0,                      -> The x coordinate of top left point.
    1.0,                        -> The y coordinate of top left point.
    121.0,                      -> The width of selected object.
    76.0                        -> The width of selected object.
],
"category_id": 1,           -> The ID of category of this selected object which following the tag of categories
"id": 0,                    -> The ID of this selected object (all object have different ID)
"image_id": 0,              -> The ID of image which have this selected object
"is_occluded": false,       -> The selected object was occluded or not
"iscrowd": 0,
"segmentation": null
```
* `is_occluded` need user to add it manually since it doesn't provide by **LabelImg**．

The tag of `category` will describe the ID of each category.
```
"id": 0,                    -> The ID of category, it will be used on tag of annotations
"name": "bg",               -> The name of category
"supercategory": ""
```

The tag of `images` will describe the information of each training/ testing image.
```
"coco_url": null,         
"dataset": "globalme",
"date_captured": null,
"file_name": "0019.jpg",    -> The filename of this image
"flickr_url": null,
"height": 360,              -> The height of this image
"id": 0,                    -> The id of this image, it will be used on tag of annotations
"image": "./img/0019.jpg",  -> The direction of this image
"license": null,
"width": 640                -> The width of this image
```






