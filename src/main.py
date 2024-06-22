import src.Persistence.Database
from src.Services.ColetarDados import *
from src.Entities.LocalizacaoGeografica import LocalizacaoGeografica
import src.Persistence.DAO.DadosClimaticosDao

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from typing import List

app = FastAPI(
    title="DDDClima",
    description="Web Service de Dados Climaticos",
    version="1.0.0",
    contact={
        "name": "Antonio Thomaz",
        "email": "antonio_thomaz@ufms.br",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)


class LocalizacaoGeograficaModel(BaseModel):
    latitude: float
    longitude: float
class RespostaColetarDados(BaseModel):
    localizacaoGeografica: LocalizacaoGeograficaModel
    umidade: float
    pressaoAtmosferica: float
    temperatura: float
    velocidadeDoVento: float


@app.post("/api/coletarDados", response_model=RespostaColetarDados, tags=["DadosClimaticos"])
def coletarDadosApi(request: LocalizacaoGeograficaModel):

    loc = LocalizacaoGeografica(request.latitude, request.longitude)
    dados = coletarDados(loc)
    return {"localizacaoGeografica": LocalizacaoGeograficaModel(
                latitude=loc.getLatitude(),
                longitude=loc.getLongitude()
            ),
            "umidade": dados.getUmidade(),
            "pressaoAtmosferica":dados.getPressaoAtmosferica(),
            "temperatura":dados.getTemperatura(),
            "velocidadeDoVento": dados.getVelocidadeDoVento()}



@app.get("/api/dadosColetados", response_model=List[RespostaColetarDados], tags=["DadosClimaticos"])
def dadosColetadosApi():
    dadosDao = DadosClimaticosDao()
    dados = dadosDao.getDadosClimaticos()
    print(dados)
    response = []
    for i in dados:
        response.append(DadosClimaticos(
            localizacaoGeografica=LocalizacaoGeograficaModel(
                latitude=i['localizacao'].getLatitude(),
                longitude=i['localizacao'].getLongitude()
            ),
            temperatura=i['temperatura'],
            umidade=i['umidade'],
            tempo=i['tempo'],
            pressaoAtmosferica=i['pressaoAtmosferica'],
            velocidadeDoVento=i['velocidadeDoVento']
        ))

    return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
