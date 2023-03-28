import typing as t
from threatexchange.api import settings, app

@app.route("/match/photo/<signal_type>/<hash>")
def getMatches(signal_type: str, hash: str) -> t.List[t.Dict[str, t.Any]]:
    signal = settings.get_signal_type(signal_type)
    index = settings.index.load(signal)
    res = index.query(hash)
    return [a.__dict__() for a in res]
