from django.db import models
from taskite.models.base import BaseTimestampModel


class Task(BaseTimestampModel):
    class Priority(models.TextChoices):
        URGENT = ("urgent", "Urgent")
        HIGH = ("high", "High")
        MEDIUM = ("medium", "Medium")
        LOW = ("low", "Low")
        NONE = ("none", "None")

    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="project_tasks"
    )
    state = models.ForeignKey(
        "State", on_delete=models.CASCADE, related_name="state_tasks"
    )
    task_id = models.CharField(max_length=10, blank=True, editable=False)
    name = models.TextField(max_length=512)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(
        max_length=20, choices=Priority.choices, default=Priority.NONE
    )
    start_date = models.DateField(blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    order = models.FloatField(default=50000, blank=True, editable=False)
    sequence = models.IntegerField(default=1, blank=True, editable=False)

    archived_at = models.DateTimeField(blank=True, null=True)

    assignees = models.ManyToManyField(
        "User", through="TaskAssignee", related_name="tasks"
    )
    labels = models.ManyToManyField("Label", through="TaskLabel", related_name="tasks")

    class Meta:
        db_table = "tasks"
        ordering = ("-created_at",)
        constraints = [
            models.UniqueConstraint(
                fields=["project_id", "task_id"],
                name="unique_project_task_identifier",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} <{self.project.name}>"

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_sequence = (
                Task.objects.filter(project=self.project)
                .aggregate(largest=models.Max("sequence"))
                .get("largest")
            )
            if last_sequence is not None:
                self.sequence = last_sequence + 1

            self.task_id = f"{self.project.project_id}-{self.sequence}"

            last_order = (
                Task.objects.filter(project=self.project, state=self.state)
                .aggregate(largest=models.Max("order"))
                .get("largest")
            )
            if last_order is not None:
                self.order = last_order + 10000
        return super().save(*args, **kwargs)


class TaskAssignee(BaseTimestampModel):
    task = models.ForeignKey(
        "Task", on_delete=models.CASCADE, related_name="task_assignees"
    )
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="user_task_assignees"
    )

    class Meta:
        db_table = "task_assignees"
        verbose_name = "Task Assignee"
        verbose_name_plural = "Task Assignees"
        constraints = [
            models.UniqueConstraint(
                fields=["task_id", "user_id"], name="unique_task_assignees"
            )
        ]
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.task.name} <{self.user.email}>"


class TaskLabel(BaseTimestampModel):
    task = models.ForeignKey("Task", on_delete=models.CASCADE, related_name="task_labels")
    label = models.ForeignKey(
        "Label", on_delete=models.CASCADE, related_name="label_task_labels"
    )

    class Meta:
        db_table = "task_labels"
        verbose_name = "Task Label"
        verbose_name_plural = "Task Labels"
        constraints = [
            models.UniqueConstraint(
                fields=["task_id", "label_id"], name="unique_task_label"
            )
        ]