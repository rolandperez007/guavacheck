import importlib
import logging

logger = logging.getLogger("irongate.bootstrap")


def safe_import(path: str, attr: str = None):
    """
    Safely import a module or attribute.
    Prevents full system crash during bootstrap.
    """
    try:
        module = importlib.import_module(path)

        if attr:
            return getattr(module, attr, None)

        return module

    except Exception as e:
        logger.warning(f"[BOOTSTRAP] Failed to import {path}: {e}")
        return None


def safe_register(gate, rule, name: str):
    """
    Prevent duplicate or broken rule registration.
    """
    if rule is None:
        logger.warning(f"[BOOTSTRAP] Skipping missing rule: {name}")
        return

    try:
        gate.register_rule(rule)
        logger.info(f"[BOOTSTRAP] Registered rule: {name}")
    except Exception as e:
        logger.error(f"[BOOTSTRAP] Failed rule {name}: {e}")
