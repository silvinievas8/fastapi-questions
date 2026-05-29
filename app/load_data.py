import pandas as pd
import requests
import tempfile
import os
from app.database import SessionLocal, engine
from app.models import Base, Question

# URL del dataset en formato Parquet
DATASET_URL = "https://huggingface.co/datasets/fka/awesome-chatgpt-prompts/resolve/main/prompts.csv"

def download_parquet(url: str) -> str:
    print(f"Descargando dataset...")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".parquet")
    tmp.write(r.content)
    tmp.close()
    return tmp.name

def load_questions():
    Base.metadata.create_all(bind=engine)
    
    print("Descargando dataset público...")
    r = requests.get(DATASET_URL)
    r.raise_for_status()
    
    # Leemos el CSV directamente desde el texto descargado
    import io
    df = pd.read_csv(io.StringIO(r.text))

    session = SessionLocal()
    try:
        for _, row in df.iterrows():
            # Mapeamos 'act' como categoría y 'prompt' como la pregunta
            question = Question(
                question=row.get("prompt", ""),
                answer="Generado por IA",
                category=row.get("act", "General"),
                source="Awesome ChatGPT Prompts"
            )
            session.add(question)

        session.commit()
        print(f"Éxito: Se insertaron {len(df)} registros correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    load_questions()
