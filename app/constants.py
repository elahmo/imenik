from .providers import bhtelecom, eronet, mtel

BHT = bhtelecom
ERONET = eronet
MTEL = mtel

# chose providers in order of most likely
AREA_CODE_MAPPINGS = {
    "060": [BHT],
    "061": [BHT],
    "062": [BHT],
    "063": [ERONET],
    "064": [ERONET],
    "065": [MTEL],
    "066": [MTEL],
    "067": [MTEL],
    "0702": [BHT],
    "030": [BHT],
    "031": [BHT],
    "032": [BHT],
    "033": [BHT],
    "034": [ERONET, BHT],
    "035": [BHT],
    "036": [ERONET, BHT],
    "037": [BHT],
    "038": [BHT],
    "039": [ERONET, BHT],
    "049": [MTEL],
    "050": [MTEL],
    "051": [MTEL],
    "052": [MTEL],
    "053": [MTEL],
    "054": [MTEL],
    "055": [MTEL],
    "056": [MTEL],
    "057": [MTEL],
    "058": [MTEL],
    "059": [MTEL],
}
