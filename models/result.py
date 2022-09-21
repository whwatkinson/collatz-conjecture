from pydantic import BaseModel


class Result(BaseModel):

    seed: int
    count: int
    value: int

    def __repr__(self) -> str:
        return f"SEED: {self.seed} VALUE: {self.value}"
