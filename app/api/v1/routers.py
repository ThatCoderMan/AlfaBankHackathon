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


@api_v1_router.get('/pdp/{pdp_id}/{task_id}/')
async def get_task():
    return {None}


@api_v1_router.post('/pdp/{pdp_id}/{task_id}/')
async def create_task():
    return {None}


@api_v1_router.patch('/pdp/{pdp_id}/{task_id}/')
async def change_task():
    return {None}


@api_v1_router.get('/statuses/')
async def get_status():
    return {None}


@api_v1_router.get('types_of_tasks')
async def get_type_of_task():
    return {None}
