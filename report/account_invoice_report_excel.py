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
        sheet.write(1, 2, lines.partner_id.name, format1)
        # sheet.write(3, 2, lines.partner_id.city, format2)
        # invoicedate = lines.invoice_date.strftime("%m/%d/%Y")
        # sheet.write(1, 8, invoicedate, format2)
        # items
        sheet.write(16, 1, '891121', format2)
        sheet.write(16, 2, 'CRATE mate', format1)
        sheet.write(17, 2, 'Gazlite Mate LPG - 230 grams', format2)
        sheet.write(18, 2, 'Gazlite Canister - 230 grams', format2)

        # for x in lines.line_ids:
        #     if x.name == 'Gaz Lite 330g LPG':
        #         sheet.write(5, 5, x.quantity)
        #         sheet.write(5, 6, x.price_unit)
        #         sheet.write(5, 8, x.price_subtotal)
        #     if x.name == 'Gaz Lite 330g Canister':
        #         sheet.write(6, 5, x.quantity)
        #         sheet.write(6, 6, x.price_unit)
        #         sheet.write(6, 8, x.price_subtotal)
        #     if x.product_id == 'Eazy Kalan Stove (Red)':
        #         sheet.write(7, 5, x.quantity)
        #         sheet.write(7, 6, x.price_unit)
        #         sheet.write(7, 8, x.price_subtotal)
        #     if x.name == 'Eazy Kalan Stove (Blue)':
        #         sheet.write(8, 5, x.quantity)
        #         sheet.write(8, 6, x.price_unit)
        #         sheet.write(8, 8, x.price_subtotal)
        #     if x.name == 'Eazy Kalan Stove (Choco)':
        #         sheet.write(9, 5, x.quantity)
        #         sheet.write(9, 6, x.price_unit)
        #         sheet.write(9, 8, x.price_subtotal)
        #     if x.name == 'Eazy Kalan Stove (Green)':
        #         sheet.write(10, 5, x.quantity)
        #         sheet.write(10, 6, x.price_unit)
        #         sheet.write(10, 8, x.price_subtotal)
        #     if x.name == 'Eazy Kalan Stove (Yellow)':
        #         sheet.write(11, 5, x.quantity)
        #         sheet.write(11, 6, x.price_unit)
        #         sheet.write(11, 8, x.price_subtotal)
        #     if x.name == 'Eazy Kalan Stove (White)':
        #         sheet.write(12, 5, x.quantity)
        #         sheet.write(12, 6, x.price_unit)
        #         sheet.write(12, 8, x.price_subtotal)
        #     if x.name == 'Torch':
        #         sheet.write(14, 5, x.quantity)
        #         sheet.write(14, 6, x.price_unit)
        #         sheet.write(14, 8, x.price_subtotal)
        #     if x.name == 'Gaz Lite 230g LPG':
        #         sheet.write(17, 5, x.quantity)
        #         sheet.write(17, 6, x.price_unit)
        #         sheet.write(17, 8, x.price_subtotal)
        #     if x.name == 'Gaz Lite 230g Canister':
        #         sheet.write(18, 5, x.quantity)
        #         sheet.write(18, 6, x.price_unit)
        #         sheet.write(18, 8, x.price_subtotal)

        # calculations
        sheet.write(20, 1, 'TRADE DISCOUNT', format2)
        # POSORISDR = lines.narration.split(',')
        # sheet.write(22, 1, POSORISDR[0])
        # sheet.write(23, 1, POSORISDR[1])
        # sheet.write(24, 1, POSORISDR[2])
        # sheet.write(25, 1, POSORISDR[3])
        # sheet.write(22, 4, lines.amount_untaxed, format3)  # vatablesales
        # sheet.write(25, 4, lines.amount_tax, format3)  # vat amount
        # sheet.write(22, 8, lines.amount_total, format3)  # total sales
        # sheet.write(23, 8, lines.amount_tax, format3)  # less vat
        # sheet.write(24, 8, lines.amount_untaxed, format3)  # amt net of vat
        # sheet.write(26, 8, lines.amount_untaxed, format3)  # amount due
        # sheet.write(27, 8, lines.amount_tax, format3)  # ADD VAT
        # sheet.write(29, 8, lines.amount_total, format3)  # total

        # footer
        sheet.write(30, 1, lines.invoice_user_id.name, format3)
        sheet.write(30, 3, 'RMD', format3)
        sheet.write(30, 5, 'REY DAVID', format3)
