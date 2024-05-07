from apideck.model.bill import Bill
from apideck.model.bill_line_item import BillLineItem
from apideck.model.currency import Currency
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_supplier import LinkedSupplier
from apideck.model.linked_tax_rate import LinkedTaxRate


class BillCreationService:
    @staticmethod
    def create_request() -> Bill:
        return Bill(
            bill_number="BILL-123",
            currency=Currency("EUR"),
            due_date=None,
            sub_total=9.9,
            total_tax=12.28,
            total=12.18,
            status="draft",
            supplier=LinkedSupplier(
                id="10",
                display_name=None,
            ),
            tax_inclusive=True,
            line_items=[
                BillLineItem(
                    total_amount=12.18,
                    type="expense_account",
                    ledger_account=LinkedLedgerAccount(
                        id="111",
                    ),
                    tax_rate=LinkedTaxRate(
                        id="6",
                    ),
                )
            ],
        )
