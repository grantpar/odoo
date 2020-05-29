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
        sheet.write(3, 2, lines.partner_id.name, format2)  # temporary
        sheet.write(1, 8, lines.invoice_date.strftime("%m/%d/%Y"), format2)

        skuproducts = {'Gaz Lite 330g LPG', 'Gaz Lite 330g Canister', 'Eazy Kalan Stove (Red)', 'Eazy Kalan Stove (Blue)', 'Eazy Kalan Stove (Choco)',
                       'Eazy Kalan Stove (Green)', 'Eazy Kalan Stove (Yellow)', 'Eazy Kalan Stove (White)', 'BBQ Griller', 'Torch', 'Output Tax', lines.name}
        remove2 = slice(-2)

        i = 16
        for x in lines.line_ids[remove2]:
            if x.name == 'Gaz Lite 330g LPG':
                sheet.write(5, 5, x.quantity)
                sheet.write(5, 6, x.price_unit)
                sheet.write(5, 8, x.price_subtotal)
                continue
            if x.name == 'Gaz Lite 330g Canister':
                sheet.write(6, 5, x.quantity)
                sheet.write(6, 6, x.price_unit)
                sheet.write(6, 8, x.price_subtotal)
                continue
            if x.name == 'Eazy Kalan Stove (Red)':
                sheet.write(7, 5, x.quantity)
                sheet.write(7, 6, x.price_unit)
                sheet.write(7, 8, x.price_subtotal)
                continue
            if x.name == 'Eazy Kalan Stove (Blue)':
                sheet.write(8, 5, x.quantity)
                sheet.write(8, 6, x.price_unit)
                sheet.write(8, 8, x.price_subtotal)
                continue
            if x.name == 'Eazy Kalan Stove (Choco)':
                sheet.write(9, 5, x.quantity)
                sheet.write(9, 6, x.price_unit)
                sheet.write(9, 8, x.price_subtotal)
            if x.name == 'Eazy Kalan Stove (Green)':
                sheet.write(10, 5, x.quantity)
                sheet.write(10, 6, x.price_unit)
                sheet.write(10, 8, x.price_subtotal)
                continue
            if x.name == 'Eazy Kalan Stove (Yellow)':
                sheet.write(11, 5, x.quantity)
                sheet.write(11, 6, x.price_unit)
                sheet.write(11, 8, x.price_subtotal)
                continue
            if x.name == 'Eazy Kalan Stove (White)':
                sheet.write(12, 5, x.quantity)
                sheet.write(12, 6, x.price_unit)
                sheet.write(12, 8, x.price_subtotal)
                continue
            if x.name == 'BBQ Griller':
                sheet.write(13, 5, x.quantity)
                sheet.write(13, 6, x.price_unit)
                sheet.write(13, 8, x.price_subtotal)
                continue
            if x.name == 'Torch':
                sheet.write(14, 5, x.quantity)
                sheet.write(14, 6, x.price_unit)
                sheet.write(14, 8, x.price_subtotal)
                continue
            while i < 19:
                if x.name not in skuproducts:
                    sheet.write(i, 2, x.name)
                    sheet.write(i, 5, x.quantity)
                    sheet.write(i, 6, x.price_unit)
                    sheet.write(i, 8, x.price_subtotal)
                    i += 1
                    break

        # calculations
        sheet.write(20, 1, 'TRADE DISCOUNT', format2)
        POSORISDR = lines.narration.split(',')
        sheet.write(22, 1, POSORISDR[0])
        sheet.write(23, 1, POSORISDR[1])
        sheet.write(24, 1, POSORISDR[2])
        sheet.write(25, 1, POSORISDR[3])
        sheet.write(22, 4, lines.amount_untaxed, format3)  # vatablesales
        sheet.write(25, 4, lines.amount_tax, format3)  # vat amount
        sheet.write(22, 8, lines.amount_total, format3)  # total sales
        sheet.write(23, 8, lines.amount_tax, format3)  # less vat
        sheet.write(24, 8, lines.amount_untaxed, format3)  # amt net of vat
        sheet.write(26, 8, lines.amount_untaxed, format3)  # amount due
        sheet.write(27, 8, lines.amount_tax, format3)  # ADD VAT
        sheet.write(29, 8, lines.amount_total, format3)  # total

        # footer
        sheet.write(30, 1, lines.invoice_user_id.name, format3)
        sheet.write(30, 3, 'RMD', format3)
        sheet.write(30, 5, 'REY DAVID', format3)
