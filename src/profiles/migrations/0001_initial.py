# Generated by Django 4.2.3 on 2023-07-13 10:21

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django_enum.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("promotions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TradingUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all"
                                  " permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer"
                                  ". Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user"
                                  " can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should "
                                  " treated as active. Unselect this"
                                  " instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("avatar", models.CharField(blank=True, max_length=100, null=True)),
                ("login", models.CharField(max_length=30)),
                (
                    "balance",
                    models.DecimalField(decimal_places=10, default=0, max_digits=20),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                (
                    "role",
                    django_enum.fields.EnumCharField(
                        blank=True,
                        choices=[
                            ("admin", "admin"),
                            ("analyst", "analyst"),
                            ("default", "default"),
                        ],
                        default="admin",
                        max_length=7,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to."
                                  " A user will get all permissions"
                                  " granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="promotions.promotion",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name="tradinguser",
            constraint=models.CheckConstraint(
                check=models.Q(("balance__gte", 0)),
                name="balance_greater_or_equals_to_zero",
            ),
        ),
    ]
