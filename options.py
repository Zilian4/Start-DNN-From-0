def parse_common_args(parser):
    parser.add_argument('--model_type', type=str, default='base_model', help='used in model_entry.py')
    parser.add_argument('--data_type', type=str, default='base_dataset', help='used in data_entry.py')
    parser.add_argument('--save_prefix', type=str, default='pref', help='some comment for model or test result dir')
    parser.add_argument('--load_model_path', type=str, default='checkpoints/base_model_pref/0.pth',
                        help='model path for pretrain or test')
    parser.add_argument('--load_not_strict', action='store_true', help='allow to load only common state dicts')
    parser.add_argument('--val_list', type=str, default='/data/dataset1/list/base/val.txt',
                        help='val list in train, test list path in test')
    parser.add_argument('--gpus', nargs='+', type=int)
    return parser

def parse_train_args(parser):
    parser = parse_common_args(parser)
    ...
    return parser

def parse_test_args(parser):
    parser = parse_common_args(parser)
    ...
    return parser