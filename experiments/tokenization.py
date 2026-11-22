import tiktoken

def run_tokenization():
    print("=== EXPERIMENT 02: TOKENIZATION ===")

    encoding = tiktoken.get_encoding("o200k_base")

    text = "Artificial Intelligence"

    tokens = encoding.encode(text)

    print("\n[INPUT TEXT]")
    print(text)

    print("\n[INPUT IDS]")
    print(tokens)

    print("\n[TOKEN DETAILS]")
    for index, token_id in enumerate(tokens):
        token_bytes = encoding.decode_single_token_bytes(token_id)
        token_text = token_bytes.decode("utf-8", errors="replace")

        print(f"{index+1}. ID:{token_id} | Text: {token_text!r}")

    print("\n[TOKEN STATISTICS]")
    print(f"Characters : {len(text)}")
    print(f"Words : {len(text.split())}")
    print(f"Tokens : {len(tokens)}")

if __name__ == "__main__":
    run_tokenization()    

