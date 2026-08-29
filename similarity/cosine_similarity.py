import numpy as np


class CosineSimilarity:

    @staticmethod
    def calculate(
        vector_a,
        vector_b
    ) -> float:

        vector_a = np.array(vector_a)
        vector_b = np.array(vector_b)

        similarity = np.dot(
            vector_a,
            vector_b
        ) / (
            np.linalg.norm(vector_a)
            *
            np.linalg.norm(vector_b)
        )

        return float(similarity)