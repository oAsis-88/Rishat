from django import forms

from PaySys.models import *


class OrderItemsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderItemsForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(quantity__gt=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        item = cleaned_data.get('item')
        order = cleaned_data.get('order')
        count = cleaned_data.get('count')

        if item:
            quantity_items = item.quantity
            if not count:
                raise forms.ValidationError(f"Вы не указали кол-во товара '{item.name}', max: {quantity_items} pcs.")

            if count > quantity_items:
                raise forms.ValidationError(f"You have exceeded number limit {item.name}. Max: {quantity_items} pcs.")

            if order:
                exists_item_in_order = OrderItems.objects.filter(item_id=item.id, order_id=order.id)
                if exists_item_in_order:
                    raise forms.ValidationError(f"{item.name} уже добавлен в '{order.name}'")


    class Meta:
        model = OrderItems
        fields = ('item', 'order', 'count', )


