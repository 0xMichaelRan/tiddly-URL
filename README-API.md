Here is the raw Markdown file content:

### API Instruction

Two interfaces: 

1. [Generate a Short-Link](#generate-short-link-interface)
1. [Resolve a Short-Link](#restore-short-link-interface).

Note the following:

- Before using the API, obtain API key in the UI, which is valid for 1 day (by default).

- Add the API key to the request header. Please refer to examples below.

## Generate Short Link Interface

##### Request

```python
URL: http://129.204.185.247/api/shorten/
Request Method: POST
Request Parameter Format: JSON
```

### Request Parameter Description

| Parameter Name | Type   | Required |                  Description |
| -------------- | ------ | -------- | ---------------------------: |
| long_url       | string | Yes      | The long URL to be shortened |

### Request POST Data Example

```JSON
{
"long_url": "https://www.baidu.com"
}
```

### Request Example

```python
http http://129.204.185.247/api/shorten/ Authorization:" Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU2NjA0NjgsIm5iZiI6MTU4NTY2MDQ2OCwianRpIjoiYmE4YTJjMDMtNjBmOS00NzIxLWFjZmMtZmM2MWU5ZTRiYzI1IiwiZXhwIjoxNTg1NjYxMzY4LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.21oYWLZ9GgueJeCIzc9yUYgGjMCBgx7KKatpfIK-heo" long_url="https://www.baidu.com"
```

### Return Parameter Description

| Name | Type     | Description   |
| ---- | -------- | ------------- |
| code | interger | Return code   |
| msg  | string   | Error message |
| data | object   | Data          |

### Data data

| Name    | Type   | Description                  |
| ------- | ------ | ---------------------------- |
| sid     | string | sid                          |
| name    | string | Group name                   |
| n_links | string | Number of links in the group |

### Return Result Example

```json
{
  "code": 0,
  "data": {
    "location": "localhost/d",
    "long": "https://www.baidu.com",
    "short": "d"
  },
  "msg": "Request successful"
}
```

### Restore Short Link Interface

##### Request

```python
URL: http://129.204.185.247/api/lengthen/
Request Method: POST
Request Parameter Format: JSON
```

### Request Parameter Description

| Parameter Name | Type   | Required |                  Description |
| -------------- | ------ | -------- | ---------------------------: |
| long_url       | string | Yes      | The short URL to be restored |

### Request POST Data Example

```JSON
{
"long_url": "129.204.185.247/5"
}
```

### Request Example

```python
http http://129.204.185.247/api/lengthen/ Authorization:" Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU2NjA0NjgsIm5iZiI6MTU4NTY2MDQ2OCwianRpIjoiYmE4YTJjMDMtNjBmOS00NzIxLWFjZmMtZmM2MWU5ZTRiYzI1IiwiZXhwIjoxNTg1NjYxMzY4LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.21oYWLZ9GgueJeCIzc9yUYgGjMCBgx7KKatpfIK-heo" long_url="https://www.baidu.com"
```

### Return Parameter Description

| Name | Type     | Description   |
| ---- | -------- | ------------- |
| code | interger | Return code   |
| msg  | string   | Error message |

### Return Result Example

```json
{
  "long": "http://www.zhihu.com",
  "msg": "Request successful"
}
```
