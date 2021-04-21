from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from torch import nn, load, tensor, cuda


class LolProNetwork(nn.Module):
    def __init__(self):
        super(LolProNetwork, self).__init__()
        self.network_stack = nn.Sequential(
            nn.Linear(19, 5),
            nn.CELU(),
            nn.Linear(5, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network_stack(x)


device = 'cuda' if cuda.is_available() else 'cpu'

model = LolProNetwork().to(device).double()
model.load_state_dict(load('./model/lol_predicter_v1'))
model.eval()

app = FastAPI()


@app.get("/api/predict")
def predict(games: int, kda: float, avgk: float, avgd: float, avga: float, csm: float, dpm: float, kp: float, dmgp: float, avgwpm: float, avgwcpm: float, avgvwpm: float, gdiff: int, csdiff: int, xpdiff: int, fb: float, fbv: float, solok: int):
    t1 = tensor([games, kda, avgk, avgd, avga, csm, dpm, kp, dmgp, 400, avgwpm, avgwcpm,
                avgvwpm, gdiff, csdiff, xpdiff, fb, fbv, solok], device=device).double().unsqueeze(0)
    res = model(t1).item()
    print(res)
    return {"win rate": res}


app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")
