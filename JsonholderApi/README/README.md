
# Jsonplaceholder API README


## API Reference

#### Create new user with name and email

```http
  POST https://jsonplaceholder.typicode.com/users/
```

Request json body

{
    "name": "Nilesh",
    "email": "nilesh@gmail.com"
}

Response json          201 CREATED

{
    
    "name": "Nilesh",
    "email": "nilesh@gmail.com",
    "id": 11
}


#### Update user details

```http
  PUT https://jsonplaceholder.typicode.com/users/3
```

Request json body

{
    "name": "Nilesh R. More",
    "username": "nileshrmore",
    "email": "newnilesh@gmail.com"
}

Response json          200 OK

{
    "name": "Nilesh R. More",
    "username": "nileshrmore",
    "email": "newnilesh@gmail.com",
    "id": 3
}




#### Get userid by title

```http
  GET https://jsonplaceholder.typicode.com/posts?titile=optio molestias id quia eum
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `optio molestias id quia eum` |

response json           200 OK

[
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
]

#### Get get user details by userid

```http
  GET https://jsonplaceholder.typicode.com/users/?userId=1
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userId`      | 1 |

response json           200 OK

{
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
]

#### Get get all comments by postid

```http
  GET https://jsonplaceholder.typicode.com/posts/?postId=1/comments
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `postId`      | 1 |

response json           200 OK

[
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
]

