import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_sandbox import NAME
from blue_sandbox.sagesemseg.dataset import upload as upload_dataset
from blue_sandbox.sagesemseg.model import SageSemSegModel
from blue_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="train_model | upload_dataset",
)
parser.add_argument(
    "--dataset_object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--model_object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--epochs",
    type=int,
    default=10,
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
)
parser.add_argument(
    "--deploy",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--delete_endpoint",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--instance_type",
    type=str,
    default="ml.p3.2xlarge",
)
args = parser.parse_args()

success = False
if args.task == "train_model":
    success = True

    model = SageSemSegModel()

    if not model.train(
        dataset_object_name=args.dataset_object_name,
        model_object_name=args.model_object_name,
        epochs=args.epochs,
        instance_type=args.instance_type,
    ):
        success = False
    elif args.deploy:
        model.deploy(
            initial_instance_count=1,
            instance_type="ml.c5.xlarge",
        )

        if args.delete_endpoint:
            model.delete_endpoint()
elif args.task == "upload_dataset":
    upload_dataset(
        dataset_object_name=args.dataset_object_name,
        object_name=args.object_name,
        count=args.count,
    )
    success = True
else:
    success = None

sys_exit(logger, NAME, args.task, success)
