from waapix import WaapiClientX



with WaapiClientX() as client:
    print(client.get_selection())

