"""Get the proverbios from the wikiquote page."""
from dataclasses import dataclass
from json import dumps as json_dumps
from requests import Response, get as requests_get
from bs4 import BeautifulSoup


@dataclass(frozen=True)
class Proverbio:
    """Create a proverbio object with the portuguese saying and the source."""

    proverbio: str
    source: str


def clean_proverbio(probervio_raw: str) -> Proverbio:
    """Clean the proverbio object."""
    saying, source = probervio_raw.split("[")
    saying = saying.strip().removesuffix('"').removeprefix('"')
    source = SOURCES[source[:-1]]

    return Proverbio(saying, source)


SOURCES: dict[str, str] = {
    "Note 1": "ROLLAND, Francisco, Typ. Rollandiana, Lisboa. Publicado em 1780.",
    "Note 2": "LOPES, Filipe Vasques do Nascimento Neto, UL-Faculdade de Direito. Publicado em 2017.(https://repositorio.ul.pt/bitstream/10451/31719/1/ulfd133977_tese.pdf)",
    "Note 3": "ALMEIDA, José João, Universidade do Minho. Publicado em 22 de Março de 2020. (https://natura.di.uminho.pt/~jj/pln/calao/dicionario.pdf)",
    "Note 4": "CECIRFAFE. Publicado em maio de 2002.(https://www.cercifaf.org.pt/mosaico.edu/1c/proverb1.txt)",
}


def write_list_obj_to_yaml(obj: list[Proverbio], file_name: str) -> None:
    """Write the object to a yaml file."""
    with open(file_name, "w", encoding="utf-8") as file_handler:
        file_handler.write(
            json_dumps(
                [obj.__dict__ for obj in proverbios], indent=4, ensure_ascii=False
            )
        )


if __name__ == "__main__":
    page: Response = requests_get(
        "https://pt.wikiquote.org/wiki/Prov%C3%A9rbios_portugueses", timeout=5
    )
    soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")

    proverbios_raw: list[str] = list(
        filter(
            lambda x: x.endswith("]"),
            map(lambda x: x.text, soup.select(".mw-parser-output > ul > li")),
        )
    )

    proverbios: list[Proverbio] = list(map(clean_proverbio, proverbios_raw))

    write_list_obj_to_yaml(proverbios, "proverbios.json")
