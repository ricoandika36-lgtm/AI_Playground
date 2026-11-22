import logging
from core.client import create_client
from experiments.basic_request import run_basic_request

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logger = logging.getLogger(__name__)

def main():
    logger.debug("Memasuki fungsi main")
    logger.info("Aplikasi dimulai")

    try:
        logger.debug("Mencoba membuat OpenAI client")
        client = create_client()
        run_basic_request(client)
        logger.debug("Object Client berhasil dibuat")
        logger.info("OpenAI Client berhasil dibuat")
        print(type(client))

    except ValueError as e:
        logger.error(f"Konfigurasi belum siap: {e}")

    logger.info("Aplikasi selesai")

if __name__ == "__main__":
    main()   