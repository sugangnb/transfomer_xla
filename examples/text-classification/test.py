# encoding:utf-8

from argparse import ArgumentParser

def parse_args(args=None):
    parser = ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)


    return parser.parse_args(args)


# def main(args):
#     pl.seed_everything(args.seed)
#     dm = GLUEDataModule.from_argparse_args(args)
#     dm.prepare_data()
#     dm.setup('fit')
#     model = GLUETransformer(num_labels=dm.num_labels, eval_splits=dm.eval_splits, **vars(args))
#     trainer = pl.Trainer.from_argparse_args(args)
#     return dm, model, trainer
#

if __name__ == '__main__':
    mocked_args = """
        --model_name_or_path distilbert-base-uncased
        --task_name mnli
        --max_epochs 1
        --gpus 1
        --limit_train_batches 10
        --progress_bar_refresh_rate 20
        --seed 42
        """.split()
    args = parse_args(mocked_args)
    print(args)
    # main(args)