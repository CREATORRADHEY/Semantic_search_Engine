from typing import Any


class MetadataFilter:

    @staticmethod
    def matches(
        metadata: dict[str, Any],
        filters: dict[str, Any]
    ) -> bool:

        for key, condition in filters.items():

            actual_value = metadata.get(key)

            # -----------------------------------------
            # Simple equality
            # -----------------------------------------

            if not isinstance(
                condition,
                dict
            ):

                if actual_value != condition:

                    return False

                continue

            # -----------------------------------------
            # Operators
            # -----------------------------------------

            for operator, expected_value in condition.items():

                if operator == "$eq":

                    if actual_value != expected_value:

                        return False

                elif operator == "$ne":

                    if actual_value == expected_value:

                        return False

                elif operator == "$gt":

                    if actual_value <= expected_value:

                        return False

                elif operator == "$gte":

                    if actual_value < expected_value:

                        return False

                elif operator == "$lt":

                    if actual_value >= expected_value:

                        return False

                elif operator == "$lte":

                    if actual_value > expected_value:

                        return False

                elif operator == "$in":

                    if actual_value not in expected_value:

                        return False

                else:

                    raise ValueError(
                        f"Unsupported filter operator: {operator}"
                    )

        return True