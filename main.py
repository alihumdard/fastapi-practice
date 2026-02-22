from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import httpx


app = FastAPI()

# 👇 یہ Laravel FormRequest جیسا ہے
class User(BaseModel):
    name: str
    email: str
    age: int


@app.get("/", response_class=HTMLResponse)
def form_page():
    return """
    <html>
        <body>
            <h2>QR Code Generator</h2>
            <form action="/generate-qr" method="post">
                <input type="text" name="data" placeholder="Enter text" required>
                <button type="submit">Generate QR</button>
            </form>
        </body>
    </html>
    """


@app.post("/generate-qr", response_class=HTMLResponse)
async def generate_qr(data: str = Form(...)):

    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={data}"

    return f"""
    <html>
        <body>
            <h2>Your QR Code</h2>
            <img src="{qr_url}" alt="QR Code">
            <br><br>
            <a href="/">Go Back</a>
        </body>
    </html>
    """

# 👇 POST endpoint
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }

@app.post("/submit-form")
def submit_form(
    name: str = Form(...),
    email: str = Form(...),
):
    return {
        "name": name,
        "email": email
    }