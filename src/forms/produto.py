from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import DecimalField, IntegerField

from wtforms.fields.simple import StringField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange


class ProdutoForm(FlaskForm):
    nome = StringField(label="Nome do Produto",
                       validators=[InputRequired(message="É obrigatório definir o nome do produto")
                                   Length(max=100,
                                          message="O produto pode ter até 100 caracteres")])
    preco = DecimalField(label="Preço", places=2,
                         validators=[InputRequired(message="É obrigatírio definir o preço"),
                                     numberRange(min=0.00,
                                                 message="Os preços devem ser positivos")])

    estoque = IntegerField(label="Estoque",
                           validators=[InputRequired(message="É preciso definir o estoque"),
                                       NumberRange(min=0,
                                                   message="O estoque precisa ser positivo")])

    ativo = BooleanField(label="Ativo?",
                         validators=[InputRequired(message="É preciso dizer se o produto"
                                                   "está o ou não ativo")])
    foto = FileField(label="Foto do produto",
                     validators=['jpg', 'png'(message="Apenas arquivos JPG ou PNG")])

    categoria = SelectField(label="Categoria do produto",
                            validators=['jpg', 'png'(message="Selecine uma categoria")])
    submit = SubmitField()