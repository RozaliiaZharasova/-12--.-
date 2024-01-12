# Автотест по шагам
import sender_stand_request
import data


def test_order_creation_and_retrieval():
    response = sender_stand_request.create_order(data.order_body)

    track = {"t":sender_stand_request.get_order('track')}
    order_response = sender_stand_request.get_order(track)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()