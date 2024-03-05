from httpx import AsyncClient


async def test_users_get(ac: AsyncClient):
    response = await ac.get("/users/", params={})
    print(
        "res",
        response.text,
    )
    assert response.status_code == 200


async def test_user_add(ac: AsyncClient):
    response = await ac.post(
        "/users/",
        json={
            "username": "string",
            "steam_token": "string",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    assert response.status_code == 201


# async def test_user_update(ac: AsyncClient):
#     response = await ac.patch(
#         "/users/1/",
#         json={
#             "username": "string",
#             "steam_token": "string",
#         },
#         headers={
#             "accept": "application/json",
#             "Content-Type": "application/json",
#         },
#     )
#     assert response.status_code == 200


# async def test_user_delete(ac: AsyncClient):
#     response = await ac.delete(
#         "/users/1/",
#         headers={
#             "accept": "application/json",
#             "Content-Type": "application/json",
#         },
#     )
#     assert response.status_code == 200
