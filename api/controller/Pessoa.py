from api.controller.generic import create_crud_router, Hooks
from lib.model.models import Pessoa
from lib.model.dto import PessoaCreate, PessoaUpdate, PessoaRead

router = create_crud_router(
    model=Pessoa,
    create_schema=PessoaCreate,
    update_schema=PessoaUpdate,
    read_schema=PessoaRead,
    prefix="/Pessoa",
    tags=["Pessoa"],
)
