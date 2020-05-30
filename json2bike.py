#!/usr/bin/python3
 
import json
import glob, argparse, os, shutil


def parse_args():
    parser = argparse.ArgumentParser(description='Count pedestrains from each camera to a txt file.')
    parser.add_argument('--data', dest='data', required=True, help='path to data.json')
    parser.add_argument('--target', dest='target', help='cam_images for train', default='bikename.txt')
    parser.add_argument('--root', dest='root', required=True, help='path to njust')
    # python json2bike.py --data ./result.json --target /Users/qingzeyin/Desktop/target/ --root /Users/qingzeyin/Desktop/test/
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    target = os.path.join(args.target, 'bikename.txt')

    if os.path.exists(target):
        os.remove(target)
    # 解析json
    with open(args.data,'r') as f:
        data = json.load(f, strict=False)
        # 生成bikename.txt
        for i in range(len(data)):
            filename = data[i]['filename']
            for j in range(len(data[i]['objects'])):
                if data[i]['objects'][j]['class_id'] == 1:
                    # print(filename)
                    with open(target, 'a') as f:
                        name = filename.split('/')[-1]
                        f.write('{}'.format(name) + '\n')
    # 从njust转移bke图片
    with open(target, 'r') as fc:
        lines = fc.readlines()
        for line in lines:
            line = line[0:-1]
            images = glob.glob(os.path.join(args.root, '*jpg'))
            for image in images:
                img = image.split('/')[-1]
                if str(img) == str(line):
                    shutil.move(image, args.target + img)

