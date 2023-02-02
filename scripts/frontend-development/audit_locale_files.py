from glob import glob
from json import load
from os import path

EN_PATH = '../../website/public/locales/en/*.json'
ALL_PATH = '../../website/public/locales/**/*.json'
dirname = path.dirname(__file__)


def get_not_translated(en_json, translation_json):
    return [key for key in en_json.keys() if key in translation_json.keys() and translation_json[key] == en_json[key]]


def get_missing(en_json, translation_json):
    return [key for key in en_json.keys() if key not in translation_json]


def audit(file, en_file):
    en_json = load(open(en_file))
    translation_json = load(open(file))
    missing = get_missing(en_json, translation_json)
    not_translated = get_not_translated(en_json, translation_json)

    if len(missing):
        print("[{0}] - missing: {1} {2}".format(
            path.basename(path.dirname(file)),
            path.basename(file),
            missing
        ))

    if (len(not_translated)):
        print("[{0}] - potentially untranslated: {1} {2}".format(
            path.basename(path.dirname(file)),
            path.basename(file),
            not_translated
        ))


def main():
    for en_file in glob(path.join(dirname, EN_PATH)):
        for file in glob(path.join(dirname, ALL_PATH)):
            if path.basename(en_file) == path.basename(file) and file != en_file:
                audit(file, en_file)


if __name__ == "__main__":
    main()
