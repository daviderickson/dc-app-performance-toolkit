import random
import re
from locustio.jira.requests_params import Login, BrowseIssue, CreateIssue, SearchJql, ViewBoard, BrowseBoards, \
    BrowseProjects, AddComment, ViewDashboard, EditIssue, ViewProjectSummary, jira_datasets
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')
jira_dataset = jira_datasets()
admin_pw="fillmein"


@jira_measure("locust_app_specific_action")
@run_as_specific_user(username='admin', password=admin_pw)  # run as specific user
def app_specific_action(locust):

    issue = random.choice(jira_dataset['issues'])
    issue_id = issue[1]
    issue_key = issue[0]
    project_key = issue[2]
    # admin is not in the users set users.csv
    user = random.choice(jira_dataset['users'])[0]

    #logger.locust_info('before comments')
    r = locust.get(f'/rest/api/latest/issue/{issue_id}/comment?maxResults=5', catch_response=True, auth=("admin", admin_pw))
    #content = r.content.decode('utf-8')   # decode response content
    #logger.locust_info(f'response: {content}')  # log info for debug when verbose is true in jira.yml file

    #logger.locust_info('before post')
    body = {"body": "lorem ipsum unum"}
    headers = {'content-type': 'application/json', 'sudo': user}
    r = locust.post(f'/rest/api/latest/issue/{issue_id}/comment', json=body, headers=headers, catch_response=True,auth=("admin", admin_pw))


    #content = r.content.decode('utf-8')   # decode response content
    #logger.locust_info(f'response: {content}\n\n')  # log info for debug when verbose is true in jira.yml file

    #token_pattern_example = '"token":"(.+?)"'
    #id_pattern_example = '"id":"(.+?)"'
    #token = re.findall(token_pattern_example, content)  # get TOKEN from response using regexp
    #id = re.findall(id_pattern_example, content)    # get ID from response using regexp

    #logger.locust_info(f'token: {token}, id: {id}')  # log info for debug when verbose is true in jira.yml file
    #if 'assertion string' not in content:
    #    logger.error(f"'assertion string' was not found in {content}")
    #assert 'assertion string' in content  # assert specific string in response content

    #body = {"id": id, "token": token}  # include parsed variables to POST request body
    #headers = {'content-type': 'application/json'}
    #r = locust.post('/app/post_endpoint', body, headers, catch_response=True)  # call app-specific POST endpoint
    #content = r.content.decode('utf-8')
    #if 'assertion string after successful POST request' not in content:
    #    logger.error(f"'assertion string after successful POST request' was not found in {content}")
    #assert 'assertion string after successful POST request' in content  # assertion after POST request
