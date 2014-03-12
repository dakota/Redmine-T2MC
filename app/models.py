# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Attachments(models.Model):
    id = models.IntegerField(primary_key=True)
    container_id = models.IntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=30, blank=True)
    filename = models.CharField(max_length=255)
    disk_filename = models.CharField(max_length=255)
    filesize = models.IntegerField()
    content_type = models.CharField(max_length=255, blank=True)
    digest = models.CharField(max_length=40)
    downloads = models.IntegerField()
    author_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    disk_directory = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'attachments'

class AuthSources(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    host = models.CharField(max_length=60, blank=True)
    port = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=255, blank=True)
    account_password = models.CharField(max_length=255, blank=True)
    base_dn = models.CharField(max_length=255, blank=True)
    attr_login = models.CharField(max_length=30, blank=True)
    attr_firstname = models.CharField(max_length=30, blank=True)
    attr_lastname = models.CharField(max_length=30, blank=True)
    attr_mail = models.CharField(max_length=30, blank=True)
    onthefly_register = models.IntegerField()
    tls = models.IntegerField()
    filter = models.CharField(max_length=255, blank=True)
    timeout = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'auth_sources'

class Banners(models.Model):
    id = models.IntegerField(primary_key=True)
    enabled = models.IntegerField(blank=True, null=True)
    style = models.CharField(max_length=255)
    banner_description = models.CharField(max_length=255, blank=True)
    use_timer = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    project_id = models.IntegerField()
    updated_on = models.DateTimeField(blank=True, null=True)
    display_part = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'banners'

