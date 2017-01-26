import pytest
from django_dynamic_fixture import G

from silver.models import (Transaction, Proforma, Invoice, Customer,
                           PaymentProcessorManager)
from silver_payu.models import PayUPaymentMethod


@pytest.fixture
def customer():
    return G(Customer, currency='RON', address_1='9', address_2='9',
             sales_tax_number=0)


@pytest.fixture
def payment_processor():
    return PaymentProcessorManager.get_instance('payu_triggered')


@pytest.fixture
def payment_processor_recurring():
    return PaymentProcessorManager.get_instance('payu_recurring')



@pytest.fixture
def payment_method(customer, payment_processor):
    return G(PayUPaymentMethod, customer=customer,
             payment_processor=payment_processor)


@pytest.fixture
def proforma(customer):
    return G(Proforma, state=Invoice.STATES.ISSUED, customer=customer,
             transaction_currency='RON')

@pytest.fixture
def invoice(customer, proforma):
    return G(Invoice, proforma=proforma, state=Invoice.STATES.ISSUED,
             customer=customer, transaction_currency='RON')

@pytest.fixture
def transaction(customer, payment_processor, payment_method, proforma, invoice):
    return G(Transaction, invoice=invoice, proforma=proforma, currency='RON',
             amount=invoice.total, payment_method=payment_method)


@pytest.fixture
def transaction_recurring(customer, payment_processor_recurring,
                          payment_method, proforma, invoice):
    return G(Transaction, invoice=invoice, proforma=proforma, currency='RON',
             amount=invoice.total, payment_method=payment_method)