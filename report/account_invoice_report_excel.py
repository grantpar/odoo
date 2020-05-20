from odoo import models, fields, api


class InvoiceXLS(models.AbstractModel):
    _name = 'report.account.report_invoice_with_payments_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format(
            {'font_size': 10, 'bold': True})
        format2 = workbook.add_format(
            {'font_size': 10, })
        format3 = workbook.add_format(
            {'font_size': 10, })
        format3.set_align('right')
        sheet = workbook.add_worksheet('Invoice Report')
        sheet.set_column(5, 5, 7)
        sheet.set_column(6, 6, 10)
        sheet.set_row(4, 19)

        # header
        #sheet.write(2, 1, lines.partner_id.name, format1)
        sheet.write(1, 2, 'Customer Name(TEMP)', format1)
        sheet.write(3, 2, 'Customer City(TEMP)', format2)
        #sheet.write(4, 1, lines.partner_id.city, format2)
        # sheet.write(2, 9, lines.invoice_date, format2)
        sheet.write(1, 8, '02/05/2019', format3)
        # items
        sheet.write(16, 1, '891121', format2)
        sheet.write(16, 2, 'CRATE mate', format1)
        sheet.write(17, 2, 'Gazlite Mate LPG - 230 grams', format2)
        sheet.write(18, 2, 'Gazlite Canister - 230 grams', format2)
        # pcs
        sheet.write(5, 5, '5,000', format3)
        sheet.write(6, 5, '5,000', format3)
        sheet.write(7, 5, '5,000', format3)
        sheet.write(8, 5, '5,000', format3)
        sheet.write(9, 5, '5,000', format3)
        sheet.write(10, 5, '5,000', format3)
        sheet.write(11, 5, '5,000', format3)
        sheet.write(12, 5, '5,000', format3)
        sheet.write(13, 5, '50', format3)
        sheet.write(14, 5, '5,000', format3)
        sheet.write(15, 5, '5,000', format3)
        sheet.write(16, 5, '5,000', format3)
        sheet.write(17, 5, '5,000', format3)
        sheet.write(18, 5, '200', format3)
        # unit price
        sheet.write(5, 6, '5,000.00', format3)
        sheet.write(6, 6, '5,000.00', format3)
        sheet.write(7, 6, '5,000.00', format3)
        sheet.write(8, 6, '5,000.00', format3)
        sheet.write(9, 6, '5,000.00', format3)
        sheet.write(10, 6, '5,000.00', format3)
        sheet.write(11, 6, '5,000.00', format3)
        sheet.write(12, 6, '5,000.00', format3)
        sheet.write(13, 6, '50.00', format3)
        sheet.write(14, 6, '5,000.00', format3)
        sheet.write(15, 6, '5,000.00', format3)
        sheet.write(16, 6, '5,000.00', format3)
        sheet.write(17, 6, '200.00', format3)
        sheet.write(18, 6, '5,000.00', format3)
        # total price
        sheet.write(5, 8, '15,000.00', format3)
        sheet.write(6, 8, '15,000.00', format3)
        sheet.write(7, 8, '15,000.00', format3)
        sheet.write(8, 8, '15,000.00', format3)
        sheet.write(9, 8, '15,000.00', format3)
        sheet.write(10, 8, '15,000.00', format3)
        sheet.write(11, 8, '15,000.00', format3)
        sheet.write(12, 8, '15,000.00', format3)
        sheet.write(13, 8, '15,000.00', format3)
        sheet.write(14, 8, '15,000.00', format3)
        sheet.write(15, 8, '15,000.00', format3)
        sheet.write(16, 8, '15,000.00', format3)
        sheet.write(17, 8, '15,000.00', format3)
        sheet.write(18, 8, '15,000.00', format3)

        # calculations
        sheet.write(20, 1, 'TRADE DISCOUNT', format2)
        sheet.write(25, 1, lines.narration, format2)
        #sheet.write(23, 2, lines.amount_untaxed, format2)
        sheet.write(22, 4, '133.93', format3)  # vatablesales
        sheet.write(25, 4, '16.07', format3)  # vat amount
        # sheet.write(26, 2, lines.amount_total, format2)
        sheet.write(22, 8, '150.00', format3)  # total sales
        sheet.write(23, 8, '16.07', format3)  # less vat
        # sheet.write(27, 9, lines.amount_untaxed, format2)
        # sheet.write(30, 9, lines.amount_untaxed, format2)
        sheet.write(24, 8, '133.93', format3)  # amt net of vat
        sheet.write(26, 8, '1,113,003.93', format3)  # amount due
        sheet.write(27, 8, '16.07', format3)  # ADD VAT
        # sheet.write(33, 9, lines.amount_total, format2)
        sheet.write(29, 8, '1,115,000.00', format3)  # total amount due
        sheet.write(23, 1, 'DR 525', format2)

        # footer
        sheet.write(30, 1, lines.invoice_user_id.name, format3)
        sheet.write(30, 3, 'RMD', format3)
        sheet.write(30, 5, 'REY DAVID', format3)
