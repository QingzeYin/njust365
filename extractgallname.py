import glob, argparse, os, shutil


def parse_args():
    parser = argparse.ArgumentParser(description='Count pedestrains from each camera to a txt file.')
    parser.add_argument('--root', dest='root', required=True, help='path to root')
    parser.add_argument('--targetimg', dest='targetimg', help='cam_images for gallery and query', default='train.txt')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    
    # for gallery and query

    images = glob.glob(os.path.join(args.root, '*.jpg'))
    targetimg = os.path.join(args.root, args.targetimg)

    if os.path.exists(targetimg):
        os.remove(targetimg)

    with open(targetimg, 'w') as f:
        # count = 0
        for im in images:
            # count = count + 1
            # name = im.split('/')[-1]
            f.write('{}'.format(im) + '\n')
        # f.write('total number is {}\n'.format(count))


    # for train
    
    # folders = glob.glob(os.path.join(args.root, '*'))
    # target = os.path.join(args.root, args.target)
    # if os.path.exists(target):
    #     os.remove(target)
    
    # for folder in folders:
    #     if not os.path.isdir(folder):
    #         continue
    #     if '\\' in folder:
    #         sep = '\\'
    #     else:
    #         sep = '/'
    #     ims = glob.glob(folder + '{}*.jpg'.format(sep))

    #     with open(target, 'w') as f:
    #         for im in ims:
    #             name = im.split(sep)[-1]
    #             newname = folder + '_' + name
    #             fullname = newname.split('/')[-1]

    #             f.write('\t{}'.format(fullname) + '\n')




















