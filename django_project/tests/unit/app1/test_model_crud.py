import django
import os
import random
from django.apps import apps
from django.test import TestCase
from model_bakery import baker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


class BrandTests(TestCase):
    """ test CRUD operations on Brand """
    def setUp(self):
        self.model = apps.get_model('app1', 'brand')
        self.to_bake = 'app1.Brand'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, )

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_manufacturer(self):
        """ verify manufacturer (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.manufacturer
        baker.make(self.model.manufacturer.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.manufacturer.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.manufacturer.field.related_model.objects.all())
        setattr(row, 'manufacturer', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'manufacturer'), updated_value)
        self.assertNotEqual(getattr(row, 'manufacturer'), original_value)
    
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    

class ManufacturerTests(TestCase):
    """ test CRUD operations on Manufacturer """
    def setUp(self):
        self.model = apps.get_model('app1', 'manufacturer')
        self.to_bake = 'app1.Manufacturer'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, )

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    

class ProductTests(TestCase):
    """ test CRUD operations on Product """
    def setUp(self):
        self.model = apps.get_model('app1', 'product')
        self.to_bake = 'app1.Product'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, )

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_brand(self):
        """ verify brand (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.brand
        baker.make(self.model.brand.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.brand.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.brand.field.related_model.objects.all())
        setattr(row, 'brand', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'brand'), updated_value)
        self.assertNotEqual(getattr(row, 'brand'), original_value)
    
    def test_update_description(self):
        """ verify description (CharField) can be updated """
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=['description']).description
        setattr(row, 'description', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'description'), updated_value)
        self.assertNotEqual(getattr(row, 'description'), original_value)
    

