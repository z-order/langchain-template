"""
Core module for instance registry: used to register and get instances of modules
"""

import logging
import inspect
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class InstanceRegistry:
    _instances: Dict[str, Any] = {}

    @classmethod
    def register(cls, key: str, instance: Any) -> None:
        """Register an instance with a string key"""
        try:
            cls._instances[key] = instance

        except Exception as e:
            # Get caller information
            caller_frame = inspect.currentframe().f_back
            caller_module = "unknown"
            caller_function = "unknown"

            if caller_frame:
                module = inspect.getmodule(caller_frame)
                if module:
                    caller_module = module.__name__
                caller_function = caller_frame.f_code.co_name

            logger.error(
                f"Failed to register instance '{key}' from {caller_module}.{caller_function}: {str(e)}")
            raise

    @classmethod
    def get(cls, key: str) -> Any:
        """Get an instance by key"""
        try:
            if key not in cls._instances:
                error_msg = f"Instance with key '{key}' not found in registry"
                # Get caller information
                caller_frame = inspect.currentframe().f_back
                caller_module = "unknown"
                caller_function = "unknown"

                if caller_frame:
                    module = inspect.getmodule(caller_frame)
                    if module:
                        caller_module = module.__name__
                    caller_function = caller_frame.f_code.co_name

                logger.error(
                    f"{error_msg} - Requested by {caller_module}.{caller_function}")
                raise KeyError(error_msg)

            return cls._instances[key]

        except Exception as e:
            # Get caller information
            caller_frame = inspect.currentframe().f_back
            caller_module = "unknown"
            caller_function = "unknown"

            if caller_frame:
                module = inspect.getmodule(caller_frame)
                if module:
                    caller_module = module.__name__
                caller_function = caller_frame.f_code.co_name

            logger.error(
                f"Failed to get instance '{key}' from {caller_module}.{caller_function}: {str(e)}")
            raise

    @classmethod
    def has(cls, key: str) -> bool:
        """Check if an instance exists with the given key"""
        try:
            return key in cls._instances

        except Exception as e:
            # Get caller information
            caller_frame = inspect.currentframe().f_back
            caller_module = "unknown"
            caller_function = "unknown"

            if caller_frame:
                module = inspect.getmodule(caller_frame)
                if module:
                    caller_module = module.__name__
                caller_function = caller_frame.f_code.co_name

            logger.error(
                f"Failed to check instance '{key}' existence from {caller_module}.{caller_function}: {str(e)}")
            raise

    @classmethod
    def unregister(cls, key: str) -> None:
        """Remove an instance from the registry"""
        try:
            if key in cls._instances:
                del cls._instances[key]

        except Exception as e:
            # Get caller information
            caller_frame = inspect.currentframe().f_back
            caller_module = "unknown"
            caller_function = "unknown"

            if caller_frame:
                module = inspect.getmodule(caller_frame)
                if module:
                    caller_module = module.__name__
                caller_function = caller_frame.f_code.co_name

            logger.error(
                f"Failed to unregister instance '{key}' from {caller_module}.{caller_function}: {str(e)}")
            raise

    @classmethod
    def clear(cls) -> None:
        """Clear all registered instances"""
        try:
            cls._instances.clear()

        except Exception as e:
            # Get caller information
            caller_frame = inspect.currentframe().f_back
            caller_module = "unknown"
            caller_function = "unknown"

            if caller_frame:
                module = inspect.getmodule(caller_frame)
                if module:
                    caller_module = module.__name__
                caller_function = caller_frame.f_code.co_name

            logger.error(
                f"Failed to clear registry from {caller_module}.{caller_function}: {str(e)}")
            raise

    @classmethod
    def list_keys(cls) -> list:
        """Get list of all registered keys"""
        try:
            return list(cls._instances.keys())

        except Exception as e:
            # Get caller information
            caller_frame = inspect.currentframe().f_back
            caller_module = "unknown"
            caller_function = "unknown"

            if caller_frame:
                module = inspect.getmodule(caller_frame)
                if module:
                    caller_module = module.__name__
                caller_function = caller_frame.f_code.co_name

            logger.error(
                f"Failed to list registry keys from {caller_module}.{caller_function}: {str(e)}")
            raise

    @classmethod
    def get_all(cls) -> Dict[str, Any]:
        """Get all registered instances"""
        try:
            return cls._instances.copy()

        except Exception as e:
            # Get caller information
            caller_frame = inspect.currentframe().f_back
            caller_module = "unknown"
            caller_function = "unknown"

            if caller_frame:
                module = inspect.getmodule(caller_frame)
                if module:
                    caller_module = module.__name__
                caller_function = caller_frame.f_code.co_name

            logger.error(
                f"Failed to get all registry instances from {caller_module}.{caller_function}: {str(e)}")
            raise


# Convenience functions with error-only logging

def register_instance(key: str, instance: Any) -> None:
    """Register an instance with a key"""
    try:
        InstanceRegistry.register(key, instance)

    except Exception as e:
        # Get caller information
        caller_frame = inspect.currentframe().f_back
        caller_module = "unknown"
        caller_function = "unknown"

        if caller_frame:
            module = inspect.getmodule(caller_frame)
            if module:
                caller_module = module.__name__
            caller_function = caller_frame.f_code.co_name

        logger.error(
            f"Failed to register instance '{key}' via convenience function from {caller_module}.{caller_function}: {str(e)}")
        raise


def get_instance(key: str) -> Any:
    """Get an instance by key"""
    try:
        return InstanceRegistry.get(key)

    except Exception as e:
        # Get caller information
        caller_frame = inspect.currentframe().f_back
        caller_module = "unknown"
        caller_function = "unknown"

        if caller_frame:
            module = inspect.getmodule(caller_frame)
            if module:
                caller_module = module.__name__
            caller_function = caller_frame.f_code.co_name

        logger.error(
            f"Failed to get instance '{key}' via convenience function from {caller_module}.{caller_function}: {str(e)}")
        raise


def has_instance(key: str) -> bool:
    """Check if an instance exists"""
    try:
        return InstanceRegistry.has(key)

    except Exception as e:
        # Get caller information
        caller_frame = inspect.currentframe().f_back
        caller_module = "unknown"
        caller_function = "unknown"

        if caller_frame:
            module = inspect.getmodule(caller_frame)
            if module:
                caller_module = module.__name__
            caller_function = caller_frame.f_code.co_name

        logger.error(
            f"Failed to check instance '{key}' existence via convenience function from {caller_module}.{caller_function}: {str(e)}")
        raise


# Additional utility function with error-only logging
def safe_get_instance(key: str, default=None):
    """Safely get an instance with a default value"""
    try:
        return get_instance(key)

    except KeyError:
        # Get caller information
        caller_frame = inspect.currentframe().f_back
        caller_module = "unknown"
        caller_function = "unknown"

        if caller_frame:
            module = inspect.getmodule(caller_frame)
            if module:
                caller_module = module.__name__
            caller_function = caller_frame.f_code.co_name

        logger.error(
            f"Instance '{key}' not found, using default value for {caller_module}.{caller_function}")
        return default
    except Exception as e:
        # Get caller information
        caller_frame = inspect.currentframe().f_back
        caller_module = "unknown"
        caller_function = "unknown"

        if caller_frame:
            module = inspect.getmodule(caller_frame)
            if module:
                caller_module = module.__name__
            caller_function = caller_frame.f_code.co_name

        logger.error(
            f"Unexpected error getting instance '{key}' from {caller_module}.{caller_function}: {str(e)}")
        return default
