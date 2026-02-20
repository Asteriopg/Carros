from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    client = None
else:
    client = OpenAI(api_key=api_key)

def get_car_ai_bio(model, brand, year):
    if client is None:
        return "Erro: OpenAI API Key não configurada no servidor."
        
    prompt = (
        f"Crie uma descrição de venda para o carro {brand} {model} {year} "
        f"em até 250 caracteres, destacando pontos fortes reais desse modelo."
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    
    return response.choices[0].message.content.strip()