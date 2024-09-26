# models/master_ruangan.py
from odoo import models, fields

class MasterRuangan(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    name = fields.Char(string="Nama Ruangan", required=True)
    tipe_ruangan = fields.Selection([
        ('kecil', 'Meeting Room Kecil'),
        ('besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string="Tipe Ruangan", required=True)
    lokasi = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')
    ], string="Lokasi Ruangan", required=True)
    foto = fields.Binary(string="Foto Ruangan", required=True)
    kapasitas = fields.Integer(string="Kapasitas Ruangan", required=True)
    keterangan = fields.Text(string="Keterangan")