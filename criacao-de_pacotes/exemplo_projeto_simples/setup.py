from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="exemplo_projeto_simples",
    version="0.0.1",
    author="Claudio ES Andrade",
    author_email="claudioe.s.andrade@gmail.com",
    description="Exemplo de criação de um simples projeto para o pacote PIP",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/claudio-es-andrade/jornada_python/criacao_de_pacotes"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.0',
)