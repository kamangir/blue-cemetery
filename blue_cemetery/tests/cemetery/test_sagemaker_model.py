import pytest

from blue_objects.objects import unique_object

from blue_sandbox.sagesemseg.model import SageSemSegModel


@pytest.mark.skip("causes cost.")
@pytest.mark.parametrize(
    "dataset_object_name",
    [
        ("pascal-voc-v1-debug-v2"),
    ],
)
def test_SageSemSegModel(dataset_object_name):
    model = SageSemSegModel()

    model_object_name = unique_object("test-SageSemSegModel-model")

    assert model.train(
        dataset_object_name=dataset_object_name,
        model_object_name=model_object_name,
        instance_type="ml.g4dn.2xlarge",
    )

    model.deploy(
        initial_instance_count=1,
        instance_type="ml.c5.xlarge",
    )

    model.delete_endpoint()
