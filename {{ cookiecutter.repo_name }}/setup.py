from setuptools import setup, find_namespace_packages

setup(
    name='{{ "conny-ml-" + cookiecutter.package_name.replace(" ", "-").replace("_", "-") }}',
    package_dir={'':'src'},
    packages=find_namespace_packages(include=['conny_ml.*', '{{ "conny_ml." +  cookiecutter.package_name.replace(" ", "_").replace("-", "_") + ".*" }}']),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
)
