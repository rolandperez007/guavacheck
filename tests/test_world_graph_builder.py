from app.world.graph import WorldGraphBuilder



def test_world_graph_builder():


    builder = WorldGraphBuilder()


    relationships = builder.build_country_tree()


    assert len(
        relationships
    ) == 3



    exported = builder.export()


    assert (
        exported[0]["source"]
        ==
        "West Africa"
    )


    assert (
        exported[0]["relation"]
        ==
        "INCLUDES"
    )


    assert (
        exported[0]["target"]
        ==
        "Nigeria"
    )


    assert (
        exported[2]["source"]
        ==
        "Lagos"
    )


    assert (
        exported[2]["target"]
        ==
        "Victoria Island"
    )