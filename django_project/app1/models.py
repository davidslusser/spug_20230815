from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel


class Brand(HandyHelperBaseModel):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name

    def disable(self):
        """disable this brand and all of its products"""
        self.enabled = False
        self.product_set.update(enabled=False)
        self.save()

    def get_absolute_url(self) -> str:
       return reverse("app1:detail_brand", kwargs={"pk": self.pk})



class Manufacturer(HandyHelperBaseModel):
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

  #  def get_absolute_url(self) -> str:
  #      return reverse("app1:detail_manufacturer", kwargs={"pk": self.pk})



class Product(HandyHelperBaseModel):
    sku = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, blank=True, null=True)
    # attributes = models.ManyToManyField("ProductAttribute", blank=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.sku

   # def get_absolute_url(self) -> str:
   #     return reverse("app1:detail_product", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.pk:
            if Product.objects.count() < 1:
                self.sku = "SKU-" + "1".zfill(8)
            else:
                self.sku = "SKU-" + str(Product.objects.count() + 1).zfill(8)
        super(Product, self).save(*args, **kwargs)


# register models with auditlog
# auditlog.register(MyModel)