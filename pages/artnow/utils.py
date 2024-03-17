from pages.artnow.embroidered_paintings_page import EmbroideredPaintingsPage
from pages.artnow.batic_page import BaticPage
from pages.artnow.jeweller_art_page import JewellerArtPage
from tdata.data_artnow import Section


def get_section_page_class(section_name):
    match section_name:
        case Section.EmbroideredPaintings:
            return EmbroideredPaintingsPage
        case Section.Batic:
            return BaticPage
        case Section.JewellerArt:
            return JewellerArtPage
        case _:
            assert False, \
                f"Page class for section with name {section_name} wasn't found"
