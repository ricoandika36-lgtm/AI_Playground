import json

from core.client import create_client
from core.config import MODEL_NAME


# SIMULASI DATA INVENTORY
inventory = {
    "Dulux Putih 5 Liter": {
        "stock": 8,
        "unit": "kaleng"
    },
    "Catylac Putih 5 Liter": {
        "stock": 15,
        "unit": "kaleng"
    }
}


# PYTHON FUNCTION
def get_stock(product_name):
    for name, data in inventory.items():
        if product_name.lower() in name.lower() or name.lower() in product_name.lower():
            return {
                "product_name": name,
                "stock": data["stock"],
                "unit": data["unit"]
            }

    return {
        "error": f"Produk {product_name} tidak ditemukan."
    }


# TOOL DEFINITION
tools = [
    {
        "type": "function",
        "name": "get_stock",
        "description": "Mencari informasi stok produk berdasarkan nama produk.",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "Nama produk yang ingin dicari."
                }
            },
            "required": ["product_name"],
            "additionalProperties": False
        },
        "strict": True
    }
]


def run_tool_calling():
    print("\n=== EXPERIMENT 05: TOOL CALLING ===")

    client = create_client()

    prompt = "Berapa stok produk Catylac Putih 5 Liter?"

    print("\n[USER]")
    print(prompt)

    # STEP 1: MODEL MEMILIH TOOL
    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt,
        tools=tools,
        tool_choice="required"
    )

    # STEP 2: PROGRAM MEMERIKSA TOOL CALL
    for item in response.output:

        if item.type == "function_call":

            print("\n[TOOL CALL]")
            print(f"Function: {item.name}")
            print(f"Arguments: {item.arguments}")

            # STEP 3: PYTHON MENJALANKAN FUNCTION
            arguments = json.loads(item.arguments)

            result = get_stock(
                arguments["product_name"]
            )

            print("\n[FUNCTION RESULT]")
            print(result)

            # STEP 4: HASIL FUNCTION DIKIRIM KE AI
            final_response = client.responses.create(
                model=MODEL_NAME,
                previous_response_id=response.id,
                input=[
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": json.dumps(
                            result,
                            ensure_ascii=False
                        )
                    }
                ],
                tools=tools
            )

            # STEP 5: AI MEMBERIKAN JAWABAN
            print("\n[AI FINAL RESPONSE]")
            print(final_response.output_text)


if __name__ == "__main__":
    run_tool_calling()