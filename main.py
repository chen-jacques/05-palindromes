"""vérifie si un string est un palindrome"""

def char_spec(p):
    """enleve les accents et characteres speciaux"""
    p = p.lower()
    char_list = str.maketrans("éèêëàâäîïùûüçôö", "eeeeaaaiiuuucoo")
    p=p.translate({ord(i): None for i in ' ,.;?!:-\''})
    return p.translate(char_list)

def ispalindrome(p):
    """renvoie si le string est un palindrome"""
    p=char_spec(p)
    return p==p[::-1]

#### Fonction principale


def main():
    """mian"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
