### Web server

- 정적 리소스 처리
- 동적 리소스 처리

#### WSGI

web server gateway interface

#### ASGI

asyncronous server gateway interface

### FAST API 명세 접근

-`http://localhost:{port}/redoc` 으로 api 명세에 접근할 수 있다.

- `http://localhost:{port}/docs` 경로로도 api 명세에 접근할 수 있다.

redoc과 docs의 차이점은 redoc은 명세를 보여주는 것이고, docs는 명세를 보여주고
테스트도 할 수 있다는 것이다.

### GET method

#### Path parameters

> Path parameter는 웹서버에 요청하는 구체적인 리소스의 경로인 path에 포함되는
> 변수를 의미한다.

{item_id} 와 같이 중괄호로 감싸진 부분을 path parameter 라고 한다.

```python
@app.get("/items/{item_id}")
def index():
    return {"message": "Hello World"}
```

#### Predefined values

> Path Parameter로 미리 정의된 값을 전달할 수 있다.

- Enum을 사용해 Predefined values를 정의할 수 있다.

```python
class Colors(Enum):
    blue = "blue"
    red = "red"
    green = "green"

@app.get("/items/color/{color}")
def get_colors(Type Colors):
    return {"color": color}
```

#### Query parameters

> 웹서버의 리소스들을 특정 조건에 따라 정렬하거나 필터링하는데 사용한다.

- url의 구조를 바꾸지 않고 값을 전달한다.
- `/items/?skip=20&limit=5` 와 같이 `?` 뒤에 key=value 형태로 전달한다.

```python
from fastapi import FastAPI

app = FastAPI()

# path parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# query parameter
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### Operation description

#### Status code

request 의 결과에 따라 status code를 반환한다.

#### Tags

taggingd을 통해 api를 그룹화 할 수 있다. (Categorizing Operations)

- Operation 그룹화
- Multiple Categories

#### Summary

#### Response description

### Routers

- Separate operations into multiple files
- Share a prefix between operations
- Share tags

```python
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")

```

#### Refactoring

#### Adding a second router

### Parameters

#### Request body

#### Path parameters

#### Query parameters

#### Parameter metadata

#### Validators

#### Multiple values

#### Number validations

#### Complex subtypes


