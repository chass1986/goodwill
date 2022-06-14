from django.db import models


class OrgUnit(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='parent', related_name='children', blank=True, null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=55, null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name} - {self.type}"


kinds = (
    ('FRCANT', 'FRCANT'),
    ('FRCOMM', 'FRCOMM'),
    ('FREPCI', 'FREPCI'),
    ('FRDEPA', 'FRDEPA'),
    ('FRPAYS', 'FRPAYS'),
    ('FRREGI', 'FRREGI'),

)


class Territories(models.Model):
    id = models.BigIntegerField(auto_created=False, primary_key=True, serialize=False, verbose_name='ID'),
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='parent',
        blank=True,
        null=True
    )
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=150, blank=True, null=True)
    kind = models.CharField(choices=kinds, max_length=15, db_index=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_current = models.BooleanField()
    population = models.BigIntegerField(blank=None, null=True)
    official_website_url = models.URLField(blank=True, null=True)
    articles_count = models.BigIntegerField(default=0)
    admin_docs_count = models.BigIntegerField(default=0)
    impacters_count = models.BigIntegerField(default=0)
    websites_count = models.BigIntegerField(default=0)
    sources_count = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name
