from spycfg import generators

from tests.helpers import BaseTestCase


class GeneratorsTestCase(BaseTestCase):
    def test_keys_path_generator_for_flat_dict(self):
        d = {i: i for i in range(5)}

        self.assertEquals(
            [[str(i)] for i in range(5)],
            list(generators.keys_path_to_simple_values(d))
        )
