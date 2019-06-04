import argparse
import os
import xml.etree.ElementTree as ET

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def parsing():
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument('-i', '--xml', default='', type=str)
    parser.add_argument('-o', '--json', default='', type=str)

    return parser

def main():
    args = parsing().parse_args()

    if args.xml == '':
        print ("pls assign the root dir for input xml file.")
        return
    
    if args.json == '':
        print ("pls assign the file name for output json file.")
        return
    
    xml_list = []
    for _, _, f in os.walk(args.xml):
        xml_list.append(f)
    xml_list = sum(xml_list, [])

    # needs info
    # "annotations": [
    #     {
    #         "area": 118206.72,
    #         "attributes": {},
    #         "bbox": [
    #             269.3, # x
    #             10.3,  # y
    #             297.6, # w
    #             397.2  # h
    #         ],
    #         "category_id": 1,
    #         "id": 39,
    #         "image_id": 10,
    #         "is_occluded": true,
    #         "iscrowd": 0,
    #         "segmentation": null
    #     },
    
    # "images": [
    #     {
    #         "coco_url": null,
    #         "dataset": "globalme",
    #         "date_captured": null,
    #         "file_name": "image_000010.jpg",
    #         "flickr_url": null,
    #         "height": 450,
    #         "id": 10,
    #         "image": "./test/image_000010.jpg",
    #         "license": null,
    #         "width": 794
    #     },

    img_filename = []
    img_dir = []
    img_boxes = []
    img_area = []

    for file_name in (xml_list):
        xml_file = ET.parse(args.xml + file_name)
        xml_content = xml_file.getroot()

        img_dir.append(xml_content.find('path').text)
        img_filename.append(xml_content.find('filename').text)
        bboxes = []
        area = []
        for _obj in xml_content.findall('object'):
            bb = _obj.find('bndbox')
            
            xmin = float(bb.find('xmin').text)
            ymin = float(bb.find('ymin').text)
            xmax = float(bb.find('xmax').text)
            ymax = float(bb.find('ymax').text)

            w = xmax - xmin
            h = ymax - ymin

            bboxes.append((xmin, ymin, w, h))
            area.append((w * h))

        img_boxes.append(bboxes)
        img_area.append(area)

    json_data = {}
    json_data["annotations"] = []
    json_data["categories"] = []
    json_data["images"] = []

    json_data["categories"].append({
        "id": 0,
        "name": "bg",
        "supercategory": ""
    })
    json_data["categories"].append({
        "id": 1,
        "name": "remote_car",
        "supercategory": ""
    })

    ID = 0

    null = None
    false = False

    for i, _data in enumerate(img_area):
        for j, area in enumerate(_data):
            json_data["annotations"].append({
                "area": area,
                "attributes": {},
                "bbox": [
                    img_boxes[i][j][0],
                    img_boxes[i][j][1],
                    img_boxes[i][j][2],
                    img_boxes[i][j][3]
                ],
                "category_id": 1,
                "id": ID,
                "image_id": i,
                "is_occluded": false,
                "iscrowd": 0,
                "segmentation": null
            })

            ID += 1

        json_data["images"].append({
            "coco_url": null,
            "dataset": "globalme",
            "date_captured": null,
            "file_name": img_filename[i],
            "flickr_url": null,
            "height": 360,
            "id": i,
            "image": img_dir[i],
            "license": null,
            "width": 640
        })   
    import json
    with open(args.json, 'w') as outputfile:
        json.dump(json_data, outputfile, indent=4) 
        # indent = 4 to make python pretty pring json

if "__main__":
    main()
