from app.world.templates import (
    TemplateEngine,
    InheritanceResolver,
    TemplateRegistry,
)



def test_template_inheritance():


    world_template = {

        "currency": "GLOBAL",

        "construction": "standard",

        "verification": True,

    }


    nigeria_override = {

        "currency": "NGN",

        "construction": "local",

    }


    engine = TemplateEngine()


    merged = engine.merge(
        world_template,
        nigeria_override,
    )


    assert (
        merged["currency"]
        ==
        "NGN"
    )


    assert (
        merged["verification"]
        is True
    )


    registry = TemplateRegistry()


    registry.register(
        "world",
        world_template,
    )


    assert (
        registry.get("world")
        ==
        world_template
    )



def test_inheritance_resolver():


    resolver = InheritanceResolver()


    result = resolver.inherit(

        {
            "security": "global",
            "finance": "base",
        },

        {
            "finance": "Nigeria",
        },

    )


    assert (
        result["security"]
        ==
        "global"
    )


    assert (
        result["finance"]
        ==
        "Nigeria"
    )