from app.world.graph import AutoGraphBuilder



def test_auto_graph_builder():


    entities = [

        {
            "name": "Nigeria",
            "level": "country",
        },

        {
            "name": "Lagos",
            "level": "state",
            "parent": "Nigeria",
        },

        {
            "name": "Victoria Island",
            "level": "district",
            "parent": "Lagos",
        },

    ]


    builder = AutoGraphBuilder()


    relationships = builder.build(
        entities
    )


    assert len(
        relationships
    ) == 2



    exported = builder.export()



    assert (
        exported[0]["source"]
        ==
        "Nigeria"
    )


    assert (
        exported[0]["relation"]
        ==
        "CONTAINS"
    )


    assert (
        exported[0]["target"]
        ==
        "Lagos"
    )


    assert (
        exported[1]["source"]
        ==
        "Lagos"
    )


    assert (
        exported[1]["target"]
        ==
        "Victoria Island"
    )