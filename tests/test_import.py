from types import ModuleType

import cloudcoil.models.prometheus_operator as prometheus_operator


def test_has_modules():
    modules = list(
        filter(lambda x: isinstance(x, ModuleType), prometheus_operator.__dict__.values())
    )
    assert modules, "No modules found in prometheus_operator"
