# models/pemesanan_ruangan.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string="Nomor Pemesanan", required=True, readonly=True, default=lambda self: self._generate_nomor_pemesanan())
    ruangan_id = fields.Many2one('master.ruangan', string="Ruangan", required=True)
    nama_pemesanan = fields.Char(string="Nama Pemesanan", required=True)
    tanggal_pemesanan = fields.Date(string="Tanggal Pemesanan", required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done')
    ], string="Status Pemesanan", default='draft')
    catatan_pemesanan = fields.Text(string="Catatan Pemesanan")

    @api.model
    def _generate_nomor_pemesanan(self):
        # Generate nomor pemesanan dengan format tertentu
        return self.env['ir.sequence'].next_by_code('pemesanan.ruangan') or '/'

    @api.constrains('ruangan_id', 'tanggal_pemesanan')
    def _check_ruangan_availability(self):
        for record in self:
            existing = self.env['pemesanan.ruangan'].search([
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError("Ruangan sudah dipesan untuk tanggal yang sama.")

    @api.constrains('nama_pemesanan')
    def _check_unique_nama_pemesanan(self):
        if self.search([('nama_pemesanan', '=', self.nama_pemesanan), ('id', '!=', self.id)]):
            raise ValidationError("Nama Pemesanan sudah digunakan.")
