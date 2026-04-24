import fastapi
import socket
import fastapi.responses
import uvicorn
app = fastapi.FastAPI()

@app.get("/")
def show_welcome():
    return fastapi.responses.FileResponse("HTML_pages/welcome.html")
@app.get("/ding")
def returnsound(r:int=123):
    return fastapi.responses.FileResponse("sounds/ding.wav", media_type="audio/wav")
@app.get("/favicon.ico")
def ico():
    return fastapi.responses.FileResponse("HTML_pages/homechat.ico", media_type="image/x-icon")
@app.get("/chathistory")
def get_chat_history():
    with open("the_chat/chat.txt", encoding="UTF-8") as f:
        history = f.read()
        f.close()
    return history
@app.get("/writemsg")
def write_message(Blame:str, abracadabra: str):
    with open("the_chat/chat.txt", "a", encoding="UTF-8") as f:
        f.write(f"{Blame}: {abracadabra}\n")
        f.close()
    return fastapi.responses.RedirectResponse("/", status_code=302)
@app.get("/smiles")
def get_smiles():
    return fastapi.responses.FileResponse("HTML_pages/smiles.html")
@app.get("/addasmile")
def addasmile(smilename: str, smilepic: str):
    from makeasmile import makeasmile
    makeasmile(":" + smilename, smilepic)
    return fastapi.responses.RedirectResponse("/", status_code=302)
uvicorn.run(app=app, host=f"{socket.gethostbyname(socket.gethostname())}", port=5000)