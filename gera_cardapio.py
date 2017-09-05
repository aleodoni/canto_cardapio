import os
from jinja2 import Environment, FileSystemLoader
from classes import Refeicao
 
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)
 
 
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
 
def create_index_html():
    fname = "output.html"
    mes = "setembro"
    aniversario = "29/09 (sexta-feira)"
    cardapio = []
    semana1 = [
        Refeicao('', '', '', '', ''), 
        Refeicao('', '', '', '', ''), 
        Refeicao('', '', '', '', ''), 
        Refeicao('', '', '', '', ''), 
        Refeicao(
            '01/09', 
            'Bolacha doce ou salgada, Chá de Camomila, Fruta', 
            'Arroz, Feijão, Peixe assado, Purê de batata, Salada, Suco de laranja', 
            'Fruta, Broinha de fubá, Suco', 
            'Sopa de batata com carne'
        )
    ]
    semana2 = [
        Refeicao(
            '04/09', 
            'Pão com doce, Fruta, Leite com chocolate', 
            'Arroz, Feijão, Macarrão a bolonhesa, abobrinha refogada, Salada de couve, Suco de limão', 
            'Fruta, Bolo de milho com coco, Chá Mate', 
            'Sopa de legumes com carne'
        ), 
        Refeicao(
            '05/09', 
            'Bolo de Milho com coco, Fruta, Chá de Erva Doce ', 
            'Arroz integral, Feijão, Frango ao molho, Polenta cremosa, Salada de beterraba cozida, Suco de maracujá', 
            'Fruta, Bolo de pão de queijo, Suco de laranja ', 
            'Creme de fubá com frango'
        ), 
        Refeicao(
            '06/09', 
            'Bolacha Salgada, Cereal com leite ou iogurte, Fruta, Chá de Maça', 
            'Arroz, Lentilha, Carne em tirinhas, Brócolis refogado, Salada de cenoura ralada, Suco de laranja', 
            'Fruta, Biscoito caseiro, Vitamina de banana', 
            'Sopa de lentilha'
        ), 
        Refeicao(
            '07/09', 
            'FERIADO', 
            'FERIADO', 
            'FERIADO', 
            'FERIADO' 
        ), 
        Refeicao(
            '08/09', 
            'FERIADO', 
            'FERIADO', 
            'FERIADO', 
            'FERIADO'
        ), 
    ]

    semana3 = [
        Refeicao(
            '11/09', 
            'Mingau de aveia, Bolacha doce ou salgada, Fruta, Chá de Hortelã', 
            'Arroz, Feijão, Omelete assado com legumes, Salada de alface, Suco de laranja', 
            'Fruta, Bolo integral de cenoura, Chá de Erva-cidreira', 
            'Sopa de legumes com carne'
        ), 
        Refeicao(
            '12/09', 
            'Bolo integral de cenoura, Fruta, Leite com chocolate ', 
            'Arroz, Feijão, Nuggets de frango caseiro assado, Macarrão penne ao molho branco, Salada de repolho cozido, Suco de maracujá', 
            'Fruta, Torta salgada de legumes com frango, Suco de laranja', 
            'Canja de Galinha'
        ), 
        Refeicao(
            '13/09', 
            'Pão de leite com manteiga e queijo, Fruta, Chá de Maçã', 
            'Arroz, Lentilha, Estrogonofe de carne, batata assada em rodelas, Acelga refogada, Salada de alface roxa, Suco de limão', 
            'Fruta, Bolo de aveia, Suco de abacaxi', 
            'Creme de lentilha com carne'
        ), 
        Refeicao(
            '14/09', 
            'Bolo de aveia, Fruta, Leite com chocolate ', 
            'Arroz, Feijão, Panqueca de espinafre com carne, abóbora refogada, Salada de tomate, Suco de abacaxi', 
            'Fruta, Pão de leite com queijo, presunto e tomate, Suco de maracujá', 
            'Sopa de abóbora' 
        ), 
        Refeicao(
            '15/09', 
            'Bolacha doce ou salgada, Chá Mate', 
            'Arroz, Feijão, Tirinhas de peixe, farofinha de ervilha, Salada de chuchu, Suco de laranja', 
            'Fruta, Bolo de maracujá, Suco de limão', 
            'Creme de ervilha'
        ), 
    ]

    semana4 = [
        Refeicao(
            '18/09', 
            'Bolacha doce ou salgada, Fruta, Chá de Maçã', 
            'Arroz, Feijão, Carne moída ao molho, espaguete, Salada de acelga, Suco de limão', 
            'Fruta, Bolo de limão, Suco de maracujá', 
            'Creme de legumes com arroz'
        ), 
        Refeicao(
            '19/09', 
            'Pão de leite com requeijão ou manteiga, Fruta, Leite com chocolate', 
            'Arroz, Feijão, Fricassê de frango, berinjela refogada, Salada de pepino, Suco de laranja', 
            'Lanche Comunitário', 
            'Sopa de frango com aveia'
        ), 
        Refeicao(
            '20/09', 
            'Bolacha Salgada, Cereal com leite ou iogurte, Fruta, Chá de Erva-cidreira', 
            'Arroz, Grão de bico, Carne de panela com cenoura e repolho, Salada de tomate, Suco de maracujá', 
            'Fruta, Gelatina, Bolacha salgada, Vitamina de mamão, maça e banana', 
            'Sopa de grão de bico com carne'
        ), 
        Refeicao(
            '21/09', 
            'Pão com queijo, Fruta, Leite com chocolate', 
            'Arroz, Feijão, Bife de fígado, Purê de batatas, Salada de beterraba ralada, Suco de abacaxi', 
            'Fruta, Pão com patê de cenoura, Suco de laranja', 
            'Sopa de feijão com macarrão' 
        ), 
        Refeicao(
            '22/09', 
            'Bolacha doce ou salgada, Chá de Camomila', 
            'Arroz, Feijão, Peixe ao molho com leite de coco, batata doce assada, Salada, Suco de limão', 
            'Fruta, Quibe assado com aveia, Suco de abacaxi', 
            'Sopa de batata com carne'
        ), 
    ]

    semana5 = [
        Refeicao(
            '25/09', 
            'Bolacha doce ou salgada, Fruta, Chá de Maçã', 
            'Arroz, Feijão, Ovos mexidos, legumes assados ao molho branco, Salada de tomate, Suco de abacaxi', 
            'Fruta, Bolo de banana com aveia, Suco de laranja ', 
            'Sopa de legumes com arroz'
        ), 
        Refeicao(
            '26/09', 
            'Bolo de banana com aveia, Fruta, Leite com chocolate', 
            'Arroz, Feijão, Sobrecoxa assada, creme de milho, Salada de abobrinha, Suco de laranja', 
            'Fruta, Torta de pão, Suco de abacaxi', 
            'Canja de galinha'
        ), 
        Refeicao(
            '27/09', 
            'Bolacha Salgada, Cereal com leite ou iogurte, Fruta, Chá de Maçã', 
            'Arroz, Lentilha, Músculo cozido, Suflê de couve-flor, Salada de alface crespa, Suco de maracujá', 
            'Fruta, Pudim, Chá de maçã com canela', 
            'Creme de lentilha com carne'
        ), 
        Refeicao(
            '28/09', 
            'Pão com queijo, Fruta, Leite com chocolate', 
            'Arroz, Feijão, Tirinhas de fígado acebolada, Bolinho de arroz assado, Salada de pepino, Suco de limão', 
            'Fruta, Pão com patê de frango com tomate, Suco de maracujá', 
            'Sopa de feijão' 
        ), 
        Refeicao(
            '29/09', 
            'Bolacha doce ou salgada, Chá de Camomila', 
            'Arroz, Feijão, Peixe empanado assado, Mandioca cozida, Salada de cenoura cozida, Suco de abacaxi', 
            'Aniversariantes do mês', 
            'Creme de mandioca'
        ), 
    ]
    cardapio.append(semana1)
    cardapio.append(semana2)
    cardapio.append(semana3)
    cardapio.append(semana4)
    cardapio.append(semana5)
    
    print(cardapio)
    context = {
        'mes': mes,
        'aniversario': aniversario,
        'cardapio': cardapio
    }

    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html)
 
 
def main():
    create_index_html()
 
 
if __name__ == "__main__":
    main()