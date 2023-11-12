from difflib import SequenceMatcher

def normalizeString(s):
    tmp = s.replace("”", "\"")
    tmp = tmp.replace("“", "\"")
    tmp = tmp.replace("Déja", "Déjà")
    tmp = tmp.replace("\\.", "...")
    tmp = tmp.replace(".\\", "...")
    tmp = tmp.replace(",..", "...")
    tmp = tmp.replace(".,.", "...")
    tmp = tmp.replace("..,", "...")
    tmp = tmp.replace("\n\n", "\n")
    return tmp


def similar(s1, s2):
    return SequenceMatcher(None, s1, s2).ratio()
