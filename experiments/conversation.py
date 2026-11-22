from core.client import create_client
from core.config import MODEL_NAME


def run_conversation():
    print("\n=== EXPERIMENT 03: CONVERSATION & MEMORY ===")

    client = create_client()

    print("\n[USER - 1]")
    prompt_1 = "Saya sedang membangun aplikasi bernama Resima menggunakan react, FastAPI, dan PostgreSQL."

    print(prompt_1)

    response_1 = client.responses.create(
        model=MODEL_NAME,
        input=prompt_1
    )

    print("\n[AI - 1]")
    print(response_1.output_text)

    print("\n[USER - 2]")
    prompt_2 = "Kalau begitu, apa fungsi masing-masing teknologi tersebut?"

    print(prompt_2)

    response_2 = client.responses.create(
        model=MODEL_NAME,
        previous_response_id=response_1.id,
        input=prompt_2
    )

    print("\n[AI - 2]")
    print(response_2.output_text)

    print("\n[CONVERSATION INFO]")
    print(f"First Response ID : {response_1.id}")
    print(f"Second Response ID: {response_2.id}")


if __name__ == "__main__":
    run_conversation()