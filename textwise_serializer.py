from pathlib import Path
from openpecha.serializers import HFMLSerializer


def get_pedurma_text(opf_path, text_id):
    serializer = HFMLSerializer(opf_path, text_id, layers=['Pagination', 'Durchen'])
    serializer.apply_layers()
    pedurma_text = serializer.get_result()
    return pedurma_text


if __name__ == "__main__":
    opf_id = "12d32eb31c1a4cc59741cda99ebc7211"
    opf_path = Path(f'./data/opfs/{opf_id}.opf')
    text_id = "D1119"
    pedurma_text = get_pedurma_text(opf_path, text_id)
    for vol_id, text in pedurma_text.items():
        Path(f'./data/hfmls/{opf_id}/{text_id}_{vol_id}.txt').write_text(text, encoding='utf-8')