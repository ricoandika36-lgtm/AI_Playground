import json

from core.client import create_client
from core.config import MODEL_NAME


# SIMULASI INVENTORY
inventory = {
    "Dulux Putih 5 Liter": {
        "stock": 8,
        "unit": "kaleng",
        "target_stock": 20
    },
    "Catylac Putih 5 Liter": {
        "stock": 15,
        "unit": "kaleng",
        "target_stock": 20
    }
}


# TOOL 1: CEK STOK
def get_stock(product_name):
    for name, data in inventory.items():
        if product_name.lower() == name.lower():
            return {
                "product_name": name,
                "stock": data["stock"],
                "unit": data["unit"],
                "target_stock": data["target_stock"]
            }

    return {"error": "Produk tidak ditemukan."}


# TOOL 2: REKOMENDASI RESTOCK
def recommend_restock(product_name):
    for name, data in inventory.items():
        if product_name.lower() == name.lower():
            quantity = max(
                data["target_stock"] - data["stock"],
                0
            )

            return {
                "product_name": name,
                "current_stock": data["stock"],
                "target_stock": data["target_stock"],
                "recommended_quantity": quantity,
                "unit": data["unit"]
            }

    return {"error": "Produk tidak ditemukan."}


# DAFTAR TOOL UNTUK AI
tools = [
    {
        "type": "function",
        "name": "get_stock",
        "description": "Mengecek stok produk inventory.",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string"
                }
            },
            "required": ["product_name"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "recommend_restock",
        "description": "Menghitung jumlah produk yang direkomendasikan untuk direstock berdasarkan target stok.",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string"
                }
            },
            "required": ["product_name"],
            "additionalProperties": False
        },
        "strict": True
    }
]


# PEMETAAN FUNCTION
available_functions = {
    "get_stock": get_stock,
    "recommend_restock": recommend_restock
}


def run_agent():

    print("\n=== EXPERIMENT 06: AI AGENT ===")

    client = create_client()

    instructions = """
    Kamu adalah Resima AI Inventory Assistant.

    Tugasmu:
    1. Periksa stok menggunakan get_stock.
    2. Jika stok kurang dari 10, gunakan recommend_restock.
    3. Jika stok 10 atau lebih, tidak perlu rekomendasi restock.
    4. Gunakan hasil tool sebagai sumber informasi.
    5. Jangan mengarang data inventory.
    """

    prompt = """
    Cek stok Dulux Putih 5 Liter.
    Jika stoknya kurang dari 10, berikan rekomendasi restock.
    """

    print("\n[USER]")
    print(prompt)

    response = client.responses.create(
        model=MODEL_NAME,
        instructions=instructions,
        input=prompt,
        tools=tools,
        tool_choice="auto"
    )

    # AGENT LOOP
    max_iterations = 5

    for iteration in range(max_iterations):

        tool_calls = [
            item for item in response.output
            if item.type == "function_call"
        ]

        # Jika tidak ada tool call, agent selesai
        if not tool_calls:
            break

        print(f"\n[AGENT ITERATION {iteration + 1}]")

        tool_outputs = []

        for item in tool_calls:

            print(f"\n[TOOL CALL] {item.name}")

            arguments = json.loads(item.arguments)
            print(f"Arguments: {arguments}")

            function = available_functions.get(item.name)

            if function is None:
                result = {"error": "Tool tidak tersedia."}
            else:
                result = function(**arguments)

            print(f"[TOOL RESULT] {result}")

            tool_outputs.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps(
                    result,
                    ensure_ascii=False
                )
            })

        # Kirim hasil tool kembali ke AI
        response = client.responses.create(
            model=MODEL_NAME,
            instructions=instructions,
            previous_response_id=response.id,
            input=tool_outputs,
            tools=tools,
            tool_choice="auto"
        )

    else:
        print("\nBatas iterasi tercapai.")
        return

    print("\n[AGENT FINAL RESPONSE]")
    print(response.output_text)


if __name__ == "__main__":
    run_agent()