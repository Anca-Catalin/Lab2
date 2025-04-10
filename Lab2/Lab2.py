import hashlib
import string

TARGET_HASH = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

Mari = string.ascii_uppercase
Mici = string.ascii_lowercase
Numere = string.digits
Special = "!@#$"

apeluri_recursive = 0
found = False

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def backtrack(candidate, total_mari, total_numere, total_special, total_mici):
    global apeluri_recursive, found


    if found:
        return

    apeluri_recursive += 1


    if len(candidate) == 6:
        if total_mari == 1 and total_numere == 1 and total_special == 1 and total_mici == 3:
            if get_hash(candidate) == TARGET_HASH:
                print(f"Parola găsită: {candidate}")
                print(f"Număr apeluri recursive: {apeluri_recursive}")
                found = True
        return


    if total_mari < 1:
        for ch in Mari:
            backtrack(candidate + ch, total_mari + 1, total_numere, total_special, total_mici)
            if found: return

    if total_numere < 1:
        for ch in Numere:
            backtrack(candidate + ch, total_mari, total_numere + 1, total_special, total_mici)
            if found: return

    if total_special < 1:
        for ch in Special:
            backtrack(candidate + ch, total_mari, total_numere, total_special + 1, total_mici)
            if found: return

    if total_mici < 3:
        for ch in Mici:
            backtrack(candidate + ch, total_mari, total_numere, total_special, total_mici + 1)
            if found: return


backtrack("", 0, 0, 0, 0)
