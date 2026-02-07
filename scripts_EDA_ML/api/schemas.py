from pydantic import BaseModel
from typing import Optional


class PredictRequest(BaseModel):
    Idade: Optional[float] = None
    Tempo_de_Casa: Optional[float] = None
    Defasagem: Optional[float] = None
    IDA: Optional[float] = None
    IEG: Optional[float] = None
    IPS: Optional[float] = None
    IPP: Optional[float] = None
    IAA: Optional[float] = None
    Gênero: Optional[str] = None
    Instituicao_ensino: Optional[str] = None


class PredictResponse(BaseModel):
    atingiu_pv: int
    proba: Optional[float] = None
    model_version: str = "v1"
