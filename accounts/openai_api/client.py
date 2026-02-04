from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_car_ai_bio(model, brand, year):
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
