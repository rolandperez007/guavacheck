from app.world import WorldKernel
from app.world import WorldBootManager


def test_world_boot():

    kernel = WorldKernel()

    boot = WorldBootManager(
        kernel=kernel
    )


    result = boot.boot()


    assert result["world_kernel"]["status"] == "running"