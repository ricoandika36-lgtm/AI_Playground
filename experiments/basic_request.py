def run_basic_request(client):
    print("\n=== EXPERIMENT 01: BASIC REQUEST ===")

    response = client.responses.create(
        model="gpt-6-luna",
        input="Jelaskan apa itu Artificial Intellegence dalam 3 kalimta sederhana."
    )

    print("\n[AI RESPONSE]")
    print(response.output_text)

    print("\n[TOKEN USAGE]")
    print(f"input tokens : {response.usage.input_tokens}")
    print(f"output tokens : {response.usage.output_tokens}")
    print(f"total tokens : {response.usage.total_tokens}")
