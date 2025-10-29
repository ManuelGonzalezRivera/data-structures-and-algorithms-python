

                                                                    ------------- Spanish version -------------

### 🌳 Descripción general del programa

Este programa implementa un sistema de almacenamiento de usuarios basado en un **árbol binario de búsqueda balanceado (AVL Tree)**.

La idea es combinar conceptos teóricos de estructuras de datos (BST y AVL) con una aplicación práctica y fácil de entender: gestionar objetos `User` dentro de un `TreeMap` **ordenado y balanceado automáticamente**.
El programa está dividido en tres partes principales:

  * **Clase `User`** → representa a una persona con su nombre, usuario y correo.
  * **Clase `BSTNode`** → define cómo funciona cada nodo del árbol binario (clave, valor, hijos, balanceo, etc.).
  * **Clase `TreeMap`** → sirve como interfaz de alto nivel, para usar el árbol como si fuera un diccionario de Python, pero internamente usa nodos BST balanceados como un árbol AVL.

-----

### 👤 Clase User

```python
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
```

Representa a cada usuario con tres atributos:

  * **username**: clave única (sirve como “key” en el árbol).
  * **name**: nombre completo.
  * **email**: correo electrónico.

Incluye un método `introduce_yourself()` que imprime una pequeña presentación, y métodos `__repr__` / `__str__` para mostrar los objetos de forma legible en consola.
Esta clase es simple, pero sirve de base para probar las operaciones del árbol con objetos reales.

-----

### 🌿 Clase BSTNode

La clase `BSTNode` es el núcleo del árbol binario de búsqueda.

Cada instancia representa un nodo con una clave y un valor, y contiene punteros a sus hijos y padre.

**Atributos importantes**

  * **key**: clave del nodo (en este caso, el nombre de usuario).
  * **value**: el objeto asociado (`User`).
  * **left**, **right**: hijos izquierdo y derecho.
  * **parent**: referencia al nodo padre.
  * **height**: altura del nodo (usada para mantener el equilibrio AVL).

**Métodos principales**
🔹 **Estructura y recorrido**

  * `traverse_in_order()` → devuelve las claves en orden ascendente (in-order traversal).
  * `to_tuple()` → convierte el árbol en una estructura anidada de tuplas para visualizarlo fácilmente.
  * `display_keys()` → imprime el árbol de forma jerárquica, visualizando los niveles.

🔹 **Altura y balance**

  * `update_height()` → recalcula la altura del nodo.
  * `get_balance()` → devuelve el factor de balance (altura izquierda - altura derecha).
  * En un AVL Tree, este valor debe estar entre -1 y 1 para que el árbol esté equilibrado.

🔹 **Operaciones estáticas del BST**

  * `insert(node, key, value)` → inserta un nuevo nodo en el lugar correcto.
  * `find(node, key)` → busca un nodo por su clave.
  * `update(node, key, value)` → cambia el valor asociado a una clave existente.
  * `delete(node, key)` → elimina un nodo siguiendo las tres reglas clásicas del BST:
      * **Sin hijos** → se elimina directamente.
      * **Con un hijo** → se sustituye por ese hijo.
      * **Con dos hijos** → se reemplaza por su sucesor in-order (el menor nodo del subárbol derecho).

🔹 **Funciones útiles**

  * `is_balanced(node)` → comprueba si el árbol está equilibrado y devuelve su altura.
  * `diameterOfBST()` → calcula el diámetro del árbol (el número máximo de aristas entre dos nodos).
  * `list_all(node)` → devuelve una lista con todos los pares (clave, valor) en orden.
  * `make_balanced_bst(data)` y `balance_bst(node)` → reconstruyen un árbol perfectamente balanceado a partir de una lista ordenada.

En conjunto, `BSTNode` define la lógica estructural del árbol, mientras que el balanceo se aplicará desde `TreeMap`.

-----

### 🗺️ Clase TreeMap

Esta clase actúa como un envoltorio (“wrapper”) sobre los nodos BST para ofrecer una interfaz similar a un diccionario de Python, pero basada en un AVL Tree.

**Ejemplo de uso**

```python
usuarios_map = TreeMap()
usuarios_map["ana"] = ana
usuarios_map["beatriz"] = beatriz

print(usuarios_map["ana"])
del usuarios_map["beatriz"]
```

Internamente, estas operaciones se traducen en inserciones, búsquedas o borrados en el árbol binario, con balanceo automático.

**Métodos clave**
🔸 **Inserción (`__setitem__`)**

  * Si el árbol está vacío → crea la raíz.
  * Si la clave existe → actualiza su valor.
  * Si no existe → inserta un nuevo nodo con `BSTNode.insert()`.
  * Después de cada inserción → llama a `do_rotations()` para mantener el equilibrio.

