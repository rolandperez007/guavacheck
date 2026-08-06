from app.world.graph import WorldGraphRuntime



def test_world_graph_runtime():


    entities = [

        {
            "name": "West Africa",
            "level": "region",
        },

        {
            "name": "Nigeria",
            "level": "country",
            "parent": "West Africa",
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


    graph = WorldGraphRuntime()


    graph.load(
        entities
    )


    children = graph.find_children(
        "Nigeria"
    )


    assert (
        "Lagos"
        in
        children
    )


    parent = graph.find_parent(
        "Victoria Island"
    )


    assert (
        parent
        ==
        "Lagos"
    )


    exported = graph.export()


    assert len(
        exported
    ) == 3