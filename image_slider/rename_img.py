import os
from PIL import Image

# 设置图片文件夹路径
folder_path = 'test/'

# 获取文件夹中的所有png文件
files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

# 按名称排序
files.sort()

# 依次处理每个文件
for index, file_name in enumerate(files):
    # 打开图片
    img = Image.open(os.path.join(folder_path, file_name))
    
    # 压缩图片到1280x720
    img = img.resize((1280, 720), Image.LANCZOS)
    
    # 保存图片为0.png, 1.png, ...
    img.save(os.path.join(folder_path, f'{index}.png'))

print("图片处理完成")