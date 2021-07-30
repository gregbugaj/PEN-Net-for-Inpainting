
import os
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path to the dataset')
parser.add_argument('--output', type=str, help='path to the file list')
args = parser.parse_args()

ext = {'.JPG', '.JPEG', '.PNG', '.TIF', 'TIFF'}

images = []
for root, dirs, files in os.walk(args.path):
    print('loading ' + root)
    for file in files:
        if os.path.splitext(file)[1].upper() in ext:
            images.append(os.path.join(root, file))

images = sorted(images)
np.savetxt(args.output, images, fmt='%s')



def main(src_dir, output_flist):
    with open(output_flist,'w') as flist:
        for filename in os.listdir(src_dir):
            try:
                img_path = os.path.join(src_dir, filename)
                img_name = os.path.basename(img_path)
                img_path = os.path.dirname(img_path).split("/")[-1]
                img_dest = os.path.join(img_path, img_name)
                # print(img_name)
                # print(img_path)
                flist.write(img_dest)
                flist.write('\n')
                print(img_dest)
            except Exception as e:
                raise e

# # main('/home/greg/dev/pytorch-CycleGAN-and-pix2pix/datasets/city/ready/city/trainA', './flist/city/train.flist')
# main('/home/greg/dev/pytorch-CycleGAN-and-pix2pix/datasets/city/ready/city/testA', './flist/city/test.flist')