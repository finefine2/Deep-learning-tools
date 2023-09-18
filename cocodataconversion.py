# coco dataformat으로 json file 생성하는 코드입니다. 
# 여러개의 annotation 파일을 하나의 .json 파일로 
# 이 경우에는 detection task 이기 때문에 bbox 를 넣는 것 
'''
coco dataset 은 아래의 형식을 따라야 한다 

'images': [
{
'file_name': 'images_1.jpg',
'height': 427, 
'width': 640, 
'id': 1268 
},
...
],

'annotations': [
{


}
]

'categories': [ 
{'id':0, 'name':'text'},
]

'''

import json 
import os 

# 아래의 directory 를 본인 상황에 알맞게 바꾸면 됨 
train_dir = '/traindataset_root'
val_dir = '/valdataset_root'
test_dir = '/testdataset_root' 

json_dir = val_dir

coco_format = {
    'images':[],
    'annotations':[],
    'categories': [{'id':1, 'name':'object'}]
}
anno_id = 0 
image_id =0 
# for every json files 
for filename in os.listdir(json_dir): 
    if filename.endswith('.json'): 
        with open(os.path.join(json_dir,filename),'r') as f: 
            data = json.load(f) 
        
        for image in data['images']: 
            coco_format['images'].append({
                'file_name':image['name'], 
                'height': image['height'],
                'width': image['width'], 
                'id': image_id 
            })
        # annotations 
        for anno in data['annotations']: 
            for poly, bbox in zip(anno["polygons"],anno["bbox"]): 
                text = poly["text"]
                idx = poly["id"]
                bbox_values = [bbox["x"],bbox["y"], 
                               bbox["width"],bbox["height"]]
                
                area = bbox_values[2] * bbox_values[3] 
                coco_format['annotations'].append({
                    'text': text,
                    'idx': idx,
                    'area': area, 
                    'iscrowd': 0,
                    'id': image_id,
                    'bbox': bbox_values,
                    'category_id': 1, 
                    'anno_id': anno_id
                })

                anno_id += 1 
        image_id += 1 


with open('val.json','w') as f: 
    json.dump(coco_format,f) 
