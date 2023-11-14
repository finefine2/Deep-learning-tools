from PIL import Image, ImageOps
import os 

from tqdm import tqdm 

def convert_exif(img_dir, save_dir):
    # 해당경로가 없다면 만들 것 
    os.makedirs(save_dir,exist_ok=True) 
    for idx, img_name in enumerate(tqdm(os.listdir(img_dir))): 
        # 이미지들을 전부 읽어오자 
        img_path = os.path.join(img_dir,img_name)

        try: 
            # 이미지를 열고 EXIF 데이터에 따라 필요한 회전이나 반전 적용 
            with Image.open(img_path) as img: 
                transposed_img = ImageOps.exif_transpose(img) 

                # 원본 이미지와 변환된 이미지가 동일하면 EXIF 태그가 없다고 판단 후 출력 
                if img == transposed_img: 
                    print(f'No EXIF: {img_dir}')
                
                # 변환된 이미지를 새로운 경로에 저장한다 
                save_path = os.path.join(save_dir, img_name) 
                transposed_img.save(save_path) 
        except Exception as e: 
            print(f'Error processing {img_path}: {e}')
# set your own path to load dataset
if __name__ == '__main__':
    convert_exif(img_dir='',
                         save_dir='')
