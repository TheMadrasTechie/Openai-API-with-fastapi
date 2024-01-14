from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import openai_work

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
@app.post("/Openai_Chatgpt")
async def receive_text(first_prompt: str, content_prompt: str, last_prompt: str, language: str):
    return openai_work.process(first_prompt,content_prompt,last_prompt,language)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
