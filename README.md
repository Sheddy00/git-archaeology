# git-archaeology

> *"Git enregistre tout. Même ce qu'on croit avoir effacé."*

Un projet Python ordinaire, en apparence. Mais quelqu'un y a caché des messages dans les recoins
les plus obscurs de son historique Git.

**Votre mission** : fouiller les entrailles de ce dépôt et en extraire les 6 flags cachés.

---

## Démarrage rapide

```bash
git clone https://github.com/Sheddy00/git-archaeology
cd git-archaeology
```

Chaque flag a le format : `CTF{...}`

Appelez le jury pour validation sur votre machine quand vous trouvez un flag.

---

## Rappels Git utiles

Avant de commencer, voici les concepts Git dont vous aurez besoin.
Pas de solution ici — juste des outils.

### Les objets Git

Git stocke tout sous forme d'objets dans `.git/objects/`. Il en existe 4 types :

| Type | Description |
|------|-------------|
| `blob` | Contenu d'un fichier |
| `tree` | Liste de fichiers (comme un répertoire) |
| `commit` | Snapshot + métadonnées + pointeur vers un tree |
| `tag` | Référence annotée vers un commit |

Chaque objet est identifié par son hash SHA-1.

```bash
# Lire n'importe quel objet Git
git cat-file -t <hash>   # type de l'objet
git cat-file -p <hash>   # contenu de l'objet
```

### Le reflog

Le reflog est le journal interne de Git. Il enregistre **chaque mouvement de HEAD**, y compris
vers des branches qui n'existent plus.

```bash
git reflog                        # historique de HEAD
git reflog --all                  # historique de toutes les refs
git reflog --all --format="%H %gs %s"   # avec les messages
```

### Les packfiles

Git optimise le stockage en compressant les objets dans des fichiers `.pack`.
Les objets "loose" (individuels) sont dans `.git/objects/XX/...`
Les packfiles sont dans `.git/objects/pack/`.

```bash
# Inspecter un packfile
git verify-pack -v .git/objects/pack/*.idx

# Lire un objet depuis un packfile (même commande)
git cat-file -p <hash>
```

### Les objets orphelins

Un objet Git peut exister dans la base de données sans être référencé par aucune branche,
aucun tag, aucun commit. Pour les trouver tous :

```bash
git cat-file --batch-all-objects --batch-check
```

### Les notes Git

Les notes permettent d'annoter un commit après coup, sans changer son hash.
Elles sont stockées dans `refs/notes/` et ne s'affichent pas par défaut.

```bash
# Récupérer les notes depuis le remote
git fetch origin 'refs/notes/*:refs/notes/*'

# Afficher les notes dans le log
git log --show-notes=*

# Afficher uniquement les commits de merge avec leurs notes
git log --show-notes=* --merges
```

### Les hooks Git

Les hooks sont des scripts dans `.git/hooks/` qui s'exécutent automatiquement.
Ils ne sont pas versionnés. Ils peuvent contenir n'importe quoi.

```bash
ls -la .git/hooks/       # lister les hooks présents
cat .git/hooks/<nom>     # lire un hook
cat -A .git/hooks/<nom>  # révéler les caractères non-imprimables (^I = tab)
```

### Les submodules

Un submodule est un repo Git imbriqué dans un autre.
Il est déclaré dans `.gitmodules` et cloné séparément.

```bash
cat .gitmodules                          # voir les submodules déclarés
git submodule init                       # initialiser
git submodule update                     # cloner les sous-repos
cd <dossier_submodule>                   # entrer dans le sous-repo
git log --all --oneline                  # historique du sous-repo
git config --list                        # configuration du sous-repo
```

---

## Encodages courants

### ROT13

Chiffrement par substitution : chaque lettre est décalée de 13 positions.

```bash
echo "texte_encodé" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

### Base64

Encodage binaire-texte utilisé pour transporter des données.

```bash
echo "texte" | base64          # encoder
echo "dGV4dGU=" | base64 -d   # décoder
```

### Inverser une chaîne

```bash
echo "texte" | rev
```

### Décoder du binaire en ASCII (Python)

```python
bits = "0100100001000101010011000100110001001111"
chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
print(''.join(chars))
```

---

## Ressources

- [Git Internals — Pro Git Book](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)
- [git cat-file documentation](https://git-scm.com/docs/git-cat-file)
- [git reflog documentation](https://git-scm.com/docs/git-reflog)
- [git notes documentation](https://git-scm.com/docs/git-notes)
- [git submodule documentation](https://git-scm.com/docs/git-submodule)

---

*6 flags. 1 150 points. Bonne fouille.*