🔸 **Rotaciones**

  * El balanceo del árbol se consigue mediante rotaciones:
  * `rotate_left(x)` y `rotate_right(y)` → reorganizan los nodos para reducir el desequilibrio.
  * `do_rotations(node)` → recorre desde un nodo hacia arriba y aplica las rotaciones necesarias según el factor de balance.
  * Estas rotaciones garantizan que el árbol se mantenga balanceado después de cada operación, cumpliendo la propiedad del AVL Tree.

🔸 **Borrado (`__delitem__`)**

  * Usa `BSTNode.delete()` para eliminar el nodo y luego llama a `do_rotations()` desde el padre afectado para restaurar el equilibrio.

🔸 **Iteración, tamaño y visualización**

  * `__iter__()` → permite recorrer el árbol con `for`.
  * `__len__()` → devuelve el número de elementos.
  * `display()` → imprime visualmente la estructura del árbol.

En resumen, `TreeMap` permite usar un árbol binario como si fuera un diccionario ordenado, pero internamente mantiene su equilibrio gracias a las rotaciones AVL.

-----

### 👥 Creación e inserción de usuarios

Se crean 50 instancias de `User` con distintos nombres y correos, que se almacenan en una lista `usuarios`.

Después, se insertan todas en el `TreeMap` usando:

```python
usuarios_map = TreeMap()
for usuario in usuarios:
    usuarios_map[usuario.username] = usuario
```

Cada inserción mantiene el árbol ordenado alfabéticamente por `username` y balanceado automáticamente.

-----

### 🧪 Pruebas y comprobaciones

El script incluye múltiples pruebas automáticas:

  * **Longitud del árbol**: `len(usuarios_map)`
  * **Acceso a claves**: `usuarios_map["lorena"]`
  * **Actualización**: asignar una clave existente cambia su valor.
  * **Iteración**: recorrer los primeros usuarios en orden.
  * **Balanceo**: `BSTNode.is_balanced(usuarios_map.root)`
  * **Diámetro del árbol**: `BSTNode.diameterOfBST(usuarios_map.root)`
  * **Visualización**: `usuarios_map.display()`
  * **Existencia de claves**: usando `"ana" in usuarios_map`
  * **Eliminación**: `del usuarios_map["hugo"]`

También hay una segunda batería de tests (`test_tree`) donde se insertan claves en orden diseñado para forzar rotaciones automáticas, comprobando que el árbol se mantenga balanceado tras cada inserción o borrado.

-----

### ⚙️ En resumen

| Elemento | Función |
| :--- | :--- |
| **`User`** | Representa datos simples de usuario |
| **`BSTNode`** | Lógica estructural del árbol binario |
| **`TreeMap`** | Interfaz amigable tipo diccionario con balanceo AVL |
| **`do_rotations`** | Garantiza el equilibrio tras cada operación |
| **`is_balanced`** | Comprueba la corrección del balanceo |
| **`diameterOfBST`** | Mide la “anchura” del árbol |
| **`display_keys`** | Muestra visualmente la jerarquía del árbol |

-----

### 🧩 Finalidad educativa

Este proyecto no busca ser una librería lista para producción, sino un entrenamiento práctico para entender:

  * Cómo se almacenan datos en un árbol binario de búsqueda.
  * Cómo funcionan las rotaciones AVL para mantener el equilibrio.
  * Cómo implementar estructuras de datos complejas con una interfaz de alto nivel y estilo Python.





                                                                    ------------- English version -------------



🌳 Program Overview
This program implements a user storage system based on a **balanced binary search tree (AVL Tree)**.

The idea is to combine theoretical data structure concepts (BST and AVL) with a practical and easy-to-understand application: managing `User` objects within a `TreeMap` that is **automatically sorted and balanced**.
The program is divided into three main parts:

  * **`User` Class** → represents a person with their name, username, and email.
  * **`BSTNode` Class** → defines how each node of the binary tree works (key, value, children, balancing, etc.).
  * **`TreeMap` Class** → serves as a high-level interface, to use the tree as if it were a Python dictionary, but internally, it uses balanced BST nodes like an AVL tree.

-----

### 👤 User Class

```python
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
```

Represents each user with three attributes:

  * **username**: unique key (serves as the "key" in the tree).
  * **name**: full name.
  * **email**: email address.

It includes an `introduce_yourself()` method that prints a small introduction, and `__repr__` / `__str__` methods to display the objects legibly in the console.
This class is simple, but it serves as a foundation for testing the tree operations with real objects.

-----

### 🌿 BSTNode Class

The `BSTNode` class is the core of the binary search tree.

Each instance represents a node with a key and a value, and contains pointers to its children and parent.

**Important Attributes**

  * **key**: the node's key (in this case, the username).
  * **value**: the associated object (`User`).
  * **left**, **right**: left and right children.
  * **parent**: reference to the parent node.
  * **height**: height of the node (used to maintain AVL balance).

**Main Methods**
🔹 **Structure and Traversal**

  * `traverse_in_order()` → returns the keys in ascending order (in-order traversal).
  * `to_tuple()` → converts the tree into a nested tuple structure for easy visualization.
  * `display_keys()` → prints the tree hierarchically, visualizing the levels.

