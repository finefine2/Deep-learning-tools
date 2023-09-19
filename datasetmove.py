import os,shutil,random
# 이미지파일과 라벨파일이 각기 다른 경로에 있을 때 랜덤하게 데이터를 추출해서 새 경로에 옮기는 코드
# 이미지파일은 .jpg
# 레이블은 .json

# 기존 데이터를 불러올 경로 
train_dir = '/train'
val_dir = '/val'

train_label_dir = '/labels/train'
val_label_dir = '/labels/val'

# 새롭게 저장할 경로  
new_train_dir = '/samples/train'
new_val_dir = '/samples/val'

new_train_label_dir = '/samples/labels/train'
new_val_label_dir = '/samples/labels/val'

# 데이터셋 종류마다 매아래 경로들을 바꿔주면 됨 
image_dir = val_dir
label_dir = val_label_dir

save_image_dir = new_val_dir
save_label_dir = new_val_label_dir

# 경로 내의 모든 파일 리스트 불러오기 (확장자 제외) 
image_files_no_ext = [os.path.splitext(fname)[0] for fname in os.listdir(image_dir)]

# 경로 내에서 랜덤하게 1000개 선택하기 
selected_files_no_ext = random.sample(image_files_no_ext, 1000)

for selected_file in selected_files_no_ext: 
    # 해당하는 이미지 및 라벨파일 확인하기 
    corresponding_image_file = selected_file + '.jpg'
    corresponding_label_file = selected_file + '.json'

    # 선택한 이미지 및 라벨파일을 새 경로로 복사하기 
    shutil.copy(os.path.join(image_dir,corresponding_image_file),save_image_dir)
    shutil.copy(os.path.join(label_dir,corresponding_label_file),save_label_dir)
