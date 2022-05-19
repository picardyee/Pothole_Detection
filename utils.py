from glob import glob

train_img_list = glob('C:/Users/User/PycharmProjects/Detection/Pothole/train/images/*.jpg')
test_img_list = glob('C:/Users/User/PycharmProjects/Detection/Pothole/test/images/*.jpg')
valid_img_list = glob('C:/Users/User/PycharmProjects/Detection/Pothole/valid/images/*.jpg')
print(len(train_img_list), len(test_img_list), len(valid_img_list))


import yaml

with open('C:/Users/User/PycharmProjects/Detection/Pothole/train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')
with open('C:/Users/User/PycharmProjects/Detection/Pothole/test.txt', 'w') as f:
    f.write('\n'.join(test_img_list) + '\n')
with open('C:/Users/User/PycharmProjects/Detection/Pothole/valid.txt', 'w') as f:
    f.write('\n'.join(valid_img_list) + '\n')
