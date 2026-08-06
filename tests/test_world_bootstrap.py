from app.world.runtime import (
    WorldRuntime,
    WorldBootstrap,
)

from app.world.registry import WorldGraphRegistry



class MockKernel:


    def __init__(self):

        self.status = "ready"



def test_world_bootstrap():


    kernel = MockKernel()


    runtime = WorldRuntime(

        kernel=kernel,

        registry=None,

    )


    registry = WorldGraphRegistry()



    bootstrap = WorldBootstrap(

        runtime,

        registry,

    )


    result = bootstrap.boot()



    assert (
        result["status"]
        ==
        "online"
    )


    assert (
        result["world"]["countries"]
        >=
        1
    )


    assert (
        result["world"]["districts"]
        >=
        1
    )


    assert (
        runtime.status
        ==
        "running"
    )