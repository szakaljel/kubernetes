from os import environ


def get_env_var(prefix, name, default=None, raise_ex=False):
    normalized_name = f'{prefix}_{name}'.upper()
    try:
        return environ[normalized_name]
    except KeyError:
        if raise_ex:
            raise RuntimeError(f'environment variable {normalized_name} does not exist')
        return default
