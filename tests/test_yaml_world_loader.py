from app.world.data import YAMLWorldLoader



def test_yaml_world_loader():


    loader = YAMLWorldLoader()


    nigeria = loader.load_file(
        "docs/world/countries/nigeria.yaml"
    )


    assert nigeria["name"] == "Nigeria"


    assert (
        nigeria["currency"]["code"]
        ==
        "NGN"
    )


    victoria = loader.load_file(
        "docs/world/districts/victoria_island.yaml"
    )


    assert victoria["name"] == "Victoria Island"


    assert (
        victoria["type"]
        ==
        "commercial"
    )