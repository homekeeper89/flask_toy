def test_post_user_should_success(flask_client):
    res = flask_client.post("/api/v1/user")
    assert res.status_code == 300
