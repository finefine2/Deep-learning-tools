import os
import json

def convert_text_to_icdar(json_dir, out_file):
    image_id = 0 
    images = [] 
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
                    pass 
                instances = []     
                for anno in data['annotations']: 
                    for poly, bbox in zip(anno["polygons"],anno["bbox"]):
                        text = poly["text"] 
                        points = poly["points"]
                        
                        #polygon_values = [x1,y1,x2,y2,x3,y3,x4,y4]
                        polygon_values=[points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1], points[3][0], points[3][1]]
                        bbox_values = [bbox["x"],bbox["y"],bbox["x"]+bbox["width"],bbox["y"]+bbox["height"]]
                        instances.append(dict(
                        bbox=bbox_values,
                        bbox_label=0,
                        polygon=polygon_values,
                        text=text,
                        ignore=False
                        ))
                images.append(dict(
                img_path=image['name'],
                height=image['height'],
                width=image['width'],
                instances=instances))
            # increment the image id after processing each json file
            image_id += 1
    icdar_format = dict(
        metainfo={
            "dataset_type": "TextDetDataset",
            "task_anme": "textdet",
            "category":[{"id": 0, "name": "text"}]
        },
        data_list = images)
    with open(out_file,'w') as f: 
        json.dump(icdar_format,f)


# set your own path to load dataset
if __name__ == '__main__':
    convert_text_to_icdar(json_dir='',
                         out_file='')
                         
    convert_text_to_icdar(json_dir='',
                         out_file='')
                         
    convert_text_to_icdar(json_dir='',
                         out_file='')
