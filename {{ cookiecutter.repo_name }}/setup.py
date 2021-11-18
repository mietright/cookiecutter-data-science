from setuptools import setup, find_namespace_packages
from pathlib import Path


def parse_requirements():
    def remove_non_reqs(line):
        return not (line.startswith("#") or line.startswith("-e")) and bool(line)

    reqs_file = list(Path(__file__).resolve().parent.glob("requirements.txt"))
    if reqs_file:
        reqs = reqs_file[0].read_text().split("\n")
        reqs = list(filter(remove_non_reqs, reqs))
        return reqs

    return []


setup(
    name='{{ "conny-ml-" + cookiecutter.package_name.replace(" ", "-").replace("_", "-") }}',
    packages=find_namespace_packages(include=['conny_ml.*']),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    install_requires=parse_requirements()
)
