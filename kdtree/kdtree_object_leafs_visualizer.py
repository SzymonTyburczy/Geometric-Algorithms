import matplotlib.pyplot as plt
from kdtree_object_implementation_leafs import KDtree

class KDtreeVisualizer:
    @staticmethod
    def plot_tree(node, depth=0, pos=(0.5, 1), parent=None, ax=None, x_offset=0.1):
        """
        Rekurencyjna funkcja do wizualizacji struktury KD-tree.

        :param node: Aktualny węzeł drzewa.
        :param depth: Głębokość węzła w drzewie.
        :param pos: Pozycja węzła na wykresie (x, y).
        :param parent: Pozycja rodzica węzła.
        :param ax: Obiekt wykresu matplotlib.
        :param x_offset: Odległość w poziomie między węzłami.
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.axis("off")

        if node is None:
            return

        # Rysowanie połączenia z rodzicem
        if parent is not None:
            ax.plot([parent[0], pos[0]], [parent[1], pos[1]], 'k-', lw=1)

        # Rysowanie węzła
        if isinstance(node, KDtree.Leaf):
            ax.text(pos[0], pos[1], f"{node.point}", fontsize=10, ha='center', bbox=dict(facecolor='blue', alpha=0.3))
        else:
            ax.text(pos[0], pos[1], f"Dim={depth % 2}\n{node.divider}", fontsize=10, ha='center', bbox=dict(facecolor='orange', alpha=0.5))

        # Wywołanie rekurencyjne dla dzieci
        child_y = pos[1] - 0.1
        if node.getclass() == KDtree.Vertex:
            if node.left is not None:
                KDtreeVisualizer.plot_tree(node.left, depth + 1, (pos[0] - x_offset, child_y), pos, ax, x_offset / 1.5)
            if node.right is not None:
                KDtreeVisualizer.plot_tree(node.right, depth + 1, (pos[0] + x_offset, child_y), pos, ax, x_offset / 1.5)

        if ax is None:
            plt.show()

test_data = [(1,1),(2,3),(0.5,4),(5.5,4.5),(6,2),(4,2.5),(3.5,6),(4.5,3.5)]
kdtree = KDtree(test_data)
print(kdtree.get_root().left.divider)
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis("off")
KDtreeVisualizer.plot_tree(kdtree.get_root(), ax=ax)
plt.show()