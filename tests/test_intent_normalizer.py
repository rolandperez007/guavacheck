from app.austin.runtime.intent import IntentNormalizer



def test_intent_normalizer():


    normalizer = IntentNormalizer()



    result = normalizer.detect_intent(
        "ok loasd nigeria"
    )



    assert (
        result["normalized"]
        ==
        "ok load nigeria"
    )



    assert (
        result["intent"]
        ==
        "load"
    )



    property_result = normalizer.detect_intent(
        "creat propety analysys"
    )



    assert (
        property_result["normalized"]
        ==
        "create property analysis"
    )



    assert (
        property_result["intent"]
        ==
        "create"
    )