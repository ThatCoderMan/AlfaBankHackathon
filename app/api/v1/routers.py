from fastapi import APIRouter

api_v1_router = APIRouter()


@api_v1_router.get('/main/')
async def get_homepage():
    return {None}


@api_v1_router.get('/my_employees/')
def get_employees():
    return {None}


@api_v1_router.get('/pdp/{pdp_id}')
async def get_pdp():
    return {None}


@api_v1_router.patch('/pdp/{pdp_id}')
async def change_pdp():
    return {None}


@api_v1_router.get('pdp/{pdp_id}/{task_id}/')
async def get_task():
    return {None}


@api_v1_router.post('pdp/{pdp_id}/{task_id}/')
async def create_task():
    return {None}


@api_v1_router.patch('pdp/{pdp_id}/{task_id}/')
async def change_task():
    return {None}


@api_v1_router.post('/creating_request/')
async def create_request():
    return {None}
