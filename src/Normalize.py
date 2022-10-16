from difflib import SequenceMatcher


def normalizeString(text):
    st = text.replace("”", "\"")
    st = st.replace("“", "\"")
    st = st.replace("Déja", "Déjà")
    st = st.replace("\\.", "...")
    st = st.replace(".\\", "...")
    st = st.replace(",..", "...")
    st = st.replace(".,.", "...")
    st = st.replace("..,", "...")
    st = st.replace("\n\n", "\n")
    return st


def similar(s1, s2):
    return SequenceMatcher(None, s1, s2).ratio()
