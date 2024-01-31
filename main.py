from waapix import WaapiClientX, TransportObject

with WaapiClientX() as client:
    # client.transport_create(TransportObject('{CE7B657B-F319-4C41-8CD7-82FBEA81EF7A}'))
    result = client.transport_get_list()
    for i in result:
        print(client.transport_get_state(i.id))
