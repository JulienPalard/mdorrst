# EasyQA Python 2 Client Library

This document describes Python 2 library that wraps [EasyQA](https://geteasyqa.com) REST API.

# Installation
```sh
$ pip install easyqa
```
### Authenticating
###### fields
[required]
> - base_url - Your server url (default is easyqa cloud(https://app.geteasyqa.com))
> - email - Your email
> - password - Your password
> - project_token - Your project token. [How find project token](https://geteasyqa.com/sdk/android)

```python
from easyqa.session import Session
easyqa = Session(login='<your email>', password='<your password>', base_url='<your server>', project_token='<your project token>')
```
# Methods

### Issues
#### Get issue
##### Get issues from project
```python
# get all issues from project
easyqa.get_issues()
```
##### Get issue by id
###### fields
[required]
> - issue_id - Issue ID

```python
# get one issue by id
easyqa.get_issue_by_id(issue_id)

# get one issue by id in project
easyqa.get_issue_by_id_in_project(issue_id)
```

#### Create issue
###### fields
[required]
> - summary - Issue summary

[optional]
> - test_object_id - ID test object on site
> - description - Issue description
> - issue_type - Type of issue ('bug', 'documentation', 'task', 'feature', 'usability_problem', 'crash')
> - priority - Issue priority ('low', 'medium', 'high', 'critical') 
> - assigner_id - Issue assigner ID
> - file - File which will be attached to issue

```python
# create one issue
easyqa.create_issue(summary, **kwargs)
```

###### examples
```python
# create one issue with optional fields
easyqa.create_issue(summary='Test', description='test description')
```
#### Update issue
###### fields
[required]
> - issue_id - Issue ID
> - summary - Issue summary

[optional]
> - test_object_id - ID test object on site
> - description - Issue description
> - issue_type - Type of issue ('bug', 'documentation', 'task', 'feature', 'usability_problem', 'crash')
> - priority - Issue priority ('low', 'medium', 'high', 'critical') 
> - assigner_id - Issue assigner ID
> - status_id - Status ID
> - file - File which will be attached to issue

```python
# Update issue by id
easyqa.update_issue_by_id(issue_id, summary, **kwargs)
```

###### examples
```python
# update one issue with optional fields
easyqa.update_issue_by_id(issue_id=2, summary='Test', description='test description')

# update one issue by id in project with optional fields
easyqa.update_issue_by_id_in_project(issue_id=2, summary='Test', description='test description')
```

#### Delete issue
###### fields
[required]
> - issue_id - Issue ID

###### examples
```python
# delete one issue
easyqa.delete_issue_by_id(issue_id=2)

# delete one issue by id in project
easyqa.delete_issue_by_id_in_project(issue_id=3)
```
### Attachment
#### Create Attachment
###### fields
[required]
> - issue_id - Issue ID
> - attach_file - File

###### examples
```python
# create attachment
easyqa.create_issue_attachment(issue_id=1, attach_file'text.txt')
```

#### Delete Attachment
###### fields
[required]
> - attachment_id - Attachment ID

###### examples
```python
# delete attachment
easyqa.delete_attachment(attachment_id=12)
```

### Organization
#### Get Organization
##### Get organizations
```python
# get all your organizations
easyqa.get_organizations()
```

##### Get organization by id
###### fields
[required]
> - id - Organization ID

###### examples
```python
# get one organization by id
easyqa.show_organization(id)
```

#### Create organization
###### fields
[required]
> - title - Organization title

[optional]
> - description - Organization description

###### examples
```python
# create one organization 
easyqa.create_organization(title='Test')

# create one organization with optional fields
easyqa.create_issue(title='Test', description='test description')
```

#### Update organization
###### fields
[required]
> - id - Organization id

[optional]
> - title - Organization title
> - description - Organization description

###### examples
```python
# update one organization 
easyqa.update_organization(id=1, title='Test', description='test description')
```

#### Delete organization
###### fields
[required]
> - id - Organization id

###### examples
```python
# delete one organization
easyqa.delete_organization(id=2)
```

### Project
#### Get Project
##### Get all your Projects
```python
# get all your projects
easyqa.get_projects()
```
##### Get project by id
###### fields
[required]
> - id - Projects ID

###### examples
```python
# get one project by id
easyqa.show_project(id)
```

#### Create project
###### fields
[required]
> - org_id - Organization id
> - title - Project title

###### examples
```python
# create one project 
easyqa.create_project(org_id=1, title='Test')
```

#### Update project
###### fields
[required]
> - org_id - Organization id

[optional]
> - title - Project title

###### examples
```python
# update one project 
easyqa.update_project(org_id=1, title='updated project')
```

#### Delete project
###### fields
[required]
> - id - Project id

###### examples
```python
# delete one project
easyqa.delete_project(id=2)
```

### Roles
#### Get Roles
###### fields
[required]
> - organization_id - Organization id

###### examples
```python
# get all roles from organizations
easyqa.get_roles(organization_id=1)
```

##### Get role by id
###### fields
[required]
> - id - Role ID

###### examples
```python
# get one organization by id
easyqa.show_role(id=1)
```

##### Create organization role
###### fields
[required]
> - organization_id - Organization id
> - user_id - User id
> - role - Role (available: 'user', 'admin')

###### examples
```python
# create organization role
easyqa.create_organization_role(organization_id=1, user_id=12, role='user')
```

##### Create project role
###### fields
[required]
> - organization_id - Organization id
> - user_id - User id
> - role - Role (available: 'developer', 'tester', 'viewer', 'project_manager')

###### examples
```python
# create project role
easyqa.create_project_role(organization_id=1, user_id=12, role='tester')
```

##### Update project role
###### fields
[required]
> - id - role id
> - role - Role (available: 'developer', 'tester', 'viewer', 'project_manager')

###### examples
```python
# update project role
easyqa.update_project_role(id=2, role='tester')
```

##### Delete project role
###### fields
[required]
> - id - role id

###### examples
```python
# delete project role
easyqa.delete_role(id=2)
```

### Test cases
#### Get Test cases
###### fields
[required]
> - test_module_id - Test module ID

###### examples
```python
# get all test cases from module
easyqa.get_test_cases(test_module_id=1)
```

##### Get test case by id
###### fields
[required]
> - id - Test case ID

###### examples
```python
# get one test case by id
easyqa.show_test_case(id=1)
```

##### Create test case
###### fields
[required]
> - test_module_id - Test module ID
> - title - Title of the test case

[optional]
> - test_case - Test case attributes
> - pre_steps - Pre steps to test case
> - steps - Steps to test case
> - expected_result - Expected test case result
> - case_type - Type of test case

###### examples
```python
# create test case
easyqa.create_test_case(test_module_id=1, title='test', steps='1. Sit in a Vulture Droid\n 2. Go to Lothal')
```

##### Update test case
###### fields
[required]
> - id - Test case ID
> - title - Title of the test case

[optional]
> - test_case - Test case attributes
> - pre_steps - Pre steps to test case
> - steps - Steps to test case
> - expected_result - Expected test case result
> - case_type - Type of test case

###### examples
```python
# update test case
easyqa.update_test_case(test_module_id=1, title='test', pre_steps='1. Sit in a Vulture Droid\n 2. Go to Lothal')
```

##### Delete test case
###### fields
[required]
> - id - test case id

###### examples
```python
# delete test case
easyqa.delete_test_case(id=2)
```

### Statuses
#### Get Statuses
###### fields

###### examples
```python
# get all statuses
easyqa.get_statuses()
```

##### Get status by id
###### fields
[required]
> - id - Status id

###### examples
```python
# get one status by id
easyqa.show_statuses(id=1)
```

##### Create status
###### fields
[required]
> - name - Status name

###### examples
```python
# create status
easyqa.create_status(name='synthesizing')
```

##### Update status
###### fields
[required]
> - name - Status name
> - id - Status id

###### examples
```python
# update status
easyqa.update_status(id=4, name='synthesizing')
```

##### Delete status
###### fields
[required]
> - id - Status id

###### examples
```python
# delete status
easyqa.delete_status(id=2)
```

### Test Modules
#### Get Test Modules
###### fields
[required]
> - test_plan_id - ID of test plan

###### examples
```python
# get all test module from test plan
easyqa.get_test_modules(test_plan_id=1)
```

##### Get test module by id
###### fields
[required]
> - id - Test module id

###### examples
```python
# get one test module by id
easyqa.show_test_module(id=1)
```

##### Create test module
###### fields
[required]
> - test_plan_id - ID of test plan
> - title - Title of the test module

[optional]
> - description - Description of the test module
> - test_module - Test module attributes
> - parent_id - Id of parent test module (If you give this parameter, this test module will be nested in parent test module)

###### examples
```python
# create test module
easyqa.create_test_module(test_plan_id=1, title='test', description='Super module')
```

##### Update test module
###### fields
[required]
> - id - Test module id
> - title - Title of the test module

[optional]
> - description - Description of the test module
> - test_module - Test module attributes
> - parent_id - Id of parent test module (If you give this parameter, this test module will be nested in parent test module)

###### examples
```python
# update test module
easyqa.update_test_module(test_plan_id=1, title='test', description='Super module2')
```

##### Delete test module
###### fields
[required]
> - id - test module id

###### examples
```python
# delete test module
easyqa.delete_test_module(id=2)
```

### Test Plan
#### Get Test Plan
###### examples
```python
# get all test plans from project
easyqa.get_test_plans()
```

#### Get Test Plan by id
###### fields
[required]
> - id - test_plan id

###### examples
```python
# get Test Plan by id from project
easyqa.show_test_plan(id=3)
```

##### Create test plan
###### fields
[required]
> - title - Title of the test plan

[optional]
> - description - Description of the test plan

###### examples
```python
# create test plan
easyqa.create_test_plan(title='test', description='Super test plan')
```

##### Update test plan
###### fields
[required]
> - id - Test plan id
> - title - Title of the test plan

[optional]
> - description - Description of the test plan

###### examples
```python
# update test plan
easyqa.update_test_plan(id=2, title='test', description='Super test plan')
```

##### Delete test plan
###### fields
[required]
> - id - Test plan id

###### examples
```python
# delete test plan
easyqa.delete_test_plan(id=2)
```

### Test Object
#### Get Test Object
###### examples
```python
# get all test objects from project
easyqa.get_test_objects()
```

#### Get Test Object by id
###### fields
[required]
> - id - test object id

###### examples
```python
# get Test Object by id from project
easyqa.show_test_object(id=3)
```

##### Create test object link
###### fields
[required]
> - link - Your link to site

###### examples
```python
# create test object link
easyqa.create_test_object_link(link='http://champlin.info')
```

##### Create test object file
###### fields
[required]
> - build_file - Path to ipa or apk file

###### examples
```python
# create test object link
    easyqa.create_test_object_file(build_file='one.apk')
```

##### Delete test object
###### fields
[required]
> - id - Test object id

###### examples
```python
# delete test object
easyqa.delete_test_object(id=2)
```

### Test Run
#### Get Test Runs
###### examples
```python
# get all test runs from project
easyqa.get_test_runs()
```

#### Get Test run by id
###### fields
[required]
> - test_run_id - test run id

###### examples
```python
# get Test run by id from project
easyqa.show_test_run(test_run_id=3)
```

##### Create test run
###### fields
[required]
> - title - Title of the test run

[optional]
> - description - Description of the test run
> - test_run_results_attributes - Attributes of test cases. If you want include they to this test run
> - ...

###### examples
```python
# create test run
easyqa.create_test_run(title='Run')
```

##### Update test run
###### fields
[required]
> - id - Test run id
> - title - Title of the test run

[optional]
> - description - Description of the test run
> - test_run_results_attributes - Attributes of test cases. If you want include they to this test run
> - ...

###### examples
```python
# update test run
easyqa.update_test_run(title='Run')
```

##### Delete test run
###### fields
[required]
> - id - Test run id

###### examples
```python
# delete test run
easyqa.delete_test_run(id=2)
```

### Test Run result
#### Get Test Run result from test run
###### fields
[required]
> - test_run_id - test run id

###### examples
```python
# get all test run result from test run
easyqa.get_test_run_results(test_run_id=12)
```

#### Get Test run result by id
###### fields
[required]
> - test_run_result_id - test run result id

###### examples
```python
# get Test run result by id from test run
easyqa.show_test_run_result(test_run_result_id=3)
```

##### Update test run result
###### fields
[required]
> - test_run_results_id - Test run result id

[optional]
> - result_status - Status of test run results, might be in "pass", "block", "untested" and "fail"
> - test_case_id - Test case id

###### examples
```python
# update test run result
easyqa.update_test_run_result(test_run_results_id=21, test_case_id=12)
```

##### Delete test run results
###### fields
[required]
> - id - Test run result id

###### examples
```python
# delete test run results
easyqa.delete_test_run_result(id=2)
```
