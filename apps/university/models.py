from django.db import models

DEGREE = (
    (0, "None"),
    (1, "Bachelor"),
    (2, "Magister"),
    (3, "Doctoral"),
)

STATUS = (
    (0, "New"),
    (1, "Process"),
    (2, "Finished"),
    (3, "Canceled"),
)


class OTM(models.Model):
    class Meta:
        verbose_name = "OTM"
        verbose_name_plural = "OTM-lar"

    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Parent Category',
                                        limit_choices_to={'is_active': True, 'parent_category__isnull': True},
                                        related_name='children', null=True, blank=True, )
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
