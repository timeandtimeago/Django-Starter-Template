# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_django_superuser]
import os

# from django.contrib.auth.models import User
from django.db import migrations
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps

import google.auth
from google.cloud import secretmanager
from django.contrib.auth import get_user_model
from app.config import AppConfig

User = get_user_model()



def createsuperuser(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    """
    Dynamically create an admin user as part of a migration
    Password is pulled from Secret Manger (previously created as part of tutorial)
    """
    if AppConfig.LOCAL_DEV:
        # We are in CI, so just create a placeholder user for unit testing.
        admin_password = AppConfig.DEFAULT_LOCAL_DEV_SUPERUSER_PASSWORD
        admin_email = AppConfig.DEFAULT_SUPERUSER_EMAIL
    else:
        client = secretmanager.SecretManagerServiceClient()

        # Get project value for identifying current context
        _, project = google.auth.default()

        # Retrieve the previously stored admin password
        name = AppConfig.DEFAULT_SUPERUSER_PASSWORD_SECRET_PATH
        admin_password = client.access_secret_version(name=name).payload.data.decode(
            "UTF-8"
        )
        admin_email = AppConfig.DEFAULT_SUPERUSER_EMAIL

    # Create a new user using acquired password, stripping any accidentally stored newline characters
    User.objects.create_superuser(admin_email, password=admin_password.strip())


class Migration(migrations.Migration):

    initial = True
    dependencies = [('BaseUser', '0001_initial'),]
    operations = [migrations.RunPython(createsuperuser)]


# [END cloudrun_django_superuser]