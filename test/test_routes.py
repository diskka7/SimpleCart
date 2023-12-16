import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200


# post new cart [UAS1]
def test_post_cart(client):
    # Test POST /api/cart
    product_id = 1
    qty = 2
    data = {
        'coupon_code': 'ABC123',
        'shipping_fee': 5000.0,
        'cart_items': [
            {
                'product_id': product_id,
                'qty': qty
            }
        ]
    }

    response = client.post("/api/cart", json=data)
    assert response.status_code == 200
   
    
def test_get_cart(client):
    # Test GET /api/cart
    response = client.get("/api/cart")
    assert response.status_code == 200
    

def test_get_cart_detail(client):
    # Test GET /api/cart/{id}
    cart_id = 1
    response = client.get(f"/api/cart/{cart_id}")
    assert response.status_code == 200
    

def test_put_cart(client):
    # Test PUT /api/cart/{id}
    cart_id = 1
    data = {
        'coupon_code': 'NEWCOUPON',
        'cart_items': [
            {
                'product_id': 2,
                'qty': 3
            }
        ]
    }

    response = client.put(f"/api/cart/{cart_id}", json=data)
    assert response.status_code == 200
   

def test_delete_cart(client):
    # Test DELETE /api/cart/{id}
    cart_id = 1
    response = client.delete(f"/api/cart/{cart_id}")
    assert response.status_code == 200
   

