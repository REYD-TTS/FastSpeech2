import yiddish
import re
import argparse

def preprocess(text, model_name):
    if model_name == "hasidic":
        text = yiddish.strip_diacritics(text)
    else:
        text = yiddish.replace_with_precombined(text)
        if "respelled" in model_name:
            text = yiddish.respell_loshn_koydesh(text)

    text = re.sub(r"[\.!,;?\-\s]+$", "", text)
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text', nargs='+')
    parser.add_argument('-o', '--orth', default='yiddish_respelled')
    args = parser.parse_args()
    print(preprocess(' '.join(args.text), args.orth))
