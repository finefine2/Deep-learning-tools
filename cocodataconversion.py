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
import os
import json

def convert_text_to_coco(json_dir, out_file):
    anno_id = 0 
    image_id = 0 
    images = [] 
    annotations = []
    for filename in os.listdir(json_dir): 
        if filename.endswith('.json'): 
            with open(os.path.join(json_dir,filename),'r') as f: 
                data = json.load(f) 

            for image in data['images']: 
                if image['name'].endswith('jpeg'): 
                    image['name'] = image['name'].replace('jpeg','jpg')
                elif image['name'].endswith('JPG'): 
                    image['name'] = image['name'].replace('JPG','jpg')
                else: 
                    image['name'] = image['name']
                    
                images.append(dict(
                    id=image_id,
                    file_name=image['name'],
                    height=image['height'],
                    width=image['width']
                ))

            for anno in data['annotations']: 
                for poly, bbox in zip(anno["polygons"],anno["bbox"]):  
                    text = poly["text"]
                    idx = poly["id"]
                    
                    bbox_values = [bbox["x"], bbox["y"], bbox["width"], bbox["height"]]
                
                    area = bbox_values[2] * bbox_values[3]
                    
                    annotations.append(dict(
                        image_id=image_id,
                        id=anno_id,
                        category_id=0,
                        bbox=bbox_values,
                        area=area,
                        segmentation=[poly],
                        iscrowd=0
                    ))                               
                    anno_id += 1
            
            # increment the image id after processing each json file
            image_id += 1
    coco_format = dict(
        images=images,
        annotations=annotations,
        categories=[{'id': 0, 'name': 'text'}])
    
    with open(out_file,'w') as f: 
        json.dump(coco_format,f)


if __name__ == '__main__':
    convert_text_to_coco(json_dir='원래 읽어들일 라벨 경로지정',
                         out_file='파일명')
                         
    convert_text_to_coco(json_dir='라벨들 위치',
                         out_file='파일명')
                         
    convert_text_to_coco(json_dir='ㄼ',
                         out_file='ㅍㅇ')
