# -*- coding: utf-8 -*-
#app/device/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField, DecimalField, FileField, IntegerField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import HiddenInput
import datetime

from ..models import Device
from .. import _
from ..forms import NonValidatingSelectFields
from . import get_ra_docs, get_photo_docs, get_manual_docs, get_safety_information_docs


class EditForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.risk_analysis.choices = zip(get_ra_docs(), get_ra_docs())
        self.photo.choices = zip(get_photo_docs(), get_photo_docs())
        self.manual.choices = zip(get_manual_docs(), get_manual_docs())
        self.safety_information.choices = zip(get_safety_information_docs(), get_safety_information_docs())
        self.category.choices = zip(Device.Category.get_list(), Device.Category.get_list())

    category = SelectField(_(u'Category'), validators=[DataRequired()])
    brand = StringField(_(u'Brand'), validators=[DataRequired()])
    type = StringField(_(u'Type'), validators=[DataRequired()])
    power = DecimalField(_(u'Power'), default=0.0)
    ce = BooleanField(_(u'CE'))
    risk_analysis = NonValidatingSelectFields('Risk Analyis')
    photo = NonValidatingSelectFields('Photo')
    manual = NonValidatingSelectFields('Manual')
    safety_information = NonValidatingSelectFields('Safety Information')
    id = IntegerField(widget=HiddenInput())

class AddForm(EditForm):
    """
    Add an asset
    """

class ViewForm(FlaskForm):
    category = StringField(_(u'Category'), render_kw={'readonly':''})
    brand = StringField(_(u'Brand'), render_kw={'readonly':''})
    type = StringField(_(u'Type'), render_kw={'readonly':''})
    power = DecimalField(_(u'Power'), render_kw={'readonly':''})
    ce = BooleanField(_(u'CE'), render_kw={'readonly':''})
    risk_analysis = StringField('Risk Analyis', render_kw={'readonly':''})
    photo = StringField('Photo', render_kw={'readonly':''})
    manual = StringField('Manual', render_kw={'readonly':''})
    safety_information = StringField('Safety Information', render_kw={'readonly':''})
    id = IntegerField(widget=HiddenInput(), render_kw={'readonly':''})
