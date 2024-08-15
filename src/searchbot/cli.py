import sys
from rag import search

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 cli.py <query> [--bot=<bot_name>] [--lang=<language>] [--verbose]")
        sys.exit(1)

    query = sys.argv[1]
    bot_name = "baidu"  # default bot
    lang = "chinese"  # default language
    verbose = False  # default verbosity

    for arg in sys.argv[2:]:
        if arg.startswith("--bot="):
            bot_name = arg.split("=")[1]
        elif arg.startswith("--lang="):
            lang = arg.split("=")[1]
        elif arg == "--verbose":
            verbose = True

    answer = search(query, bot_name=bot_name, lang=lang, verbose=verbose)
    print(answer)
