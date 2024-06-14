from dotenv import load_dotenv
import os


def setup_openai_key():
    load_dotenv()
    os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