class Boards(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    position = models.IntegerField(blank=True, null=True)
    topics_count = models.IntegerField()
    messages_count = models.IntegerField()
    last_message_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'boards'

class BurndownDataPoints(models.Model):
    id = models.IntegerField(primary_key=True)
    iteration_id = models.IntegerField(blank=True, null=True)
    story_points = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'burndown_data_points'

class Changes(models.Model):
    id = models.IntegerField(primary_key=True)
    changeset_id = models.IntegerField()
    action = models.CharField(max_length=1)
    path = models.TextField()
    from_path = models.TextField(blank=True)
    from_revision = models.CharField(max_length=255, blank=True)
    revision = models.CharField(max_length=255, blank=True)
    branch = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'changes'

class ChangesetParents(models.Model):
    changeset_id = models.IntegerField()
    parent_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'changeset_parents'

class Changesets(models.Model):
    id = models.IntegerField(primary_key=True)
    repository_id = models.IntegerField()
    revision = models.CharField(max_length=255)
    committer = models.CharField(max_length=255, blank=True)
    committed_on = models.DateTimeField()
    comments = models.TextField(blank=True)
    commit_date = models.DateField(blank=True, null=True)
    scmid = models.CharField(max_length=255, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'changesets'

class ChangesetsIssues(models.Model):
    changeset_id = models.IntegerField()
    issue_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'changesets_issues'

class ChartDoneRatios(models.Model):
    id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField()
    project_id = models.IntegerField()
    issue_id = models.IntegerField()
    done_ratio = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'chart_done_ratios'

class ChartIssueStatuses(models.Model):
    id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField()
    project_id = models.IntegerField()
    issue_id = models.IntegerField()
    status_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'chart_issue_statuses'

class ChartSavedConditions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    project_id = models.IntegerField(blank=True, null=True)
    conditions = models.CharField(max_length=255)
    chart = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'chart_saved_conditions'

class ChartTimeEntries(models.Model):
    id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField()
    logged_hours = models.FloatField()
    entries = models.IntegerField()
    user_id = models.IntegerField()
    issue_id = models.IntegerField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'chart_time_entries'

class CodeReviewAssignments(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_id = models.IntegerField(blank=True, null=True)
    change_id = models.IntegerField(blank=True, null=True)
    attachment_id = models.IntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True)
    rev = models.CharField(max_length=255, blank=True)
    rev_to = models.CharField(max_length=255, blank=True)
    action_type = models.CharField(max_length=255, blank=True)
    changeset_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'code_review_assignments'

class CodeReviewProjectSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    tracker_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    hide_code_review_tab = models.IntegerField(blank=True, null=True)
    auto_relation = models.IntegerField(blank=True, null=True)
    assignment_tracker_id = models.IntegerField(blank=True, null=True)
    auto_assign = models.TextField(blank=True)
    lock_version = models.IntegerField()
    tracker_in_review_dialog = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'code_review_project_settings'

class CodeReviewUserSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    mail_notification = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'code_review_user_settings'

class CodeReviews(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    change_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    line = models.IntegerField(blank=True, null=True)
    updated_by_id = models.IntegerField(blank=True, null=True)
    lock_version = models.IntegerField()
    status_changed_from = models.IntegerField(blank=True, null=True)
    status_changed_to = models.IntegerField(blank=True, null=True)
    issue_id = models.IntegerField(blank=True, null=True)
    action_type = models.CharField(max_length=255, blank=True)
    file_path = models.CharField(max_length=255, blank=True)
    rev = models.CharField(max_length=255, blank=True)
    rev_to = models.CharField(max_length=255, blank=True)
    attachment_id = models.IntegerField(blank=True, null=True)
    file_count = models.IntegerField()
    diff_all = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'code_reviews'

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    commented_type = models.CharField(max_length=30)
    commented_id = models.IntegerField()
    author_id = models.IntegerField()
    comments = models.TextField(blank=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'comments'

class CustomFields(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    field_format = models.CharField(max_length=30)
    possible_values = models.TextField(blank=True)
    regexp = models.CharField(max_length=255, blank=True)
    min_length = models.IntegerField(blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)
    is_required = models.IntegerField()
    is_for_all = models.IntegerField()
    is_filter = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    searchable = models.IntegerField(blank=True, null=True)
    default_value = models.TextField(blank=True)
    editable = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField()
    multiple = models.IntegerField(blank=True, null=True)
    format_store = models.TextField(blank=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'custom_fields'

class CustomFieldsProjects(models.Model):
    custom_field_id = models.IntegerField()
    project_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'custom_fields_projects'

class CustomFieldsRoles(models.Model):
    custom_field_id = models.IntegerField()
    role_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'custom_fields_roles'

class CustomFieldsTrackers(models.Model):
    custom_field_id = models.IntegerField()
    tracker_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'custom_fields_trackers'

class CustomValues(models.Model):
    id = models.IntegerField(primary_key=True)
    customized_type = models.CharField(max_length=30)
    customized_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'custom_values'

class DelayedJobs(models.Model):
    id = models.IntegerField(primary_key=True)
    priority = models.IntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    handler = models.TextField(blank=True)
    last_error = models.TextField(blank=True)
    run_at = models.DateTimeField(blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    failed_at = models.DateTimeField(blank=True, null=True)
    locked_by = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'delayed_jobs'

class Diagrams(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    user_story_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    content_type = models.CharField(max_length=255, blank=True)
    filename = models.CharField(max_length=255, blank=True)
    thumbnail = models.CharField(max_length=255, blank=True)
    size = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    version = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'diagrams'

class DmsfFileRevisionAccesses(models.Model):
    id = models.IntegerField(primary_key=True)
    dmsf_file_revision_id = models.IntegerField()
    action = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'dmsf_file_revision_accesses'

class DmsfFileRevisions(models.Model):
    id = models.IntegerField(primary_key=True)
    dmsf_file_id = models.IntegerField()
    source_dmsf_file_revision_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    dmsf_folder_id = models.IntegerField(blank=True, null=True)
    disk_filename = models.CharField(max_length=255)
    size = models.IntegerField(blank=True, null=True)
    mime_type = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    workflow = models.IntegerField(blank=True, null=True)
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
    comment = models.TextField(blank=True)
    deleted = models.IntegerField()
    deleted_by_user_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    project_id = models.IntegerField()
    dmsf_workflow_id = models.IntegerField(blank=True, null=True)
    dmsf_workflow_assigned_by = models.IntegerField(blank=True, null=True)
    dmsf_workflow_assigned_at = models.DateTimeField(blank=True, null=True)
    dmsf_workflow_started_by = models.IntegerField(blank=True, null=True)
    dmsf_workflow_started_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dmsf_file_revisions'

class DmsfFiles(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    dmsf_folder_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    notification = models.IntegerField()
    deleted = models.IntegerField()
    deleted_by_user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'dmsf_files'

class DmsfFolders(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    dmsf_folder_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    notification = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'dmsf_folders'

class DmsfLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    target_project_id = models.IntegerField()
    target_id = models.IntegerField()
    target_type = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    project_id = models.IntegerField()
    dmsf_folder_id = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    deleted_by_user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'dmsf_links'

class DmsfLocks(models.Model):
    id = models.IntegerField(primary_key=True)
    entity_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    entity_type = models.IntegerField()
    lock_type_cd = models.IntegerField()
    lock_scope_cd = models.IntegerField()
    uuid = models.CharField(max_length=36, blank=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dmsf_locks'

class DmsfWorkflowStepActions(models.Model):
    id = models.IntegerField(primary_key=True)
    dmsf_workflow_step_assignment_id = models.IntegerField()
    action = models.IntegerField()
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    author_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'dmsf_workflow_step_actions'

class DmsfWorkflowStepAssignments(models.Model):
    id = models.IntegerField(primary_key=True)
    dmsf_workflow_step_id = models.IntegerField()
    user_id = models.IntegerField()
    dmsf_file_revision_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'dmsf_workflow_step_assignments'

class DmsfWorkflowSteps(models.Model):
    id = models.IntegerField(primary_key=True)
    dmsf_workflow_id = models.IntegerField()
    step = models.IntegerField()
    user_id = models.IntegerField()
    operator = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'dmsf_workflow_steps'

class DmsfWorkflows(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    project_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dmsf_workflows'

class Documentations(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True)
    revision = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'documentations'

class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    category_id = models.IntegerField()
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'documents'

class EnabledModules(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'enabled_modules'

class Enumerations(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    position = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField()
    type = models.CharField(max_length=255, blank=True)
    active = models.IntegerField()
    project_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    position_name = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'enumerations'

class FavoriteProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'favorite_projects'

class GitCaches(models.Model):
    id = models.IntegerField(primary_key=True)
    command = models.TextField(blank=True)
    command_output = models.TextField(blank=True)
    repo_identifier = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'git_caches'

class GitolitePublicKeys(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    identifier = models.CharField(max_length=255, blank=True)
    key = models.TextField(blank=True)
    active = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    key_type = models.IntegerField(blank=True, null=True)
    delete_when_unused = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gitolite_public_keys'

class GroupsUsers(models.Model):
    group_id = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'groups_users'

class HomeBlocks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'home_blocks'

class HudsonBuildArtifacts(models.Model):
    id = models.IntegerField(primary_key=True)
    hudson_build_id = models.IntegerField(blank=True, null=True)
    display_path = models.TextField(blank=True)
    file_name = models.TextField(blank=True)
    relative_path = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'hudson_build_artifacts'

class HudsonBuildChangesets(models.Model):
    id = models.IntegerField(primary_key=True)
    hudson_build_id = models.IntegerField(blank=True, null=True)
    repository_id = models.IntegerField(blank=True, null=True)
    revision = models.CharField(max_length=255, blank=True)
    error = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'hudson_build_changesets'

class HudsonBuildTestResults(models.Model):
    id = models.IntegerField(primary_key=True)
    hudson_build_id = models.IntegerField(blank=True, null=True)
    fail_count = models.IntegerField(blank=True, null=True)
    skip_count = models.IntegerField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hudson_build_test_results'

class HudsonBuilds(models.Model):
    id = models.IntegerField(primary_key=True)
    hudson_job_id = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    building = models.CharField(max_length=255, blank=True)
    error = models.CharField(max_length=255, blank=True)
    caused_by = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hudson_builds'

class HudsonHealthReports(models.Model):
    id = models.IntegerField(primary_key=True)
    hudson_job_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    score = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'hudson_health_reports'

class HudsonJobSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    hudson_job_id = models.IntegerField(blank=True, null=True)
    build_rotate = models.IntegerField(blank=True, null=True)
    build_rotator_days_to_keep = models.IntegerField(blank=True, null=True)
    build_rotator_num_to_keep = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hudson_job_settings'

class HudsonJobs(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    hudson_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    latest_build_number = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    state = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'hudson_jobs'

class HudsonSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    job_filter = models.CharField(max_length=255, blank=True)
    show_compact = models.IntegerField(blank=True, null=True)
    auth_user = models.CharField(max_length=255, blank=True)
    auth_password = models.CharField(max_length=255, blank=True)
    get_build_details = models.IntegerField(blank=True, null=True)
    url_for_plugin = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'hudson_settings'

class HudsonSettingsHealthReports(models.Model):
    id = models.IntegerField(primary_key=True)
    hudson_settings_id = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True)
    url_format = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'hudson_settings_health_reports'

class IssueCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=30)
    assigned_to_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'issue_categories'

class IssueChecklists(models.Model):
    id = models.IntegerField(primary_key=True)
    is_done = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True)
    position = models.IntegerField(blank=True, null=True)
    issue_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'issue_checklists'

class IssueFaviconUserSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'issue_favicon_user_settings'

class IssueRelations(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_from_id = models.IntegerField()
    issue_to_id = models.IntegerField()
    relation_type = models.CharField(max_length=255)
    delay = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'issue_relations'

class IssueStatuses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    is_closed = models.IntegerField()
    is_default = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    default_done_ratio = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'issue_statuses'

class IssueTemplateSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    help_message = models.TextField(blank=True)
    enabled = models.IntegerField(blank=True, null=True)
    inherit_templates = models.IntegerField()
    should_replaced = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'issue_template_settings'

class IssueTemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    project_id = models.IntegerField(blank=True, null=True)
    tracker_id = models.IntegerField()
    author_id = models.IntegerField()
    note = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    enabled = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    issue_title = models.CharField(max_length=255, blank=True)
    position = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    enabled_sharing = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'issue_templates'

class Issues(models.Model):
    id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()
    project_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField()
    assigned_to_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    deliverable_id = models.IntegerField(blank=True, null=True)
    user_story_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    delayed_job_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    is_private = models.IntegerField()
    remaining_hours = models.FloatField(blank=True, null=True)
    story_points = models.FloatField(blank=True, null=True)
    closed_on = models.DateTimeField(blank=True, null=True)
    release_id = models.IntegerField(blank=True, null=True)
    release_relationship = models.CharField(max_length=255)
    ir_position = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'issues'

class Iterations(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    duration = models.IntegerField(blank=True, null=True)
    initial_estimate = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'iterations'

class JournalDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    journal_id = models.IntegerField()
    property = models.CharField(max_length=30)
    prop_key = models.CharField(max_length=30)
    old_value = models.TextField(blank=True)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'journal_details'

class Journals(models.Model):
    id = models.IntegerField(primary_key=True)
    journalized_id = models.IntegerField()
    journalized_type = models.CharField(max_length=30)
    user_id = models.IntegerField()
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField()
    private_notes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'journals'

class KanbanIssues(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    issue_id = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'kanban_issues'

class MemberRoles(models.Model):
    id = models.IntegerField(primary_key=True)
    member_id = models.IntegerField()
    role_id = models.IntegerField()
    inherited_from = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'member_roles'

class Members(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    mail_notification = models.IntegerField()
    dmsf_mail_notification = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'members'

class Menutabs(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=255)
    wiki_page = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    project_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    content_page = models.TextField(blank=True)
    wiki_type = models.CharField(max_length=255, blank=True)
    external_link = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'menutabs'

class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    board_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author_id = models.IntegerField(blank=True, null=True)
    replies_count = models.IntegerField()
    last_reply_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    locked = models.IntegerField(blank=True, null=True)
    sticky = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'messages'

class Milestones(models.Model):
    id = models.IntegerField(primary_key=True)
    target = models.CharField(max_length=255, blank=True)
    deadline = models.DateField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'milestones'

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    author_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    comments_count = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'news'

class OpenIdAuthenticationAssociations(models.Model):
    id = models.IntegerField(primary_key=True)
    issued = models.IntegerField(blank=True, null=True)
    lifetime = models.IntegerField(blank=True, null=True)
    handle = models.CharField(max_length=255, blank=True)
    assoc_type = models.CharField(max_length=255, blank=True)
    server_url = models.TextField(blank=True)
    secret = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'open_id_authentication_associations'

class OpenIdAuthenticationNonces(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.IntegerField()
    server_url = models.CharField(max_length=255, blank=True)
    salt = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'open_id_authentication_nonces'

class OverviewBlocks(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'overview_blocks'

class Projects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    homepage = models.CharField(max_length=255, blank=True)
    is_public = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True)
    status = models.IntegerField()
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    inherit_members = models.IntegerField()
    dmsf_description = models.TextField(blank=True)
    dmsf_notification = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'projects'

class ProjectsTrackers(models.Model):
    project_id = models.IntegerField()
    tracker_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'projects_trackers'

class Queries(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    filters = models.TextField(blank=True)
    user_id = models.IntegerField()
    column_names = models.TextField(blank=True)
    sort_criteria = models.TextField(blank=True)
    group_by = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    visibility = models.IntegerField(blank=True, null=True)
    options = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'queries'

class QueriesRoles(models.Model):
    query_id = models.IntegerField()
    role_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'queries_roles'

class Rates(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    date_in_effect = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rates'

class RbIssueHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_id = models.IntegerField(unique=True)
    history = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'rb_issue_history'

class RbJournals(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_id = models.IntegerField()
    property = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    value = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'rb_journals'

class RbProjectSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    show_stories_from_subprojects = models.IntegerField()
    show_in_scrum_stats = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'rb_project_settings'

class RbReleaseBurnchartDayCaches(models.Model):
    issue_id = models.IntegerField()
    release_id = models.IntegerField()
    day = models.DateField()
    total_points = models.FloatField()
    added_points = models.FloatField()
    closed_points = models.FloatField()
    class Meta:
        managed = False
        db_table = 'rb_release_burnchart_day_caches'

class RbReleasesMultiview(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project_id = models.IntegerField(blank=True, null=True)
    release_ids = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'rb_releases_multiview'

class RbSprintBurndown(models.Model):
    id = models.IntegerField(primary_key=True)
    version_id = models.IntegerField(unique=True)
    stories = models.TextField(blank=True)
    burndown = models.TextField(blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'rb_sprint_burndown'

class Releases(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    release_start_date = models.DateField()
    release_end_date = models.DateField()
    project_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sharing = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    planned_velocity = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'releases'

class Repositories(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    url = models.CharField(max_length=255)
    login = models.CharField(max_length=60, blank=True)
    password = models.CharField(max_length=255, blank=True)
    root_url = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    path_encoding = models.CharField(max_length=64, blank=True)
    log_encoding = models.CharField(max_length=64, blank=True)
    extra_info = models.TextField(blank=True)
    identifier = models.CharField(max_length=255, blank=True)
    is_default = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'repositories'

class RepositoryDeploymentCredentials(models.Model):
    id = models.IntegerField(primary_key=True)
    repository_id = models.IntegerField(blank=True, null=True)
    gitolite_public_key_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    perm = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'repository_deployment_credentials'

class RepositoryGitConfigKeys(models.Model):
    id = models.IntegerField(primary_key=True)
    repository_id = models.IntegerField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'repository_git_config_keys'

class RepositoryGitExtras(models.Model):
    id = models.IntegerField(primary_key=True)
    repository_id = models.IntegerField(blank=True, null=True)
    git_daemon = models.IntegerField(blank=True, null=True)
    git_http = models.IntegerField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True)
    git_notify = models.IntegerField(blank=True, null=True)
    default_branch = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'repository_git_extras'

class RepositoryGitNotifications(models.Model):
    id = models.IntegerField(primary_key=True)
    repository_id = models.IntegerField(blank=True, null=True)
    include_list = models.TextField(blank=True)
    exclude_list = models.TextField(blank=True)
    prefix = models.CharField(max_length=255, blank=True)
    sender_address = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'repository_git_notifications'

class RepositoryMirrors(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    push_mode = models.IntegerField(blank=True, null=True)
    include_all_branches = models.IntegerField(blank=True, null=True)
    include_all_tags = models.IntegerField(blank=True, null=True)
    explicit_refspec = models.CharField(max_length=255, blank=True)
    repository_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'repository_mirrors'

class RepositoryPostReceiveUrls(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True)
    repository_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'repository_post_receive_urls'

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    position = models.IntegerField(blank=True, null=True)
    assignable = models.IntegerField(blank=True, null=True)
    builtin = models.IntegerField()
    permissions = models.TextField(blank=True)
    issues_visibility = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'roles'

class ScheduleClosedEntries(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    date = models.DateField()
    hours = models.FloatField()
    comment = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'schedule_closed_entries'

class ScheduleDefaults(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    weekday_hours = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'schedule_defaults'

class ScheduleEntries(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    date = models.DateField()
    hours = models.FloatField()
    class Meta:
        managed = False
        db_table = 'schedule_entries'

class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)
    class Meta:
        managed = False
        db_table = 'schema_migrations'

class Settings(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'settings'

class StatusNotifications(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    option = models.CharField(max_length=255, blank=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'status_notifications'

class Statuses(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_on = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'statuses'

class Stories(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    iteration_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    estimate = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'stories'

class StoryActions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    story_id = models.IntegerField(blank=True, null=True)
    iteration_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'story_actions'

class StoryTeamMembers(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    story_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'story_team_members'

class TaskLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    sprint_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'task_logs'

class TestCases(models.Model):
    id = models.IntegerField(primary_key=True)
    test_suite_id = models.IntegerField()
    issue_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'test_cases'

class TestSuites(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    parent_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test_suites'

class TimeEntries(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    issue_id = models.IntegerField(blank=True, null=True)
    hours = models.FloatField()
    comments = models.CharField(max_length=255, blank=True)
    activity_id = models.IntegerField()
    spent_on = models.DateField()
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    rate_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'time_entries'

class TimeEstimates(models.Model):
    id = models.IntegerField(primary_key=True)
    estimation = models.CharField(max_length=255, blank=True)
    value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'time_estimates'

class TimeTrackers(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    issue_id = models.IntegerField(blank=True, null=True)
    started_on = models.DateTimeField(blank=True, null=True)
    time_spent = models.FloatField(blank=True, null=True)
    paused = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'time_trackers'

class Tokens(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    action = models.CharField(max_length=30)
    value = models.CharField(unique=True, max_length=40)
    created_on = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'tokens'

class Trackers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    is_in_chlog = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    is_in_roadmap = models.IntegerField()
    template = models.TextField(blank=True)
    fields_bits = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'trackers'

class UserPreferences(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    others = models.TextField(blank=True)
    hide_mail = models.IntegerField(blank=True, null=True)
    time_zone = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'user_preferences'

class UserStories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    project_id = models.IntegerField(blank=True, null=True)
    time_estimate_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    us_number = models.IntegerField(blank=True, null=True)
    milestone_id = models.IntegerField(blank=True, null=True)
    version_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'user_stories'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=40)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=255)
    mail = models.CharField(max_length=60)
    admin = models.IntegerField()
    status = models.IntegerField()
    last_login_on = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=5, blank=True)
    auth_source_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True)
    identity_url = models.CharField(max_length=255, blank=True)
    mail_notification = models.CharField(max_length=255)
    salt = models.CharField(max_length=64, blank=True)
    must_change_passwd = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'users'

class Versions(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    effective_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    wiki_page_title = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    sharing = models.CharField(max_length=255)
    duration = models.IntegerField(blank=True, null=True)
    sprint_start_date = models.DateField(blank=True, null=True)
    ir_start_date = models.DateField(blank=True, null=True)
    ir_end_date = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'versions'

class Watchers(models.Model):
    id = models.IntegerField(primary_key=True)
    watchable_type = models.CharField(max_length=255)
    watchable_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'watchers'

class WikiContentVersions(models.Model):
    id = models.IntegerField(primary_key=True)
    wiki_content_id = models.IntegerField()
    page_id = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True)
    compression = models.CharField(max_length=6, blank=True)
    comments = models.CharField(max_length=255, blank=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'wiki_content_versions'

class WikiContents(models.Model):
    id = models.IntegerField(primary_key=True)
    page_id = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True)
    comments = models.CharField(max_length=255, blank=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'wiki_contents'

class WikiLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    wiki_id = models.IntegerField()
    from_page_id = models.IntegerField()
    to_page_title = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'wiki_links'

class WikiPages(models.Model):
    id = models.IntegerField(primary_key=True)
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    protected = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'wiki_pages'

class WikiRedirects(models.Model):
    id = models.IntegerField(primary_key=True)
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    redirects_to = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'wiki_redirects'

class Wikis(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    start_page = models.CharField(max_length=255)
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'wikis'

class Workflows(models.Model):
    id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()
    old_status_id = models.IntegerField()
    new_status_id = models.IntegerField()
    role_id = models.IntegerField()
    assignee = models.IntegerField()
    author = models.IntegerField()
    type = models.CharField(max_length=30, blank=True)
    field_name = models.CharField(max_length=30, blank=True)
    rule = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'workflows'

