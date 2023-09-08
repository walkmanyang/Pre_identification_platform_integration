import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 定义图像1和图像2的路径
image_path1 = 'path/to/your/image1.jpg'
image_path2 = 'path/to/your/image2.jpg'

# 加载图像1和图像2
image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

# 定义SIFT特征提取器
sift = cv2.xfeatures2d.SIFT_create()

# 提取图像1和图像2的SIFT特征向量
kp1, des1 = sift.detectAndCompute(image1, None)
kp2, des2 = sift.detectAndCompute(image2, None)

# 计算图像1和图像2的余弦距离
if des1 is not None and des2 is not None:
    distance = cosine_similarity(des1, des2)
    mean_distance = np.mean(distance)
else:
    mean_distance = -1

print(mean_distance)
