from typing import List, Tuple


class GeoLocalizator:
    def geo_localize(self, trees: List, coordenates: Tuple) -> List:
        """
        Localize from Tree object List all them coordenates.

        :param List trees: The list with all trees to operate with.
        :param Tuple coordenates: The coordenates off the target image.
        :return: The list off all Trees with all coordenates calculated.
        """
        self._coordenates = coordenates

        for tree in trees:
            x, y = self._calculate_coordenates(tree)
            tree.set_coordenates(x, y)

        return trees

    def _calculate_coordenates(self, tree: "Tree") -> Tuple:
        """
        Localize Tree object with its coordenates.

        :param Tree tree: The Tree to work with.
        :return: The Tuple of GPS coordenates witch represent its center.
        """
        x = None
        y = None
        return x, y
