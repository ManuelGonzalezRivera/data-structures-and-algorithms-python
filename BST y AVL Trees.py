# -------------------- Clase User --------------------

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


# -------------------- Clase BSTNode --------------------

class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1  # al crear, altura inicial 1

    # ------------------ Métodos de instancia ------------------

    def update_height(self):
        """Actualiza la altura del nodo en función de sus hijos"""
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)

    def get_balance(self):
        """Devuelve el factor de balance (izquierda - derecha)."""
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return 1 + left_size + right_size

    def traverse_in_order(self):
        left = self.left.traverse_in_order() if self.left else []
        right = self.right.traverse_in_order() if self.right else []
        return left + [self.key] + right

    def to_tuple(self):
        left = self.left.to_tuple() if self.left else None
        right = self.right.to_tuple() if self.right else None
        if left is None and right is None:
            return self.key
        return (left, self.key, right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return self.__str__()

    def diameterOfBST(self):
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        depth(self)
        return self.diameter

    # ------------------ Métodos estáticos ------------------

    @staticmethod
    def insert(node, key, value):
        if node is None:
            return BSTNode(key, value)
        elif key < node.key:
            node.left = BSTNode.insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = BSTNode.insert(node.right, key, value)
            node.right.parent = node
        node.update_height()
        return node

    @staticmethod
    def find(node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return BSTNode.find(node.left, key)
        else:
            return BSTNode.find(node.right, key)

    @staticmethod
    def update(node, key, value):
        target = BSTNode.find(node, key)
        if target:
            target.value = value

    @staticmethod
    def display_keys(node, space='\t', level=0):
        if node is None:
            print(space * level + '∅')
            return
        if node.left is None and node.right is None:
            print(space * level + str(node.key))
            return
        BSTNode.display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        BSTNode.display_keys(node.left, space, level + 1)

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = BSTNode(data[1])
            node.left = BSTNode.parse_tuple(data[0])
            node.right = BSTNode.parse_tuple(data[2])
        else:
            node = BSTNode(data)
        return node

    @staticmethod
    def balanced_insert_order(items):
        if not items:
            return []
        mid = len(items) // 2
        return (
            [items[mid]]
            + BSTNode.balanced_insert_order(items[:mid])
            + BSTNode.balanced_insert_order(items[mid + 1:])
        )

    @staticmethod
    def remove_none(nums):
        return [x for x in nums if x is not None]

    @staticmethod
    def list_all(node):
        if node is None:
            return []
        return (
            BSTNode.list_all(node.left)
            + [(node.key, node.value)]
            + BSTNode.list_all(node.right)
        )

    @staticmethod
    def is_bst(node, verbose=False):
        if node is None:
            return True, None, None

        is_bst_l, min_l, max_l = BSTNode.is_bst(node.left, verbose)
        is_bst_r, min_r, max_r = BSTNode.is_bst(node.right, verbose)

        is_bst_node = (
            is_bst_l and is_bst_r and
            (max_l is None or node.key > max_l) and
            (min_r is None or node.key < min_r)
        )

        min_key = min(BSTNode.remove_none([min_l, node.key, min_r]))
        max_key = max(BSTNode.remove_none([max_l, node.key, max_r]))

        if verbose:
            print(node.key, min_key, max_key, is_bst_node)

        return is_bst_node, min_key, max_key

    @staticmethod
    def is_balanced(node):
        if node is None:
            return True, 0
        balanced_l, height_l = BSTNode.is_balanced(node.left)
        balanced_r, height_r = BSTNode.is_balanced(node.right)
        balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
        height = 1 + max(height_l, height_r)
        return balanced, height

    @staticmethod
    def make_balanced_bst(data, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(data) - 1
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        key, value = data[mid]
        root = BSTNode(key, value)
        root.parent = parent
        root.left = BSTNode.make_balanced_bst(data, lo, mid - 1, root)
        root.right = BSTNode.make_balanced_bst(data, mid + 1, hi, root)
        return root

    @staticmethod
    def balance_bst(node):
        return BSTNode.make_balanced_bst(BSTNode.list_all(node))

    @staticmethod
    def delete(node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = BSTNode.delete(node.left, key)
        elif key > node.key:
            node.right = BSTNode.delete(node.right, key)
        else:
            # Caso 1: sin hijos
            if node.left is None and node.right is None:
                return None
            # Caso 2: un solo hijo
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Caso 3: dos hijos
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key, node.value = successor.key, successor.value
            node.right = BSTNode.delete(node.right, successor.key)

        node.update_height()
        return node


# -------------------- Clase TreeMap --------------------

class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
            return

        node = BSTNode.find(self.root, key)
        if node:
            node.value = value
            start_node = node
        else:
            self.root = BSTNode.insert(self.root, key, value)
            start_node = BSTNode.find(self.root, key)

        # Y aquí la clave:
        self.root = self.do_rotations(start_node)

    def __getitem__(self, key):
        node = BSTNode.find(self.root, key)
        return node.value if node else None

    def __contains__(self, key):
        return BSTNode.find(self.root, key) is not None

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(f"Key '{key}' not found in TreeMap.")
        deleted_node = BSTNode.find(self.root, key)
        self.root = BSTNode.delete(self.root, key)
        if deleted_node:
            # Balanceamos desde el padre del nodo eliminado
            start_node = deleted_node.parent if deleted_node.parent else self.root
            self.root = self.do_rotations(start_node)

    def __iter__(self):
        return (x for x in BSTNode.list_all(self.root))

    def __len__(self):
        return self.root.size() if self.root else 0

    def display(self):
        return BSTNode.display_keys(self.root)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        x.update_height()
        y.update_height()
        return y

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        y.update_height()
        x.update_height()
        return x

    def do_rotations(self, node):
        """Revisa el balance desde 'node' hacia arriba y realiza rotaciones si es necesario."""
        while node:
            node.update_height()
            balance = node.get_balance()

            if balance > 1 and node.left.get_balance() >= 0:
                node = self.rotate_right(node)
            elif balance < -1 and node.right.get_balance() <= 0:
                node = self.rotate_left(node)
            elif balance > 1 and node.left.get_balance() < 0:
                self.rotate_left(node.left)
                node = self.rotate_right(node)
            elif balance < -1 and node.right.get_balance() > 0:
                self.rotate_right(node.right)
                node = self.rotate_left(node)

            # Este paso es el importante:
            # si después de rotar, el nodo no tiene padre, significa que es la nueva raíz
            if node.parent is None:
                self.root = node

            node = node.parent

        return self.root

        # Devolver la raíz
        while last.parent:
            last = last.parent
        return last


# -------------------- Creación de usuarios --------------------

ana = User('ana', 'Ana Torres', 'ana.torres@example.com')
sergio = User('sergio', 'Sergio Díaz', 'sergio.diaz@example.com')
clara = User('clara', 'Clara Ruiz', 'clara.ruiz@example.com')
david = User('david', 'David Navarro', 'david.navarro@example.com')
beatriz = User('beatriz', 'Beatriz Gómez', 'beatriz.gomez@example.com')
javier = User('javier', 'Javier Alonso', 'javier.alonso@example.com')
marta = User('marta', 'Marta Sánchez', 'marta.sanchez@example.com')
adrian = User('adrian', 'Adrián Molina', 'adrian.molina@example.com')
ines = User('ines', 'Inés Domínguez', 'ines.dominguez@example.com')
raul = User('raul', 'Raúl Cabrera', 'raul.cabrera@example.com')
noelia = User('noelia', 'Noelia Ortega', 'noelia.ortega@example.com')
hugo = User('hugo', 'Hugo Ramos', 'hugo.ramos@example.com')
pablo = User('pablo', 'Pablo Gil', 'pablo.gil@example.com')
gema = User('gema', 'Gema León', 'gema.leon@example.com')
alejandro = User('alejandro', 'Alejandro Vargas', 'alejandro.vargas@example.com')
valeria = User('valeria', 'Valeria Campos', 'valeria.campos@example.com')
ivan = User('ivan', 'Iván Rojas', 'ivan.rojas@example.com')
carla = User('carla', 'Carla Reyes', 'carla.reyes@example.com')
ricardo = User('ricardo', 'Ricardo Ponce', 'ricardo.ponce@example.com')
lorena = User('lorena', 'Lorena Muñoz', 'lorena.munoz@example.com')
nicolas = User('nicolas', 'Nicolás Santos', 'nicolas.santos@example.com')
angela = User('angela', 'Ángela Fuentes', 'angela.fuentes@example.com')
samuel = User('samuel', 'Samuel Castro', 'samuel.castro@example.com')
elena = User('elena', 'Elena Delgado', 'elena.delgado@example.com')
martin = User('martin', 'Martín Guerrero', 'martin.guerrero@example.com')
diana = User('diana', 'Diana Romero', 'diana.romero@example.com')
oscar = User('oscar', 'Óscar Paredes', 'oscar.paredes@example.com')
camila = User('camila', 'Camila Herrera', 'camila.herrera@example.com')
ruben = User('ruben', 'Rubén Blanco', 'ruben.blanco@example.com')
patricia = User('patricia', 'Patricia Cruz', 'patricia.cruz@example.com')
jaime = User('jaime', 'Jaime Soto', 'jaime.soto@example.com')
candela = User('candela', 'Candela Ramos', 'candela.ramos@example.com')
francisco = User('francisco', 'Francisco Peña', 'francisco.pena@example.com')
rosa = User('rosa', 'Rosa Nieto', 'rosa.nieto@example.com')
julian = User('julian', 'Julián Bravo', 'julian.bravo@example.com')
paula = User('paula', 'Paula Cabrera', 'paula.cabrera@example.com')
daniel = User('daniel', 'Daniel Estévez', 'daniel.estevez@example.com')
veronica = User('veronica', 'Verónica Lara', 'veronica.lara@example.com')
eduardo = User('eduardo', 'Eduardo Castro', 'eduardo.castro@example.com')
isabel = User('isabel', 'Isabel Medina', 'isabel.medina@example.com')
alejandra = User('alejandra', 'Alejandra Flores', 'alejandra.flores@example.com')
marcos = User('marcos', 'Marcos Fernández', 'marcos.fernandez@example.com')
rocio = User('rocio', 'Rocío Álvarez', 'rocio.alvarez@example.com')
victoria = User('victoria', 'Victoria Ramos', 'victoria.ramos@example.com')
tomas = User('tomas', 'Tomás García', 'tomas.garcia@example.com')
gema2 = User('gema2', 'Gema Paredes', 'gema.paredes@example.com')
luciano = User('luciano', 'Luciano Serrano', 'luciano.serrano@example.com')
monica = User('monica', 'Mónica Reyes', 'monica.reyes@example.com')
fernando = User('fernando', 'Fernando Prieto', 'fernando.prieto@example.com')
irene = User('irene', 'Irene Lozano', 'irene.lozano@example.com')

usuarios = [
    ana, sergio, clara, david, beatriz,
    javier, marta, adrian, ines, raul,
    noelia, hugo, pablo, gema, alejandro,
    valeria, ivan, carla, ricardo, lorena,
    nicolas, angela, samuel, elena, martin,
    diana, oscar, camila, ruben, patricia,
    jaime, candela, francisco, rosa, julian,
    paula, daniel, veronica, eduardo, isabel,
    alejandra, marcos, rocio, victoria, tomas,
    gema2, luciano, monica, fernando, irene
]

usuarios_map = TreeMap()
for usuario in usuarios:
    usuarios_map[usuario.username] = usuario


# -------------------- Tests --------------------

# Longitud del árbol
print(f"Longitud del árbol binario de usuarios: {len(usuarios_map)}")

# Acceso
print(f"Usuario Lorena: {usuarios_map['lorena']}")

# Update
usuarios_map["adrian"] = User("adri", "Adrian Vazquez", "adrian.vazquez@example.com")

# Iteración
print("Primeros 5 usuarios:")
I = 1
for key, value in usuarios_map:
    print(f"Usuario {I}: {key, value}")
    I += 1
    if I == 6:
        break

# Check balanceo
print("¿Está balanceado?", BSTNode.is_balanced(usuarios_map.root))

# Diámetro
print("Diámetro del árbol:", BSTNode.diameterOfBST(usuarios_map.root))

# Conversión a tupla
print("Árbol como tupla:", BSTNode.to_tuple(usuarios_map.root))

# Display visual
usuarios_map.display()

# Test de __contains__
print("¿Existe 'ana' en el árbol?", 'ana' in usuarios_map)
print("¿Existe 'zzz' en el árbol?", 'zzz' in usuarios_map)

# Test de borrado
print("Borrando usuario 'hugo'...")
del usuarios_map['hugo']
print("¿Sigue existiendo 'hugo'?", 'hugo' in usuarios_map)
print(f"Nuevo tamaño del árbol: {len(usuarios_map)}")

# -------------------- TEST BALANCEO AUTOMÁTICO --------------------

# Creamos un TreeMap vacío
test_tree = TreeMap()

# Insertamos usuarios en orden que produce inicialmente un árbol balanceado
usuarios_test = [
    ("u4", User("u4", "User 4", "u4@example.com")),
    ("u2", User("u2", "User 2", "u2@example.com")),
    ("u6", User("u6", "User 6", "u6@example.com")),
    ("u1", User("u1", "User 1", "u1@example.com")),
    ("u3", User("u3", "User 3", "u3@example.com")),
    ("u5", User("u5", "User 5", "u5@example.com")),
    ("u7", User("u7", "User 7", "u7@example.com")),
]

# Insertamos los primeros 7 usuarios
print("Prueba de balanceo en nuevo arbol: Insertando primeros 7 usuarios (árbol balanceado)...")
for key, user in usuarios_test:
    test_tree[key] = user

# Verificamos que está balanceado
balanced, height = BSTNode.is_balanced(test_tree.root)
print(f"¿Árbol balanceado después de 7 inserciones? {balanced}, Altura: {height}")
test_tree.display()

# Insertamos usuarios adicionales que desbalancearán el árbol
usuarios_adicionales = [
    ("u8", User("u8", "User 8", "u8@example.com")),
    ("u9", User("u9", "User 9", "u9@example.com")),
    ("u91", User("u10", "User 10", "u10@example.com")),
    ("u92", User("u11", "User 11", "u11@example.com")),
    ("u93", User("u12", "User 12", "u12@example.com")),
    ("u95", User("u13", "User 13", "u13@example.com")),
]

print("\nInsertando usuarios nuevos para provocar rotaciones automáticas...")
for key, user in usuarios_adicionales:
    test_tree[key] = user
    # Mostramos si el árbol sigue balanceado tras cada inserción
    balanced, height = BSTNode.is_balanced(test_tree.root)
    print(f"Después de insertar {key}: ¿balanceado? {balanced}, Altura: {height}")

# Mostramos visualmente el árbol final
print("\nÁrbol final tras todas las inserciones y rotaciones:")
test_tree.display()

# Comprobación final: recorrer todos los usuarios en orden
print("\nUsuarios en orden (in-order traversal):")
for k, v in test_tree:
    print(f"{k}: {v.name}")

print("Borrando los usuarios u4 y u2...")
del test_tree['u4']
del test_tree['u3']
print("\nÁrbol final tras todas los borrados:")
test_tree.display()