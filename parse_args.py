#!/usr/env/bin python3
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--num_img', type=int, default=500, help="Number of images to generate")

    parser.add_argument('--length', type=int, default=10,
                        help='Chars(chn) or words(eng) in a image. For eng corpus mode, default length is 3')

    parser.add_argument('--clip_max_chars', action='store_true', default=False,
                        help='For training a CRNN model, max number of chars in an image'
                             'should less then the width of last CNN layer.')

    parser.add_argument('--img_height', type=int, default=32)
    parser.add_argument('--img_width', type=int, default=800,
                        help="If 0, output images will have different width")

    ##配置說明，例如font的size範圍，是否加noise、line等
    parser.add_argument('--config_file', type=str, default='./configs/default.yaml',
                        help='Set the parameters when rendering images')

    ##txt的文件路徑，該txt中存儲需要使用的font的ttc、ttf文件的路徑
    parser.add_argument('--fonts_list', type=str, default='./data/fonts_list/chn.txt',
                        help='Fonts file path to use')

    ##背景圖片路徑
    parser.add_argument('--bg_dir', type=str, default='./data/bg',
                        help="Some text images(according to your config in yaml file) will"
                             "use pictures in this folder as background")

    ##字典txt的路徑
    parser.add_argument('--chars_file', type=str, default='./data/chars/new_complex_simplified.txt',
                        help='Chars allowed to be appear in generated images.')

    ##chn和eng時，依然會過濾出char file文件中字符外的字符
    parser.add_argument('--corpus_mode', type=str, default='eng', choices=['random', 'chn', 'eng', 'list'],
                        help='Different corpus type have different load/get_sample method'
                             'random: random pick chars from chars file'
                             'chn: pick continuous chars from corpus'
                             'eng: pick continuous words from corpus, space is included in label')

    ##語料txt文件的路徑
    parser.add_argument('--corpus_dir', type=str, default="./data/english_corpus",
                        help='When corpus_mode is chn or eng, text on image will randomly selected from corpus.'
                             'Recursively find all txt file in corpus_dir')


    ##生成圖片放在output_dir/{tag}路徑下
    parser.add_argument('--output_dir', type=str, default='/data/nfs/yangsuhui/data/complex_font_generater_six', help='Images save dir')

    parser.add_argument('--tag', type=str, default='images', help='output images are saved under output_dir/{tag} dir')


    ##debug為true，程序運行時print一些中間運行的結果信息
    parser.add_argument('--debug', action='store_true', default=False, help="output uncroped image")

    parser.add_argument('--viz', action='store_true', default=False)


    parser.add_argument('--strict', action='store_true', default=False,
                        help="check font supported chars when generating images")

    parser.add_argument('--gpu', action='store_true', default=False, help="use CUDA to generate image")

    parser.add_argument('--num_processes', type=int, default=None,
                        help="Number of processes to generate image. If None, use all cpu cores")


    flags, _ = parser.parse_known_args()
    #flags.save_dir = os.path.join(flags.output_dir, flags.tag)
    flags.save_dir = os.path.join(flags.output_dir, 'recognition', flags.tag)
    flags.save_dir_det = os.path.join(flags.output_dir, 'detection', flags.tag)


    if os.path.exists(flags.bg_dir):
        num_bg = len(os.listdir(flags.bg_dir))
        flags.num_bg = num_bg

    if not os.path.exists(flags.save_dir):
        os.makedirs(flags.save_dir)

    if not os.path.exists(flags.save_dir_det):
        os.makedirs(flags.save_dir_det)

    if flags.num_processes == 1:
        parser.error("num_processes min value is 2")

    return flags


if __name__ == '__main__':
    args = parse_args()
    print(args.corpus_dir)