🔹 **Height and Balance**

  * `update_height()` → recalculates the node's height.
  * `get_balance()` → returns the balance factor (left height - right height).
  * In an AVL Tree, this value must be between -1 and 1 for the tree to be balanced.

🔹 **Static BST Operations**

  * `insert(node, key, value)` → inserts a new node in the correct place.
  * `find(node, key)` → searches for a node by its key.
  * `update(node, key, value)` → changes the value associated with an existing key.
  * `delete(node, key)` → deletes a node following the three classic BST rules:
      * **No children** → it is deleted directly.
      * **One child** → it is replaced by that child.
      * **Two children** → it is replaced by its in-order successor (the smallest node in the right subtree).

🔹 **Utility Functions**

  * `is_balanced(node)` → checks if the tree is balanced and returns its height.
  * `diameterOfBST()` → calculates the tree's diameter (the maximum number of edges between two nodes).
  * `list_all(node)` → returns a list of all (key, value) pairs in order.
  * `make_balanced_bst(data)` and `balance_bst(node)` → rebuild a perfectly balanced tree from a sorted list.

Altogether, `BSTNode` defines the structural logic of the tree, while the balancing will be applied from `TreeMap`.

-----

### 🗺️ TreeMap Class

This class acts as a "wrapper" around the BST nodes to offer an interface similar to a Python dictionary, but based on an AVL Tree.

**Example Usage**

```python
usuarios_map = TreeMap()
usuarios_map["ana"] = ana
usuarios_map["beatriz"] = beatriz

print(usuarios_map["ana"])
del usuarios_map["beatriz"]
```

Internally, these operations translate into insertions, searches, or deletions in the binary tree, with automatic balancing.

**Key Methods**
🔸 **Insertion (`__setitem__`)**

  * If the tree is empty → creates the root.
  * If the key exists → updates its value.
  * If it doesn't exist → inserts a new node using `BSTNode.insert()`.
  * After each insertion → calls `do_rotations()` to maintain balance.

🔸 **Rotations**

  * The tree's balancing is achieved through rotations:
  * `rotate_left(x)` and `rotate_right(y)` → reorganize the nodes to reduce imbalance.
  * `do_rotations(node)` → traverses up from a node and applies the necessary rotations based on the balance factor.
  * These rotations ensure the tree remains balanced after each operation, fulfilling the AVL Tree property.

🔸 **Deletion (`__delitem__`)**

  * Uses `BSTNode.delete()` to remove the node and then calls `do_rotations()` from the affected parent to restore balance.

🔸 **Iteration, Size, and Visualization**

  * `__iter__()` → allows iterating through the tree with a `for` loop.
  * `__len__()` → returns the number of elements.
  * `display()` → visually prints the tree structure.

In summary, `TreeMap` allows using a binary tree as if it were a sorted dictionary, but internally maintains its balance thanks to AVL rotations.

-----

### 👥 User Creation and Insertion

50 `User` instances are created with different names and emails, which are stored in a list `usuarios`.

Afterward, they are all inserted into the `TreeMap` using:

```python
usuarios_map = TreeMap()
for usuario in usuarios:
    usuarios_map[usuario.username] = usuario
```

Each insertion keeps the tree sorted alphabetically by `username` and automatically balanced.

-----

### 🧪 Tests and Checks

The script includes multiple automatic tests:

  * **Tree length**: `len(usuarios_map)`
  * **Key access**: `usuarios_map["lorena"]`
  * **Update**: assigning to an existing key changes its value.
  * **Iteration**: looping through the first few users in order.
  * **Balance**: `BSTNode.is_balanced(usuarios_map.root)`
  * **Tree diameter**: `BSTNode.diameterOfBST(usuarios_map.root)`
  * **Visualization**: `usuarios_map.display()`
  * **Key existence**: using `"ana" in usuarios_map`
  * **Deletion**: `del usuarios_map["hugo"]`

There is also a second battery of tests (`test_tree`) where keys are inserted in an order designed to force automatic rotations, checking that the tree remains balanced after each insertion or deletion.

-----

### ⚙️ In Summary

| Element | Function |
| :--- | :--- |
| **`User`** | Represents simple user data |
| **`BSTNode`** | Structural logic of the binary tree |
| **`TreeMap`** | User-friendly dictionary-style interface with AVL balancing |
| **`do_rotations`** | Ensures balance after each operation |
| **`is_balanced`** | Checks the correctness of the balance |
| **`diameterOfBST`** | Measures the "width" of the tree |
| **`display_keys`** | Visually displays the tree hierarchy |

-----

### 🧩 Educational Purpose

This project is not intended to be a production-ready library, but rather a practical exercise to understand:

  * How data is stored in a binary search tree.
  * How AVL rotations work to maintain balance.
  * How to implement complex data structures with a high-level, Pythonic interface.
