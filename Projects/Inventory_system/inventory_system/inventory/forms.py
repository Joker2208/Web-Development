from django import forms

from .models import Category, Product, StockTransaction


class BootstrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = "form-select" if isinstance(field.widget, forms.Select) else "form-control"
            field.widget.attrs.setdefault("class", css)


class CategoryForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class ProductForm(BootstrapMixin, forms.ModelForm):
    """Quantity is only set when creating a product. After that it changes only through stock movements."""

    class Meta:
        model = Product
        fields = ["name", "sku", "category", "unit_price", "quantity", "reorder_level"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            del self.fields["quantity"]

    def clean_sku(self):
        return self.cleaned_data["sku"].strip().upper()


class StockMovementForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ["product", "movement_type", "quantity", "note"]

    def clean(self):
        data = super().clean()
        product, kind, qty = data.get("product"), data.get("movement_type"), data.get("quantity")
        # Stock control rule: you can never remove more than what is on the shelf.
        if product and kind == StockTransaction.OUT and qty and qty > product.quantity:
            raise forms.ValidationError(
                f"Cannot remove {qty} units of {product.name}: only {product.quantity} in stock."
            )
        return data
